"use client";

import { Badge } from "@/components/ui/badge";
import { AnswerCard } from "@/components/answer-card";
import { LoadingCard } from "@/components/loading-card";
import { ErrorCard } from "@/components/error-card";
import type { ConversationTurn } from "@/lib/types";

interface Props {
  turns: ConversationTurn[];
  onRetry: (turnId: string) => void;
}

export function ConversationThread({ turns, onRetry }: Props) {
  return (
    <div className="flex flex-col gap-6">
      {turns.map((turn) => (
        <div key={turn.id} className="flex flex-col gap-3">
          <div className="flex justify-end">
            <div className="max-w-2xl rounded-2xl rounded-tr-sm bg-primary px-4 py-2.5 text-sm text-primary-foreground">
              <p>{turn.question}</p>
              {turn.department !== "All" && (
                <Badge
                  variant="outline"
                  className="mt-1.5 border-primary-foreground/30 text-[10px] text-primary-foreground/80"
                >
                  {turn.department}
                </Badge>
              )}
            </div>
          </div>

          <div className="flex justify-start">
            {turn.status === "loading" && <LoadingCard />}
            {turn.status === "error" && (
              <ErrorCard
                message={turn.errorMessage ?? "Something went wrong."}
                onRetry={() => onRetry(turn.id)}
              />
            )}
            {turn.status === "success" && turn.response && (
              <AnswerCard response={turn.response} />
            )}
          </div>
        </div>
      ))}
    </div>
  );
}
