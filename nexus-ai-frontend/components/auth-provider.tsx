"use client";

import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import {
  clearStoredUser,
  getStoredUser,
  storeUser,
  type AuthUser,
  type UserRole,
} from "@/lib/auth";

interface AuthContextValue {
  user: AuthUser | null;
  ready: boolean;
  login: (email: string, name: string, role: UserRole) => AuthUser;
  register: (email: string, name: string, role: UserRole) => AuthUser;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    setUser(getStoredUser());
    setReady(true);
  }, []);

  const login = (email: string, name: string, role: UserRole) => {
    const nextUser: AuthUser = { email, name: name || email, role };
    storeUser(nextUser);
    setUser(nextUser);
    return nextUser;
  };

  // MVP auth has no real account store, so "register" and "login" both just
  // persist the chosen identity — there is nothing to validate against yet.
  const register = (email: string, name: string, role: UserRole) => login(email, name, role);

  const logout = () => {
    clearStoredUser();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, ready, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within an AuthProvider");
  return ctx;
}
