"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { History, LogOut, ShieldCheck } from "lucide-react";
import { RouteGuard } from "@/components/route-guard";
import { useAuth } from "@/components/auth-provider";
import { ChatInput } from "@/components/chat-input";
import { ConversationThread } from "@/components/conversation-thread";
import { EmptyState } from "@/components/empty-state";
import { Card } from "@/components/ui/card";
import { postQuery, ApiError } from "@/lib/api";
import type { ConversationTurn, Department } from "@/lib/types";

const SUGGESTED_QUESTIONS = [
  "What is the vacation policy?",
  "How long does probation last for a new employee?",
  "What expenses require itemized receipts?",
  "What is the password policy for company systems?",
  "What is Nexus Technologies' incident response process?",
];

interface HistoryEntry {
  id: string;
  question: string;
  answer: string;
  createdAt: string;
}

function makeId() {
  return `turn_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
}

function historyKey(email: string) {
  return `nexus_history_${email}`;
}

function loadHistory(email: string): HistoryEntry[] {
  try {
    const raw = window.localStorage.getItem(historyKey(email));
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

function saveHistory(email: string, entries: HistoryEntry[]) {
  window.localStorage.setItem(historyKey(email), JSON.stringify(entries.slice(0, 50)));
}

function EmployeeDashboard() {
  const { user, logout } = useAuth();
  const [turns, setTurns] = useState<ConversationTurn[]>([]);
  const [history, setHistory] = useState<HistoryEntry[]>([]);
  const [sessionCount, setSessionCount] = useState(0);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (user) setHistory(loadHistory(user.email));
  }, [user]);

  const runQuery = useCallback(
    async (turnId: string, question: string) => {
      try {
        const response = await postQuery({ question, department: "All" });
        setTurns((prev) =>
          prev.map((t) => (t.id === turnId ? { ...t, status: "success", response } : t))
        );

        if (user) {
          const entry: HistoryEntry = {
            id: turnId,
            question,
            answer: response.grounded ? response.answer : "No grounded answer found.",
            createdAt: new Date().toISOString(),
          };
          setHistory((prev) => {
            const next = [entry, ...prev];
            saveHistory(user.email, next);
            return next;
          });
        }
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
    },
    [user]
  );

  const askQuestion = useCallback(
    (question: string) => {
      const id = makeId();
      const turn: ConversationTurn = { id, question, department: "All", status: "loading" };
      setTurns((prev) => [...prev, turn]);
      setSessionCount((prev) => prev + 1);
      requestAnimationFrame(() => {
        scrollRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
      });
      void runQuery(id, question);
    },
    [runQuery]
  );

  const handleRetry = useCallback(
    (turnId: string) => {
      const turn = turns.find((t) => t.id === turnId);
      if (!turn) return;
      setTurns((prev) => prev.map((t) => (t.id === turnId ? { ...t, status: "loading" } : t)));
      void runQuery(turnId, turn.question);
    },
    [turns, runQuery]
  );

  const isBusy = turns.some((t) => t.status === "loading");

  return (
    <div className="flex h-screen flex-col overflow-hidden">
      <header className="glass shrink-0 border-x-0 border-t-0">
        <div className="container flex h-16 items-center justify-between">
          <div className="flex items-center gap-2.5">
            <span className="flex h-8 w-8 items-center justify-center rounded-md bg-primary text-primary-foreground">
              <ShieldCheck size={18} strokeWidth={2.25} />
            </span>
            <span className="flex flex-col leading-tight">
              <span className="text-sm font-semibold tracking-tight">Nexus AI</span>
              <span className="text-[11px] text-muted-foreground">Employee Workspace</span>
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

      <main className="container flex flex-1 flex-col gap-4 overflow-hidden py-6">
        <Card className="glass shrink-0 border-none p-4">
          <p className="text-lg font-semibold tracking-tight">Welcome, {user?.name}</p>
          <p className="mt-1 text-sm text-muted-foreground">
            Ask about HR, IT, Finance, Legal, or Security policy — every answer is grounded and
            cited.
          </p>

          <div className="mt-3 flex flex-wrap items-center gap-2">
            {SUGGESTED_QUESTIONS.map((q) => (
              <button
                key={q}
                type="button"
                disabled={isBusy}
                onClick={() => askQuestion(q)}
                className="rounded-full border border-border bg-background/40 px-3 py-1.5 text-xs font-medium text-muted-foreground transition-colors hover:border-primary/40 hover:bg-accent/20 hover:text-foreground disabled:cursor-not-allowed disabled:opacity-50"
              >
                {q}
              </button>
            ))}
          </div>

          <div className="mt-3 flex items-center gap-1.5 text-xs text-muted-foreground">
            <History size={13} />
            {sessionCount} question{sessionCount === 1 ? "" : "s"} asked this session
          </div>
        </Card>

        <div className="grid flex-1 grid-cols-1 gap-4 overflow-hidden lg:grid-cols-[1fr_280px]">
          <div className="flex min-h-0 flex-col">
            <div className="scrollbar-thin flex-1 overflow-y-auto pb-4">
              {turns.length === 0 ? (
                <EmptyState onPick={(ex) => askQuestion(ex.question)} />
              ) : (
                <>
                  <ConversationThread turns={turns} onRetry={handleRetry} />
                  <div ref={scrollRef} />
                </>
              )}
            </div>

            <div className="mt-4 shrink-0">
              <ChatInput
                department={"All" as Department}
                onDepartmentChange={() => {}}
                onSubmit={askQuestion}
                disabled={isBusy}
              />
            </div>
          </div>

          <Card className="glass h-full overflow-y-auto border-none p-4">
            <p className="mb-3 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
              My history
            </p>
            {history.length === 0 ? (
              <p className="text-sm text-muted-foreground">No questions yet.</p>
            ) : (
              <ul className="flex flex-col gap-3">
                {history.map((entry) => (
                  <li key={entry.id} className="border-b border-border/50 pb-2 last:border-none">
                    <p className="line-clamp-2 text-sm text-foreground">{entry.question}</p>
                    <p className="mt-0.5 text-[11px] text-muted-foreground">
                      {new Date(entry.createdAt).toLocaleString()}
                    </p>
                  </li>
                ))}
              </ul>
            )}
          </Card>
        </div>
      </main>
    </div>
  );
}

export default function EmployeePage() {
  return (
    <RouteGuard role="employee">
      <EmployeeDashboard />
    </RouteGuard>
  );
}
