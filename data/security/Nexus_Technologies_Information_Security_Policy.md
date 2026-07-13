# Nexus Technologies — Information Security Policy

---
Document ID: SEC-001
Department: Engineering & IT / Information Security
Document Owner: IT & Internal Systems + Legal & Compliance
Version: 1.0
Classification: Internal
Last Updated: July 2026
Related Documents:
- Company Profile
- IT Policy
- Legal & Compliance Manual
- General Company Policies
Keywords:
- data classification
- customer data
- confidential information
- access control
- phishing
- malware
- USB
- encryption
- incident reporting
---


**Document Owner:** IT & Internal Systems (the IT function within the Engineering & IT Department, Company Profile §6), in partnership with Legal & Compliance
**Approval Authority:** CTO + General Counsel + CHRO for policy-wide changes (per Company Profile §9.4 Approval Hierarchy)
**Applies To:** All Nexus employees, contractors, and temporary staff (informally, "Nexons" — Company Profile §13) across all office locations and remote work arrangements
**Related Document:** This policy should be read alongside the **Nexus Technologies IT Policy**, which governs device management, passwords, MFA, VPN, and software controls referenced throughout this document.

---

## 1. Purpose & Scope

This Information Security Policy establishes how Nexus Technologies classifies, protects, and responds to risks affecting company and customer data. Where technical controls are already defined in the **IT Policy** (e.g., MFA, VPN, device management, password requirements), this policy references those controls rather than duplicating them, and focuses instead on data handling, classification, and security behavior expectations.

---

## 2. Data Classification

All Nexus data must be classified into one of four tiers. Classification determines handling, storage, and access requirements throughout this policy.

| Tier | Description | Examples |
|---|---|---|
| **Tier 1 — Public** | Information approved for external release | Marketing materials, published blog posts, job postings |
| **Tier 2 — Internal** | Non-sensitive internal information | Internal newsletters (*The Nexus Signal*), org charts, internal wiki pages |
| **Tier 3 — Confidential** | Sensitive business information | Financial forecasts, contracts, source code, employee records, product roadmaps |
| **Tier 4 — Restricted** | Highly sensitive; regulatory or contractual protection required | Customer PII, payment data, health data (where applicable), authentication credentials, encryption keys |

- Data owners (typically Directors or above within the relevant department) are responsible for assigning and reviewing classification annually.
- Default classification for any newly created document with no explicit label is **Tier 3 — Confidential**.
- Classification labels should be applied in document metadata within **NexusDocs** where supported.

---

## 3. Customer Data Handling

