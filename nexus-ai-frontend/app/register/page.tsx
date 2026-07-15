"use client";

import { useState, type FormEvent } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Briefcase, ShieldCheck, User } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { useAuth } from "@/components/auth-provider";
import { dashboardPathForRole, type UserRole } from "@/lib/auth";

export default function RegisterPage() {
  const { register } = useAuth();
  const router = useRouter();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState<UserRole>("employee");
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    if (!name.trim() || !email.trim() || !password.trim()) {
      setError("Fill in your name, email, and password.");
      return;
    }

    // MVP auth: this only writes to localStorage, there is no backend
    // account creation — any role choice is accepted at face value.
    const user = register(email, name, role);
    router.replace(dashboardPathForRole(user.role));
  };

  return (
    <div className="flex min-h-screen items-center justify-center px-4 py-10">
      <div className="glass w-full max-w-sm rounded-2xl p-8">
        <div className="mb-6 flex flex-col items-center text-center">
          <span className="mb-3 flex h-11 w-11 items-center justify-center rounded-xl bg-primary text-primary-foreground">
            <ShieldCheck size={22} strokeWidth={2.25} />
          </span>
          <h1 className="text-lg font-semibold tracking-tight">Create your account</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            Join Nexus AI Enterprise Knowledge Intelligence
          </p>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div className="flex flex-col gap-1.5">
            <label htmlFor="name" className="text-xs font-medium text-muted-foreground">
              Full name
            </label>
            <input
              id="name"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Jane Doe"
              className="rounded-lg border border-input bg-background/60 px-3 py-2 text-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
              autoComplete="name"
            />
          </div>

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
              autoComplete="new-password"
            />
          </div>

          <div className="flex flex-col gap-1.5">
            <span className="text-xs font-medium text-muted-foreground">I am a</span>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => setRole("employee")}
                className={cn(
                  "flex flex-col items-center gap-1.5 rounded-lg border px-3 py-3 text-sm transition-colors",
                  role === "employee"
                    ? "border-primary bg-primary/15 text-foreground"
                    : "border-border bg-background/40 text-muted-foreground hover:bg-accent/20"
                )}
              >
                <User size={18} />
                Employee
              </button>
              <button
                type="button"
                onClick={() => setRole("company")}
                className={cn(
                  "flex flex-col items-center gap-1.5 rounded-lg border px-3 py-3 text-sm transition-colors",
                  role === "company"
                    ? "border-primary bg-primary/15 text-foreground"
                    : "border-border bg-background/40 text-muted-foreground hover:bg-accent/20"
                )}
              >
                <Briefcase size={18} />
                Company / Admin
              </button>
            </div>
          </div>

          {error && <p className="text-xs text-destructive">{error}</p>}

          <Button type="submit" className="mt-2 w-full">
            Create account
          </Button>
        </form>

        <p className="mt-6 text-center text-sm text-muted-foreground">
          Already have an account?{" "}
          <Link href="/login" className="font-medium text-primary hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
