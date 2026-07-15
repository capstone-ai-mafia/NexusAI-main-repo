// GET /api/metrics/ returns text/plain, one "key value" pair per line —
// not JSON. Known keys as of app/services/metrics_service.py: rag_requests_total,
// rag_success_total, rag_failed_total, rag_avg_latency_seconds,
// documents_total, documents_processed_total. There is no per-department
// breakdown and no confidence figure here.
export type Metrics = Record<string, number>;

export function parseMetrics(text: string): Metrics {
  const metrics: Metrics = {};

  for (const line of text.split("\n")) {
    const trimmed = line.trim();
    if (!trimmed) continue;

    const spaceIndex = trimmed.lastIndexOf(" ");
    if (spaceIndex === -1) continue;

    const key = trimmed.slice(0, spaceIndex).trim();
    const value = Number(trimmed.slice(spaceIndex + 1).trim());

    if (key && !Number.isNaN(value)) {
      metrics[key] = value;
    }
  }

  return metrics;
}
