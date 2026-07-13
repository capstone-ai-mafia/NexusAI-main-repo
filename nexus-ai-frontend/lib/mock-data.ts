import type { Citation, ExampleQuestion, QueryResponse } from "./types";

/**
 * Realistic seed data grounded in the Nexus policy corpus.
 * Each entry maps a set of keyword triggers -> a grounded mock response.
 * The matcher in api.ts does simple keyword scoring against `question`
 * so a range of natural phrasings will still resolve to the right seed.
 */
interface Seed {
  keywords: string[];
  department: Citation["department"];
  answer: string;
  citations: Citation[];
}

const SEEDS: Seed[] = [
  {
    keywords: ["annual leave", "vacation", "pto", "days off", "4 years", "leave days"],
    department: "HR",
    answer:
      "After 4 years of service you are entitled to 23 working days of paid annual leave.",
    citations: [
      {
        doc_id: "HR-001",
        title: "Nexus HR Policy Manual",
        department: "HR",
        section: "§5.1 Annual Leave — Company baseline entitlement",
        snippet: "3–5 years of service: 23 working days (full-time).",
      },
    ],
  },
  {
    keywords: ["itemized receipt", "receipt", "expense report", "reimbursement"],
    department: "Finance",
    answer: "Itemized receipts are required for any expense over $25 USD.",
    citations: [
      {
        doc_id: "FIN-002",
        title: "Finance & Expense Policy",
        department: "Finance",
        section: "§2.3 Receipt Requirements",
        snippet:
          "Employees must submit itemized receipts for any single expense exceeding $25 USD.",
      },
    ],
  },
  {
    keywords: ["30,000", "30000", "purchase approv", "who approves", "vp", "cfo"],
    department: "Finance",
    answer:
      "A purchase of $30,000 requires approval from a VP plus the CFO.",
    citations: [
      {
        doc_id: "FIN-004",
        title: "Finance & Expense Policy",
        department: "Finance",
        section: "§6.2 Purchase Approval Thresholds",
        snippet:
          "$10,001–$50,000: requires VP approval plus CFO sign-off before purchase order is issued.",
      },
    ],
  },
  {
    keywords: ["core collaboration", "collaboration day", "office days", "in office"],
    department: "General",
    answer: "Core Collaboration Days are Tuesday through Thursday.",
    citations: [
      {
        doc_id: "GEN-011",
        title: "Company Profile",
        department: "General",
        section: "§11 Working Norms",
        snippet: "Core Collaboration Days: Tuesday, Wednesday, and Thursday.",
      },
      {
        doc_id: "GEN-002",
        title: "General Company Policies",
        department: "General",
        section: "§2 Hybrid Work Schedule",
        snippet:
          "All employees are expected to be on-site during Core Collaboration Days (Tue–Thu) unless otherwise approved.",
      },
    ],
  },
  {
    keywords: ["phishing", "suspicious link", "suspected phishing"],
    department: "Security",
    answer:
      "Disconnect from the network, report to IT Security, and change affected passwords via NexusVault.",
    citations: [
      {
        doc_id: "SEC-006",
        title: "Information Security Policy",
        department: "Security",
        section: "§6 Incident Response — Phishing",
        snippet:
          "If you click a suspected phishing link: (1) disconnect the device from the network, (2) report the incident to IT Security immediately, (3) change any potentially affected passwords via NexusVault.",
      },
    ],
  },
  {
    keywords: ["password", "password requirement", "password policy"],
    department: "IT",
    answer:
      "Passwords must be at least 14 characters and include upper case, lower case, a number, and a special character. Reuse of the last 10 passwords is not allowed.",
    citations: [
      {
        doc_id: "IT-003",
        title: "Nexus IT Policy",
        department: "IT",
        section: "§3.1 Password Requirements",
        snippet:
          "Minimum 14 characters, including at least one uppercase letter, one lowercase letter, one number, and one special character. The last 10 passwords may not be reused.",
      },
    ],
  },
  {
    keywords: ["nda", "non-disclosure", "confidential", "non disclosure"],
    department: "Legal",
    answer:
      "An NDA is required before sharing confidential information in sales, partnership, vendor, or proof-of-concept engagements.",
    citations: [
      {
        doc_id: "LEG-002",
        title: "Legal & Compliance Manual",
        department: "Legal",
        section: "§2.1 When an NDA Is Required",
        snippet:
          "Confidential information must not be shared with any external party — sales prospects, partners, vendors, or PoC participants — until a mutual or one-way NDA has been fully executed.",
      },
    ],
  },
];

export const EXAMPLE_QUESTIONS: ExampleQuestion[] = [
  { question: "How many annual leave days do I get after 4 years?", department: "HR" },
  { question: "When are itemized receipts required?", department: "Finance" },
  { question: "Who approves a $30,000 purchase?", department: "Finance" },
  { question: "Which days are Core Collaboration Days?", department: "General" },
  {
    question: "What should I do after clicking a suspected phishing link?",
    department: "Security",
  },
  { question: "What are the password requirements?", department: "IT" },
];

function score(question: string, keywords: string[]): number {
  const q = question.toLowerCase();
  return keywords.reduce((acc, kw) => (q.includes(kw) ? acc + kw.length : acc), 0);
}

export function resolveMockResponse(
  question: string,
  department: string
): QueryResponse {
  const start = Date.now();
  const deptFilter = department && department !== "All" && department !== "all" ? department : null;

  const candidates = SEEDS.filter((s) => !deptFilter || s.department === deptFilter);
  let best: Seed | null = null;
  let bestScore = 0;

  for (const seed of candidates) {
    const s = score(question, seed.keywords);
    if (s > bestScore) {
      bestScore = s;
      best = seed;
    }
  }

  // Simulated network/inference latency, kept comfortably under the 3s target.
  const latency = 900 + Math.round(Math.random() * 1400);

  if (!best || bestScore === 0) {
    return {
      answer: "",
      grounded: false,
      latency_ms: latency,
      citations: [],
    };
  }

  return {
    answer: best.answer,
    grounded: true,
    latency_ms: latency,
    citations: best.citations,
  };
}
