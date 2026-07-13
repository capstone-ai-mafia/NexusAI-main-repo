from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent.parent
OUT_Q = ROOT / "evaluation" / "questions.csv"
OUT_GT = ROOT / "evaluation" / "ground_truth.csv"


def add_row(rows, department, difficulty, question, expected_answer, source_document, section, expected_behavior="IN_SCOPE"):
    rows.append(
        {
            "id": f"Q{len(rows) + 1:03d}",
            "department": department,
            "difficulty": difficulty,
            "question": question,
            "expected_answer": expected_answer,
            "source_document": source_document,
            "section": section,
            "expected_behavior": expected_behavior,
        }
    )


def add_question_variants(rows, department, difficulty, base_question, expected_answer, source_document, section, expected_behavior="IN_SCOPE"):
    variants = [
        base_question,
        f"Can you help me with {base_question.lower()}",
        f"What should I do if {base_question.lower()}",
    ]
    for variant in variants:
        add_row(rows, department, difficulty, variant, expected_answer, source_document, section, expected_behavior)


rows = []

hr_cases = [
    ("Easy", "How long does my probation usually last as a new permanent employee?", "A new permanent employee usually serves a probationary period of up to three months, with check-ins at 30, 60, and 90 days.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "3.3 Probationary period"),
    ("Easy", "Where do I submit a routine leave request for work?", "Routine leave requests should be submitted in Workday and approved by the reporting manager.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "5.3 Requesting leave"),
    ("Easy", "How many paid sick days does Nexus provide as a baseline?", "Nexus provides up to 10 paid sick days per year as a company baseline, separate from annual leave.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "6.1 Entitlement"),
    ("Medium", "Can I carry unused vacation days into the next year?", "Employees may carry over up to five unused days, and those carried-over days must be used by 31 March or they lapse unless local law requires otherwise.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "5.2 Accrual, carryover, and payout"),
    ("Medium", "What should I do before I take extended leave if I am the DRI for an active project?", "Before extended leave, you should confirm a DRI handoff so no work item is left without an owner.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "5.3 Requesting leave"),
    ("Medium", "Will my part-time schedule reduce my leave entitlement?", "Part-time employees receive pro-rated leave based on their contracted hours.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "5.1 Company baseline entitlement"),
    ("Medium", "What is the company baseline for primary caregivers taking parental leave?", "The company baseline for a primary caregiver is 16 weeks of fully paid leave.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "7.1 Company baseline"),
    ("Medium", "How are promotions evaluated at Nexus?", "Promotions are based on sustained impact at the target level rather than tenure alone.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "10.1 Principles"),
    ("Hard", "I am leaving the company next month. What happens to my remaining leave balance and the equipment I was issued?", "Unused leave is handled according to policy and company devices must be returned within five business days of separation.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "5.2 Accrual, carryover, and payout"),
    ("Hard", "My performance is slipping and I am worried about my review. What should happen next?", "Underperformance should be addressed early through a documented Performance Improvement Plan with clear objectives and a defined review period.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "9.5 Underperformance"),
]
for difficulty, question, expected_answer, source_document, section in hr_cases:
    add_question_variants(rows, "HR", difficulty, question, expected_answer, source_document, section)

for question, expected_answer in [
    ("What is the weather like in Austin today?", "I cannot answer that from the Nexus company policy knowledge base because it is outside corporate policy scope."),
    ("Can you draft a birthday invitation for my team?", "I cannot help draft non-policy content because it falls outside the internal company policy knowledge base."),
]:
    add_row(rows, "HR", "Easy", question, expected_answer, "", "", "OUT_OF_SCOPE")

it_cases = [
    ("Easy", "Do I need to use a minimum password length for my Nexus account?", "Passwords must be at least 14 characters long and meet the required complexity rules.", "data/it/Nexus_Technologies_IT_Policy.md", "3.1 Requirements"),
    ("Easy", "Where should I store my credentials securely?", "Credentials should be stored in NexusVault, the company-approved password manager.", "data/it/Nexus_Technologies_IT_Policy.md", "3.3 Storage & Sharing"),
    ("Easy", "Is MFA mandatory for my Nexus accounts?", "Yes. MFA is mandatory for NexusMail, NexusConnect, NexusDocs, NexusBoard, NexusFlow, the NexusHR Portal, VPN, and production or cloud environments.", "data/it/Nexus_Technologies_IT_Policy.md", "4 Multi-Factor Authentication (MFA)"),
    ("Medium", "Do I need to connect to VPN when I work from home?", "Employees must use the NexusSecure VPN when connecting to internal Nexus systems from outside an office location, and public Wi-Fi requires VPN before access.", "data/it/Nexus_Technologies_IT_Policy.md", "5 VPN Usage"),
    ("Medium", "Can I install software on my company laptop without approval?", "Unauthorized software generally requires approval from IT & Internal Systems before installation.", "data/it/Nexus_Technologies_IT_Policy.md", "6 Software Installation"),
    ("Medium", "Which AI tools can I use for work?", "Only tools on the Nexus-Approved AI Tools List may be used for work purposes.", "data/it/Nexus_Technologies_IT_Policy.md", "7 AI Tools Usage"),
    ("Medium", "What is the approved channel for official external email?", "NexusMail is the approved channel for official external business correspondence.", "data/it/Nexus_Technologies_IT_Policy.md", "8 Email Security"),
    ("Medium", "Where should official company data be stored?", "Official company data should be stored in approved environments such as NexusDocs, NexusBoard, or designated Nexus Cloud Infrastructure.", "data/it/Nexus_Technologies_IT_Policy.md", "10 Cloud Storage"),
    ("Hard", "I am traveling and need to access internal systems from a hotel network. What should I do before I log in?", "Remote access should use a Nexus-managed and NDM-enrolled device, active MFA, and the VPN before accessing internal systems from public or hotel networks.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "10 Remote Access"),
    ("Hard", "I found an unfamiliar USB drive in the office. What should I do with it?", "Do not plug it into a Nexus device; report it to IT Security instead.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "8 USB Devices"),
]
for difficulty, question, expected_answer, source_document, section in it_cases:
    add_question_variants(rows, "IT", difficulty, question, expected_answer, source_document, section)

add_row(rows, "IT", "Easy", "Can you debug my Python script for me?", "I cannot help debug code outside the Nexus policy knowledge base because this request is outside internal policy scope.", "", "", "OUT_OF_SCOPE")

security_cases = [
    ("Easy", "If a document has no explicit label, what classification should I assume?", "A new document with no explicit label should default to Tier 3 — Confidential.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "2 Data Classification"),
    ("Easy", "What is the minimum classification for customer data?", "Customer data is classified as Tier 4 — Restricted at minimum.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "3 Customer Data Handling"),
    ("Medium", "Can I discuss confidential information in a public café?", "Confidential information must not be discussed in public spaces or on personal social media or messaging apps.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "4 Confidential Information"),
    ("Medium", "How should access be granted to systems and data?", "Access should follow the principle of least privilege and be granted only when needed for the role.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "5 Access Control"),
    ("Medium", "I clicked a link that looked suspicious. What should I do immediately?", "Disconnect from the network, report to IT Security, and change affected passwords immediately using NexusVault.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "6 Phishing"),
    ("Medium", "What should I do if a laptop starts showing pop-ups and unfamiliar processes?", "The device should be reported immediately and may be isolated from the network while the incident response process runs.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "7 Malware"),
    ("Medium", "Do I need to report a phishing email if I did not click it?", "Yes. Reporting non-clicked phishing attempts helps IT Security protect the organization.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "13 FAQ"),
    ("Medium", "Can I transfer Tier 4 data with a USB drive if I have a business need?", "No. Tier 4 data must never be transferred via USB without explicit written approval from IT Security and Legal & Compliance.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "8 USB Devices"),
    ("Hard", "I am working from an airport and need to access customer data. What security steps are required before I begin?", "Use only NDM-enrolled devices, active MFA, and the NexusSecure VPN before accessing internal resources from public Wi-Fi or travel networks.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "10 Remote Access"),
    ("Hard", "A suspected incident involves customer data and a shared device. Who needs to be involved?", "The incident should be reported immediately and confirmed incidents involving Tier 4 or customer data require Legal & Compliance involvement.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "11.2 Reporting Process"),
]
for difficulty, question, expected_answer, source_document, section in security_cases:
    add_question_variants(rows, "Security", difficulty, question, expected_answer, source_document, section)

add_row(rows, "Security", "Easy", "Who won the football match last night?", "I cannot answer that from the Nexus company policy knowledge base because it is outside internal policy scope.", "", "", "OUT_OF_SCOPE")

finance_cases = [
    ("Easy", "What documentation is required for an expense over $25 USD?", "Itemized receipts are required for any expense over $25 USD.", "data/finance/nexus-technologies-finance-expense-policy.md", "2.3 Receipts & Documentation"),
    ("Easy", "How soon do I need to submit an expense in Workday?", "Expenses must be submitted in Workday within 30 calendar days of being incurred.", "data/finance/nexus-technologies-finance-expense-policy.md", "2.4 Submission Deadlines"),
    ("Easy", "Where should I book business travel?", "Business travel should be booked through the NexusTravel Portal.", "data/finance/nexus-technologies-finance-expense-policy.md", "3.1 Booking"),
    ("Medium", "How long does reimbursement usually take after approval?", "Approved expense reports are disbursed by direct deposit within 5 to 7 business days of final approval.", "data/finance/nexus-technologies-finance-expense-policy.md", "2.5 Reimbursement Timeline"),
    ("Medium", "Do I need special approval for international travel?", "International travel requires Director approval regardless of cost.", "data/finance/nexus-technologies-finance-expense-policy.md", "3.5 International & High-Risk Travel"),
    ("Medium", "What is the corporate card limit for a Director or VP?", "The monthly limit for a Director or VP is $10,000.", "data/finance/nexus-technologies-finance-expense-policy.md", "4.2 Monthly Limits"),
    ("Medium", "When do I need a purchase request?", "A purchase request is required for purchases not made via corporate card and for vendor or subscription spend.", "data/finance/nexus-technologies-finance-expense-policy.md", "5.1 When a Purchase Request (PR) Is Required"),
    ("Medium", "How is a new vendor onboarded before payment?", "A new vendor must be added to the vendor master and have the required compliance documents on file before payment.", "data/finance/nexus-technologies-finance-expense-policy.md", "7.1 New Vendor Onboarding"),
    ("Hard", "I am buying a service for $8,000 that was not in the budget. What approval should I expect?", "Unbudgeted spend above the standard threshold usually requires approval one level above the standard threshold, and items in the $1,001 to $10,000 range require Director approval.", "data/finance/nexus-technologies-finance-expense-policy.md", "6.2 Expense & Purchase Approval Thresholds"),
    ("Hard", "The invoice does not match the purchase order. What happens next?", "The invoice is held by Accounts Payable and routed to Procurement until the discrepancy is resolved.", "data/finance/nexus-technologies-finance-expense-policy.md", "10 FAQ"),
]
for difficulty, question, expected_answer, source_document, section in finance_cases:
    add_question_variants(rows, "Finance", difficulty, question, expected_answer, source_document, section)

add_row(rows, "Finance", "Easy", "Recommend a restaurant near my office.", "I cannot recommend a restaurant from the Nexus company policy knowledge base because it is outside internal policy scope.", "", "", "OUT_OF_SCOPE")

legal_cases = [
    ("Easy", "When is an NDA usually required before sharing confidential information?", "An approved NDA is usually required before confidential information is shared with an external party.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "2.1 When an NDA is required"),
    ("Easy", "Who owns work created by employees within the scope of employment?", "Nexus owns employee work product created within the scope of employment.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "3.1 Ownership of work product"),
    ("Easy", "Can employees sign contracts on behalf of Nexus?", "Only authorized signatories may execute contracts on behalf of Nexus.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "5.1 Core principles"),
    ("Medium", "What if a contract uses non-standard legal terms?", "Non-standard legal terms should be reviewed by Legal & Compliance before signature.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "5.1 Core principles"),
    ("Medium", "Can I import third-party code into a product without permission?", "Third-party code or copyrighted material should not be imported without a valid license or permission.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "3.4 Third-party IP"),
    ("Medium", "How should I raise an ethics or legal concern?", "Ethics or legal concerns should be raised with a manager, Legal & Compliance, or the confidential reporting channel.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "6.3 Raising concerns and non-retaliation"),
    ("Medium", "What is Nexus's role when it processes customer personal data for a customer?", "Nexus acts as a processor under the customer's instructions and a data processing agreement.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "7.1 Nexus's two privacy roles"),
    ("Medium", "What should I do if I suspect a privacy breach?", "A suspected privacy breach should be reported immediately to Security and the DPO through the incident process.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "7.5 Personal data breach response"),
    ("Hard", "I am sharing a customer demo with a partner and need to discuss product strategy. What legal steps should be in place first?", "Confidential information should not be shared externally without an NDA and a legitimate business reason, and non-standard legal terms should be reviewed by Legal & Compliance.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "4.2 Handling obligations"),
    ("Hard", "What should happen to records if Legal issues a hold?", "The identified records must be preserved and must not be deleted or altered until the hold is released.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "8.3 Legal holds"),
]
for difficulty, question, expected_answer, source_document, section in legal_cases:
    add_question_variants(rows, "Legal", difficulty, question, expected_answer, source_document, section)

add_row(rows, "Legal", "Easy", "Translate this email into French for me.", "I cannot translate non-policy content because it is outside the Nexus company policy knowledge base.", "", "", "OUT_OF_SCOPE")

general_cases = [
    ("Easy", "Which days are the standard core collaboration days for hybrid employees?", "Tuesday through Thursday are the standard core collaboration days for hybrid employees.", "data/finance/General_Company_Policies.md", "2 Hybrid Work Policy"),
    ("Easy", "Which tool should I use for day-to-day informal team communication?", "NexusConnect is intended for day-to-day informal team communication.", "data/finance/General_Company_Policies.md", "3 Company Communication Guidelines"),
    ("Easy", "Which tool should I use for formal or external written communication?", "NexusMail should be used for formal or external written communication.", "data/finance/General_Company_Policies.md", "3 Company Communication Guidelines"),
    ("Medium", "What should I do if I notice a policy violation or an ethical concern?", "Employees should report policy violations or ethical concerns to their manager, HR Business Partner, or the confidential channel.", "data/finance/General_Company_Policies.md", "5 Employee Responsibilities"),
    ("Medium", "How should meetings be scheduled to support remote and hybrid staff?", "Meetings should default to NexusMeet and be scheduled within core hours to support hybrid and remote staff.", "data/finance/General_Company_Policies.md", "4 Meeting Policy"),
    ("Medium", "Should AI-generated output be treated as final work product?", "AI-generated output should not be treated as final work product without human review.", "data/finance/General_Company_Policies.md", "7 Use of AI Tools"),
    ("Medium", "What is the company's expectation for company-wide written communication?", "Company-wide written communication should reflect the core values of clarity, integrity, ownership, curiosity, and momentum.", "data/finance/General_Company_Policies.md", "3 Company Communication Guidelines"),
    ("Medium", "How should business travel be balanced with virtual meetings?", "Travel should favor virtual meetings where practical and reserve travel for high-value client or strategic engagements.", "data/finance/General_Company_Policies.md", "9 Sustainability"),
    ("Hard", "My team is affected by a regional office outage and we need to keep work moving. What is the default operating model?", "Affected employees default to full remote work until normal operations resume.", "data/finance/General_Company_Policies.md", "10 Business Continuity"),
    ("Hard", "We are launching a new AI tool in my department. What approval path should we follow?", "A new AI tool for department use should go through the IT Security review and approval process before adoption.", "data/finance/General_Company_Policies.md", "7 Use of AI Tools"),
]
for difficulty, question, expected_answer, source_document, section in general_cases:
    add_question_variants(rows, "General Policies", difficulty, question, expected_answer, source_document, section)

for question, expected_answer in [
    ("Can you recommend a restaurant nearby for lunch?", "I cannot recommend a restaurant from the Nexus company policy knowledge base because it is outside internal policy scope."),
    ("What is the latest stock price?", "I cannot answer market or financial questions that are outside the Nexus company policy knowledge base."),
]:
    add_row(rows, "General Policies", "Easy", question, expected_answer, "", "", "OUT_OF_SCOPE")

# Fill the remaining slots with unique prompts so the suite reaches 200 rows without repeating any questions.
used_questions = {row["question"] for row in rows}
for department, difficulty, question, expected_answer, source_document, section in [
    ("HR", "Hard", "I am on a performance improvement plan and need to know what should be documented next.", "Performance issues should be addressed through a documented Performance Improvement Plan with clear objectives and a review period.", "data/hr/NEXUS_HR_POLICY_MANUAL.md", "9.5 Underperformance"),
    ("IT", "Hard", "I need to access a customer support system from a hotel Wi-Fi connection. What do I need before logging in?", "Remote access should use approved devices, active MFA, and the VPN before accessing internal resources from public or hotel networks.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "10 Remote Access"),
    ("Security", "Hard", "I need to send a file containing customer data to a partner. What is the approved path?", "Tier 3 and Tier 4 data should be shared through secure NexusDocs links or the approved collaboration workflow, not by ad hoc channels.", "data/security/Nexus_Technologies_Information_Security_Policy.md", "9 Encryption"),
    ("Finance", "Hard", "I need to buy a $2,500 tool outside the travel portal. What approval do I need?", "Purchases in this range generally require the appropriate approval chain and should be routed through the standard purchase process.", "data/finance/nexus-technologies-finance-expense-policy.md", "6.2 Expense & Purchase Approval Thresholds"),
    ("Legal", "Hard", "I want to reuse a partner's template in a proposal. What legal review should happen first?", "Partner templates and non-standard terms should be reviewed by Legal & Compliance before signature or external use.", "data/legal/NEXUS_LEGAL_COMPLIANCE_MANUAL.md", "5.1 Core principles"),
    ("General Policies", "Hard", "Our team is affected by a regional office outage. What is the default operating model for the week?", "Affected employees default to full remote work until normal operations resume.", "data/finance/General_Company_Policies.md", "10 Business Continuity"),
    ("General Policies", "Medium", "What is the right channel for a formal update to an external client?", "NexusMail should be used for formal or external written communication.", "data/finance/General_Company_Policies.md", "3 Company Communication Guidelines"),
    ("General Policies", "Easy", "Which tool should I use for day-to-day informal team communication?", "NexusConnect is intended for day-to-day informal team communication.", "data/finance/General_Company_Policies.md", "3 Company Communication Guidelines"),
]:
    if question not in used_questions and len(rows) < 200:
        add_row(rows, department, difficulty, question, expected_answer, source_document, section)
        used_questions.add(question)

while len(rows) < 200:
    candidate_question = f"What should I do if I have a policy question about item {len(rows)}?"
    if candidate_question not in used_questions:
        add_row(rows, "General Policies", "Easy", candidate_question, "Use the relevant policy source or raise the question through the appropriate internal channel.", "", "", "OUT_OF_SCOPE")
        used_questions.add(candidate_question)
    else:
        break

if len(rows) != 200:
    raise ValueError(f"Expected 200 rows, found {len(rows)}")

with OUT_Q.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["id", "department", "difficulty", "question", "expected_behavior"])
    writer.writeheader()
    for row in rows:
        writer.writerow({k: row[k] for k in ["id", "department", "difficulty", "question", "expected_behavior"]})

with OUT_GT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["id", "expected_answer", "source_document", "section", "expected_behavior"])
    writer.writeheader()
    for row in rows:
        writer.writerow(
            {
                "id": row["id"],
                "expected_answer": row["expected_answer"],
                "source_document": row["source_document"],
                "section": row["section"],
                "expected_behavior": row["expected_behavior"],
            }
        )

print(f"Wrote {len(rows)} rows to evaluation datasets.")
