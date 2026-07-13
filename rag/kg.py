"""Runtime Knowledge Graph loader and lightweight graph expansion."""

from __future__ import annotations

import json
import logging
import re
from collections import deque
from functools import lru_cache
from typing import Any, Dict, Iterable, List, Optional

from .config import BASE_DIR


logger = logging.getLogger(__name__)

GRAPH_PATH = BASE_DIR / "data" / "graph.json"

EMPTY_GRAPH = {
    "nodes": [],
    "edges": [],
}

EMPTY_EXPANSION = {
    "nodes": [],
    "edges": [],
    "reasoning_path": [],
}


def _normalize(value: Any) -> str:
    """Normalize text for case-insensitive matching."""
    return re.sub(r"\s+", " ", str(value or "").strip()).casefold()


def _node_department(node: Dict[str, Any]) -> str:
    """
    Get a node department.

    kg_extract.py stores department metadata inside node["sources"],
    so use the first valid department found there.
    """
    direct_department = str(node.get("department") or "").strip()

    if direct_department:
        return direct_department

    sources = node.get("sources") or []

    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, dict):
                continue

            department = str(source.get("department") or "").strip()

            if department:
                return department

    return ""


@lru_cache(maxsize=1)
def load_graph() -> Dict[str, List[Dict[str, Any]]]:
    """
    Load and cache data/graph.json.

    If the graph is missing, unreadable, or invalid, return an empty graph
    so the main RAG system continues working normally.
    """
    try:
        raw_graph = json.loads(
            GRAPH_PATH.read_text(encoding="utf-8")
        )
    except FileNotFoundError:
        logger.warning(
            "Knowledge Graph file not found at %s.",
            GRAPH_PATH,
        )
        return {
            "nodes": [],
            "edges": [],
        }
    except (OSError, json.JSONDecodeError, TypeError) as error:
        logger.warning(
            "Could not load Knowledge Graph from %s: %s",
            GRAPH_PATH,
            error,
        )
        return {
            "nodes": [],
            "edges": [],
        }

    if not isinstance(raw_graph, dict):
        return {
            "nodes": [],
            "edges": [],
        }

    raw_nodes = raw_graph.get("nodes")
    raw_edges = raw_graph.get("edges")

    if not isinstance(raw_nodes, list):
        raw_nodes = []

    if not isinstance(raw_edges, list):
        raw_edges = []

    nodes: List[Dict[str, Any]] = []
    node_names = set()

    for raw_node in raw_nodes:
        if not isinstance(raw_node, dict):
            continue

        name = str(raw_node.get("name") or "").strip()

        if not name:
            continue

        normalized_name = _normalize(name)

        if normalized_name in node_names:
            continue

        node_names.add(normalized_name)

        nodes.append(
            {
                "name": name,
                "department": _node_department(raw_node),
            }
        )

    edges: List[Dict[str, Any]] = []

    for raw_edge in raw_edges:
        if not isinstance(raw_edge, dict):
            continue

        source = str(raw_edge.get("from") or "").strip()
        target = str(raw_edge.get("to") or "").strip()
        relation = str(
            raw_edge.get("relation") or ""
        ).strip()

        if not source or not target or not relation:
            continue

        edges.append(
            {
                "from": source,
                "relation": relation,
                "to": target,
            }
        )

    return {
        "nodes": nodes,
        "edges": edges,
    }


def _join_sections(
    retrieved_sections: Optional[Iterable[Any]],
) -> str:
    """Convert source sections into one searchable text value."""
    if retrieved_sections is None:
        return ""

    if isinstance(retrieved_sections, str):
        return retrieved_sections

    return " ".join(
        str(section).strip()
        for section in retrieved_sections
        if section is not None and str(section).strip()
    )


