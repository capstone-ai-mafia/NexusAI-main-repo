import { AlertTriangle, RotateCw } from "lucide-react";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export function ErrorCard({ message, onRetry }: { message: string; onRetry: () => void }) {
  return (
    <Card
      className="animate-fade-in max-w-2xl border-destructive/30 bg-destructive/5 p-4"
      role="alert"
    >
      <div className="flex items-start gap-3">
        <span className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-destructive/10 text-destructive">
          <AlertTriangle size={15} />
        </span>
        <div className="flex-1">
          <p className="text-sm font-semibold text-foreground">Couldn&apos;t reach Nexus AI</p>
          <p className="mt-1 text-sm text-muted-foreground">{message}</p>
          <Button size="sm" variant="outline" className="mt-3" onClick={onRetry}>
            <RotateCw size={13} className="mr-1.5" />
            Retry
          </Button>
        </div>
      </div>
    </Card>
  );
}
