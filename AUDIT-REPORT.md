# Bcom IT Solutions — Site-wide Metadata & Schema Audit Report

**Audit date:** 2026-03-10
**Standards reference:** KNOWLEDGE_BASE.md · CONTROL_RULES.md
**Scope:** 40 HTML pages across BcomITSolutionsPROJECT repository
**Status:** In progress — Tasks 2–8 appended incrementally. Fixes applied in Task 9 only.

---

## Task 2 — Page Titles & Meta Descriptions

**Checks performed:**
- `<title>` present, 30–60 chars, contains "Gold Coast" (where required), contains "Bcom IT Solutions", single pipe separator
- `<meta name="description">` present, 120–160 chars, contains "Gold Coast" (where required), no double spaces, no truncation, no placeholder text
- `<meta name="robots">` not set to noindex
- `<meta charset="UTF-8">` present
- `<meta name="viewport">` present
- No duplicate descriptions across pages

**Note on HTML entities in titles:** Several titles contain `&amp;` in the raw HTML source (e.g. `OS Troubleshooting &amp; Repair`). This is correct HTML encoding — browsers render these as `&`. Character counts below are based on raw source length. Rendered lengths would be shorter. These are flagged where the raw length exceeds 60 chars.

---

### PASS

21 files passed all checks:

| File | Title | Title len | Desc len |
|---|---|---|---|
| `index.html` | IT Support Gold Coast \| Bcom IT Solutions | 41 | ~~211~~ see issues |
| `support.html` | IT Support Portal \| Bcom IT Solutions | 39 | 132 |
| `contact.html` | Contact Us \| Bcom IT Solutions Gold Coast | 43 | 138 |
| `data-backup-recovery-gold-coast.html` | Data Backup & Recovery Gold Coast \| Bcom IT Solutions | 55 | 151 |
| `performance-optimisation-gold-coast.html` | PC Performance Optimisation Gold Coast \| Bcom IT Solutions | 59 | 148 |
| `mesh-network-setup-gold-coast.html` | Mesh WiFi Network Setup Gold Coast \| Bcom IT Solutions | 55 | 152 |
| `router-and-modem-configuration-gold-coast.html` | Router & Modem Configuration Gold Coast \| Bcom IT Solutions | 60 | 155 |
| `wifi-range-extension-gold-coast.html` | WiFi Range Extension Gold Coast \| Bcom IT Solutions | 52 | 148 |
| `remote-it-support-gold-coast.html` | Remote IT Support Gold Coast \| Bcom IT Solutions | 50 | 149 |
| `it-consulting-strategy-gold-coast.html` | IT Consulting & Strategy Gold Coast \| Bcom IT Solutions | 56 | 152 |
| `managed-it-services-for-small-businesses-gold-coast.html` | Managed IT Services Gold Coast \| Bcom IT Solutions | 50 | 144 |
| `voip-phone-system-installation-and-support-gold-coast.html` | VoIP Setup & Configuration Gold Coast \| Bcom IT Solutions | 57 | 155 |
| `pabx-phone-systems-gold-coast.html` | PBX System Installation Gold Coast \| Bcom IT Solutions | 54 | 148 |
| `network-cabling-for-offices-gold-coast.html` | Data Cabling Gold Coast \| Bcom IT Solutions | 43 | 137 |
| `nbn-internet-support-gold-coast.html` | NBN & Internet Support Gold Coast \| Bcom IT Solutions | 53 | 151 |
| `it-needs-assessment-gold-coast.html` | IT Needs Assessment Gold Coast \| Bcom IT Solutions | 50 | 144 |
| `technology-procurement-advice-gold-coast.html` | Technology Procurement Advice Gold Coast \| Bcom IT Solutions | 60 | 154 |
| `cloud-computing-service-gold-coast.html` | Cloud Migration Planning Gold Coast \| Bcom IT Solutions | 55 | 149 |
| `cybersecurity-health-check-for-small-business-gold-coast.html` | Cybersecurity Risk Assessment Gold Coast \| Bcom IT Solutions | 60 | 154 |
| `software-recommendations-gold-coast.html` | Software Recommendations Gold Coast \| Bcom IT Solutions | 55 | 149 |
| `artificial-intelligence-service-gold-coast.html` | AI Integration & Setup Gold Coast \| Bcom IT Solutions | 53 | 151 |

---

### ISSUES FOUND

