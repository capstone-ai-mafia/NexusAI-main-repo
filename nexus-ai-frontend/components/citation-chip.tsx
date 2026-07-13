"use client";

import { useState } from "react";
import { ChevronDown, FileText } from "lucide-react";
import { cn } from "@/lib/utils";
import type { Citation } from "@/lib/types";

export function CitationChip({ citation, index }: { citation: Citation; index: number }) {
  const [open, setOpen] = useState(false);
  const panelId = `citation-panel-${citation.doc_id}-${index}`;

  return (
    <div className="overflow-hidden rounded-lg border border-border bg-background">
      <button
        type="button"
        aria-expanded={open}
        aria-controls={panelId}
        onClick={() => setOpen((o) => !o)}
        className="flex w-full items-center gap-2.5 px-3 py-2 text-left transition-colors hover:bg-accent/60 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
      >
        <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-md bg-accent text-accent-foreground">
          <FileText size={13} strokeWidth={2.25} />
        </span>
        <span className="min-w-0 flex-1">
          <span className="block truncate text-xs font-semibold text-foreground">
            {citation.title}
          </span>
          <span className="block truncate text-[11px] text-muted-foreground">
            {citation.section}
          </span>
        </span>
        <ChevronDown
          size={15}
          className={cn("shrink-0 text-muted-foreground transition-transform", open && "rotate-180")}
        />
      </button>
      {open && (
        <div id={panelId} className="animate-fade-in border-t border-border bg-muted/40 px-3 py-2.5">
          <p className="text-xs leading-relaxed text-foreground/80">
            &ldquo;{citation.snippet}&rdquo;
          </p>
          <p className="mt-1.5 text-[10px] uppercase tracking-wide text-muted-foreground">
            {citation.doc_id} · {citation.department}
          </p>
        </div>
      )}
    </div>
  );
}
