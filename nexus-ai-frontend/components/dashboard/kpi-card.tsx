import type { LucideIcon } from "lucide-react";
import { Card } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

interface Props {
  label: string;
  value: string;
  icon: LucideIcon;
  loading?: boolean;
}

export function KpiCard({ label, value, icon: Icon, loading }: Props) {
  return (
    <Card className="glass border-none p-4">
      <div className="flex items-center gap-3">
        <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-primary/15 text-primary">
          <Icon size={18} />
        </span>
        <div className="min-w-0">
          <p className="text-xs font-medium text-muted-foreground">{label}</p>
          {loading ? (
            <Skeleton className="mt-1 h-6 w-16" />
          ) : (
            <p className="truncate text-xl font-semibold tracking-tight">{value}</p>
          )}
        </div>
      </div>
    </Card>
  );
}
