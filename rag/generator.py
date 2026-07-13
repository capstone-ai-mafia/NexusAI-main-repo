import logging
import os

import requests

logger = logging.getLogger(__name__)

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
# llama3.1:8b is the preferred model, but on a memory-constrained GPU (e.g.
# a 4GB laptop card shared with the OS desktop) it only partially fits in
# VRAM, spilling the rest to CPU and producing highly inconsistent latency
# (20s-200s+ observed). llama3.2:3b fits far more comfortably and answers
# just as reliably for this RAG use case; override via OLLAMA_MODEL for a
# machine with more headroom (e.g. "llama3.1:8b" or "mistral:7b").
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_TIMEOUT_SECONDS = float(os.getenv("OLLAMA_TIMEOUT_SECONDS", "120"))

FALLBACK_MESSAGE = (
    "I'm unable to generate an answer right now. Please try again shortly."
)


def generate(prompt):
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0},
            },
            timeout=OLLAMA_TIMEOUT_SECONDS,
        )
        response.raise_for_status()

        answer = response.json().get("response", "").strip()
        if not answer:
            logger.warning(f"Ollama ({OLLAMA_MODEL}) returned an empty response.")
            return FALLBACK_MESSAGE

        return answer

    except requests.exceptions.Timeout:
        logger.error(
            f"Ollama request timed out after {OLLAMA_TIMEOUT_SECONDS}s "
            f"(model={OLLAMA_MODEL}, url={OLLAMA_BASE_URL})."
        )
        return FALLBACK_MESSAGE

    except requests.exceptions.ConnectionError as e:
        logger.error(f"Could not reach Ollama at {OLLAMA_BASE_URL}: {e}")
        return FALLBACK_MESSAGE

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response is not None else "unknown"
        logger.error(
            f"Ollama returned HTTP {status} for model '{OLLAMA_MODEL}'. "
            f"Is it pulled? (docker exec -it ollama ollama pull {OLLAMA_MODEL}) Error: {e}"
        )
        return FALLBACK_MESSAGE

    except requests.exceptions.RequestException as e:
        logger.error(f"Ollama request failed: {e}")
        return FALLBACK_MESSAGE
