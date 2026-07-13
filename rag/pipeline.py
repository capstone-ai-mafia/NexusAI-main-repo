import logging
import re

from .retriever import retrieve_with_scores, MIN_RELEVANCE_SCORE, CROSS_CUTTING_DEPARTMENTS
from .prompt_builder import build_prompt
from .generator import generate
from .config import DEPT_CLASSIFIER_ENABLED, DEPT_CLASSIFIER_MIN_PROBA
from . import kg

logger = logging.getLogger(__name__)

# Classifier labels use Title Case, while document metadata uses the
# lowercase data-folder name.
#
# General Policies and Company intentionally route to data/company because
# that corpus exists in this repository. data/shared remains cross-cutting
# reference content and is available during unfiltered retrieval.
_DEPARTMENT_ALIASES = {
    "hr": "hr",
    "it": "it",
    "finance": "finance",
    "legal": "legal",
    "security": "security",
    "general policies": "company",
    "general policy": "company",
    "company": "company",
    "shared": "shared",
}

# Anchors used to rescale the raw cosine-similarity score of the best
# retrieved chunk into a confidence value: at or below the retriever's own
# relevance floor, retrieval effectively found nothing; at or above
# STRONG_MATCH_SCORE, treat it as a fully confident, well-grounded match.
STRONG_MATCH_SCORE = 0.55

NOT_FOUND_MESSAGE = "I cannot answer that from the Nexus company policy knowledge base."

# Greedy decoding on the small local generator model can occasionally
# degenerate into repeating the same short phrase dozens of times instead
# of stopping. Detect a phrase (6-80 chars) immediately repeated 3+ times
# and cut the answer back to its first, non-repeated occurrence rather
# than surface a wall of repeated text to the user.
_REPEAT_RE = re.compile(r"(.{6,80}?)(\s*\1){2,}", re.IGNORECASE)


# If collapsing a detected repetition loop leaves fewer characters than
# this, the loop started almost immediately and there isn't enough
# pre-loop content left to call it an answer.
MIN_VIABLE_ANSWER_CHARS = 60


def _collapse_repetition(answer):
    """Returns (cleaned_answer, was_degenerate)."""
    match = _REPEAT_RE.search(answer)
    if not match:
        return answer, False
    return answer[: match.start() + len(match.group(1))].strip(), True


def _generate_answer(question, documents):
    """Generate an answer, retrying against just the single best chunk if
    the full multi-chunk prompt triggers the small model's greedy-decoding
    repetition loop and leaves too little usable text behind."""
    answer, degenerate = _collapse_repetition(generate(build_prompt(question, documents)))
    if degenerate and len(answer) < MIN_VIABLE_ANSWER_CHARS and len(documents) > 1:
        logger.info("Generation degenerated into a repetition loop; retrying with the single best chunk.")
        retry_answer, _ = _collapse_repetition(generate(build_prompt(question, documents[:1])))
        if len(retry_answer) > len(answer):
            answer = retry_answer
    return answer


def _resolve_department(label):
    if not label:
        return None
    return _DEPARTMENT_ALIASES.get(label.strip().lower())


def _confidence_from_sources(scores, sources):
    """Confidence reflects retrieval quality, not just a raw score average.

    Combines three signals:
      - top1: how strongly the single best chunk matches the question,
        rescaled against the retriever's own relevance floor/ceiling.
      - department focus: what share of the *specific*-department evidence
        (excluding shared/company reference material) agrees with the
        best chunk's department -- mixed, unfocused evidence should not
        score as confidently as a clean, single-department hit.
      - agreement: how many of the returned chunks are close to the top
        score, rather than one lucky hit surrounded by weak filler.
    """
    if not scores:
        return 0.0

    top1 = scores[0]
    span = max(STRONG_MATCH_SCORE - MIN_RELEVANCE_SCORE, 1e-6)
    top1_rescaled = max(0.0, min(1.0, (top1 - MIN_RELEVANCE_SCORE) / span))

    if top1_rescaled <= 0.0:
        # The best chunk didn't even clear the relevance floor (the
        # out-of-scope fallback case) -- no amount of department/agreement
        # agreement should manufacture confidence out of that.
        return 0.0

    top_department = sources[0].get("department")
    specific = [s for s in sources if s.get("department") not in CROSS_CUTTING_DEPARTMENTS]
    if specific:
        department_share = sum(
            1 for s in specific if s.get("department") == top_department
        ) / len(specific)
    else:
        department_share = 1.0

    agreement = sum(1 for s in scores if s >= top1 - 0.08) / len(scores)

    confidence = top1_rescaled + (0.15 * department_share) + (0.05 * agreement)
    return round(max(0.0, min(0.97, confidence)), 3)


