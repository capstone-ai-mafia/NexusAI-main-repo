export type Department = "All" | "HR" | "IT" | "Finance" | "Legal" | "Security" | "General";

export const DEPARTMENTS: Department[] = [
  "All",
  "HR",
  "IT",
  "Finance",
  "Legal",
  "Security",
  "General",
];

export const DEPARTMENT_LABELS: Record<Department, string> = {
  All: "All Departments",
  HR: "HR",
  IT: "IT",
  Finance: "Finance",
  Legal: "Legal",
  Security: "Security",
  General: "General",
};

export const DEPARTMENT_SOURCE_LABELS: Record<Exclude<Department, "All">, string> = {
  HR: "Nexus HR Policy Manual",
  IT: "Nexus IT Policy",
  Finance: "Finance & Expense Policy",
  Legal: "Legal & Compliance Manual",
  Security: "Information Security Policy",
  General: "Company Profile + General Company Policies",
};

export interface Citation {
  doc_id: string;
  title: string;
  department: Exclude<Department, "All">;
  section: string;
  snippet: string;
}

export interface KnowledgeGraphNode {
  name: string;
  department: string;
}

export interface KnowledgeGraphEdge {
  from: string;
  relation: string;
  to: string;
}

export interface KnowledgeGraph {
  nodes: KnowledgeGraphNode[];
  edges: KnowledgeGraphEdge[];
  reasoning_path: string[];
}

export interface QueryRequest {
  question: string;
  department?: Department | string;
}

export interface QueryResponse {
  answer: string;
  grounded: boolean;
  latency_ms: number;
  citations: Citation[];
  graph?: KnowledgeGraph | null;
}

export interface ConversationTurn {
  id: string;
  question: string;
  department: Department;
  status: "loading" | "success" | "error";
  response?: QueryResponse;
  errorMessage?: string;
}

export interface ExampleQuestion {
  question: string;
  department: Department;
}
