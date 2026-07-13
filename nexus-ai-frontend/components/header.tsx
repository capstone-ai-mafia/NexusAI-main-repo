import Link from "next/link";
import { ShieldCheck } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { IS_MOCK_MODE } from "@/lib/api";

export function Header() {
  return (
    <header className="border-b border-border bg-card/60 backdrop-blur supports-[backdrop-filter]:bg-card/60">
      <div className="container flex h-16 items-center justify-between">
        <Link href="/" className="flex items-center gap-2.5">
          <span className="flex h-8 w-8 items-center justify-center rounded-md bg-primary text-primary-foreground">
            <ShieldCheck size={18} strokeWidth={2.25} />
          </span>
          <span className="flex flex-col leading-tight">
            <span className="text-sm font-semibold tracking-tight">Nexus AI</span>
            <span className="text-[11px] text-muted-foreground">
              Enterprise Knowledge Intelligence
            </span>
          </span>
        </Link>

        <nav className="flex items-center gap-3">
          {IS_MOCK_MODE && (
            <Badge variant="outline" className="hidden font-normal text-muted-foreground sm:inline-flex">
              Mock data mode
            </Badge>
          )}
          <Link
            href="/evaluation"
            className="rounded-md px-3 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-accent hover:text-accent-foreground"
          >
            Evaluation
          </Link>
        </nav>
      </div>
    </header>
  );
}