def expand(
    question: str,
    retrieved_sections: Optional[Iterable[Any]] = None,
    max_hops: int = 1,
    max_nodes: int = 8,
) -> Dict[str, List[Any]]:
    """
    Match graph concepts and expand through neighbouring relations.

    Matching is intentionally simple and fast:
    - case-insensitive text matching
    - no embeddings
    - no additional model calls
    """
    graph = load_graph()

    if not graph["nodes"] or max_nodes <= 0:
        return {
            "nodes": [],
            "edges": [],
            "reasoning_path": [],
        }

    max_hops = max(0, int(max_hops))
    max_nodes = max(1, int(max_nodes))

    question_text = _normalize(question)
    sections_text = _normalize(
        _join_sections(retrieved_sections)
    )

    node_lookup: Dict[str, Dict[str, str]] = {}

    for node in graph["nodes"]:
        name = str(node.get("name") or "").strip()

        if not name:
            continue

        node_lookup[_normalize(name)] = {
            "name": name,
            "department": str(
                node.get("department") or ""
            ).strip(),
        }

    # Prefer concepts explicitly present in the question.
    matched_keys = [
        key
        for key in node_lookup
        if key and key in question_text
    ]

    # If the question has no direct concept match, use retrieved sections.
    if not matched_keys and sections_text:
        matched_keys = [
            key
            for key in node_lookup
            if key and key in sections_text
        ]

    if not matched_keys:
        return {
            "nodes": [],
            "edges": [],
            "reasoning_path": [],
        }

    adjacency: Dict[str, List[int]] = {
        key: []
        for key in node_lookup
    }

    usable_edges: List[Dict[str, str]] = []

    for edge in graph["edges"]:
        source = str(edge.get("from") or "").strip()
        target = str(edge.get("to") or "").strip()
        relation = str(
            edge.get("relation") or ""
        ).strip()

        source_key = _normalize(source)
        target_key = _normalize(target)

        if (
            source_key not in node_lookup
            or target_key not in node_lookup
            or not relation
        ):
            continue

        edge_index = len(usable_edges)

        usable_edges.append(
            {
                "from": node_lookup[source_key]["name"],
                "relation": relation,
                "to": node_lookup[target_key]["name"],
                "_from_key": source_key,
                "_to_key": target_key,
            }
        )

        adjacency[source_key].append(edge_index)
        adjacency[target_key].append(edge_index)

    selected_keys: List[str] = []
    selected_key_set = set()

    selected_edge_indexes: List[int] = []
    selected_edge_set = set()

    queue = deque()

    for matched_key in matched_keys:
        if len(selected_keys) >= max_nodes:
            break

        if matched_key in selected_key_set:
            continue

        selected_key_set.add(matched_key)
        selected_keys.append(matched_key)
        queue.append((matched_key, 0))

    while queue:
        current_key, depth = queue.popleft()

        if depth >= max_hops:
            continue

        for edge_index in adjacency.get(current_key, []):
            edge = usable_edges[edge_index]

            if edge["_from_key"] == current_key:
                neighbour_key = edge["_to_key"]
            else:
                neighbour_key = edge["_from_key"]

            if neighbour_key not in selected_key_set:
                if len(selected_keys) >= max_nodes:
                    continue

                selected_key_set.add(neighbour_key)
                selected_keys.append(neighbour_key)
                queue.append(
                    (neighbour_key, depth + 1)
                )

            if (
                edge_index not in selected_edge_set
                and edge["_from_key"] in selected_key_set
                and edge["_to_key"] in selected_key_set
            ):
                selected_edge_set.add(edge_index)
                selected_edge_indexes.append(edge_index)

    result_nodes = [
        {
            "name": node_lookup[key]["name"],
            "department": node_lookup[key]["department"],
        }
        for key in selected_keys
    ]

    result_edges = [
        {
            "from": usable_edges[index]["from"],
            "relation": usable_edges[index]["relation"],
            "to": usable_edges[index]["to"],
        }
        for index in selected_edge_indexes
    ]

    reasoning_path = [
        (
            f'{edge["from"]} → '
            f'{edge["relation"]} → '
            f'{edge["to"]}'
        )
        for edge in result_edges
    ]

    return {
        "nodes": result_nodes,
        "edges": result_edges,
        "reasoning_path": reasoning_path,
    }


if __name__ == "__main__":
    result = expand(
        "We are launching a new AI tool. What approval path?"
    )

    print(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False,
        )
    )
