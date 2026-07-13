import math
import os


DEFAULT_MAX_CONTEXT_TOKENS = 3500
CHARS_PER_TOKEN = 4
MIN_PARTIAL_CONTENT_TOKENS = 20


def _read_positive_int_env(name: str, default: int) -> int:
    """Read a positive integer from the environment with a safe fallback."""
    raw_value = os.getenv(name)

    if raw_value is None:
        return default

    try:
        value = int(raw_value)
    except (TypeError, ValueError):
        return default

    return value if value > 0 else default


# Conservative context budget for llama3.2:3b.
# It can be overridden without changing code:
# MAX_CONTEXT_TOKENS=4500
MAX_CONTEXT_TOKENS = _read_positive_int_env(
    "MAX_CONTEXT_TOKENS",
    DEFAULT_MAX_CONTEXT_TOKENS,
)


def _estimate_tokens(text: str) -> int:
    """
    Estimate token count without loading a tokenizer model.

    A four-characters-per-token approximation is intentionally used to avoid
    downloading or initializing a heavyweight tokenizer only for prompt
    budgeting.
    """
    if not text:
        return 0

    return max(1, math.ceil(len(text) / CHARS_PER_TOKEN))


def _truncate_to_token_budget(text: str, token_budget: int) -> str:
    """Truncate text approximately to the supplied token budget."""
    if not text or token_budget <= 0:
        return ""

    max_characters = token_budget * CHARS_PER_TOKEN

    if len(text) <= max_characters:
        return text

    truncated = text[:max_characters].rstrip()

    # Avoid cutting the final word where possible.
    if " " in truncated:
        word_safe_truncation = truncated.rsplit(" ", 1)[0].rstrip()

        if word_safe_truncation:
            truncated = word_safe_truncation

    return truncated


def build_prompt(question, documents):
    """
    Build an Ollama-compatible RAG prompt from retrieved documents.

    The context budget is intentionally separate from the prompt instructions
    and question. With the default TOP_K and chunk size, all retrieved chunks
    should normally fit without unnecessary truncation.
    """
    instruction_start = (
        "You are Nexus AI, a professional HR and company-policy assistant. "
        "Summarize the numbered context passages below into one detailed, "
        "complete-sentence answer to the question. Combine the relevant facts "
        "from every passage that applies -- do not rely on only one source if "
        "others are also relevant. Include exact numbers, durations, "
        "thresholds, and conditions as stated in the context, and cite each "
        "fact with its source number in brackets, like [1].\n\n"
        "Context:\n"
    )

    instruction_end = f"\n\nQuestion: {question}\n\nSummary:"

    blocks = []
    current_tokens = 0
    separator_tokens = _estimate_tokens("\n\n")

    for index, document in enumerate(documents, 1):
        source = document.metadata.get("source", "unknown")
        section = document.metadata.get("section", "")

        header = f"[{index}] {source}"
        if section:
            header += f" — {section}"

        content = document.page_content or ""
        block = f"{header}\n{content}"
        block_tokens = _estimate_tokens(block)

        separator_cost = separator_tokens if blocks else 0

        if (
            current_tokens
            + separator_cost
            + block_tokens
            <= MAX_CONTEXT_TOKENS
        ):
            blocks.append(block)
            current_tokens += separator_cost + block_tokens
            continue

        # The complete block does not fit. Use the remaining budget for a
        # final partial chunk, preserving the original aggregation behavior.
        header_tokens = _estimate_tokens(f"{header}\n")
        remaining_tokens = (
            MAX_CONTEXT_TOKENS
            - current_tokens
            - separator_cost
            - header_tokens
        )

        if remaining_tokens > MIN_PARTIAL_CONTENT_TOKENS:
            truncated_content = _truncate_to_token_budget(
                content,
                remaining_tokens,
            )

            if truncated_content:
                blocks.append(f"{header}\n{truncated_content}...")

        break

    context = "\n\n".join(blocks) if blocks else "(no context retrieved)"

    return instruction_start + context + instruction_end
