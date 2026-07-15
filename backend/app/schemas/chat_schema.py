from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ChatRequest(BaseModel):
    question: str
    department: str | None = None


class GraphNode(BaseModel):
    name: str
    department: str = ""


class GraphEdge(BaseModel):
    from_: str = Field(alias="from")
    relation: str
    to: str

    model_config = ConfigDict(populate_by_name=True)


class KnowledgeGraph(BaseModel):
    nodes: list[GraphNode] = Field(default_factory=list)
    edges: list[GraphEdge] = Field(default_factory=list)
    reasoning_path: list[str] = Field(default_factory=list)


class ChatResponse(BaseModel):
    answer: str
    department: str | None = None
    sources: list = Field(default_factory=list)
    confidence: float
    latency: float
    graph: KnowledgeGraph | None = None


class ChatHistoryResponse(BaseModel):
    id: int
    question: str
    answer: str | None
    confidence: float | None
    latency: float | None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
