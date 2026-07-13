import os
import sys

# Add the project root (main-repo) to Python path
PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from rag.pipeline import ask


def get_rag_answer(question: str):
    result = ask(question)

    department = None

    if result["sources"]:
        department = result["sources"][0].get("department")

    return {
        "answer": result["answer"],
        "department": department,
        "sources": result["sources"],
        "confidence": result.get("confidence", 0.0),
        "graph": result.get("graph"),
    }
