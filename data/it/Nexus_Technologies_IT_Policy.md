# Nexus Technologies — Information Technology (IT) Policy

---
Document ID: IT-001
Department: Engineering & IT
Document Owner: IT & Internal Systems
Version: 1.0
Classification: Internal
Last Updated: July 2026
Related Documents:
- Company Profile
- Information Security Policy
- General Company Policies
- Legal & Compliance Manual
Keywords:
- devices
- passwords
- MFA
- VPN
- software installation
- AI tools
- email security
- cloud storage
- NexusBoard
- NexusVault
---


**Document Owner:** IT & Internal Systems (the IT function within the Engineering & IT Department, Company Profile §6)
**Approval Authority:** CTO + CHRO (per Approval Hierarchy, Company Profile §9)
**Applies To:** All Nexus employees, contractors, and temporary staff (informally, "Nexons" — Company Profile §13) across all office locations and remote work arrangements

---

## 1. Purpose & Scope

This policy establishes the standards for the secure and responsible use of Nexus Technologies' IT resources, including company devices, networks, software, cloud services, and communication tools. It applies to all office-based, Remote-First, and hybrid employees as defined in the Company Profile's Working Model.

---

## 2. Company Devices

### 2.1 Issuance
- All full-time employees are issued a **Nexus-managed laptop** (standard: MacBook Pro or Dell Latitude, department-dependent) upon onboarding.
- Engineering and IT roles may request additional hardware (external monitors, docking stations) via **NexusBoard** IT Request queue, subject to Manager approval.
- Personal devices used for company work (BYOD) require enrollment in **Nexus Device Management** (see Section 10) before accessing any company system.

### 2.2 Acceptable Use
- Company devices are intended primarily for business use. Limited, reasonable personal use is permitted provided it does not violate other Nexus policies or introduce security risk.
- Devices must not be shared with family members, roommates, or third parties.
- Lost or stolen devices must be reported to **IT & Internal Systems** within **2 hours** of discovery via the emergency IT hotline or NexusConnect #it-urgent channel.

### 2.3 Return of Devices
- All company devices must be returned within **5 business days** of separation, as coordinated with the employee's HRBP and IT.

---

## 3. Password Policy

### 3.1 Requirements
- Minimum **14 characters**, including at least one uppercase letter, one lowercase letter, one number, and one special character.
- Passwords must not reuse any of the **last 10** previously used passwords.
- Passwords must not contain the employee's name, username, or "Nexus"/"NexusTech" variants.

### 3.2 Rotation
- Passwords for **privileged accounts** (admin, finance systems, production infrastructure) must be rotated every **90 days**.
- Standard user account passwords do not require forced rotation but must be changed immediately if compromise is suspected.

### 3.3 Storage & Sharing
- Passwords must never be shared, written on physical notes, or stored in plaintext files.
- Approved password manager: **NexusVault** (company-provisioned) is mandatory for all credential storage.
- Sharing of account credentials between employees is strictly prohibited, including between manager and direct report.

---

## 4. Multi-Factor Authentication (MFA)

- MFA is **mandatory** for all Nexus systems: NexusMail, NexusConnect, NexusDocs, NexusBoard, NexusFlow, NexusHR Portal, VPN, and all production/cloud environments.
- Approved MFA methods: **NexusAuth** mobile app (primary), hardware security key (for Engineering/IT privileged accounts), SMS backup (fallback only, not primary).
- MFA fatigue attacks (repeated push notifications) must be reported immediately to IT Security; employees must never approve an MFA prompt they did not initiate.
- Loss of MFA device must be reported within **1 hour** to IT & Internal Systems for account recovery via identity verification.

---

## 5. VPN Usage

- All employees connecting to internal Nexus systems (production databases, internal wikis, financial systems) from outside an office location **must** use the **NexusSecure VPN** client.
- Split-tunneling is disabled by default; all traffic to Nexus internal resources routes through the corporate VPN.
- VPN access is tied to individual MFA-authenticated accounts; shared or generic VPN logins are not issued.
- Public Wi-Fi (airports, cafés, hotels) requires VPN activation **before** accessing any Nexus system — no exceptions.
- VPN sessions auto-disconnect after **30 minutes** of inactivity and require re-authentication.

---

## 6. Software Installation

- Employees may not install unauthorized software on company devices without approval from **IT & Internal Systems**.
- Pre-approved software catalog is available via the **NexusBoard Software Request** portal; most common developer and productivity tools are pre-approved for self-service install.
- Engineering teams may install open-source development dependencies and packages relevant to their work, subject to the **Software Bill of Materials (SBOM)** scan performed automatically by IT security tooling.
- Installation of unlicensed, pirated, or unvetted software is strictly prohibited and may result in disciplinary action.
- Browser extensions requesting broad data access must be reviewed and approved by IT Security before install.

---

## 7. AI Tools Usage

- Use of AI tools (including generative AI, coding assistants, and chatbots) for work purposes is permitted **only** through the **Nexus-Approved AI Tools List**, maintained by IT & Internal Systems and Legal & Compliance.
- Approved categories include AI coding assistants, meeting summarization tools, and internal knowledge assistants integrated with **NexusDocs**.
- **Confidential, customer, or personally identifiable information (PII) must never be entered into public/consumer-facing AI tools** not on the approved list.
- Employees must not use unapproved AI tools to generate code, contracts, or customer-facing content without human review.
- Any AI-generated output used in customer deliverables, code, or legal/financial documents must be reviewed and approved by a qualified employee before use.
- Requests to add new AI tools to the approved list go through **IT & Internal Systems**, with Legal & Compliance sign-off for tools processing customer data.

