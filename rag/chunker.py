from langchain_text_splitters import RecursiveCharacterTextSplitter

# Tuned for markdown policy documents: large enough that a section or
# sub-section usually survives intact in one chunk (better grounding,
# less mid-sentence fragmentation), small enough to stay topically
# focused for precise retrieval.
CHUNK_SIZE = 1100
CHUNK_OVERLAP = 200

# Chunks shorter than this (e.g. a lone trailing heading or a one-line
# leftover paragraph) carry too little standalone context to be useful
# retrieval targets, so they get folded into a neighboring chunk instead.
MIN_CHUNK_CHARS = 200

# Prefer splitting on markdown section/sub-section boundaries first, then
# paragraphs, then sentences, only falling back to raw words as a last
# resort. This keeps a section's heading together with its own content
# instead of letting the splitter cut mid-topic.
_SEPARATORS = [
    "\n## ",
    "\n### ",
    "\n#### ",
    "\n\n",
    "\n",
    ". ",
    " ",
    "",
]


def _merge_small_chunks(chunks):
    merged = []
    for chunk in chunks:
        prev = merged[-1] if merged else None
        if (
            prev is not None
            and len(chunk.page_content) < MIN_CHUNK_CHARS
            and prev.metadata.get("source") == chunk.metadata.get("source")
        ):
            prev.page_content = f"{prev.page_content}\n\n{chunk.page_content}"
        else:
            merged.append(chunk)
    return merged


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=_SEPARATORS,
    )

    chunks = splitter.split_documents(
        documents
    )

    return _merge_small_chunks(chunks)
