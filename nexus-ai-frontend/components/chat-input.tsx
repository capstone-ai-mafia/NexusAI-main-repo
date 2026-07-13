"use client";

import { useRef, useState, type KeyboardEvent } from "react";
import { ArrowUp } from "lucide-react";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { DepartmentSelector } from "@/components/department-selector";
import type { Department } from "@/lib/types";

interface Props {
  department: Department;
  onDepartmentChange: (dept: Department) => void;
  onSubmit: (question: string) => void;
  disabled?: boolean;
}

export function ChatInput({ department, onDepartmentChange, onSubmit, disabled }: Props) {
  const [value, setValue] = useState("");
  const ref = useRef<HTMLTextAreaElement>(null);

  const submit = () => {
    const trimmed = value.trim();
    if (!trimmed || disabled) return;
    onSubmit(trimmed);
    setValue("");
    requestAnimationFrame(() => ref.current?.focus());
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      submit();
    }
  };

  return (
    <div className="rounded-xl border border-border bg-card p-3 shadow-sm">
      <div className="mb-3">
        <DepartmentSelector value={department} onChange={onDepartmentChange} disabled={disabled} />
      </div>
      <div className="flex items-end gap-2">
        <Textarea
          ref={ref}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask about an internal policy — e.g. “When are itemized receipts required?”"
          aria-label="Ask Nexus AI a question"
          rows={1}
          disabled={disabled}
          className="min-h-[44px] max-h-40 border-none px-2 py-2.5 shadow-none focus-visible:ring-0"
        />
        <Button
          type="button"
          size="icon"
          aria-label="Send question"
          disabled={disabled || value.trim().length === 0}
          onClick={submit}
          className="h-10 w-10 shrink-0 rounded-full"
        >
          <ArrowUp className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}