---

## 8. Email Security

- NexusMail is the only approved channel for official external business correspondence.
- Employees must not auto-forward NexusMail to personal or third-party email accounts.
- Suspicious emails (phishing, spoofing, unexpected attachments) must be reported via the **"Report Phishing"** button in NexusMail or forwarded to **security@nexustech.example**.
- External email senders are automatically flagged with an **"[EXTERNAL]"** banner.
- Sensitive attachments (contracts, financial data, customer PII) must be encrypted or shared via **NexusDocs** secure links rather than direct attachment where possible.
- Nexus performs periodic simulated phishing tests; repeated failures may require additional security training.

---

## 9. Internet Usage

- Internet access via Nexus networks/devices is provided primarily for business purposes; reasonable personal use is permitted.
- Access to categories including gambling, adult content, and known malicious/high-risk domains is blocked by default at the network level.
- Peer-to-peer file sharing and unauthorized torrenting is prohibited on all Nexus networks and devices.
- Streaming and high-bandwidth personal use should be limited during Core Hours (10:00 AM–3:00 PM) to preserve network performance for business-critical systems.
- IT & Internal Systems monitors network traffic for security purposes; usage may be logged in accordance with the (forthcoming) Data Privacy Policy.

---

## 10. Cloud Storage

- Official company data must be stored in approved cloud environments: **NexusDocs** (documents/wikis), **NexusBoard** (project artifacts), and the designated **Nexus Cloud Infrastructure** (engineering/production data).
- Use of unauthorized personal cloud storage (personal Google Drive, Dropbox, iCloud, etc.) for company data is prohibited.
- Customer data and PII must only be stored in environments that meet Nexus's data residency and compliance requirements, as designated by Legal & Compliance.
- File-sharing links from NexusDocs must use the **minimum necessary access level** (view vs. edit) and should have expiration dates set for external shares.
- Departing employees' cloud storage access is revoked automatically upon offboarding; data ownership transfers to the employee's manager.

---

## 11. Device Management

- All company-owned and BYOD devices accessing Nexus systems must be enrolled in **Nexus Device Management (NDM)**, the company's Mobile Device Management (MDM)/Endpoint Management platform.
- NDM enforces: disk encryption, minimum OS version compliance, automatic security patching, remote lock/wipe capability, and screen-lock timeout (5 minutes of inactivity).
- Jailbroken, rooted, or otherwise modified devices are prohibited from enrollment.
- Lost/stolen devices are remotely wiped by IT & Internal Systems upon confirmed report.
- Devices failing compliance checks (outdated OS, disabled encryption) are automatically restricted from accessing sensitive systems until remediated.

---

## 12. Backup Policy

- **Company systems and production data:** Automated backups run daily, with retention of 30 days rolling and monthly archives retained for 12 months, managed by IT & Internal Systems and Engineering.
- **Employee devices:** Local device backup to Nexus Cloud is automatic and continuous for documents, desktop, and designated folders; employees should not rely on local-only storage for critical work files.
- **Disaster Recovery:** Critical business systems maintain a Recovery Point Objective (RPO) of 4 hours and Recovery Time Objective (RTO) of 24 hours, tested semi-annually.
- Employees are responsible for ensuring work-critical files reside in approved cloud/backup-covered locations (Section 10), not solely on local drives.

---

## 13. FAQ

**Q: I forgot my NexusVault master password. What do I do?**
A: Contact IT & Internal Systems via the NexusConnect #it-support channel or NexusBoard IT Request. Identity verification is required before any credential reset.

**Q: Can I use my personal laptop to check NexusMail?**
A: Only if the device is enrolled in Nexus Device Management (NDM) and MFA is active. Unenrolled personal devices cannot access NexusMail or any internal system.

**Q: Is ChatGPT or another public AI tool okay to use for drafting client emails?**
A: Only tools on the Nexus-Approved AI Tools List may be used for work purposes, and no confidential or customer data may be entered into public/consumer AI tools. Check the approved list in NexusDocs before use.

**Q: Do I need VPN if I'm working from a Nexus office location?**
A: No — VPN is required only when connecting from outside an office network (remote work, travel, public Wi-Fi).

**Q: What happens if I fail a phishing simulation test?**
A: You'll receive immediate educational feedback and may be required to complete a short security refresher module. Repeated failures are flagged to your manager and HRBP for additional support.

**Q: Can I install Slack, Figma, or other common tools myself?**
A: Most common productivity and developer tools are pre-approved for self-service install via the NexusBoard Software Request portal. Uncommon or data-access-heavy tools require IT Security review.

**Q: What should I do if I lose my company laptop while traveling?**
A: Report it immediately (within 2 hours) via the IT emergency hotline or NexusConnect #it-urgent. IT will remotely lock and, if necessary, wipe the device via NDM.

**Q: Who approves exceptions to this policy?**
A: Exceptions require written approval from the CTO or a delegated Director of Engineering/IT, in consultation with Legal & Compliance where data handling is involved (per Company Profile §9 Approval Hierarchy).

---

*This IT Policy is a living document maintained by IT & Internal Systems and is subject to periodic review. It should be read in conjunction with the Nexus Technologies Company Profile and future policies including Data Privacy, Acceptable Use, and Security Incident Response.*
