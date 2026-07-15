"use client";

import {
  Bar,
  BarChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import type { DocumentRecord } from "@/lib/types";

interface Props {
  documents: DocumentRecord[];
}

interface TooltipPayload {
  active?: boolean;
  payload?: { payload: { department: string; count: number } }[];
}

function ChartTooltip({ active, payload }: TooltipPayload) {
  if (!active || !payload?.length) return null;
  const { department, count } = payload[0].payload;

  return (
    <div className="glass rounded-lg px-3 py-2 text-xs">
      <p className="font-medium text-foreground">{department}</p>
      <p className="text-muted-foreground">
        {count} document{count === 1 ? "" : "s"}
      </p>
    </div>
  );
}

export function DepartmentChart({ documents }: Props) {
  const counts = new Map<string, number>();
  for (const doc of documents) {
    const dept = doc.department?.trim() || "Unassigned";
    counts.set(dept, (counts.get(dept) ?? 0) + 1);
  }

  const data = Array.from(counts.entries())
    .map(([department, count]) => ({ department, count }))
    .sort((a, b) => b.count - a.count);

  if (data.length === 0) {
    return <p className="p-4 text-sm text-muted-foreground">No documents to chart yet.</p>;
  }

  return (
    <div className="h-64 w-full">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" vertical={false} />
          <XAxis
            dataKey="department"
            tick={{ fill: "hsl(var(--muted-foreground))", fontSize: 12 }}
            axisLine={{ stroke: "hsl(var(--border))" }}
            tickLine={false}
          />
          <YAxis
            allowDecimals={false}
            tick={{ fill: "hsl(var(--muted-foreground))", fontSize: 12 }}
            axisLine={false}
            tickLine={false}
            width={28}
          />
          <Tooltip content={<ChartTooltip />} cursor={{ fill: "hsl(var(--accent) / 0.08)" }} />
          <Bar dataKey="count" fill="hsl(var(--primary))" radius={[4, 4, 0, 0]} maxBarSize={48} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

// Note: /api/metrics/ has no per-department question counters (only
// rag_requests_total / success / failed / avg_latency and document counts),
// so there is no data to drive a questions-by-department pie chart. Once the
// backend exposes that breakdown, add a PieChart here fed from the same
// metrics response.
