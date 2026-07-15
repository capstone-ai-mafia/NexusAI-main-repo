"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/components/auth-provider";
import { dashboardPathForRole } from "@/lib/auth";

export default function RootPage() {
  const { user, ready } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!ready) return;
    router.replace(user ? dashboardPathForRole(user.role) : "/login");
  }, [ready, user, router]);

  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="glass rounded-2xl px-6 py-4 text-sm text-muted-foreground">Loading…</div>
    </div>
  );
}