def _empty_graph():
    """Return a fresh empty Knowledge Graph response."""
    return {
        "nodes": [],
        "edges": [],
        "reasoning_path": [],
    }


def _expand_graph_safely(question, sources):
    """
    Expand the Knowledge Graph without allowing KG failures to break RAG.

    Source file names and section titles are passed as fallback matching
    evidence when the question does not directly mention a graph concept.
    """
    retrieved_sections = []

    for source in sources or []:
        if not isinstance(source, dict):
            continue

        for field in ("section", "source"):
            value = source.get(field)

            if value and str(value).strip():
                retrieved_sections.append(str(value).strip())

    try:
        graph_result = kg.expand(
            question,
            retrieved_sections=retrieved_sections,
        )

        if not isinstance(graph_result, dict):
            return _empty_graph()

        nodes = graph_result.get("nodes")
        edges = graph_result.get("edges")
        reasoning_path = graph_result.get("reasoning_path")

        return {
            "nodes": nodes if isinstance(nodes, list) else [],
            "edges": edges if isinstance(edges, list) else [],
            "reasoning_path": (
                reasoning_path
                if isinstance(reasoning_path, list)
                else []
            ),
        }

    except Exception as error:
        logger.warning(
            "Knowledge Graph expansion failed: %s. "
            "Continuing without graph context.",
            error,
        )
        return _empty_graph()


def ask(question, department=None):
    chosen_dept = department
    if chosen_dept is None and DEPT_CLASSIFIER_ENABLED:
        try:
            from .classifier import predict_department
            label, proba = predict_department(question)
            resolved = _resolve_department(label)
            if proba >= DEPT_CLASSIFIER_MIN_PROBA and resolved:
                chosen_dept = resolved
                logger.info(f"Classified department as '{resolved}' (label '{label}') with proba {proba:.3f}")
            else:
                logger.info(f"Classifier returned '{label}' with proba {proba:.3f} (< {DEPT_CLASSIFIER_MIN_PROBA} or unmapped). Retrieving unfiltered.")
        except Exception as e:
            logger.warning(f"Failed to run department classifier: {e}. Skipping classification.")

    pairs = retrieve_with_scores(question, chosen_dept)
    scores = [s for _, s in pairs]

    if not scores or scores[0] < MIN_RELEVANCE_SCORE:
        # Nothing retrieved actually clears the relevance floor. Small local
        # LLMs are unreliable at self-assessing "can I answer this from the
        # context" via a conditional prompt instruction (empirically, adding
        # that clause degrades *every* answer's quality, not just this
        # case) -- so that decision is made here, from our own calibrated
        # retrieval score, instead of asking the model to make it.
        logger.info(f"No chunk cleared the relevance floor ({MIN_RELEVANCE_SCORE}); declining to answer.")
        return {
            "answer": NOT_FOUND_MESSAGE,
            "sources": [],
            "confidence": 0.0,
            "graph": _empty_graph(),
        }

    documents = [d for d, _ in pairs]
    answer = _generate_answer(question, documents)
    sources = [{
        "source": d.metadata.get("source"),
        "department": d.metadata.get("department"),
        "section": d.metadata.get("section"),
        "relevance_score": d.metadata.get("relevance_score"),
        "context": d.page_content,
    } for d in documents]

    graph_result = _expand_graph_safely(question, sources)

    return {
        "answer": answer,
        "sources": sources,
        "confidence": _confidence_from_sources(scores, sources),
        "graph": graph_result,
    }
