from pathlib import Path

from langchain_core.documents import Document

from .config import DATA_PATH

# Runtime-generated artifacts that also live under DATA_PATH (per the
# CHROMA_PATH/HF_HOME/UPLOAD_DIR/LOG_DIR env vars) and must never be
# scanned as source documents -- e.g. HuggingFace model cards cached
# inside hf_cache/ would otherwise get ingested as bogus "department"
# content.
_NON_CONTENT_DIRS = {"chroma_db", "hf_cache", "uploads", "logs"}


def load_documents():

    documents = []

    for file in DATA_PATH.rglob("*.md"):

        # Skip stray files sitting directly in data/ (not a department folder)
        if file.parent == DATA_PATH:
            continue

        if file.relative_to(DATA_PATH).parts[0] in _NON_CONTENT_DIRS:
            continue

        content = file.read_text(
            encoding="utf-8"
        )

        department = file.parent.name

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": file.name,
                    "department": department
                }
            )
        )

    # Note: data/pdf/ contains a single consolidated PDF export of the same
    # per-department markdown policies above ("frozen cleaned corpus" backup).
    # It is intentionally not ingested here to avoid duplicating content.

    return documents