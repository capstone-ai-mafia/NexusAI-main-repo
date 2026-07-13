import re

_HEADING = re.compile(r"^\s*(#{1,6}\s+|§?\s*\d+(\.\d+)*\s+)(?P<title>.+?)\s*$")


def _extract_section(text):
    for line in text.splitlines():
        m = _HEADING.match(line)
        if m:
            return m.group("title").strip()
    return None


def add_metadata(chunks):
    for i, chunk in enumerate(chunks):
        dept = chunk.metadata.get("department", "unknown")
        chunk.metadata["chunk_id"] = f"{dept}_{i}"
        sec = _extract_section(chunk.page_content)
        if sec:
            chunk.metadata["section"] = sec
    return chunks