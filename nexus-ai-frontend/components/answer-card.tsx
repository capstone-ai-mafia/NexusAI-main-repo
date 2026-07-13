import {
  CheckCircle2,
  SearchX,
  Zap,
} from "lucide-react";

import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CitationChip } from "@/components/citation-chip";
import { KnowledgeGraph } from "@/components/knowledge-graph";

import type { QueryResponse } from "@/lib/types";

function LatencyBadge({ ms }: { ms: number }) {
  const seconds = (ms / 1000).toFixed(1);
  const fast = ms <= 3000;

  return (
    <Badge
      variant={fast ? "success" : "outline"}
      className="gap-1 font-normal"
    >
      <Zap size={11} />
      {seconds}s
    </Badge>
  );
}

export function AnswerCard({
  response,
}: {
  response: QueryResponse;
}) {
  if (
    !response.grounded ||
    response.citations.length === 0
  ) {
    return (
      <Card className="animate-fade-in max-w-2xl p-4">
        <div className="flex items-start gap-3">
          <span className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-muted text-muted-foreground">
            <SearchX size={15} />
          </span>

          <div className="flex-1">
            <p className="text-sm font-semibold text-foreground">
              No supported answer found
            </p>

            <p className="mt-1 text-sm leading-relaxed text-muted-foreground">
              Nexus AI couldn&apos;t find a passage in the
              policy corpus grounded enough to answer this
              confidently, so no answer is shown. Try
              rephrasing the question, widening the department
              filter to &ldquo;All&rdquo;, or asking about a
              different topic.
            </p>

            <div className="mt-3">
              <LatencyBadge ms={response.latency_ms} />
            </div>
          </div>
        </div>
      </Card>
    );
  }

  return (
    <Card className="animate-fade-in w-full max-w-5xl p-4 md:p-5">
      <div className="flex items-start gap-3">
        <span className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-success/10 text-success">
          <CheckCircle2 size={15} />
        </span>

        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-center gap-2">
            <Badge
              variant="success"
              className="gap-1 font-normal"
            >
              Grounded
            </Badge>

            <LatencyBadge ms={response.latency_ms} />
          </div>

          <p className="mt-3 text-sm leading-7 text-foreground">
            {response.answer}
          </p>

          {response.graph &&
            response.graph.nodes.length > 0 && (
              <KnowledgeGraph graph={response.graph} />
            )}

          <div className="mt-5">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-wide text-muted-foreground">
              Sources ({response.citations.length})
            </p>

            <div className="flex flex-col gap-1.5">
              {response.citations.map((citation, index) => (
                <CitationChip
                  key={`${citation.doc_id}-${index}`}
                  citation={citation}
                  index={index}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </Card>
  );
}
