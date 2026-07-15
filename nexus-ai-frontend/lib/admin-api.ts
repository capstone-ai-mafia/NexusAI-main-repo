import { ApiError, getApiBaseUrl } from "@/lib/api";
import { parseMetrics, type Metrics } from "@/lib/metrics";
import type { ChatHistoryEntry, DocumentRecord } from "@/lib/types";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const baseUrl = getApiBaseUrl();

  let res: Response;
  try {
    res = await fetch(`${baseUrl}${path}`, { mode: "cors", ...init });
  } catch {
    throw new ApiError("Couldn't reach the Nexus AI backend. Check your connection and try again.");
  }

  if (!res.ok) {
    throw new ApiError(`Request to ${path} failed (${res.status}).`, res.status);
  }

  return res.json() as Promise<T>;
}

export async function fetchMetrics(): Promise<Metrics> {
  const baseUrl = getApiBaseUrl();

  let res: Response;
  try {
    res = await fetch(`${baseUrl}/api/metrics/`, { mode: "cors" });
  } catch {
    throw new ApiError("Couldn't reach the Nexus AI backend. Check your connection and try again.");
  }

  if (!res.ok) {
    throw new ApiError(`Metrics request failed (${res.status}).`, res.status);
  }

  const text = await res.text();
  return parseMetrics(text);
}

export function fetchDocuments(): Promise<DocumentRecord[]> {
  return request<DocumentRecord[]>("/api/documents/");
}

export async function deleteDocument(id: number): Promise<void> {
  await request(`/api/documents/${id}`, { method: "DELETE" });
}

export async function uploadDocument(file: File): Promise<DocumentRecord> {
  const baseUrl = getApiBaseUrl();
  const formData = new FormData();
  formData.append("file", file);

  let res: Response;
  try {
    res = await fetch(`${baseUrl}/api/upload/`, {
      method: "POST",
      mode: "cors",
      body: formData,
    });
  } catch {
    throw new ApiError("Couldn't reach the Nexus AI backend. Check your connection and try again.");
  }

  if (!res.ok) {
    throw new ApiError(`Upload failed (${res.status}).`, res.status);
  }

  const data = await res.json();
  return data.document as DocumentRecord;
}

export function fetchChatHistory(): Promise<ChatHistoryEntry[]> {
  return request<ChatHistoryEntry[]>("/api/chat/history");
}
