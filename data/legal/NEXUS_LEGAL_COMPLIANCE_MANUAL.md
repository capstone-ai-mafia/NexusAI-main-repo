# Nexus Technologies — Legal & Compliance Manual

---
Document ID: LEG-001
Department: Legal & Compliance
Document Owner: Legal & Compliance / General Counsel
Version: 1.0
Classification: Internal
Last Updated: July 2026
Related Documents:
- Company Profile
- HR Policy Manual
- Information Security Policy
- General Company Policies
- Finance & Expense Policy
Keywords:
- NDA
- intellectual property
- confidential information
- contract approval
- ethics
- data privacy
- compliance
- legal review
---


> **Document type:** Legal & Compliance Manual (Company-Wide Policy of Record)
> **Owner:** Legal & Compliance Department — led by General Counsel, reporting to the CEO (Company Profile §6)
> **Data privacy owner:** Data Protection Officer (DPO), within Legal & Compliance
> **Approved by:** Executive Leadership Team (ELT); security-related sections jointly with the CISO (Company Profile §9.4)
> **Applies to:** Nexus Technologies, Inc. and all wholly owned subsidiaries (US, Portugal, India)
> **Classification:** Internal — All Employees
> **Version:** 1.0 — July 2026
> **Review cycle:** Annual, or earlier on material legal/regulatory change

### Related documents

- **Company Profile** — canonical source for structure, roles, hierarchy, offices, approval thresholds, and terminology. All defined terms (ELT, DRI, CISO, CHRO, NexusFlow, etc.) carry the meaning given there.
- **HR Policy Manual** — governs the employment relationship. **Cross-referenced throughout** wherever legal obligations attach to people (Code of Conduct, confidentiality, IP assignment, onboarding/offboarding access, training, reporting, and non-retaliation).
- **Remote Work Policy** — governs remote/hybrid mechanics, including home-office security and device handling referenced in the confidentiality and data-privacy sections.
- **Security (InfoSec) Standards** — owned by the CISO; governs the technical controls that operationalize the confidentiality, privacy, and regulatory requirements below.
- **Regional / Local Addenda** — jurisdiction-specific supplements. **Where a local addendum or applicable law requires a different or stricter standard, that requirement governs for that jurisdiction.**

### Boundary note — Legal vs. Security

This manual sets the **legal and policy** requirements. The **CISO / InfoSec** team owns the **technical controls** that implement them (access management, encryption, monitoring, incident response tooling). Where this manual says "protected" or "secured," the specific control is defined in the Security Standards. Legal and Security co-own privacy incident response.

---

## 1. Purpose & Scope

### 1.1 Purpose

This manual establishes how Nexus Technologies meets its legal, contractual, ethical, and regulatory obligations. It exists to:

- Protect Nexus, its customers, and its people by setting clear, consistent rules for confidentiality, intellectual property, contracting, privacy, and compliance.
- Translate the Core Values — especially **Integrity**, **Ownership**, and **Clarity** — into enforceable legal practice.
- Give employees a single reference for what the law and Nexus require of them, and where to go when unsure.

Consistent with **clarity over cleverness**, this manual is written to be understood by non-lawyers. When a situation is genuinely ambiguous, the rule is simple: **ask Legal & Compliance before acting.**

### 1.2 Scope

This manual applies to **all employees, interns, and fixed-term staff** across every office and remote arrangement, and — for the obligations that extend to them — to **contractors, vendors, and partners** who handle Nexus or customer information. The employment-category definitions in the HR Policy Manual (§3) determine who falls into each group.

This manual is not legal advice for any specific situation and does not replace advice from Legal & Compliance or qualified local counsel.

---

## 2. Non-Disclosure Agreements (NDAs)

An NDA is the baseline legal instrument protecting confidential information exchanged with, or by, Nexus.

### 2.1 When an NDA is required

An approved NDA must be in place **before** confidential information is shared, in situations including:

- Sales and partnership discussions where either party will disclose non-public information.
- Vendor and supplier engagements involving access to Nexus systems or data.
- Evaluations, proofs of concept, and pilots of NexusFlow with a prospective customer.
- Any exchange with an external party where non-public technical, product, financial, or customer information will be shared.

