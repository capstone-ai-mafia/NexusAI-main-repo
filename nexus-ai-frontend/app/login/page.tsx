"use client";

import { useState, type FormEvent } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ShieldCheck } from "lucide-react";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/components/auth-provider";
import { dashboardPathForRole, getStoredUser } from "@/lib/auth";

export default function LoginPage() {
  const { login } = useAuth();
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    if (!email.trim() || !password.trim()) {
      setError("Enter both an email and a password.");
      return;
    }

    // MVP auth: no real credential check, no backend call, no user store —
    // the only "record" of a role is whatever this browser last registered
    // for this email, read straight from localStorage.
    const previous = getStoredUser();
    const role = previous?.email === email ? previous.role : "employee";

    const name = email.split("@")[0];
    const user = login(email, name, role);
    router.replace(dashboardPathForRole(user.role));
  };

  return (
    <div className="flex min-h-screen items-center justify-center px-4 py-10">
      <div className="glass w-full max-w-sm rounded-2xl p-8">
        <div className="mb-6 flex flex-col items-center text-center">
          <span className="mb-3 flex h-11 w-11 items-center justify-center rounded-xl bg-primary text-primary-foreground">
            <ShieldCheck size={22} strokeWidth={2.25} />
          </span>
          <h1 className="text-lg font-semibold tracking-tight">Sign in to Nexus AI</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            Enterprise Knowledge Intelligence
          </p>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div className="flex flex-col gap-1.5">
            <label htmlFor="email" className="text-xs font-medium text-muted-foreground">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="you@company.com"
              className="rounded-lg border border-input bg-background/60 px-3 py-2 text-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
              autoComplete="email"
            />
          </div>

          <div className="flex flex-col gap-1.5">
            <label htmlFor="password" className="text-xs font-medium text-muted-foreground">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              className="rounded-lg border border-input bg-background/60 px-3 py-2 text-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
              autoComplete="current-password"
            />
          </div>

          {error && <p className="text-xs text-destructive">{error}</p>}

          <Button type="submit" className="mt-2 w-full">
            Sign in
          </Button>
        </form>

        <p className="mt-6 text-center text-sm text-muted-foreground">
          Don&apos;t have an account?{" "}
          <Link href="/register" className="font-medium text-primary hover:underline">
            Create one
          </Link>
        </p>
      </div>
    </div>
  );
}
