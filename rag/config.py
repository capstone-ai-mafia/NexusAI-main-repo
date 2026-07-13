import os
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent


# Data folder
DATA_PATH = BASE_DIR / "data"


# Vector database location
CHROMA_PATH = Path(os.getenv("CHROMA_PATH", str(BASE_DIR / "chroma_db"))).expanduser()

# Classifier model location
CLASSIFIER_MODEL_PATH = BASE_DIR / "models" / "department_clf.joblib"


# Embedding model
# MIN_RELEVANCE_SCORE=0.32 in rag/retriever.py is calibrated specifically for this embedding model.
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# Chunking settings
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150


# Retrieval settings
TOP_K = 5

# Reranking settings
RERANK_ENABLED = False
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
RETRIEVE_K = 15

# Classifier settings
DEPT_CLASSIFIER_ENABLED = True
DEPT_CLASSIFIER_MIN_PROBA = 0.60