import { resolveMockResponse } from "./mock-data";
import type {
  Citation,
  Department,
  KnowledgeGraph,
  QueryRequest,
  QueryResponse,
} from "./types";

const CONFIG_API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL?.replace(/\/$/, "") ?? "";

const REQUEST_TIMEOUT_MS = 60_000;

export function getApiBaseUrl(): string {
  if (CONFIG_API_BASE_URL) {
    return CONFIG_API_BASE_URL;
  }

  if (typeof window !== "undefined") {
    const hostname = window.location.hostname;
    return `http://${hostname}:8000`;
  }

  return "http://localhost:8000";
}

const FORCE_MOCK = process.env.NEXT_PUBLIC_USE_MOCK === "true";

export const IS_MOCK_MODE = FORCE_MOCK;

export class ApiError extends Error {
  constructor(message: string, public status?: number) {
    super(message);
    this.name = "ApiError";
  }
}

function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

// Maps the frontend's department labels onto the lowercase department tags
// used as Chroma metadata / retrieval filters on the backend. "General"
// corresponds to the company-wide corpus (data/company), matching the
// backend's own classifier-label mapping.
const BACKEND_DEPARTMENT: Record<string, string> = {
  hr: "hr",
  it: "it",
  finance: "finance",
  legal: "legal",
  security: "security",
  general: "company",
};

function toBackendDepartment(department: unknown): string | undefined {
  const key = String(department ?? "").toLowerCase();
  if (key === "all" || key === "") return undefined;
  return BACKEND_DEPARTMENT[key];
}

function normalizeDepartment(
  value: unknown
): Exclude<Department, "All"> {
  const department = String(value ?? "").toLowerCase();

  if (department === "hr") return "HR";
  if (department === "it") return "IT";
  if (department === "finance") return "Finance";
  if (department === "legal") return "Legal";
  if (department === "security") return "Security";

  return "General";
}

function normalizeGraph(value: unknown): KnowledgeGraph | null {
  if (!isObject(value)) {
    return null;
  }

  const rawNodes = Array.isArray(value.nodes) ? value.nodes : [];
  const rawEdges = Array.isArray(value.edges) ? value.edges : [];
  const rawPaths = Array.isArray(value.reasoning_path)
    ? value.reasoning_path
    : [];

  const nodes = rawNodes
    .filter(isObject)
    .map((node) => ({
      name: String(node.name ?? "").trim(),
      department: String(node.department ?? "shared").trim(),
    }))
    .filter((node) => node.name.length > 0);

  const edges = rawEdges
    .filter(isObject)
    .map((edge) => ({
      from: String(edge.from ?? "").trim(),
      relation: String(edge.relation ?? "relates to").trim(),
      to: String(edge.to ?? "").trim(),
    }))
    .filter((edge) => edge.from.length > 0 && edge.to.length > 0);

  const reasoning_path = rawPaths
    .map((path) => String(path).trim())
    .filter(Boolean);

  return {
    nodes,
    edges,
    reasoning_path,
  };
}

function simulateNetworkDelay(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function mockQuery(
  request: QueryRequest
): Promise<QueryResponse> {
  const response = resolveMockResponse(
    request.question,
    String(request.department ?? "All")
  );

  await simulateNetworkDelay(response.latency_ms);

  return response;
}

async function liveQuery(
  request: QueryRequest
): Promise<QueryResponse> {
  const controller = new AbortController();

  const timeout = setTimeout(
    () => controller.abort(),
    REQUEST_TIMEOUT_MS
  );

  try {
    const baseUrl = getApiBaseUrl();

    const res = await fetch(`${baseUrl}/api/chat/`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question: request.question,
        department: toBackendDepartment(request.department),
      }),
      signal: controller.signal,
    });

    if (!res.ok) {
      throw new ApiError(
        `The assistant backend returned an error (${res.status}).`,
        res.status
      );
    }

    const rawData: unknown = await res.json();

    if (!isObject(rawData)) {
      throw new ApiError("The backend returned an invalid response.");
    }

    const rawSources = Array.isArray(rawData.sources)
      ? rawData.sources
      : [];

    const citations: Citation[] = rawSources
      .filter(isObject)
      .map((source, index) => {
        const context =
          typeof source.context === "string"
            ? source.context.trim()
            : "";

        const snippet =
          context.length > 240
            ? `${context.slice(0, 240)}...`
            : context;

        const relevance =
          typeof source.relevance_score === "number"
            ? source.relevance_score.toFixed(3)
            : "N/A";

        return {
          doc_id: String(index),
          title:
            typeof source.source === "string"
              ? source.source
              : "Document",
          department: normalizeDepartment(source.department),
          section:
            typeof source.section === "string"
              ? source.section
              : "",
          snippet: snippet || `Relevance score: ${relevance}`,
        };
      });

    const confidence = Number(rawData.confidence ?? 0);
    const latency = Number(rawData.latency ?? 0);

    return {
      answer:
        typeof rawData.answer === "string"
          ? rawData.answer
          : "",
      grounded: confidence > 0.1,
      latency_ms: Math.round(latency * 1000),
      citations,
      graph: normalizeGraph(rawData.graph),
    };
  } catch (error) {
    if (error instanceof ApiError) {
      throw error;
    }

    if (
      error instanceof DOMException &&
      error.name === "AbortError"
    ) {
      throw new ApiError(
        "The request timed out. The backend may still be processing the answer."
      );
    }

    throw new ApiError(
      "Couldn't reach the Nexus AI backend. Check your connection and try again."
    );
  } finally {
    clearTimeout(timeout);
  }
}

export async function postQuery(
  request: QueryRequest
): Promise<QueryResponse> {
  if (IS_MOCK_MODE) {
    return mockQuery(request);
  }

  return liveQuery(request);
}
