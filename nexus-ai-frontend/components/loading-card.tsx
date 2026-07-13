import { Skeleton } from "@/components/ui/skeleton";
import { Card } from "@/components/ui/card";

export function LoadingCard() {
  return (
    <Card className="animate-fade-in max-w-2xl p-4" role="status" aria-live="polite">
      <span className="sr-only">Nexus AI is retrieving a grounded answer…</span>
      <div className="mb-3 flex items-center gap-2">
        <span className="flex gap-1" aria-hidden="true">
          <span className="h-1.5 w-1.5 animate-pulse-dot rounded-full bg-primary [animation-delay:0ms]" />
          <span className="h-1.5 w-1.5 animate-pulse-dot rounded-full bg-primary [animation-delay:160ms]" />
          <span className="h-1.5 w-1.5 animate-pulse-dot rounded-full bg-primary [animation-delay:320ms]" />
        </span>
        <span className="text-xs font-medium text-muted-foreground">
          Searching the policy corpus…
        </span>
      </div>
      <div className="space-y-2">
        <Skeleton className="h-3.5 w-[85%]" />
        <Skeleton className="h-3.5 w-[95%]" />
        <Skeleton className="h-3.5 w-[60%]" />
      </div>
      <div className="mt-4 flex gap-2">
        <Skeleton className="h-7 w-32 rounded-full" />
        <Skeleton className="h-7 w-28 rounded-full" />
      </div>
    </Card>
  );
}
