"use client";

import { DEPARTMENTS, DEPARTMENT_LABELS, type Department } from "@/lib/types";
import { cn } from "@/lib/utils";

interface Props {
  value: Department;
  onChange: (dept: Department) => void;
  disabled?: boolean;
}

export function DepartmentSelector({ value, onChange, disabled }: Props) {
  return (
    <div
      role="radiogroup"
      aria-label="Filter by department"
      className="flex flex-wrap gap-1.5"
    >
      {DEPARTMENTS.map((dept) => {
        const active = value === dept;
        return (
          <button
            key={dept}
            type="button"
            role="radio"
            aria-checked={active}
            disabled={disabled}
            onClick={() => onChange(dept)}
            className={cn(
              "rounded-full border px-3 py-1.5 text-xs font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
              active
                ? "border-primary bg-primary text-primary-foreground"
                : "border-border bg-background text-muted-foreground hover:bg-accent hover:text-accent-foreground"
            )}
          >
            {DEPARTMENT_LABELS[dept]}
          </button>
        );
      })}
    </div>
  );
}
