# Nexus AI — Enterprise RAG Assistant

Nexus AI is an internal knowledge assistant that lets employees ask natural-language
questions about company policy documents (HR, IT, Finance, Legal, Security) and get
grounded answers with cited sources — instead of digging through PDFs and wikis.

## Problem Statement

Company policy knowledge is scattered across long-form HR, IT, Finance, Legal, and
Security documents. Employees waste time searching for answers, and get inconsistent
or out-of-date information from colleagues. Nexus AI answers policy questions directly,
grounded in the actual source documents, and always shows where the answer came from.

## Architecture

```
Frontend (Next.js)
      |
      v
Backend API (FastAPI)  --  SQLite (chat logs, documents, metrics)
      |
      v
RAG Pipeline
  Documents (data/*)
      -> chunking (RecursiveCharacterTextSplitter)
      -> embeddings (sentence-transformers/all-MiniLM-L6-v2)
      -> vector database (Chroma)
      -> retrieval (similarity search, optional department filter)
      -> LLM answer generation (llama3.2:3b via Ollama)
```

On first startup, the backend automatically ingests every document under `data/`
into the Chroma vector store and trains the department classifier if they don't
already exist — no manual setup step is required.

## Features

- Clean chat interface with conversation history, loading state, and error handling
- Grounded answers with cited sources (document, department, section, relevance score)
- Confidence score per answer, based on retrieval relevance
- Automatic department routing (HR / IT / Finance / Legal / Security) via a TF-IDF classifier
- Document upload endpoint and chat/document metrics for observability
- Fully self-contained: local embedding + local LLM, no external API keys required

## Tech Stack

| Layer      | Technology |
|------------|------------|
| Frontend   | Next.js 14, React, Tailwind CSS |
| Backend    | FastAPI, SQLAlchemy, SQLite |
| RAG | LangChain, ChromaDB, sentence-transformers, Ollama (`llama3.2:3b`) |
| Classifier | scikit-learn (TF-IDF + Logistic Regression) |
| Testing    | pytest |
| Deployment | Docker, Docker Compose |

## Project Structure

```
backend/          FastAPI app (routes, services, models, schemas)
rag/              RAG pipeline (loader, chunker, embeddings, vector store, retriever, generator)
nexus-ai-frontend/ Next.js chat UI
data/             Source policy documents, organized by department
tests/            pytest suite
evaluation/       Offline RAG quality evaluation scripts and reports
```

## Setup

### Prerequisites
- Docker + Docker Compose (recommended), **or**
- Python 3.11+ and Node.js 20+ for running services natively

### Environment Variables

Copy `.env.example` to `.env` and adjust as needed:

```
DATABASE_URL=sqlite:////app/data/nexus_ai.db
UPLOAD_DIR=/app/data/uploads
LOG_DIR=/app/data/logs
CHROMA_PATH=/app/data/chroma_db
HF_HOME=/app/data/hf_cache

NEXT_PUBLIC_API_BASE_URL=http://backend:8000
NEXT_PUBLIC_USE_MOCK=false
```

When running natively (outside Docker), omit the `/app` prefix or point these at
local paths — sensible defaults are used if unset.

## Running with Docker (recommended)

```bash
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Backend docs (Swagger): http://localhost:8000/docs

The first boot downloads the embedding/LLM models and ingests `data/` into Chroma,
so it can take a few minutes. Subsequent restarts reuse the persisted vector store
in `./data/chroma_db`.

## Running Natively

```bash
# Backend
pip install -r backend/requirements.txt
cd backend
python -m uvicorn app.main:app --reload --port 8000

# Frontend (in a separate terminal)
cd nexus-ai-frontend
npm install
npm run dev
```

## API Examples

**Health check**

```bash
curl http://localhost:8000/api/health
# {"status": "healthy"}
```

**Ask a question**

```bash
curl -X POST http://localhost:8000/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the vacation policy?"}'
```

```json
{
  "answer": "Employees accrue... [1]",
  "department": "hr",
  "sources": [
    {
      "source": "NEXUS_HR_POLICY_MANUAL.md",
      "department": "hr",
      "section": "Annual Leave",
      "relevance_score": 0.83
    }
  ],
  "confidence": 0.79,
  "latency": 1.42
}
```

## Testing

```bash
pip install -r requirements.txt
pytest
```

The suite covers:
- `tests/test_health.py` — backend health endpoint
- `tests/test_chat_api.py` — `/api/chat/` question/answer contract
- `tests/test_rag_retrieval.py` — vector retrieval and department filtering
- `tests/test_e2e.py` — full document → chunk → embed → retrieve → generate flow

The first run builds the vector store if it doesn't exist yet (same auto-ingest
behavior as the backend).

## Demo Questions

- "What is the vacation policy?"
- "How long does probation last for a new employee?"
- "What expenses require itemized receipts?"
- "What is the password policy for company systems?"
- "What is Nexus Technologies' incident response process?"

## Known Limitations

- The local LLM (`llama3.2:3b` via Ollama) is suitable for local deployment, but may be less capable than larger hosted models on complex or ambiguous policy questions.
  shorter, less fluent answers than a hosted large model.
- The department classifier falls back to unfiltered retrieval when confidence is
  low, which is correct behavior but means not every question gets department-scoped
  answers.
- First container startup is slow (model downloads + ingestion); it requires
  internet access at least once.
- No authentication/authorization — this is a single-tenant capstone MVP.

## Department Routing

Classifier labels `General Policies` and `Company` are explicitly mapped to
the `data/company` corpus. The `data/shared` corpus contains cross-cutting
reference material and remains available during unfiltered retrieval.

