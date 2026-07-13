from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import upload, documents, chat, metrics, health


app = FastAPI(
    title="Nexus AI Backend",
    description="Backend API for Nexus AI Enterprise Knowledge Intelligence Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register APIs with prefixes

app.include_router(
    upload.router,
    prefix="/api"
)

app.include_router(
    documents.router,
    prefix="/api"
)

app.include_router(
    chat.router,
    prefix="/api"
)

app.include_router(
    metrics.router,
    prefix="/api"
)

app.include_router(
    health.router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Nexus AI Backend"
    }


@app.on_event("startup")
def warmup_models():
    import os
    import sys
    # Add the project root to Python path if not present
    PROJECT_ROOT = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)

    from rag.config import CHROMA_PATH, CLASSIFIER_MODEL_PATH

    try:
        if not CHROMA_PATH.exists() or not any(CHROMA_PATH.iterdir()):
            print("LOG: No vector store found. Running one-time document ingestion...")
            from rag.ingest import ingest
            ingest()
            print("LOG: Ingestion completed.")
    except Exception as e:
        print(f"LOG: Document ingestion failed: {e}")

    try:
        if not CLASSIFIER_MODEL_PATH.exists():
            print("LOG: No department classifier found. Training one-time...")
            from rag.classifier import train
            train(report=False)
            print("LOG: Classifier training completed.")
    except Exception as e:
        print(f"LOG: Classifier training failed: {e}")

    try:
        print("LOG: Startup warmup: Loading Vector DB...")
        from rag.retriever import _get_db
        _get_db()
        print("LOG: Startup warmup: Running dummy LLM generation...")
        from rag.generator import generate
        generate("Warmup")
        print("LOG: Startup warmup: Completed successfully.")
    except Exception as e:
        print(f"LOG: Startup warmup failed: {e}")