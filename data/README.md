# Nexus Technologies Cleaned Corpus

---
## Purpose

These documents are used as the knowledge source for the RAG system.

The ingestion pipeline performs the following steps:

1. Load Markdown and PDF documents.
2. Split documents into chunks.
3. Generate embeddings.
4. Store embeddings in ChromaDB.
5. Retrieve the most relevant chunks.
6. Generate grounded answers using the LLM.

---

## Supported Departments

- Company
- Human Resources (HR)
- Information Technology (IT)
- Information Security
- Finance
- Legal & Compliance

---

## Vector Database

**ChromaDB**

---

## Recommended Configuration

| Setting | Value |
|----------|-------|
| Chunk Size | 800 |
| Chunk Overlap | 150 |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Language | English |

---

## Document Status

Current Version: **1.0**

Status: **Frozen Corpus**

No policy documents should be modified after the evaluation dataset has been created.

---

## Notes

- The PDF version is included only as a reference.
- The Markdown files are the primary source for document ingestion.
- All generated answers must include citations from the original documents.