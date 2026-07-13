import logging
import math
from functools import lru_cache

from .embeddings import get_embeddings
from .vector_client import get_vectorstore

logger = logging.getLogger(__name__)

# How many nearest-neighbor candidates to pull from the vector store before
# re-scoring, threshold-filtering, and diversifying down to the final set
# handed to the prompt builder.
CANDIDATE_K = 20

# Final number of chunks used to ground the answer.
TOP_K = 5

# Chroma's built-in "relevance score" is a poorly-calibrated function of
# its internal distance metric (it can land outside [0, 1] entirely). We
# instead score every candidate ourselves with true cosine similarity
# between the query embedding and the chunk embedding, which is stable,
# bounded, and comparable across queries. Chunks below this bar are
# treated as not actually relevant and are dropped rather than forced
# into the answer's context.
MIN_RELEVANCE_SCORE = 0.32

# MMR trade-off between relevance (1.0) and novelty vs. already-selected
# chunks (0.0). Keeps the final set from being five near-duplicate
# restatements of the same sentence.
MMR_LAMBDA = 0.7

# data/shared and data/company hold cross-cutting reference material (FAQ,
# glossary, company overview) rather than one department's own policy, so
# they're never penalized by the department-focus re-ranking below.
CROSS_CUTTING_DEPARTMENTS = {"shared", "company"}

# When one specific department accounts for at least this share of the
# relevance-weighted evidence, chunks from *other* specific departments are
# treated as likely off-topic noise (e.g. a generic Finance boilerplate
# paragraph that happens to word-match an HR question) and are down-ranked
# rather than allowed to crowd out the genuinely relevant department.
DOMINANT_DEPARTMENT_SHARE = 0.5
OFF_TOPIC_PENALTY = 0.7


@lru_cache(maxsize=1)
def _get_db():
    return get_vectorstore(get_embeddings())


def _cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def _dominant_department(scored):
    """Relevance-weighted vote for the single specific department (i.e.
    excluding shared/company) that the evidence is actually about.

    Returns (department, share) or (None, 0.0) when there isn't a clear
    majority -- which is the normal, expected case for genuinely
    cross-department questions (e.g. a password policy spanning IT and
    Security), where no penalty should be applied at all.
    """
    weights = {}
    for _doc, _vec, relevance, department in scored:
        if department in CROSS_CUTTING_DEPARTMENTS:
            continue
        weights[department] = weights.get(department, 0.0) + max(relevance, 0.0)

    total = sum(weights.values())
    if total <= 0 or len(weights) < 2:
        return None, 0.0

    dept, weight = max(weights.items(), key=lambda item: item[1])
    share = weight / total
    if share >= DOMINANT_DEPARTMENT_SHARE:
        return dept, share
    return None, share


def _mmr_select(candidates, k, lambda_mult=MMR_LAMBDA):
    """Greedy Maximal Marginal Relevance selection.

    Picks chunks that rank highly (by rank_score, i.e. after the
    department-focus penalty) but are not redundant with chunks already
    selected, so the final context spans the breadth of what was
    retrieved instead of several restatements of one passage.
    """
    pool = list(candidates)
    selected = []

    while pool and len(selected) < k:
        best_idx, best_score = 0, None
        for idx, (doc, vec, relevance, rank_score) in enumerate(pool):
            redundancy = max(
                (_cosine_similarity(vec, s_vec) for _, s_vec, _, _ in selected),
                default=0.0,
            )
            mmr_score = lambda_mult * rank_score - (1 - lambda_mult) * redundancy
            if best_score is None or mmr_score > best_score:
                best_idx, best_score = idx, mmr_score
        selected.append(pool.pop(best_idx))

    return selected


def retrieve(question, department=None):
    return [doc for doc, _ in retrieve_with_scores(question, department)]


def retrieve_with_scores(question, department=None):
    db = _get_db()
    embeddings = get_embeddings()

    kwargs = {"k": CANDIDATE_K}
    if department:
        # Metadata is always the lowercase department-folder name; normalize
        # defensively so an upstream caller can't silently zero-out results
        # by passing a differently-cased label (e.g. a classifier's "HR").
        kwargs["filter"] = {"department": department.strip().lower()}

    candidates = db.similarity_search(question, **kwargs)
    if not candidates:
        return []

    query_vec = embeddings.embed_query(question)
    doc_vecs = embeddings.embed_documents([d.page_content for d in candidates])

    scored = [
        (doc, vec, _cosine_similarity(query_vec, vec), doc.metadata.get("department"))
        for doc, vec in zip(candidates, doc_vecs)
    ]
    relevant = [item for item in scored if item[2] >= MIN_RELEVANCE_SCORE]

    if not relevant:
        # No candidate cleared the calibrated relevance threshold.
        # Return no context so the pipeline can make the explicit
        # NOT_FOUND decision with confidence 0.0.
        logger.info(
            "No candidate cleared MIN_RELEVANCE_SCORE; "
            "returning no retrieved chunks."
        )
        return []

    # Down-rank specific departments other than the dominant one so a
    # generic, tangentially-word-matching chunk from another department
    # can't outrank the actually-relevant department's own content. Applied
    # as a soft re-rank (not a hard filter) so nothing is thrown away if
    # it's genuinely the best evidence available.
    dominant_dept, _share = _dominant_department(relevant)
    ranked = []
    for doc, vec, relevance, department_tag in relevant:
        if (
            dominant_dept
            and department_tag != dominant_dept
            and department_tag not in CROSS_CUTTING_DEPARTMENTS
        ):
            rank_score = relevance * OFF_TOPIC_PENALTY
        else:
            rank_score = relevance
        ranked.append((doc, vec, relevance, rank_score))

    ranked.sort(key=lambda item: item[3], reverse=True)
    selected = _mmr_select(ranked, TOP_K)
    selected.sort(key=lambda item: item[2], reverse=True)

    out = []
    for doc, _vec, relevance, _rank_score in selected:
        doc.metadata["relevance_score"] = round(relevance, 4)
        out.append((doc, relevance))
    return out
