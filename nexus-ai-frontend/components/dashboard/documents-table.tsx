"use client";

import { useState } from "react";
import { Loader2, Trash2 } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import type { DocumentRecord } from "@/lib/types";

interface Props {
  documents: DocumentRecord[];
  loading?: boolean;
  onDelete: (id: number) => Promise<void>;
}

function formatSize(bytes: number | null) {
  if (bytes === null || bytes === undefined) return "—";
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

function formatDate(value: string | null) {
  if (!value) return "—";
  return new Date(value).toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

export function DocumentsTable({ documents, loading, onDelete }: Props) {
  const [deletingId, setDeletingId] = useState<number | null>(null);

  const handleDelete = async (id: number) => {
    setDeletingId(id);
    try {
      await onDelete(id);
    } finally {
      setDeletingId(null);
    }
  };

  if (loading) {
    return (
      <div className="flex flex-col gap-2 p-4">
        {[...Array(4)].map((_, i) => (
          <Skeleton key={i} className="h-10 w-full" />
        ))}
      </div>
    );
  }

  if (documents.length === 0) {
    return <p className="p-4 text-sm text-muted-foreground">No documents uploaded yet.</p>;
  }

  return (
    <div className="scrollbar-thin overflow-x-auto">
      <table className="w-full min-w-[640px] text-left text-sm">
        <thead>
          <tr className="border-b border-border/60 text-xs uppercase tracking-wide text-muted-foreground">
            <th className="px-4 py-3 font-medium">Name</th>
            <th className="px-4 py-3 font-medium">Department</th>
            <th className="px-4 py-3 font-medium">Type</th>
            <th className="px-4 py-3 font-medium">Size</th>
            <th className="px-4 py-3 font-medium">Status</th>
            <th className="px-4 py-3 font-medium">Uploaded</th>
            <th className="px-4 py-3 font-medium text-right">Actions</th>
          </tr>
        </thead>
        <tbody>
          {documents.map((doc) => (
            <tr key={doc.id} className="border-b border-border/30 last:border-none">
              <td className="max-w-[220px] truncate px-4 py-3 text-foreground">{doc.filename}</td>
              <td className="px-4 py-3 text-muted-foreground">{doc.department ?? "—"}</td>
              <td className="px-4 py-3 text-muted-foreground">{doc.file_type ?? "—"}</td>
              <td className="px-4 py-3 text-muted-foreground">{formatSize(doc.file_size)}</td>
              <td className="px-4 py-3">
                <Badge variant={doc.status === "processed" ? "success" : "outline"}>
                  {doc.status}
                </Badge>
              </td>
              <td className="px-4 py-3 text-muted-foreground">{formatDate(doc.uploaded_at)}</td>
              <td className="px-4 py-3 text-right">
                <button
                  type="button"
                  aria-label={`Delete ${doc.filename}`}
                  disabled={deletingId === doc.id}
                  onClick={() => void handleDelete(doc.id)}
                  className="inline-flex h-8 w-8 items-center justify-center rounded-md text-muted-foreground transition-colors hover:bg-destructive/15 hover:text-destructive disabled:cursor-not-allowed disabled:opacity-50"
                >
                  {deletingId === doc.id ? (
                    <Loader2 size={15} className="animate-spin" />
                  ) : (
                    <Trash2 size={15} />
                  )}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
