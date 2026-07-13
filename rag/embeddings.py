from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings

from .config import EMBEDDING_MODEL


@lru_cache(maxsize=1)
def get_embeddings():
    print("LOG: Loading embedding model from disk...")
    # Cache location is controlled globally via the HF_HOME env var.
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return embeddings