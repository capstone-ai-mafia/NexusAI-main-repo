import Link from "next/link";
import { ArrowLeft, BarChart3 } from "lucide-react";
import { Header } from "@/components/header";
import { Card } from "@/components/ui/card";

export const metadata = {
  title: "Evaluation | Nexus AI",
};

export default function EvaluationPage() {
  return (
    <div className="flex min-h-screen flex-col">
      <Header />
      <main className="container flex flex-1 items-center justify-center py-16">
        <Card className="max-w-md p-8 text-center">
          <span className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-accent text-accent-foreground">
            <BarChart3 size={22} />
          </span>
          <h1 className="text-lg font-semibold text-foreground">Evaluation dashboard</h1>
          <p className="mt-2 text-sm text-muted-foreground">
            Retrieval &amp; groundedness metrics (precision, latency distribution, citation
            coverage) are being built separately. This route is a placeholder stub so the nav
            link resolves.
          </p>
          <Link
            href="/"
            className="mt-6 inline-flex items-center gap-1.5 text-sm font-medium text-primary hover:underline"
          >
            <ArrowLeft size={14} />
            Back to Ask
          </Link>
        </Card>
      </main>
    </div>
  );
}