- All customer data is classified **Tier 4 — Restricted** at minimum and handled according to applicable regulatory frameworks (e.g., GDPR, CCPA, HIPAA where relevant to the customer's industry).
- Customer data may only be stored in Nexus-approved cloud environments as defined in the **IT Policy, Section 10 (Cloud Storage)** — never in personal cloud storage or unmanaged local files.
- Access to customer data is granted strictly on a **need-to-know basis** and reviewed quarterly by the relevant Director and IT Security.
- Customer data must never be:
  - Entered into unapproved AI tools (see **IT Policy, Section 7 — AI Tools Usage**)
  - Exported to personal devices or unmanaged USB drives (see Section 7 of this policy)
  - Shared with third parties without Legal & Compliance review and, where applicable, a signed Data Processing Agreement (DPA)
- Customer data access for support/debugging purposes must be logged and time-limited; standing access to production customer data is prohibited except for designated on-call Engineering/SRE roles.
- Data retention and deletion timelines are defined per customer contract; Customer Success and Legal & Compliance jointly maintain the deletion schedule.

---

## 4. Confidential Information

- Confidential information (Tier 3 and Tier 4) includes but is not limited to: unreleased product plans, financial data, employee records, legal contracts, source code, and internal strategy documents.
- Employees may discuss confidential information only with colleagues who have a legitimate business need, regardless of department or seniority.
- Confidential information must not be discussed in public spaces (cafés, public transit, conferences) or on personal social media/messaging apps.
- Employees separating from Nexus retain confidentiality obligations indefinitely for Tier 3/4 information, as outlined in their employment agreement.
- Sharing confidential information externally requires sign-off per the Approval Hierarchy (Company Profile §9); Legal & Compliance approval is mandatory for any external disclosure of Tier 4 data.

---

## 5. Access Control

- Access follows the **principle of least privilege**: employees receive access only to the systems and data necessary for their role.
- All system access requires MFA as defined in **IT Policy, Section 4**.
- Access provisioning follows the Reporting Hierarchy (Company Profile §8): new access requests are submitted by the employee's Manager via NexusBoard and approved based on the Approval Hierarchy thresholds.
- **Role-Based Access Control (RBAC)** is enforced across NexusDocs, NexusFlow, NexusBoard, production systems, and financial systems.
- Access reviews:
  - **Quarterly** review of privileged/admin access by IT Security and relevant Directors
  - **Immediate revocation** upon role change or separation, coordinated between HRBP, Manager, and IT & Internal Systems
- Shared accounts are prohibited except for designated service accounts, which require IT Security approval and enhanced logging.

---

## 6. Phishing

- All Nexus employees complete mandatory phishing awareness training during onboarding and annually thereafter.
- Suspicious emails must be reported using the **"Report Phishing"** button in NexusMail, consistent with **IT Policy, Section 8 (Email Security)**.
- Nexus conducts periodic simulated phishing campaigns; results are used for training purposes, not punitive action, except in cases of repeated, uncorrected failure.
- Employees who suspect they have clicked a malicious link or entered credentials into a phishing site must immediately:
  1. Disconnect from the network (or disable Wi-Fi)
  2. Report to IT Security via the emergency hotline or NexusConnect **#security-incident** channel
  3. Change affected passwords immediately using NexusVault
- Vishing (voice phishing) and smishing (SMS phishing) attempts should be reported through the same channel; IT Security will never request passwords or MFA codes via phone or text.

---

## 7. Malware

- All company-managed devices run Nexus-approved endpoint protection software, deployed and monitored via **Nexus Device Management (NDM)** as described in **IT Policy, Section 11**.
- Employees must not disable, bypass, or attempt to uninstall endpoint security software.
- Suspicious device behavior (unexpected pop-ups, slow performance, unfamiliar processes) should be reported immediately to IT & Internal Systems.
- Downloading executable files or macros from unverified or external sources is prohibited without IT Security review.
- USB devices and external media must be scanned automatically before file access is permitted (see Section 8 below).
- Suspected malware infections trigger the Incident Reporting process (Section 10) and may result in immediate device isolation from the network.

---

## 8. USB Devices

- Use of personal or unknown-origin USB drives on Nexus devices is **prohibited by default**.
- Nexus-issued encrypted USB drives may be requested through IT & Internal Systems for specific business needs (e.g., secure offline data transfer) and must be returned or securely wiped after use.
- Any USB device connected to a Nexus device is automatically scanned by endpoint security tooling; unscanned or blocked devices will be denied access at the OS level.
- Tier 4 (Restricted) data must never be transferred via USB device under any circumstance without explicit written approval from IT Security and Legal & Compliance.
- Found or unknown USB devices (e.g., picked up in public, received as promotional gifts) must **never** be plugged into a Nexus device — report to IT Security instead.

---

## 9. Encryption

- **Data at rest:** All company devices enforce full-disk encryption via Nexus Device Management (NDM), per IT Policy §11. Production databases and Tier 3/4 data stores use AES-256 encryption at minimum.
- **Data in transit:** All internal and customer-facing traffic uses TLS 1.2 or higher. VPN connections (per IT Policy §5) are mandatory for remote access to internal systems.
- **Credential/key management:** Encryption keys and secrets are managed exclusively through the approved **Nexus Key Management Service (KMS)**; hardcoding credentials in source code or config files is strictly prohibited and enforced via automated code-scanning in CI/CD pipelines.
- **Email encryption:** Emails containing Tier 3/4 data should use encrypted transmission options within NexusMail or be shared via secure NexusDocs links rather than plaintext attachments.
- Employees must never disable or circumvent encryption settings on company devices or cloud storage configurations.

---

## 10. Remote Access

- Remote access to internal Nexus systems must follow the **VPN Usage** requirements defined in **IT Policy, Section 5**.
- Remote-First and hybrid employees (per Company Profile Working Model) accessing systems from home or while traveling must:
  - Use only Nexus-managed, NDM-enrolled devices
  - Connect via NexusSecure VPN when accessing internal resources
  - Ensure MFA is active on all sessions
- Public Wi-Fi use requires VPN activation before any Nexus system access — no exceptions (IT Policy §5).
- Remote access from countries under Nexus's Legal & Compliance travel/data-residency restrictions requires prior approval from IT Security and Legal & Compliance.
- Split-tunneling, unauthorized remote-access software (e.g., unapproved remote desktop tools), and personal VPN services are prohibited for accessing Nexus systems.

---

## 11. Incident Reporting

### 11.1 What Qualifies as an Incident
Includes but is not limited to: suspected phishing compromise, malware infection, lost/stolen device, unauthorized access, data leakage, suspicious account activity, or physical security breaches (e.g., tailgating into an office location).

### 11.2 Reporting Process
1. **Report immediately** via NexusConnect **#security-incident** channel or the IT Security emergency hotline — do not wait for confirmation that an incident is "serious enough."
2. **Do not attempt to remediate independently** (e.g., do not try to delete files or "fix" a suspected malware infection) — preserve evidence for IT Security investigation.
3. IT Security triages and classifies incident severity (Low / Medium / High / Critical) within **1 hour** of report during business hours, or **immediately** for Critical/production-impacting issues via the 24/7 on-call rotation.
4. Confirmed incidents involving Tier 4 data or customer data trigger mandatory Legal & Compliance involvement for regulatory assessment (e.g., breach notification obligations).

### 11.3 Escalation Path
Employee → Manager (informational) → IT Security (actionable report) → Director of Engineering/IT (High/Critical) → CTO + General Counsel (Critical, regulatory, or customer-impacting) → CEO + Board notification (material incidents), consistent with the Approval Hierarchy in the Company Profile.

### 11.4 Post-Incident
- All Medium+ severity incidents receive a documented post-incident review (blameless retrospective) within 10 business days.
- Findings are logged as a **Nexus Decision Record (NDR)** per Company Profile terminology and shared with relevant Guilds (e.g., Security Guild) where applicable.

---

## 12. Security Responsibilities

| Role | Responsibility |
|---|---|
| **All Employees** | Follow this policy, complete annual security training, report suspicious activity promptly |
| **Managers** | Ensure team compliance, approve access requests appropriately, escalate concerns |
| **IT & Internal Systems** | Maintain endpoint security, NDM enrollment, VPN, MFA infrastructure, incident triage |
| **Information Security Analysts** | Monitor threats, run phishing simulations, lead incident investigations |
| **Legal & Compliance** | Regulatory compliance, breach notification obligations, DPA/contract review |
| **Directors/VPs** | Own data classification decisions within their function, quarterly access reviews |
| **CTO** | Overall accountability for technical security posture and incident response |
| **CHRO** | Ensures security training compliance and addresses HR aspects of incidents (e.g., insider threat) |
| **CEO/Board** | Notified of material/critical incidents; ultimate accountability for organizational risk |

---

## 13. FAQ

**Q: How do I know what classification tier a document falls under?**
A: If unlabeled, treat it as **Tier 3 — Confidential** by default. Check with the data owner (typically a Director) if uncertain, especially before external sharing.

**Q: Can I forward a customer's data to a personal email to work on it over the weekend?**
A: No. Customer data (Tier 4) must remain within Nexus-approved systems at all times, per Section 3 and IT Policy §10. This applies regardless of intent.

**Q: I plugged in a USB drive and got blocked — why?**
A: All USB devices are automatically scanned, and personal/unknown-origin drives are blocked by default per Section 8. Request an approved encrypted USB drive from IT if you have a legitimate business need.

**Q: What's the difference between reporting through IT Policy channels vs. Security Incident channels?**
A: Routine IT issues (software requests, device problems) go through NexusBoard IT Request. Suspected security incidents (phishing, malware, unauthorized access, lost devices with data exposure) go through **NexusConnect #security-incident** or the emergency hotline for faster triage.

**Q: Do I need to report a phishing email even if I didn't click anything?**
A: Yes — reporting non-clicked phishing attempts helps IT Security block similar attacks organization-wide and is not treated as a failure.

**Q: I'm traveling internationally for work — do I need special approval to access Nexus systems?**
A: If traveling to a country under Legal & Compliance travel/data-residency restrictions, yes — obtain prior approval from IT Security and Legal & Compliance before departure.

**Q: Who decides if an incident is "big enough" to escalate to the CEO or Board?**
A: IT Security and the CTO/General Counsel make that determination based on severity classification (Section 11.2) and the Approval Hierarchy; individual employees should always report upward rather than self-assess severity.

**Q: Can I use an AI tool to summarize a confidential internal document?**
A: Only if the tool is on the Nexus-Approved AI Tools List (see **IT Policy, Section 7**). Confidential (Tier 3) and Restricted (Tier 4) data must never be entered into unapproved or public AI tools.

---

*This Information Security Policy works in conjunction with the Nexus Technologies IT Policy and Company Profile. It is maintained by IT & Internal Systems and Legal & Compliance and is subject to periodic review, particularly as regulatory requirements evolve. Future related documents may include the Data Privacy Policy and Acceptable Use Policy.*
