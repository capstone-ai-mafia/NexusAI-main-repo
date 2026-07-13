# Team Contract — AI Capstone Project

**Team Name:** Capstone AI Mafia
**Sprint Duration:** 2 Weeks
**Document Owner:** Luma Alazzeh & Alaa Falugi (Team Co-Leaders)
**Status:** Active — reviewed at sprint mid-point

---

## 1. Team Roster

| Full Name | GitHub Handle & Portfolio | Project Role | Primary Strengths | Secondary Strengths | Expected Contribution | Preferred Contact Hours | Name Pronunciation (Demo Day) |
|---|---|---|---|---|---|---|---|
| **Luma Alazzeh** | @alazzehluma03-afk · [portfolio](https://alazzehluma03-afk.github.io/) | AI Lead / ML Pipeline & Knowledge Graph Coordinator | ML pipeline design, RAG evaluation, PyTorch, ETL foundations, architecture decision-making | SQL analytics, NLP/NER, anomaly-detection thinking | Owns model/RAG evaluation metrics, coordinates how the Knowledge Graph integrates with retrieval, and makes final architecture calls (merges to `main` still require two teammate approvals, same as everyone) | 10:00 AM – 6:00 PM (Sun–Thu), async in evenings | "LOO-ma Al-AZ-zeh" |
| **Alaa Falugi** | @alaafalugi88-arch · [portfolio](https://alaafalugi88-arch.github.io/alaa-falugi/) | RAG Engineer / FastAPI & Prompt Engineering Lead | RAG pipeline construction, FastAPI service design, prompt engineering, embeddings-based retrieval | Business analysis, client communication, requirements translation | Owns the retrieval pipeline (embedding generation, vector search, prompt construction) and the FastAPI endpoints exposing it; leads prompt design and iteration for LLM response quality | 11:00 AM – 7:00 PM (Sun–Thu) | "Uh-LAH Fah-LOO-jee" |
| **Majd Albashtawi** | @bishtawimajed-afk · [portfolio](https://bishtawimajed-afk.github.io/) | Data Engineer / Vector DB & Knowledge Graph Data Prep | PostgreSQL, ETL pipeline construction, data validation, structuring data for graph and vector representations | HTML/CSS/JS basics, computer vision fundamentals | Owns the data layer: PostgreSQL schema, vector database ingestion, and preparing structured entities/relationships that feed the Knowledge Graph | 12:00 PM – 8:00 PM (Sun–Thu) | "Majd Al-bash-TAH-wi" |
| **Zaid Jafari** | @zaidjafari · [portfolio](https://zaidjafari.github.io/portfolio/#about) | Backend & Full-Stack Integration Engineer / System Architecture | Full-stack web engineering, prior RAG system build experience (QG-RAG), FastAPI integration, systems thinking | Business analysis, embedded systems, interface design | Owns end-to-end integration — wiring the frontend, Alaa's RAG/FastAPI backend, and Majd's data/vector layer into one working, deployable application; owns overall system architecture diagrams | 1:00 PM – 9:00 PM (Sun–Thu) | "Zayd Ja-FAH-ree" |
| **Ameer Esam Hussein** | @ameer-00 · [portfolio](https://ameer-00.github.io/) | Evaluation, QA & Analytics Lead | Python, SQL, Pandas, ETL design, Plotly/Dash dashboarding | Git/GitHub discipline, PyTorch fundamentals | Owns retrieval and response evaluation (precision of retrieved chunks, groundedness of LLM answers), performance dashboards, and the QA pass on every branch before merge | 10:00 AM – 6:00 PM (Sun–Thu) | "Ah-MEER Eh-SAM Hoo-SAYN" |

---

## 2. Team Vision

Our goal is to deliver a working, demo-ready RAG system enhanced with Knowledge Graph retrieval — one that grounds LLM answers in real, structured, and vector-retrieved data rather than producing generic or hallucinated output — within a two-week sprint.

We are optimizing for **a system that actually runs end-to-end**: a user question flows through retrieval (vector + graph), into a well-engineered prompt, through the LLM, and back as a grounded, explainable answer — demonstrable live at any point after Day 3.

**Quality expectations:** code that runs without manual patching, a clean commit history, containerized services that start with a single Docker command, and a `README.md` that lets any teammate (or the instructor) set up the project in under five minutes.

**Team values:** honesty about blockers, respect for each other's time, and a bias toward finishing over polishing. We would rather ship a smaller retrieval scope that's accurate and well-evaluated than a broad one that isn't grounded properly.

**Professional behavior:** we treat this like a real engineering team building a production-style RAG service — deadlines are commitments, reviews are taken seriously, and disagreements over architecture or prompt design are resolved with evaluation data, not opinion.

**Learning mindset:** each member is at a different point with this stack — some have direct RAG/FastAPI experience, others are building it fresh this sprint. We treat every task as a chance to either apply an existing strength or close a gap in vector search, Knowledge Graph design, or LLM integration, and we pair people intentionally so this knowledge moves across the whole team.

---

## 3. Cooperation Plan

### Luma Alazzeh — AI Lead / ML Pipeline & Knowledge Graph Coordinator

**Strengths:** Demonstrated ML pipeline and ETL experience, strong SQL analytics, and NLP fundamentals (entity extraction) that map directly onto Knowledge Graph entity/relationship modeling. Comfortable evaluating model output quality, which extends naturally into evaluating RAG groundedness.

**Responsibilities:** Sets sprint priorities and coordinates how the Knowledge Graph integrates with vector retrieval so the two retrieval paths complement rather than duplicate each other. Owns RAG evaluation criteria (retrieval relevance, answer groundedness), reviews architecture-critical pull requests, and is the final tie-breaker on architecture decisions (routine merges just need the standard two teammate approvals).

**Skills she wants to develop:** Hands-on LangChain orchestration and production-grade vector database tuning.

**How the team will support her:** Alaa and Zaid, both closer to the FastAPI/RAG implementation details, will loop Luma into design decisions early; Majd will walk her through the Knowledge Graph data model as it's built so evaluation criteria stay grounded in the real schema.

---

### Alaa Falugi — RAG Engineer / FastAPI & Prompt Engineering Lead

**Strengths:** Direct, applied experience with RAG pipelines, embeddings, semantic search, and FastAPI/Docker — the closest match on the team to this project's core stack — plus a client-facing background that translates into clear requirements-gathering and stakeholder framing.

**Responsibilities:** Owns the retrieval pipeline end-to-end: embedding generation, vector search queries, and prompt construction that combines retrieved context (from both vector search and the Knowledge Graph) into the LLM call. Owns the FastAPI endpoints exposing retrieval and generation, and leads prompt engineering iteration to improve answer quality and reduce hallucination.

**Skills she wants to develop:** Deeper Knowledge Graph query design (e.g., graph traversal patterns) and more hands-on Docker-based deployment beyond prototype scale.

**How the team will support her:** Majd will pair with her on how graph-structured data can be queried and merged into her retrieval pipeline; Zaid will co-own the Docker deployment work so it isn't solo.

---

### Majd Albashtawi — Data Engineer / Vector DB & Knowledge Graph Data Prep

**Strengths:** Strong PostgreSQL and ETL background, plus prior applied experience combining structured data pipelines with a modeling layer (her DeepSolar graduation project) — a good foundation for preparing data that feeds both a vector database and a Knowledge Graph.

**Responsibilities:** Owns PostgreSQL schema design, the ETL process that cleans and structures source data, ingestion into the vector database (chunking and embedding storage), and preparation of entities/relationships for the Knowledge Graph. Ensures all retrieval sources — relational, vector, and graph — stay consistent with each other.

**Skills she wants to develop:** Front-end integration and hands-on FastAPI endpoint design (she currently sits upstream of the API layer and wants more visibility into how her data is consumed).

**How the team will support her:** Zaid will bring her into the FastAPI/frontend wiring for the dashboard views so she sees her data consumed end-to-end; Alaa will explain how retrieval queries actually use her vector and graph data so her schema decisions anticipate real query patterns.

---

### Zaid Jafari — Backend & Full-Stack Integration Engineer / System Architecture

**Strengths:** The broadest full-stack profile on the team, with prior direct experience building a RAG-based platform (QG-RAG interview assistant) and a separate full-stack web application — meaning he's touched nearly every layer this project needs, from API to frontend.

**Responsibilities:** Owns the integration layer — wiring the frontend, Alaa's FastAPI/RAG backend, and Majd's PostgreSQL/vector/graph data layer into one deployable application. Owns overall system architecture documentation and is responsible for the demo running as one coherent system rather than disconnected services.

**Skills he wants to develop:** Deeper PostgreSQL/vector-database query optimization and formal Knowledge Graph modeling (his portfolio is stronger on application layers than on structured data design).

**How the team will support him:** Majd will walk him through the schema, vector index, and graph structure he needs to consume; Alaa will pair with him on how the RAG API responses should be shaped for the frontend.

---

### Ameer Esam Hussein — Evaluation, QA & Analytics Lead

**Strengths:** Strong, well-rounded fundamentals across Python, SQL, Pandas, and ETL, with specific applied experience in Plotly/Dash dashboards — directly useful for visualizing retrieval quality and system performance rather than just model accuracy.

**Responsibilities:** Owns evaluation of the RAG system — measuring retrieval precision (vector and graph), groundedness of LLM answers, and response latency — and builds the dashboard presenting these metrics. Also owns the QA pass on every feature branch before merge, running the full pipeline end-to-end to catch breakage before it reaches `main`.

**Skills he wants to develop:** Hands-on exposure to vector search internals and LLM prompt evaluation techniques.

**How the team will support him:** Alaa will walk him through how retrieved chunks and prompts are structured so his evaluation metrics target the right failure points; Luma will include him in RAG evaluation review sessions so he's building real judgment, not just running scripts.

---

## 4. Communication Plan

| Item | Policy |
|---|---|
| **Primary platform** | Discord (team server, dedicated capstone channel) |
| **Secondary platform** | WhatsApp group (used only if Discord is inaccessible) |
| **Meeting platform** | Google Meet |
| **Meeting schedule** | Daily stand-up at 12:00 PM (Amman time), 15 minutes max; full planning session every Monday and Thursday, 45 minutes |
| **Daily check-ins** | Each member posts a 3-line update in Discord by 11:00 AM: what was finished yesterday, what's planned today, and any blocker |
| **Expected response window** | Messages must receive at least an emoji acknowledgment within 4 working hours during each member's stated contact hours; a full reply within 8 hours |
| **Emergency communication** | Phone call or WhatsApp for anything blocking the whole team (e.g., broken `main` branch, a down vector DB/Docker environment, or a missed deadline risk) — Discord is not sufficient for urgent issues |
| **After-hours policy** | No expectation to respond outside stated contact hours; messages sent after-hours are answered the next working period unless flagged "urgent" |
| **Weekend expectations** | No mandatory work on Fridays/Saturdays; asynchronous progress is welcome but never required, and no one is penalized for not responding |
| **Meeting etiquette** | Stand-ups start on time regardless of who has joined; agenda items are posted in Discord beforehand so meetings don't turn into planning from scratch |
| **Camera expectations** | Cameras on for the twice-weekly planning sessions; optional for daily stand-ups |
| **Decision documentation** | Every technical decision (e.g., embedding model choice, graph schema, prompt template changes) is summarized in a pinned Discord thread within 30 minutes by whoever proposed it, so absent members can review and object within 24 hours |

---

## 5. Work Plan

**Task tracking tool:** GitHub Projects (Kanban board with columns: Backlog → In Progress → In Review → Done), linked directly to the repository's issues.

**Sprint workflow:** The two-week sprint is split into four 2–3 day mini-cycles: (1) environment setup, PostgreSQL schema, and Docker baseline, (2) core RAG pipeline (embeddings, vector search) and initial Knowledge Graph structure, (3) FastAPI integration, frontend wiring, and evaluation dashboard, (4) prompt tuning, polish, testing, and rehearsal. Each cycle ends with a working, demoable increment — no cycle ends with broken `main`.

**Task assignment:** Tasks are created as GitHub issues by whoever owns that area (see Section 3), assigned to a primary owner, and tagged with a backup owner. No task exists without both.

**Definition of Done:** A task is Done only when: the code runs from a clean clone via Docker, it has been reviewed and approved by at least two other teammates, it is merged to `main`, and any relevant documentation (README, docstrings, API schema) is updated.

**Code ownership:** Each functional area (data/vector/graph, RAG/prompting, FastAPI, integration, evaluation/dashboard) has one clear owner from Section 3, but ownership means accountability for quality — not exclusive permission to touch that code. Anyone can propose changes via PR.

**Documentation ownership:** Whoever writes a piece of functionality documents it in the same PR, including any new API endpoints in a shared API reference. Luma maintains the top-level `README.md` and architecture overview.

**Anti-silo policy:** No component may be understood by only one person. Every owner must walk their area through in a 10-minute recorded or live explanation to the rest of the team by the end of cycle 3 — this explicitly includes the Knowledge Graph schema and the retrieval/prompt logic, which are the easiest pieces to become siloed.

**Knowledge sharing:** Non-trivial technical decisions (embedding model, vector DB choice, graph schema, prompt template design) follow the decision-documentation rule in Section 4 — posted in Discord with a one-paragraph rationale before implementation begins, so the whole team can weigh in and absent members can object within 24 hours.

**No solo committing policy:** No one merges their own PR into `main` without at least two approvals from other teammates — including the co-leads. This is enforced automatically by branch protection on `main`.

**Pair programming expectations:** Each mini-cycle includes at least one scheduled pairing session between an owner and their support partner (as defined in Section 3), specifically for the integration-heavy tasks (RAG↔FastAPI, data/graph↔retrieval).

**Backup owner for every task:** Every GitHub issue has a "Backup" field filled in at creation. If the primary owner is blocked or unavailable for more than 24 hours, the backup owner picks up the task without waiting for a discussion.

**File organization:** The repository follows a standard structure — `/data`, `/etl`, `/knowledge_graph`, `/vector_store`, `/rag`, `/api`, `/frontend`, `/dashboard`, `/docs`, `/tests`, plus a root `docker-compose.yml` — agreed on Day 1 and not restructured mid-sprint without team consensus.

---

## 6. Git Process

**Repository links:**
- **Team org:** https://github.com/capstone-ai-mafia
- **Main repo:** https://github.com/capstone-ai-mafia/main-repo
- **Project board:** https://github.com/orgs/capstone-ai-mafia/projects/1

**Branch naming convention:**
- `feature/<short-description>` — e.g. `feature/vector-search`, `feature/kg-schema`, `feature/fastapi-endpoints`
- `bugfix/<short-description>` — e.g. `bugfix/embedding-mismatch`
- `hotfix/<short-description>` — e.g. `hotfix/api-timeout`

**Development flow:** All work branches off `main`. No one commits directly to `main`. Each branch maps to a single GitHub issue.

**Pull Request requirements:** Every PR must include a short description of what changed, a link to the related issue, and confirmation that the code runs locally via Docker. PRs touching retrieval or prompting must include a short before/after example of a query and response.

**Review requirements:** Every PR needs at least two approvals from teammates other than the author before merge (enforced by branch protection on `main`; stale approvals are dismissed when new commits are pushed). PRs touching the integration layer (owned by Zaid) additionally require his sign-off, since he's accountable for the system running end-to-end.

**Approval rules:** Reviewers must actually pull and run the branch for non-trivial changes — approving based on a code read alone is only acceptable for small documentation or config changes.

**Merge strategy:** Squash-and-merge into `main`, so the main branch history stays readable as one commit per completed feature.

**Commit message format:** `<type>: <short description>` using `feat`, `fix`, `docs`, `refactor`, `test`, or `chore` — e.g. `feat: add vector similarity search endpoint`.

**Conflict resolution (Git):** Whoever opens the PR that causes a conflict is responsible for resolving it before requesting re-review, with help from the other party if the conflict touches shared logic (e.g., a shared schema file).

**Protected main branch:** `main` is protected in GitHub settings — direct pushes are disabled, a pull request is required, and merging requires **two approving reviews**. Stale approvals are dismissed when new commits are pushed, and no bypass path exists (branch protection cannot be overridden, including by admins).

**Merge cadence:** PRs are merged as soon as they're approved rather than batched, to avoid large end-of-sprint merge conflicts.

**Release tagging:** The repository is tagged `v0.1` at the end of cycle 2 (working RAG + KG pipeline), `v0.2` at the end of cycle 3 (integrated system with API and dashboard), and `v1.0` at final submission.

---

## 7. Conflict Resolution Plan

**Technical disagreements:** The two (or more) people involved present their reasoning in the Discord thread or stand-up first — for example, a disagreement over vector DB choice or graph schema design is settled by comparing retrieval quality on a small test set, not opinion. If they can't agree within one discussion, the final call goes to the co-lead who owns that domain — Luma for architecture, evaluation, and data-model decisions; Alaa for retrieval, prompt, and product decisions.

**Communication issues:** If someone feels unheard or misread in a discussion, they raise it directly and privately with the person first. If the issue persists, it's brought to a co-lead (Luma or Alaa), who mediates a short conversation between the two.

**Missed deadlines:** The first missed deadline gets a no-blame check-in during the next stand-up to understand the blocker and adjust the plan. A second missed deadline on the same task triggers reassignment to the backup owner, communicated respectfully.

**Dominating teammate:** If one person is consistently speaking over others or making unilateral architecture calls (e.g., on prompt design or schema) in meetings, whichever co-lead is chairing (Luma or Alaa) will actively redirect airtime during the meeting itself rather than letting it become a separate confrontation.

**Inactive teammate:** After two missed check-ins with no communication, a co-lead (Luma or Alaa) reaches out directly and privately to understand what's going on before reassigning any of their tasks. Tasks are only reassigned, never simply left undone.

**Unequal workload:** Workload is checked visually against the GitHub Projects board at each Monday/Thursday planning session. If one person's column is consistently heavier — for instance, if Alaa is absorbing both prompt engineering and API work without support — tasks are rebalanced at that meeting.

**Skill mismatch:** If a task turns out to be a poor fit for its owner (e.g., graph query design turns out harder than expected for whoever's handling it), the owner says so immediately, and the task is either paired or reassigned per Section 3's support plan.

**Escalation path:** Direct conversation → co-lead mediation (Luma / Alaa) → full-team discussion and vote → instructor escalation (last resort only).

**Conflict discussion process:** Any team-wide conflict discussion happens synchronously (call, not text), is time-boxed to 20 minutes, and ends with a written one-line resolution posted in Discord.

**Voting rules:** If a technical or process decision can't be resolved through discussion, the team votes; a simple majority (3 of 5) decides. The co-leads (Luma and Alaa) vote like everyone else; if a vote is genuinely split, the tiebreaker goes to the co-lead who owns that domain — Luma for architecture/evaluation/data-model, Alaa for retrieval/prompt/product.

**Leader responsibilities:** Luma and Alaa (co-leads) are responsible for noticing early warning signs (silence in Discord, missed check-ins, visibly uneven boards, or a component quietly becoming a one-person silo) and raising them before they become conflicts.

**Instructor escalation:** Used only if a conflict threatens the team's ability to submit the capstone and cannot be resolved internally after the steps above have genuinely been tried.

---

## 8. Quality Standards

**Coding standards:** Python code follows PEP 8; functions are typed where practical; no commented-out code or debug print statements in merged code; FastAPI endpoints use Pydantic models for request/response validation.

**Documentation standards:** Every module has a top-of-file docstring explaining its purpose; API endpoints are documented (FastAPI's auto-generated docs are kept clean and annotated); the root `README.md` always reflects current setup steps, including how to bring up the Docker environment.

**Testing expectations:** Every pipeline stage (ETL, vector ingestion, Knowledge Graph queries, RAG retrieval, FastAPI endpoints) has at least one passing test before merge. Full test suite must pass before a release tag is applied.

**AI ethics:** Any LLM-generated content presented in the demo is clearly distinguishable as such; retrieved context used to ground an answer is shown or referenceable so the team never presents an ungrounded or cherry-picked response as representative.

**Professional behavior:** Disagreements stay focused on the work, not the person; feedback is given on pull requests the way it would be given in a real engineering team — direct but respectful.

**Respectful communication:** No dismissive language in reviews or chat ("this is wrong" becomes "this retrieval query breaks on empty results — here's why").

**Meeting attendance:** Attendance at the two weekly planning sessions is mandatory barring communicated emergencies; daily stand-ups allow one flexible miss per week with an async written update instead.

**Repository hygiene:** No dead branches left open past merge; `.gitignore` enforced from Day 1 so no environment files, API keys, credentials, or large model/vector files are committed.

**Review quality:** Reviewers are expected to actually run the code, not just skim it — see Section 6's approval rules.

**Demo readiness:** By the start of cycle 4, the full application — Docker environment, PostgreSQL, vector store, Knowledge Graph, FastAPI backend, and frontend — must run start-to-finish on a machine that isn't the original developer's, with no manual fixes required.

---

## 9. Presentation Practice Plan

| Role | Owner | Rationale |
|---|---|---|
| **Narrative lead** | Alaa Falugi | Strongest business-framing and communication background; best positioned to explain why RAG + Knowledge Graph grounding matters in accessible, non-technical terms |
| **Demo lead** | Zaid Jafari | Owns the integrated system end-to-end and has prior experience presenting full-stack platforms he built solo |
| **Technical Q&A lead** | Luma Alazzeh | Deepest technical breadth across the architecture as a technical co-lead; best equipped to field questions on evaluation, retrieval design, and graph/vector trade-offs |
| **Slide owners** | Ameer Esam Hussein (evaluation/performance visuals) & Majd Albashtawi (data/graph/architecture slides) | Matches their existing strengths in visualization and structured data work |
| **Backup presenter** | Majd Albashtawi | Familiar with both the data/graph layer and, through paired work with Zaid, the integration layer — able to step in for either narrative or demo sections |

**Practice frequency:** Two full run-throughs during cycle 4 — one internal (team only) and one dress rehearsal open to feedback from outside the team.

**Rehearsal schedule:** Internal run-through on the second-to-last day of the sprint; dress rehearsal the day before submission.

**Feedback process:** After each run-through, every teammate writes one specific "keep doing" and one specific "change" comment in a shared Discord thread.

**Time management:** The presentation is scripted to a strict time budget (e.g., 3 minutes narrative, 5 minutes live RAG/KG demo, remainder Q&A) with Alaa timing both rehearsals and flagging any section running over.

**Backup presenter role:** Majd shadows both Alaa's narrative and Zaid's demo during both rehearsals so she can step in seamlessly if either is unavailable on the actual day.

**Emergency plan if demo fails:** A short pre-recorded screen capture of a working query flowing through retrieval, the Knowledge Graph, and the LLM response (recorded during the dress rehearsal) is kept on hand as a fallback; Zaid narrates over it live if the live environment fails, so the team never presents with nothing to show.

---

## 10. Mid-Sprint Review

This contract is formally reviewed once, at the mid-sprint mark (end of cycle 2), during the scheduled Thursday planning session.

**Review triggers:** The contract is revisited earlier than the scheduled checkpoint only if: a role clearly isn't working (e.g., consistent overload on one person), a communication or conflict issue recurs more than once, or the RAG/Knowledge Graph scope changes significantly.

**How updates are agreed:** Any proposed change to this contract is discussed in a planning session (not decided async), and requires agreement from at least 4 of the 5 members to take effect — the same majority threshold used for technical decisions in Section 7.

**How decisions are documented:** Any accepted change is edited directly into this `TEAM_CONTRACT.md` file in the same sprint, with a short note in the commit message (e.g., `docs: update contract — reassign evaluation ownership`), so the document always reflects how the team is actually operating.

---

## 11. Team Commitments

- ✓ Respect deadlines and communicate proactively if one is at risk
- ✓ Review teammates' pull requests promptly and thoroughly
- ✓ Communicate blockers within the same working day they appear
- ✓ Keep documentation, API references, and the GitHub Projects board updated in real time
- ✓ Help teammates who are stuck rather than working around them
- ✓ Maintain code quality standards defined in Section 8
- ✓ Attend both weekly planning sessions and give notice for any absence
- ✓ Never merge unreviewed code to `main`
- ✓ Ground every demoed answer in real retrieval output — no cherry-picked or fabricated results
- ✓ Show up to the final presentation fully rehearsed and on time

---

## 12. Sign-Off

| Name | Role | Agreement Statement | Signature | Date |
|---|---|---|---|---|
| Luma Alazzeh | AI Lead / ML Pipeline & Knowledge Graph Coordinator | I have read and agree to uphold this Team Contract for the duration of the capstone sprint. | Luma Muin Alazzeh | 7/6/2026 |
| Alaa Falugi | RAG Engineer / FastAPI & Prompt Engineering Lead | I have read and agree to uphold this Team Contract for the duration of the capstone sprint. | Alaa Falugi | 7/6/2026 |
| Majd Albashtawi | Data Engineer / Vector DB & Knowledge Graph Data Prep | I have read and agree to uphold this Team Contract for the duration of the capstone sprint. | Majd Amjad Methqal | 7/6/2026 |
| Zaid Jafari | Backend & Full-Stack Integration Engineer / System Architecture | I have read and agree to uphold this Team Contract for the duration of the capstone sprint. | zaid kaml alja’fari | 7/6/2026 |
| Ameer Esam Hussein | Evaluation, QA & Analytics Lead | I have read and agree to uphold this Team Contract for the duration of the capstone sprint. | Ameer Esam Hussin | 7/6/2026 |