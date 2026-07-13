import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_DIR = PROJECT_ROOT / "backend"

for path in (str(PROJECT_ROOT), str(BACKEND_DIR)):
    if path not in sys.path:
        sys.path.insert(0, path)

# Point the backend at an isolated, disposable database/log/upload location
# so running the test suite never touches real app data.
_TEST_STATE_DIR = PROJECT_ROOT / "tests" / ".tmp"
_TEST_STATE_DIR.mkdir(parents=True, exist_ok=True)

os.environ.setdefault("DATABASE_URL", f"sqlite:///{(_TEST_STATE_DIR / 'test_nexus_ai.db').as_posix()}")
os.environ.setdefault("LOG_DIR", str(_TEST_STATE_DIR / "logs"))
os.environ.setdefault("UPLOAD_DIR", str(_TEST_STATE_DIR / "uploads"))

import pytest


@pytest.fixture(scope="session", autouse=True)
def ensure_vector_store():
    """The RAG tests need a populated Chroma store; build it once if missing."""
    from rag.config import CHROMA_PATH

    if not CHROMA_PATH.exists() or not any(CHROMA_PATH.iterdir()):
        from rag.ingest import ingest
        ingest()
