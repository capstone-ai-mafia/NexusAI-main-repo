"use client";

import { useCallback, useEffect, useState } from "react";
import { Files, Gauge, LogOut, MessageSquareText, ShieldCheck, TrendingUp } from "lucide-react";
import { RouteGuard } from "@/components/route-guard";
import { useAuth } from "@/components/auth-provider";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { KpiCard } from "@/components/dashboard/kpi-card";
import { DocumentsTable } from "@/components/dashboard/documents-table";
import { UploadZone } from "@/components/dashboard/upload-zone";
import { DepartmentChart } from "@/components/dashboard/department-chart";
import {
  deleteDocument,
  fetchChatHistory,
  fetchDocuments,
  fetchMetrics,
  uploadDocument,
} from "@/lib/admin-api";
import type { ChatHistoryEntry, DocumentRecord } from "@/lib/types";
import type { Metrics } from "@/lib/metrics";

function CompanyDashboard() {
  const { user, logout } = useAuth();
  const [metrics, setMetrics] = useState<Metrics | null>(null);
  const [documents, setDocuments] = useState<DocumentRecord[]>([]);
  const [history, setHistory] = useState<ChatHistoryEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadAll = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const [metricsData, documentsData, historyData] = await Promise.all([
        fetchMetrics(),
        fetchDocuments(),
        fetchChatHistory(),
      ]);
      setMetrics(metricsData);
      setDocuments(documentsData);
      setHistory(historyData);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load dashboard data.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    void loadAll();
  }, [loadAll]);

  const handleDelete = async (id: number) => {
    await deleteDocument(id);
    setDocuments((prev) => prev.filter((doc) => doc.id !== id));
  };

  const handleUpload = async (file: File) => {
    const uploaded = await uploadDocument(file);
    setDocuments((prev) => [
      { ...uploaded, department: null, file_type: null, file_size: file.size, uploaded_at: new Date().toISOString() },
      ...prev,
    ]);
  };

  const totalQuestions = metrics?.rag_requests_total ?? 0;
  const avgLatency = metrics?.rag_avg_latency_seconds ?? 0;

  const confidenceValues = history
    .map((entry) => entry.confidence)
    .filter((c): c is number => typeof c === "number");
  const avgConfidence =
    confidenceValues.length > 0
      ? confidenceValues.reduce((sum, c) => sum + c, 0) / confidenceValues.length
      : 0;

  const recentActivity = history.slice(0, 10);

  return (
    <div className="flex min-h-screen flex-col">
      <header className="glass sticky top-0 z-10 border-x-0 border-t-0">
        <div className="container flex h-16 items-center justify-between">
          <div className="flex items-center gap-2.5">
            <span className="flex h-8 w-8 items-center justify-center rounded-md bg-primary text-primary-foreground">
              <ShieldCheck size={18} strokeWidth={2.25} />
            </span>
            <span className="flex flex-col leading-tight">
              <span className="text-sm font-semibold tracking-tight">Nexus AI</span>
              <span className="text-[11px] text-muted-foreground">Company Console</span>
            </span>
          </div>

          <div className="flex items-center gap-3">
            <span className="hidden text-sm text-muted-foreground sm:inline">{user?.name}</span>
            <button
              type="button"
              onClick={logout}
              className="flex items-center gap-1.5 rounded-md px-3 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-accent/20 hover:text-foreground"
            >
              <LogOut size={15} />
              Sign out
            </button>
          </div>
        </div>
      </header>

      <main className="container flex flex-1 flex-col gap-5 py-6">
        {error && (
          <Card className="border-destructive/30 bg-destructive/10 p-3 text-sm text-destructive">
            {error}
          </Card>
        )}

        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <KpiCard label="Total questions" value={String(totalQuestions)} icon={MessageSquareText} loading={loading} />
          <KpiCard
            label="Avg. response time"
            value={`${avgLatency.toFixed(2)}s`}
            icon={Gauge}
            loading={loading}
          />
          <KpiCard
            label="Avg. confidence"
            value={`${Math.round(avgConfidence * 100)}%`}
            icon={TrendingUp}
            loading={loading}
          />
          <KpiCard label="Documents" value={String(documents.length)} icon={Files} loading={loading} />
        </div>

        <div className="grid grid-cols-1 gap-5 lg:grid-cols-[1.2fr_1fr]">
          <Card className="glass border-none p-4">
            <p className="mb-3 text-sm font-semibold tracking-tight">Documents by department</p>
            {loading ? <Skeleton className="h-64 w-full" /> : <DepartmentChart documents={documents} />}
          </Card>

          <Card className="glass border-none p-4">
            <p className="mb-3 text-sm font-semibold tracking-tight">Upload a document</p>
            <UploadZone onUpload={handleUpload} />
          </Card>
        </div>

        <Card className="glass border-none p-0">
          <div className="flex items-center justify-between p-4 pb-0">
            <p className="text-sm font-semibold tracking-tight">Documents</p>
          </div>
          <DocumentsTable documents={documents} loading={loading} onDelete={handleDelete} />
        </Card>

        <Card className="glass border-none p-4">
          <p className="mb-3 text-sm font-semibold tracking-tight">Recent activity</p>
          {loading ? (
            <div className="flex flex-col gap-2">
              {[...Array(3)].map((_, i) => (
                <Skeleton key={i} className="h-8 w-full" />
              ))}
            </div>
          ) : recentActivity.length === 0 ? (
            <p className="text-sm text-muted-foreground">No questions asked yet.</p>
          ) : (
            <div className="scrollbar-thin overflow-x-auto">
              <table className="w-full min-w-[560px] text-left text-sm">
                <thead>
                  <tr className="border-b border-border/60 text-xs uppercase tracking-wide text-muted-foreground">
                    <th className="px-3 py-2 font-medium">Question</th>
                    <th className="px-3 py-2 font-medium">Status</th>
                    <th className="px-3 py-2 font-medium">Confidence</th>
                    <th className="px-3 py-2 font-medium">Latency</th>
                    <th className="px-3 py-2 font-medium">Asked</th>
                  </tr>
                </thead>
                <tbody>
                  {recentActivity.map((entry) => (
                    <tr key={entry.id} className="border-b border-border/30 last:border-none">
                      <td className="max-w-[280px] truncate px-3 py-2 text-foreground">{entry.question}</td>
                      <td className="px-3 py-2">
                        <Badge variant={entry.status === "success" ? "success" : "outline"}>
                          {entry.status}
                        </Badge>
                      </td>
                      <td className="px-3 py-2 text-muted-foreground">
                        {entry.confidence !== null ? `${Math.round(entry.confidence * 100)}%` : "—"}
                      </td>
                      <td className="px-3 py-2 text-muted-foreground">
                        {entry.latency !== null ? `${entry.latency.toFixed(2)}s` : "—"}
                      </td>
                      <td className="px-3 py-2 text-muted-foreground">
                        {new Date(entry.created_at).toLocaleString()}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </Card>
      </main>
    </div>
  );
}

export default function CompanyPage() {
  return (
    <RouteGuard role="company">
      <CompanyDashboard />
    </RouteGuard>
  );
}
