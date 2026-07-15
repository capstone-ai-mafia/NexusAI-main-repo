import os
from functools import lru_cache
from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings

from .config import EMBEDDING_MODEL


def _is_model_cached() -> bool:
    """Best-effort check for a complete local snapshot of EMBEDDING_MODEL."""
    hf_home = Path(os.getenv("HF_HOME", Path.home() / ".cache" / "huggingface"))
    snapshots = hf_home / "hub" / f"models--{EMBEDDING_MODEL.replace('/', '--')}" / "snapshots"
    return snapshots.exists() and any(snapshots.iterdir())


@lru_cache(maxsize=1)
def get_embeddings():
    print("LOG: Loading embedding model from disk...")
    # Once cached, skip Hugging Face Hub's online revision check: it's an
    # unnecessary network dependency for a model that never changes, and a
    # redirect that fails to resolve cleanly (observed under Docker's
    # networking) throws an uncaught JSONDecodeError that otherwise 500s
    # every single chat request.
    if _is_model_cached():
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
    # Cache location is controlled globally via the HF_HOME env var.
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return embeddings