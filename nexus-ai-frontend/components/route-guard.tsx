"use client";

import { useEffect, type ReactNode } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/components/auth-provider";
import { dashboardPathForRole, type UserRole } from "@/lib/auth";

interface Props {
  role: UserRole;
  children: ReactNode;
}

export function RouteGuard({ role, children }: Props) {
  const { user, ready } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!ready) return;

    if (!user) {
      router.replace("/login");
      return;
    }

    if (user.role !== role) {
      router.replace(dashboardPathForRole(user.role));
    }
  }, [ready, user, role, router]);

  if (!ready || !user || user.role !== role) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="glass rounded-2xl px-6 py-4 text-sm text-muted-foreground">
          Loading…
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
