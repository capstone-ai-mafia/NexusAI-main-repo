"""
Offline Knowledge Graph extractor.

Reads the same policy documents the RAG pipeline ingests, asks the local
Ollama model to extract policy concepts and the relationships between
them, and writes data/graph.json for the runtime KG layer (rag/kg.py).

Run once (offline), with Ollama up:
    python -m rag.kg_extract

Re-run only when the source documents change. Progress is checkpointed to
data/graph_checkpoint.json after every chunk, so an interrupted run resumes
where it left off instead of starting over.
"""
import json
import logging

from .loader import load_documents
from .cleaner import clean_text
from .chunker import split_documents
from .metadata import add_metadata
from .generator import generate, FALLBACK_MESSAGE
from .config import BASE_DIR

logger = logging.getLogger(__name__)

GRAPH_PATH = BASE_DIR / "data" / "graph.json"
CHECKPOINT_PATH = BASE_DIR / "data" / "graph_checkpoint.json"

# One chunk per call keeps each request small and reliable on llama3.2:3b.
_EXTRACT_PROMPT = """You are building a knowledge graph from a company policy document.

From the passage below, extract the key policy CONCEPTS and the RELATIONSHIPS between them.

Rules:
- A concept is a short noun phrase of 1-4 words (e.g. "Password Policy", "IT Security Review", "Remote Work", "Data Protection").
- A relationship links two concepts with a short verb phrase (e.g. "requires", "is governed by", "refers to", "applies to", "must be approved by").
- Extract at most 4 relationships. Only what is clearly stated in the passage. Do not invent.
- Respond with STRICT JSON only, no explanation, exactly this shape:
{{"relationships": [{{"from": "Concept A", "relation": "requires", "to": "Concept B"}}]}}
- If the passage has no clear relationships, respond: {{"relationships": []}}

Passage:
{passage}

JSON:"""


def _parse_json(text):
    """Best-effort: pull the first {...} block out of the model output."""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end < start:
        return None
    try:
        return json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None


def _normalize(concept):
    """Merge trivially-different mentions of the same concept
    ('IT security review' / 'IT Security Review ')."""
    return " ".join(concept.strip().split()).title()


def _load_checkpoint():
    if CHECKPOINT_PATH.exists():
        try:
            return json.loads(CHECKPOINT_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            logger.warning("Corrupt checkpoint; starting fresh.")
    return {"done_chunks": [], "nodes": {}, "edges": []}


def _save_checkpoint(state):
    CHECKPOINT_PATH.write_text(
        json.dumps(state, ensure_ascii=False), encoding="utf-8"
    )


def _chunk_key(chunk, index):
    return f"{chunk.metadata.get('source', 'unknown')}::{index}"


def build_graph():
    print("Loading documents...")
    documents = load_documents()
    for doc in documents:
        doc.page_content = clean_text(doc.page_content)
    chunks = add_metadata(split_documents(documents))
    print(f"Extracting relationships from {len(chunks)} chunks (slow, one LLM call each)...")

    state = _load_checkpoint()
    done = set(state["done_chunks"])
    nodes = state["nodes"]   # concept -> {"sources": [...]}
    edges = state["edges"]

    skipped = 0
    for i, chunk in enumerate(chunks, 1):
        key = _chunk_key(chunk, i)
        if key in done:
            continue

        source = chunk.metadata.get("source", "unknown")
        department = chunk.metadata.get("department", "unknown")
        section = chunk.metadata.get("section") or ""

        raw = generate(_EXTRACT_PROMPT.format(passage=chunk.page_content))
        if raw == FALLBACK_MESSAGE:
            print(f"[{i}/{len(chunks)}] Ollama unavailable; stopping. Re-run to resume.")
            break

        parsed = _parse_json(raw)
        if not parsed or not isinstance(parsed.get("relationships"), list):
            skipped += 1
            done.add(key)
            state["done_chunks"] = list(done)
            _save_checkpoint(state)
            continue

        added = 0
        for rel in parsed["relationships"]:
            if not isinstance(rel, dict):
                continue
            frm = _normalize(str(rel.get("from", "")))
            to = _normalize(str(rel.get("to", "")))
            relation = str(rel.get("relation", "")).strip().lower()
            if not frm or not to or not relation or frm == to:
                continue

            for concept in (frm, to):
                entry = {"source": source, "department": department, "section": section}
                nodes.setdefault(concept, {"sources": []})
                if entry not in nodes[concept]["sources"]:
                    nodes[concept]["sources"].append(entry)

            edge = {
                "from": frm,
                "relation": relation,
                "to": to,
                "source": source,
                "department": department,
                "section": section,
            }
            if edge not in edges:
                edges.append(edge)
                added += 1

        done.add(key)
        state["done_chunks"] = list(done)
        state["nodes"] = nodes
        state["edges"] = edges
        _save_checkpoint(state)
        print(f"[{i}/{len(chunks)}] {source}: +{added} relationships (total {len(edges)})")

    graph = {
        "nodes": [{"name": name, **meta} for name, meta in nodes.items()],
        "edges": edges,
    }
    GRAPH_PATH.write_text(
        json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nGraph written to {GRAPH_PATH}")
    print(f"  {len(graph['nodes'])} concepts, {len(graph['edges'])} relationships")
    if skipped:
        print(f"  ({skipped} chunks produced unparseable output and were skipped)")
    return graph


if __name__ == "__main__":
    build_graph()