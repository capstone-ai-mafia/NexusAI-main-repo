import os
import sys
import math
from typing import Optional

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

_embeddings = None


def _get_embedding_similarity(text1: Optional[str], text2: Optional[str]) -> Optional[float]:
    global _embeddings
    if not text1 or not text2:
        return 0.0
    try:
        if _embeddings is None:
            from rag.embeddings import get_embeddings
            _embeddings = get_embeddings()
        v1 = _embeddings.embed_query(text1)
        v2 = _embeddings.embed_query(text2)
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        if not norm1 or not norm2:
            return 0.0
        return max(0.0, min(1.0, dot / (norm1 * norm2)))
    except Exception as e:
        print(f"LOG: Embedding similarity calculation failed: {e}")
        return None


def compute_retrieval_accuracy(retrieved_document: Optional[str], expected_document: Optional[str]) -> float:
    if not retrieved_document or not expected_document:
        return 0.0
    r_base = os.path.basename(retrieved_document).lower()
    e_base = os.path.basename(expected_document).lower()
    return 1.0 if r_base == e_base else 0.0


def compute_answer_relevance(model_answer: Optional[str], expected_answer: Optional[str]) -> float:
    if not model_answer or not expected_answer:
        return 0.0

    sim = _get_embedding_similarity(model_answer, expected_answer)
    if sim is not None:
        return sim

    # Fallback
    answer = (model_answer or "").lower()
    expected = (expected_answer or "").lower()
    if answer == expected:
        return 1.0
    overlap = len(set(answer.split()) & set(expected.split()))
    if not overlap:
        return 0.0
    return min(1.0, overlap / max(3, len(set(expected.split()))))


def compute_groundedness(model_answer: Optional[str], retrieved_document: Optional[str], expected_document: Optional[str]) -> float:
    if not model_answer:
        return 0.0
    r_base = os.path.basename(retrieved_document).lower() if retrieved_document else None
    e_base = os.path.basename(expected_document).lower() if expected_document else None
    if r_base and e_base and r_base == e_base:
        return 0.8
    if r_base and e_base:
        return 0.4
    return 0.2


def compute_faithfulness(model_answer: Optional[str], expected_answer: Optional[str]) -> float:
    if not model_answer or not expected_answer:
        return 0.0

    sim = _get_embedding_similarity(model_answer, expected_answer)
    if sim is not None:
        return sim

    # Fallback
    answer = (model_answer or "").lower()
    expected = (expected_answer or "").lower()
    if "cannot" in answer and "outside" in answer:
        return 1.0
    return 0.6 if len(set(answer.split()) & set(expected.split())) > 0 else 0.2


def compute_out_of_scope_detection(model_answer: Optional[str], expected_behavior: str) -> float:
    if expected_behavior != "OUT_OF_SCOPE":
        return 0.0
    if not model_answer:
        return 0.0
    answer = (model_answer or "").lower()
    if "cannot" in answer or "outside" in answer or "not" in answer and "policy" in answer:
        return 1.0
    return 0.0


def compute_multi_hop_success(model_answer: Optional[str], expected_answer: Optional[str], difficulty: str) -> float:
    if difficulty != "Hard":
        return 0.0
    if not model_answer or not expected_answer:
        return 0.0
    answer = (model_answer or "").lower()
    expected = (expected_answer or "").lower()
    if len(set(answer.split()) & set(expected.split())) > 0:
        return 0.7
    return 0.2
