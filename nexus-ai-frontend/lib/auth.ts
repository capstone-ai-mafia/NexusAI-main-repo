// MVP authentication — UI only, no real security. Any email/password combo is
// accepted and the user picks their own role at registration. There is no
// backend auth endpoint yet; this is a placeholder ready to be swapped for a
// real /api/auth flow (JWT, password hashing, etc.) later.

export type UserRole = "employee" | "company";

export interface AuthUser {
  name: string;
  email: string;
  role: UserRole;
}

const STORAGE_KEY = "nexus_auth";

export function getStoredUser(): AuthUser | null {
  if (typeof window === "undefined") return null;

  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as Partial<AuthUser>;
    if (!parsed.email || !parsed.role) return null;
    return {
      name: parsed.name ?? parsed.email,
      email: parsed.email,
      role: parsed.role === "company" ? "company" : "employee",
    };
  } catch {
    return null;
  }
}

export function storeUser(user: AuthUser) {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(user));
}

export function clearStoredUser() {
  window.localStorage.removeItem(STORAGE_KEY);
}

export function dashboardPathForRole(role: UserRole): string {
  return role === "company" ? "/company" : "/employee";
}