### 2.2 Types of NDA

| Type | Use |
|---|---|
| **Employee confidentiality obligation** | Built into every employment agreement — not a separate NDA per engagement. See §4 (Confidential Information) and HR Policy §11.3. |
| **Mutual NDA** | Both parties will disclose confidential information (most common with customers and partners). |
| **One-way NDA** | Only one party discloses (e.g., a vendor receiving Nexus information). |
| **Vendor / contractor NDA** | Signed by third parties before they access Nexus systems or data, in addition to their commercial agreement. |

### 2.3 Standard terms and approval

- Nexus maintains **approved NDA templates** owned by Legal & Compliance. Using the standard template with no material edits is the fast path.
- **Standard NDA (unmodified template):** may be approved and executed by the deal or engagement owner (e.g., an Account Executive or engagement DRI) per their delegated authority.
- **Non-standard NDA** (counterparty's paper, or material edits — e.g., unusual term length, broad indemnities, governing-law changes): must be reviewed and approved by **Legal & Compliance** before signature.
- NDAs are **records** and are stored in Legal's contract repository (§9.5 principles for signature authority apply).

### 2.4 Duration and survival

- Confidentiality obligations typically survive for a defined period after the relationship ends (commonly several years), and **indefinitely for trade secrets**, per the specific agreement.
- Employee confidentiality obligations **survive termination of employment**, as reinforced in HR Policy §17.3.

---

## 3. Intellectual Property (IP)

Nexus's intellectual property — its platform, code, connectors, designs, brand, and know-how — is among its most valuable assets. Protecting it is everyone's responsibility.

### 3.1 Ownership of work product

- Work created by employees within the scope of their employment — code, designs, documentation, inventions, and other work product — is **owned by Nexus**. This assignment is established in the **employment agreement** each employee signs (see HR Policy §16.1 onboarding and §11 conduct).
- Contractors and agencies assign relevant IP to Nexus through their engagement contracts; **no external work is accepted without a valid IP-assignment clause** vetted by Legal.

### 3.2 Inventions and patents

- Employees must **promptly disclose** potentially patentable inventions to Legal & Compliance via the invention-disclosure process.
- Nexus decides whether to pursue patent protection. Employees cooperate with filings, including after they leave, per their agreement.

### 3.3 Open-source software

- Nexus both uses and, in defined cases, contributes to open-source software. Because open-source licenses carry obligations that can affect the proprietary platform, **all open-source use and contribution follows the Open-Source Software standard** co-owned by Engineering and Legal.
- Incoming open-source components must be license-cleared before inclusion in NexusFlow. Copyleft/reciprocal licenses (e.g., strong copyleft) require Legal review before use in distributed or hosted code.
- Employees may not contribute Nexus code to external open-source projects without approval.

### 3.4 Third-party IP

- Employees must not import third-party code, content, designs, or copyrighted material into Nexus products or materials without a valid license or permission.
- Respecting others' IP is part of the Code of Ethics (§6) and fair-dealing obligations.

### 3.5 Trademarks and brand

- **Nexus Technologies** and **NexusFlow** are brand assets. Use of Nexus names, logos, and marks follows brand-usage guidance; external use by partners requires approval.
- Employees must not register domains, handles, or marks incorporating Nexus branding on the company's behalf without Legal approval.

---

## 4. Confidential Information

### 4.1 Data classification

Nexus classifies information into four tiers. Every employee is responsible for handling information according to its classification. The **technical controls** for each tier are defined in the Security Standards (CISO).

| Tier | Definition | Examples |
|---|---|---|
| **Public** | Approved for public release. | Marketing content, published docs, press releases. |
| **Internal** | Default for internal business information; not for external release. | Internal plans, most Confluence pages, org information. |
| **Confidential** | Sensitive information whose disclosure could harm Nexus, customers, or individuals. | Non-public financials, product roadmaps, contracts, source code. |
| **Restricted** | Highest sensitivity; strict need-to-know. | Customer personal data, security keys/credentials, regulated data, M&A materials. |

### 4.2 Handling obligations

- Access is on a **need-to-know / least-privilege** basis (implemented by IT and Security).
- Confidential and Restricted information must not be shared externally without an NDA (§2) and a legitimate business reason.
- **Customer data** processed on the platform is treated as Restricted and handled under the Data Privacy section (§7) and customer contracts (DPAs).
- Do not discuss Confidential/Restricted matters in public spaces, and do not post them in unsanctioned tools. Use only the sanctioned tool stack (Company Profile §12).

### 4.3 Confidentiality and remote work

- Confidentiality obligations apply **identically** in the office and remotely. Remote employees must protect screens, conversations, printed materials, and devices from household or public exposure. The specific home-office security requirements are set in the **Remote Work Policy** and Security Standards, and reinforced in HR Policy §11.3.

### 4.4 Duration

- Confidentiality obligations **continue after employment or engagement ends** (HR Policy §17.3). Departing employees must return or destroy confidential materials as part of offboarding (§8 record disposal; HR Policy §17.3).

---

## 5. Contract Approval

No one may bind Nexus to a contract without authority. This section defines **who can approve and sign what**, consistent with the approval hierarchy in the Company Profile (§9).

### 5.1 Core principles

- **Only authorized signatories** may execute contracts on behalf of Nexus. Approval authority does not equal signature authority — both must be satisfied.
- **No self-approval.** The person requesting a contract cannot be its sole approver (Company Profile §9 approval principle).
- **Standard templates are the fast path.** Nexus's approved templates (NDAs, order forms, DPAs, vendor terms) route faster than counterparty paper or custom terms.
- **Legal reviews non-standard terms.** Any deviation from approved templates — unusual liability, indemnity, IP, data, or governing-law terms — requires Legal & Compliance review before signature.

### 5.2 Commercial (customer) contract approval

Mapped to the Company Profile commercial approval thresholds (§9.5):

| Situation | Approval required |
|---|---|
| Standard contract at list pricing | Account Executive + Sales Manager |
| Discount up to 15% | Sales Manager |
| Discount 15–30% | Regional Sales Director |
| Discount above 30% or non-standard commercial terms | VP of Sales + CFO |
| Non-standard **legal** terms (liability, IP, data, indemnity) | **Legal & Compliance** (in addition to commercial approvals) |
| Enterprise deal above $1M ARR | CRO + CEO |

### 5.3 Procurement (vendor) contract approval

Vendor spend follows the spending thresholds in the Company Profile (§9.1) — Manager → Director → VP → C-suite → CFO/CEO by amount — **plus** Legal review of the contract terms, and Security review where the vendor will access Nexus systems or data.

### 5.4 Document and policy sign-off

Per Company Profile §9.4:

- **Customer-facing legal / contract terms:** Legal + CFO (or CRO for commercial terms).
- **Security / compliance policy:** CISO + Legal.
- **Company-wide policy (including this manual):** Executive Leadership Team.

### 5.5 Workflow

1. **Initiate** — the deal or engagement DRI selects the correct template.
2. **Review** — Legal reviews non-standard terms; Security and the DPO review data/security terms where applicable (§7).
3. **Approve** — the required approvers per §5.2–5.4 sign off.
4. **Execute** — an authorized signatory signs.
5. **Store** — the fully executed contract is filed in Legal's contract repository as a retained record (§8). Commercial records are also tracked in Salesforce, the company's CRM system.

---

## 6. Code of Ethics

This section states Nexus's ethical standard. It builds on — and shares a single source of truth with — the **Code of Business Conduct & Ethics** summarized in HR Policy §11. Where the two are read together, they must not conflict; this manual owns the legal detail, the HR manual owns the employment framing.

### 6.1 Ethical foundations

Ethics at Nexus flow from the Core Values, especially **integrity, honesty, and owning the outcome**. Every employee, contractor, and intern is bound by them.

### 6.2 Core ethical obligations

| Area | Standard |
|---|---|
| **Conflicts of interest** | Disclose any personal, financial, or family interest that could conflict with your role. When in doubt, disclose to your manager or Legal. |
| **Gifts & hospitality** | Never give or accept gifts, entertainment, or hospitality intended to improperly influence a decision. Modest, customary business courtesy is acceptable within the gifts standard. |
| **Anti-bribery & corruption** | Zero tolerance for bribes, kickbacks, or facilitation payments, directly or through third parties — consistent with anti-corruption laws (e.g., US FCPA, UK Bribery Act) across all jurisdictions where Nexus operates. |
| **Fair dealing & competition** | Compete honestly. Do not misrepresent Nexus's products or a competitor's, and comply with competition/antitrust law. |
| **Insider information** | Do not trade on, or share, material non-public information about Nexus (as a private company) or about customers/partners. |
| **Accurate records** | Keep truthful business, financial, and evaluation records. Never falsify data — including demo, benchmark, or evaluation results presented to customers. |
| **Respect for IP and privacy** | Respect the IP and personal data of others (§3, §7). |
| **Sanctions & trade** | Do not transact with sanctioned parties or in violation of export controls (§10). |

### 6.3 Raising concerns and non-retaliation

- Ethics or legal concerns can be raised with a manager, Legal & Compliance, or through the **confidential reporting channel** (shared with the HR reporting channels in HR Policy §11.4 and §13.4).
- **Retaliation is prohibited** against anyone who reports a concern in good faith or cooperates with an investigation — reinforcing HR Policy §13.4.
- Good-faith reporting is expected: staying silent about a known violation is itself a breach of the Code.

---

## 7. Data Privacy

Nexus handles personal data both as an employer and as a technology provider whose platform processes customer data. This section governs how that data is protected. The **DPO**, within Legal & Compliance, owns privacy; the **CISO** owns the security controls that protect the data.

### 7.1 Nexus's two privacy roles

| Role | When it applies | Example |
|---|---|---|
| **Controller** | Nexus decides why/how personal data is used. | Employee HR data, job applicants, marketing prospects, website visitors. |
| **Processor** | Nexus processes personal data **on behalf of a customer** under their instructions. | Personal data flowing through a customer's Flows and connectors on NexusFlow. |

This distinction matters: as a **processor**, Nexus acts only on documented customer instructions under a **Data Processing Agreement (DPA)**, and does not use customer personal data for its own purposes.

### 7.2 Privacy principles

Nexus applies globally consistent principles, tightened by local law:

- **Lawfulness, fairness, transparency** — process personal data with a valid basis and clear notice.
- **Purpose limitation & data minimization** — collect only what is needed, for stated purposes.
- **Accuracy & storage limitation** — keep data accurate and retain it only as long as needed (see §8).
- **Security** — protect personal data with appropriate technical and organizational controls (Security Standards).
- **Accountability** — be able to demonstrate compliance.
- **Privacy & security by design** — build privacy into products and processes from the start; the Data & AI and Product teams engage the DPO for features touching personal data.

### 7.3 Data subject rights

- Individuals may have rights to access, correct, delete, restrict, or port their personal data, and to object to certain processing, depending on jurisdiction.
- **Controller requests** (e.g., from employees or prospects) are handled by the DPO within legal timeframes.
- **Processor requests** (from a customer's end users) are **forwarded to the customer**, who is the controller; Nexus assists per the DPA.

### 7.4 International data transfers

- Nexus operates across the Americas, EMEA, and APAC (Company Profile §10). Cross-border transfers of personal data use an approved legal transfer mechanism (e.g., standard contractual clauses or equivalent) and are reviewed by the DPO.

### 7.5 Personal data breach response

- Any suspected exposure of personal data must be reported **immediately** to Security and the DPO through the incident process (Company Profile §12 incident channels).
- **Legal and Security co-own** privacy incident response: containment (Security), legal assessment and any regulatory/customer notification within required deadlines (DPO/Legal).
- As a **processor**, Nexus notifies affected **customers** without undue delay so they can meet their own obligations.

### 7.6 Employee and candidate privacy

- Employee and applicant personal data (held in Workday and recruiting systems) is processed as controller, per the privacy notice and HR Policy. Access is need-to-know and retained per §8.

---

## 8. Record Retention

Nexus keeps records long enough to meet legal, tax, contractual, and operational needs — and disposes of them securely when that need ends. Keeping data forever creates risk; deleting too early breaks obligations.

### 8.1 Principles

- Every record has an **owner** and a **retention period** defined by a **Retention Schedule** maintained by Legal & Compliance.
- Records are retained in **sanctioned systems** only (Company Profile §12), never in unmanaged personal storage.
- When the period expires, records are **securely disposed of** unless a legal hold applies.

### 8.2 Representative retention categories

The schedule is authoritative; the table illustrates the approach. Actual periods are set per category and jurisdiction (Regional Addenda may extend them).

| Record type | Illustrative retention approach |
|---|---|
| **Executed contracts & NDAs** | Retained for the life of the agreement plus a defined period after termination. |
| **Financial & tax records** | Retained for the period required by tax and accounting law in each jurisdiction. |
| **Employee records** | Retained during employment and for a defined period after departure (coordinated with HR Policy §17). |
| **Recruitment records** | Retained for a limited period after a hiring decision. |
| **Customer personal data (processor)** | Retained and deleted per the customer's instructions and DPA. |
| **Security & audit logs** | Retained per the Security Standards and applicable regulation. |
| **Marketing/consent records** | Retained while consent is valid, then disposed. |

### 8.3 Legal holds

- When litigation, an investigation, or a regulatory request is reasonably anticipated, Legal issues a **legal hold** that **suspends normal disposal** for the affected records.
- Employees who receive a legal hold notice must preserve the specified records and must not delete or alter them. Legal holds override the standard retention schedule until released by Legal.

### 8.4 Disposal

- Expired records are disposed of securely (secure deletion or destruction) so they cannot be reconstructed — the technical method is defined by the Security Standards.
- Offboarding disposal of an employee's confidential materials is coordinated with HR Policy §17.3 and IT/Security deprovisioning.

---

## 9. Compliance Program

The compliance program is the operating system that keeps the obligations in this manual working in practice.

### 9.1 Ownership and structure

- **Legal & Compliance** owns the program, with the **DPO** for privacy and the **CISO** for security compliance.
- Executive accountability sits with the **ELT**; the program reports on posture to leadership on a regular cadence (aligned with the QBR rhythm, Company Profile §13.4).

### 9.2 Training and awareness

- All employees complete **mandatory compliance training**, delivered and tracked through the learning framework in HR Policy §15.2 — including **security-awareness training (CISO)**, **privacy training (DPO)**, anti-harassment (HR), and role-specific training (e.g., anti-bribery for customer-facing and procurement roles).
- New joiners complete required training in their first week (HR Policy §16.2).

### 9.3 Third-party and vendor compliance

- Vendors and partners are risk-assessed before engagement. Those handling Nexus or customer data sign appropriate NDAs (§2), DPAs (§7), and security terms, and are reviewed by Legal and Security (§5.3).

### 9.4 Monitoring, reporting, and enforcement

- The confidential reporting channel (§6.3, HR Policy §11.4) lets anyone raise a concern without retaliation.
- Reported issues are investigated fairly and consistently; substantiated violations may lead to disciplinary action up to termination (through the HR process, HR Policy §9.5/§17) and, where relevant, legal or regulatory action.
- Compliance failures are treated as learning inputs, not just penalties — consistent with **own the outcome**.

---

## 10. Regulatory Compliance

As an enterprise iPaaS serving regulated industries — financial services, healthcare, retail, logistics, and public sector (Company Profile §1) — Nexus operates within a broad regulatory landscape. This section frames the main areas; specifics live with the responsible owners.

### 10.1 Security and trust certifications

- Nexus maintains an information-security program aligned to recognized frameworks (e.g., **SOC 2 Type II** and **ISO/IEC 27001**), owned by the CISO with Legal support. Certifications and attestations are provided to customers through the standard trust/security review process rather than ad hoc.

### 10.2 Data protection regulations

- Because Nexus operates across multiple regions, its privacy program (§7) is built to satisfy applicable regimes in the jurisdictions where it operates and where customers are based — including, without limitation, the EU/UK GDPR (via the London/EMEA operations), US state privacy laws (e.g., California), Canada's PIPEDA, Singapore's PDPA, India's data-protection law, and Jordan's personal-data-protection requirements. The DPO maintains the mapping; Regional Addenda carry the detail.

### 10.3 Industry-specific obligations

- **Healthcare customers:** where Nexus processes protected health information on a customer's behalf, it acts as a **processor/business associate** under the appropriate agreement and controls (e.g., HIPAA-aligned terms in the US), rather than assuming those obligations independently.
- **Financial-services customers:** Nexus supports customers' own regulatory needs through security, auditability, and contractual commitments, without itself becoming a regulated financial institution.
- **Public-sector customers:** additional procurement, security, and data-residency terms may apply and are handled with Legal.

### 10.4 Export controls and sanctions

- Nexus complies with applicable export-control and economic-sanctions laws. Employees must not provide the platform, technology, or services to sanctioned parties or embargoed destinations. Questions route to Legal (§6.2).

### 10.5 Responsible AI

- Nexus's **Data & AI** team (Company Profile §6) builds AI/ML features (e.g., workflow suggestions). These follow a **responsible-AI standard** co-owned by Data & AI, Legal, and Security: transparency about AI-generated output, appropriate handling of training and customer data (§7), and human oversight. This extends the AI-ethics principle already reflected in the team's engineering norms.

### 10.6 Accessibility and employment law

- Nexus works toward accessibility standards for its products and workplace.
- Employment-law compliance across the six jurisdictions is handled jointly by Legal and People (HR) through the **Regional Addenda** referenced in the HR Policy Manual (§2).

---

## 11. Frequently Asked Questions (FAQ)

**Q1. Someone wants to see our product before signing anything — do we need an NDA first?**
Yes. If non-public information will be shared, an approved NDA must be in place first. A standard mutual NDA is the fast path; counterparty paper or edited terms go to Legal (§2).

**Q2. I built something useful on the side that relates to my work. Who owns it?**
Work created within the scope of your employment is owned by Nexus under your employment agreement. If you think something falls outside that scope, disclose it to Legal rather than assuming (§3.1).

**Q3. Can I add an open-source library to our codebase?**
Only after it's license-cleared under the Open-Source Software standard. Some licenses create obligations that affect our proprietary platform, so certain licenses need Legal review before use (§3.3).

**Q4. How do I know how sensitive a document is?**
Use the four-tier classification: Public, Internal, Confidential, Restricted. Customer personal data and credentials are Restricted and need-to-know (§4.1).

**Q5. A customer sent us their own contract instead of our template. Can I just sign it?**
No. Counterparty paper and any non-standard legal terms require Legal review, and only an authorized signatory can execute it — after the right approvals for the deal size and discount (§5).

**Q6. Can I accept a gift from a vendor or customer?**
Modest, customary business courtesy is fine. Anything that could look like it's meant to influence a decision is not. When unsure, disclose to your manager or Legal (§6.2).

**Q7. I think I saw personal data exposed. What do I do?**
Report it immediately to Security and the DPO through the incident process — do not wait to be certain. Legal and Security handle assessment and any required notifications (§7.5).

**Q8. A customer's user asked us to delete their data. Do we?**
If it relates to data we process on a customer's behalf, we forward the request to that customer (the controller) and assist per the DPA — we don't act on it unilaterally (§7.3).

**Q9. Can I delete old files to clean up?**
Follow the Retention Schedule. And if you've received a **legal hold** covering those records, you must preserve them — legal holds override normal deletion (§8.3).

**Q10. How does this manual relate to the HR manual?**
They're designed to work together. The HR Policy Manual owns the employment framing (conduct, confidentiality obligations, reporting, discipline); this manual owns the legal and regulatory detail. Where they touch — the Code of Ethics, confidentiality, IP assignment, training, offboarding — they cross-reference each other and must stay consistent.

**Q11. I'm not sure whether something is allowed. What's the safe move?**
Ask Legal & Compliance before acting. "I asked first" is always better than "I assumed." (§1.1)

**Q12. Do these rules apply when I work from home?**
Yes — identically. Confidentiality and privacy obligations don't change location. The specific home-office security and device requirements are in the Remote Work Policy and Security Standards (§4.3).

---

*This Legal & Compliance Manual is a company-wide policy of record, aligned to the Nexus Technologies Company Profile and intended to be read alongside the HR Policy Manual, the Remote Work Policy, the Security Standards, and applicable Regional Addenda. It is reviewed annually and updated as Nexus's legal and regulatory obligations evolve. When in doubt, ask Legal & Compliance before acting.*