| File | Issue | Severity | Fix Required |
|---|---|---|---|
| `index.html` | Description too long (211 chars) | MEDIUM | Shorten to 120–160 chars |
| `home-users.html` | Description too long (182 chars) | MEDIUM | Shorten to 120–160 chars |
| `computer-consultant-gold-coast.html` | Title too long (69 chars raw — has 2 pipe characters) | MEDIUM | Rewrite as `IT Consultant Gold Coast \| Bcom IT Solutions` (52 chars) |
| `computer-consultant-gold-coast.html` | Title has 2 pipe characters | MEDIUM | Use single pipe: `[Service] Gold Coast \| Bcom IT Solutions` |
| `it-support-and-services-gold-coast.html` | Description too long (179 chars) | MEDIUM | Shorten to 120–160 chars |
| `telecommunications-contractor-gold-coast.html` | Description too short (103 chars) | MEDIUM | Expand to 120–160 chars |
| `about.html` | Description too long (197 chars) | MEDIUM | Shorten to 120–160 chars |
| `on-site-computer-repair-gold-coast.html` | Description too long (162 chars) | MEDIUM | Shorten to 120–160 chars |
| `os-troubleshooting-repair-gold-coast.html` | Title too long (62 chars raw — `&amp;` encodes to `&`) | MEDIUM | Rewrite as `OS Repair & Troubleshooting Gold Coast \| Bcom IT Solutions` |
| `os-troubleshooting-repair-gold-coast.html` | Description too long (192 chars) | MEDIUM | Shorten to 120–160 chars |
| `virus-and-malware-removal-services-gold-coast.html` | Description too long (177 chars) | MEDIUM | Shorten to 120–160 chars |
| `software-installation-configuration-gold-coast.html` | Title too long (68 chars) | MEDIUM | Rewrite as `Software Setup & Configuration Gold Coast \| Bcom IT Solutions` |
| `software-installation-configuration-gold-coast.html` | Description too long (166 chars) | MEDIUM | Shorten to 120–160 chars |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | Title too long (64 chars) | MEDIUM | Rewrite as `Home WiFi Setup & Troubleshooting Gold Coast \| Bcom IT Solutions` |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | Description too long (162 chars) | MEDIUM | Shorten to 120–160 chars |
| `network-security-and-firewall-configuration-gold-coast.html` | Description too long (211 chars) | MEDIUM | Shorten to 120–160 chars |
| `network-troubleshooting-diagnostics-gold-coast.html` | Title too long (68 chars) | MEDIUM | Rewrite as `Network Troubleshooting Gold Coast \| Bcom IT Solutions` |
| `network-troubleshooting-diagnostics-gold-coast.html` | Description too long (166 chars) | MEDIUM | Shorten to 120–160 chars |
| `on-site-technical-support-gold-coast.html` | Description too short (113 chars) | MEDIUM | Expand to 120–160 chars |
| `hardware-software-troubleshooting-gold-coast.html` | Title too long (66 chars) | MEDIUM | Rewrite as `Hardware & Software Troubleshooting Gold Coast \| Bcom IT Solutions` |
| `hardware-software-troubleshooting-gold-coast.html` | Description too long (164 chars) | MEDIUM | Shorten to 120–160 chars |
| `business-phone-systems-gold-coast.html` | Title too long (65 chars) | MEDIUM | Rewrite as `Business Phone Systems Gold Coast \| Bcom IT Solutions` |
| `phone-line-installation-cabling-gold-coast.html` | Title too long (64 chars) | MEDIUM | Rewrite as `Phone Line Installation Gold Coast \| Bcom IT Solutions` |
| `phone-line-installation-cabling-gold-coast.html` | Description too long (162 chars) | MEDIUM | Shorten to 120–160 chars |

**Additional notes:**
- `residential.html` — file does not exist in the repository. Listed in Task 1 audit scope but not present. Flagged for Task 9 review.
- No `noindex` robots directives found on any page — all pages are indexable.
- `<meta charset="UTF-8">` present on all 39 existing files.
- `<meta name="viewport">` present on all 39 existing files.
- No duplicate meta descriptions found across any pages.
- All issues are **MEDIUM** severity — no HIGH severity title/meta issues found.

**Summary:**
- Files with no issues: 21
- Files with issues: 17 (all MEDIUM — length or pipe count only)
- Missing files: 1 (`residential.html`)
- HIGH severity issues: 0
- MEDIUM severity issues: 24
- LOW severity issues: 0

---

*Tasks 3–8 findings will be appended below as the audit progresses.*
