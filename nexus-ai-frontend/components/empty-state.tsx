"use client";

import { Sparkles } from "lucide-react";
import { Card } from "@/components/ui/card";
import { DEPARTMENT_LABELS } from "@/lib/types";
import { EXAMPLE_QUESTIONS } from "@/lib/mock-data";
import type { ExampleQuestion } from "@/lib/types";

interface Props {
  onPick: (example: ExampleQuestion) => void;
}

export function EmptyState({ onPick }: Props) {
  return (
    <div className="flex flex-1 flex-col items-center justify-center py-10 text-center">
      <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-accent text-accent-foreground">
        <Sparkles size={22} strokeWidth={2} />
      </span>
      <h1 className="text-xl font-semibold tracking-tight text-foreground">
        Ask Nexus AI about company policy
      </h1>
      <p className="mt-2 max-w-md text-sm text-muted-foreground">
        Every answer is grounded in your internal document corpus and cited down to the exact
        section — grounded, not guessed.
      </p>

      <div className="mt-8 grid w-full max-w-2xl gap-2.5 sm:grid-cols-2">
        {EXAMPLE_QUESTIONS.map((ex) => (
          <Card
            key={ex.question}
            role="button"
            tabIndex={0}
            onClick={() => onPick(ex)}
            onKeyDown={(e) => {
              if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                onPick(ex);
              }
            }}
            className="cursor-pointer p-3.5 text-left transition-colors hover:border-primary/40 hover:bg-accent/50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          >
            <span className="mb-1.5 inline-block rounded-full bg-secondary px-2 py-0.5 text-[10px] font-medium uppercase tracking-wide text-secondary-foreground">
              {DEPARTMENT_LABELS[ex.department]}
            </span>
            <p className="text-sm text-foreground">{ex.question}</p>
          </Card>
        ))}
      </div>
    </div>
  );
}
