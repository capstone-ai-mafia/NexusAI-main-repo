"use client";

import { useCallback, useRef, useState } from "react";
import { Header } from "@/components/header";
import { ChatInput } from "@/components/chat-input";
import { ConversationThread } from "@/components/conversation-thread";
import { EmptyState } from "@/components/empty-state";
import { postQuery, ApiError } from "@/lib/api";
import type { ConversationTurn, Department, ExampleQuestion } from "@/lib/types";

function makeId() {
  return `turn_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
}

export default function HomePage() {
  const [department, setDepartment] = useState<Department>("All");
  const [turns, setTurns] = useState<ConversationTurn[]>([]);
  const scrollRef = useRef<HTMLDivElement>(null);

  const runQuery = useCallback(async (turnId: string, question: string, dept: Department) => {
    try {
      const response = await postQuery({ question, department: dept });
      setTurns((prev) =>
        prev.map((t) => (t.id === turnId ? { ...t, status: "success", response } : t))
      );
    } catch (err) {
      const message = err instanceof ApiError ? err.message : "Unexpected error. Please retry.";
      setTurns((prev) =>
        prev.map((t) => (t.id === turnId ? { ...t, status: "error", errorMessage: message } : t))
      );
    } finally {
      requestAnimationFrame(() => {
        scrollRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
      });
    }
  }, []);

  const handleSubmit = useCallback(
    (question: string) => {
      const id = makeId();
      const turn: ConversationTurn = { id, question, department, status: "loading" };
      setTurns((prev) => [...prev, turn]);
      requestAnimationFrame(() => {
        scrollRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
      });
      void runQuery(id, question, department);
    },
    [department, runQuery]
  );

  const handleExample = useCallback(
    (example: ExampleQuestion) => {
      setDepartment(example.department);
      const id = makeId();
      const turn: ConversationTurn = {
        id,
        question: example.question,
        department: example.department,
        status: "loading",
      };
      setTurns((prev) => [...prev, turn]);
      void runQuery(id, example.question, example.department);
    },
    [runQuery]
  );

  const handleRetry = useCallback(
    (turnId: string) => {
      const turn = turns.find((t) => t.id === turnId);
      if (!turn) return;
      setTurns((prev) => prev.map((t) => (t.id === turnId ? { ...t, status: "loading" } : t)));
      void runQuery(turnId, turn.question, turn.department);
    },
    [turns, runQuery]
  );

  const isBusy = turns.some((t) => t.status === "loading");

  return (
    <div className="flex min-h-screen flex-col">
      <Header />

      <main className="container flex flex-1 flex-col py-6">
        {turns.length === 0 ? (
          <EmptyState onPick={handleExample} />
        ) : (
          <div className="scrollbar-thin flex-1 overflow-y-auto pb-4">
            <ConversationThread turns={turns} onRetry={handleRetry} />
            <div ref={scrollRef} />
          </div>
        )}

        <div className="sticky bottom-4 mt-6">
          <ChatInput
            department={department}
            onDepartmentChange={setDepartment}
            onSubmit={handleSubmit}
            disabled={isBusy}
          />
          <p className="mt-2 text-center text-[11px] text-muted-foreground">
            Nexus AI answers are grounded in internal policy documents and always cite their
            source. When no grounded source is found, no answer is fabricated.
          </p>
        </div>
      </main>
    </div>
  );
}
