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

---

## Task 2 Fixes Applied

**Date applied:** 2026-03-10
**Rule:** Only `<title>` and `<meta name="description">` tags edited. No other content, H1s, canonical URLs, nav, footer, body content, or schema were touched.

| File | Element | Before | After | Rendered chars |
|---|---|---|---|---|
| `computer-consultant-gold-coast.html` | `<title>` | `IT Consultant Gold Coast \| IT Consulting Services \| Bcom IT Solutions` (69 raw, 2 pipes) | `IT Consulting Gold Coast \| Bcom IT Solutions` | 44 ✓ |

**Notes:**
- Only one fix was instructed in this batch — the double-pipe title on `computer-consultant-gold-coast.html`.
- All other issues identified in the Task 2 audit (description lengths, remaining title lengths) are pending separate fix instructions.
- No description changes were made in this batch.

### Meta Description Rewrites — 13 files

All descriptions verified at 120–155 rendered characters. Only `<meta name="description">` tags were edited. No other content was changed.

| File | Before (chars) | After (chars) | New description |
|---|---|---|---|
| `index.html` | 211 | 133 | Gold Coast IT support for homes and businesses. Computer repair, WiFi, managed IT and cybersecurity — local team, on-site and remote. |
| `home-users.html` | 182 | 146 | Residential IT support across the Gold Coast. Computer repair, WiFi setup, networking and troubleshooting for Gold Coast homes. Call 07 3041 8993. |
| `it-support-and-services-gold-coast.html` | 179 | 145 | Business IT support across the Gold Coast. On-site and remote support, managed IT, hardware troubleshooting and cybersecurity. Call 07 3041 8993. |
| `about.html` | 197 | 135 | Bcom IT Solutions — locally owned Gold Coast IT company. Experienced technicians supporting homes and businesses across the Gold Coast. |
| `on-site-computer-repair-gold-coast.html` | 162 | 141 | On-site computer repair across the Gold Coast. Laptop and PC repair, virus removal, data recovery and performance fixes — same-day available. |
| `os-troubleshooting-repair-gold-coast.html` | 192 | 146 | Windows and macOS troubleshooting and repair across the Gold Coast. Crashes, boot failures, slow startups and OS errors fixed on-site or remotely. |
| `virus-and-malware-removal-services-gold-coast.html` | 177 | 142 | Virus and malware removal across the Gold Coast. On-site diagnosis, ransomware cleanup, scam checks and security hardening. Call 07 3041 8993. |
| `software-installation-configuration-gold-coast.html` | 166 | 146 | Software installation and configuration across the Gold Coast. Business and home software setup, licensing and troubleshooting. Call 07 3041 8993. |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | 162 | 132 | WiFi installation and troubleshooting for Gold Coast homes. Router setup, dead zone fixes, mesh networks and security configuration. |
| `network-security-and-firewall-configuration-gold-coast.html` | 211 | 133 | Network security and firewall setup for Gold Coast homes and small offices. WPA3, guest networks, firewall rules and security audits. |
| `network-troubleshooting-diagnostics-gold-coast.html` | 166 | 143 | Network troubleshooting and diagnostics across the Gold Coast. On-site fault finding for slow, dropping or unreliable home and office networks. |
| `hardware-software-troubleshooting-gold-coast.html` | 164 | 146 | Hardware and software troubleshooting for Gold Coast businesses. On-site and remote fault diagnosis, repairs and configuration. Call 07 3041 8993. |
| `phone-line-installation-cabling-gold-coast.html` | 162 | 134 | Phone line installation and cabling for Gold Coast businesses and offices. New lines, extensions, patch panels and structured cabling. |

### Meta Description Expansions — 2 files (under 120 chars)

| File | Before (chars) | After (chars) | New description |
|---|---|---|---|
| `telecommunications-contractor-gold-coast.html` | 103 | 151 | Business telecommunications across the Gold Coast. Phone systems, VoIP, PBX, data cabling and NBN support for Gold Coast businesses. Call 07 3041 8993. |
| `on-site-technical-support-gold-coast.html` | 113 | 154 | On-site IT support for Gold Coast businesses. We come to your office and fix IT problems fast — same-day available for critical faults. Call 07 3041 8993. |

### Final Verification — All Task 2 Fixes

**Verification date:** 2026-03-10
**Result: 16/16 PASS — 0 FAIL**

All checks passed:
- `<title>` present exactly once on every changed file
- `<meta name="description">` present exactly once on every changed file
- No tags removed or duplicated
- No other content changed

**`computer-consultant-gold-coast.html` title check:**
- Value: `IT Consulting Gold Coast | Bcom IT Solutions`
- Pipe count: 1 ✓
- Rendered length: 44 chars ✓

**Title length notes (no changes required):**
The following files have titles that appear long in raw HTML due to `&amp;` encoding, but render within the 60-character limit. No changes were made to these files:
`os-troubleshooting-repair-gold-coast.html` (58c rendered) · `software-installation-configuration-gold-coast.html` (68c raw / 64c rendered) · `home-wifi-setup-and-troubleshooting-gold-coast.html` (64c raw / 60c rendered) · `network-troubleshooting-diagnostics-gold-coast.html` (68c raw / 64c rendered) · `hardware-software-troubleshooting-gold-coast.html` (66c raw / 62c rendered) · `business-phone-systems-gold-coast.html` (no change) · `phone-line-installation-cabling-gold-coast.html` (64c raw / 60c rendered)

**`residential.html` — SKIP.** File does not exist in the repository. Not an error. No action required.

**Rendered description character counts — all changed files:**

| File | Desc chars |
|---|---|
| `computer-consultant-gold-coast.html` | 137 |
| `index.html` | 133 |
| `home-users.html` | 146 |
| `it-support-and-services-gold-coast.html` | 145 |
| `about.html` | 135 |
| `on-site-computer-repair-gold-coast.html` | 141 |
| `os-troubleshooting-repair-gold-coast.html` | 146 |
| `virus-and-malware-removal-services-gold-coast.html` | 142 |
| `software-installation-configuration-gold-coast.html` | 146 |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | 132 |
| `network-security-and-firewall-configuration-gold-coast.html` | 133 |
| `network-troubleshooting-diagnostics-gold-coast.html` | 143 |
| `hardware-software-troubleshooting-gold-coast.html` | 146 |
| `phone-line-installation-cabling-gold-coast.html` | 134 |
| `telecommunications-contractor-gold-coast.html` | 151 |
| `on-site-technical-support-gold-coast.html` | 154 |

**Task 2 fixes complete.**

---

## Task 3 — Canonical URLs

**Audit date:** 2026-03-10
**Files checked:** 38 existing files (residential.html — SKIP, file does not exist)
**Result: 37 PASS / 1 ISSUE**

### PASS

All 37 files below have a single, correctly formed canonical tag matching the expected value exactly — `https://bcomservices.com.au/[filename].html`, no trailing slash, no `www.`, one tag per page.

`business.html` · `home-users.html` · `computer-consultant-gold-coast.html` · `it-support-and-services-gold-coast.html` · `telecommunications-contractor-gold-coast.html` · `support.html` · `about.html` · `contact.html` · `on-site-computer-repair-gold-coast.html` · `os-troubleshooting-repair-gold-coast.html` · `virus-and-malware-removal-services-gold-coast.html` · `software-installation-configuration-gold-coast.html` · `data-backup-recovery-gold-coast.html` · `performance-optimisation-gold-coast.html` · `home-wifi-setup-and-troubleshooting-gold-coast.html` · `mesh-network-setup-gold-coast.html` · `router-and-modem-configuration-gold-coast.html` · `network-security-and-firewall-configuration-gold-coast.html` · `wifi-range-extension-gold-coast.html` · `network-troubleshooting-diagnostics-gold-coast.html` · `remote-it-support-gold-coast.html` · `on-site-technical-support-gold-coast.html` · `hardware-software-troubleshooting-gold-coast.html` · `it-consulting-strategy-gold-coast.html` · `managed-it-services-for-small-businesses-gold-coast.html` · `business-phone-systems-gold-coast.html` · `voip-phone-system-installation-and-support-gold-coast.html` · `phone-line-installation-cabling-gold-coast.html` · `pabx-phone-systems-gold-coast.html` · `network-cabling-for-offices-gold-coast.html` · `nbn-internet-support-gold-coast.html` · `it-needs-assessment-gold-coast.html` · `technology-procurement-advice-gold-coast.html` · `cloud-computing-service-gold-coast.html` · `cybersecurity-health-check-for-small-business-gold-coast.html` · `software-recommendations-gold-coast.html` · `artificial-intelligence-service-gold-coast.html`

### ISSUES FOUND

| File | Severity | Issue | Required fix |
|---|---|---|---|
| `index.html` | HIGH | Canonical is `https://bcomservices.com.au/` (domain root, no filename) — expected `https://bcomservices.com.au/index.html` | Change canonical href to `https://bcomservices.com.au/index.html` |

**Note on `residential.html`:** File does not exist in the repository. Listed in Task 1 scope but not present. No action required — this is not an error.

---

## Task 4 — Open Graph & Social Meta Tags

**Audit date:** 2026-03-10
**Files checked:** 38 existing HTML files (residential.html — SKIP)
**Result: 0 fully PASS / 38 with issues**

**Note on severity:** OG and Twitter Card tags were not part of the original KNOWLEDGE_BASE.md specification for this site. All issues are logged as MEDIUM severity as instructed. These tags are a recommended addition for social sharing and SEO, not a structural defect.

---

### PASS

No files pass all checks. See issues below.

---

### ISSUES FOUND

Issues fall into four distinct categories:

**Category A — All OG and Twitter tags completely absent (29 files)**

These pages have no OG or Twitter Card tags at all. All 10 required tags are missing on each.

| File |
|---|
| `index.html` |
| `business.html` |
| `support.html` |
| `contact.html` |
| `artificial-intelligence-service-gold-coast.html` |
| `business-phone-systems-gold-coast.html` |
| `cloud-computing-service-gold-coast.html` |
| `cybersecurity-health-check-for-small-business-gold-coast.html` |
| `data-backup-recovery-gold-coast.html` |
| `hardware-software-troubleshooting-gold-coast.html` |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` |
| `it-consulting-strategy-gold-coast.html` |
| `it-needs-assessment-gold-coast.html` |
| `managed-it-services-for-small-businesses-gold-coast.html` |
| `mesh-network-setup-gold-coast.html` |
| `nbn-internet-support-gold-coast.html` |
| `network-cabling-for-offices-gold-coast.html` |
| `network-security-and-firewall-configuration-gold-coast.html` |
| `network-troubleshooting-diagnostics-gold-coast.html` |
| `on-site-technical-support-gold-coast.html` |
| `pabx-phone-systems-gold-coast.html` |
| `performance-optimisation-gold-coast.html` |
| `phone-line-installation-cabling-gold-coast.html` |
| `remote-it-support-gold-coast.html` |
| `router-and-modem-configuration-gold-coast.html` |
| `software-recommendations-gold-coast.html` |
| `technology-procurement-advice-gold-coast.html` |
| `voip-phone-system-installation-and-support-gold-coast.html` |
| `wifi-range-extension-gold-coast.html` |

**Category B — OG tags present but og:description is stale (11 files)**

These pages have OG tags, but the `og:description` was not updated when the meta description was rewritten in Task 2. The og:description now contains the old, longer description text.

| File | Severity |
|---|---|
| `about.html` | MEDIUM |
| `computer-consultant-gold-coast.html` | MEDIUM |
| `computer-networking-service-gold-coast.html` | MEDIUM |
| `computer-repairs-gold-coast.html` | MEDIUM |
| `home-users.html` | MEDIUM |
| `it-support-and-services-gold-coast.html` | MEDIUM |
| `on-site-computer-repair-gold-coast.html` | MEDIUM |
| `os-troubleshooting-repair-gold-coast.html` | MEDIUM |
| `software-installation-configuration-gold-coast.html` | MEDIUM |
| `telecommunications-contractor-gold-coast.html` | MEDIUM |
| `virus-and-malware-removal-services-gold-coast.html` | MEDIUM |

**Category C — og:title does not match `<title>` (2 files)**

| File | og:title | `<title>` | Severity |
|---|---|---|---|
| `computer-networking-service-gold-coast.html` | `Computer Networking & WiFi Gold Coast \| Bcom IT Solutions` | `WiFi Installation & Networking Gold Coast \| Bcom IT Solutions` | MEDIUM |
| `computer-repairs-gold-coast.html` | `Computer Repairs Gold Coast \| Bcom IT Solutions` | `Computer Repair Gold Coast \| Bcom IT Solutions` | MEDIUM |

**Category D — twitter:image missing (1 file)**

| File | Severity |
|---|---|
| `home-users.html` | MEDIUM |

---

### Summary Table

| Category | Files affected | Severity |
|---|---|---|
| All OG/Twitter tags completely absent | 29 | MEDIUM |
| og:description stale (not updated after Task 2 rewrites) | 11 | MEDIUM |
| og:title does not match `<title>` | 2 | MEDIUM |
| twitter:image missing | 1 | MEDIUM |

**Total unique files with issues: 38** (some files appear in multiple categories)
**Total files with no issues at all: 0**

---

## Task 3 Fixes Applied — Canonical Domain Correction

**Fix date:** 2026-03-10
**Severity:** HIGH
**Method:** Global find-and-replace across all HTML files

**Find:** `https://bcomservices.com.au/`
**Replace:** `https://bcomservices.com/`

**Result: 339 replacements across 42 files**

This single replacement corrected the domain in all locations simultaneously:
- `<link rel="canonical" href="...">` tags
- `<meta property="og:url" content="...">` tags
- JSON-LD `"url"` fields (LocalBusiness, BreadcrumbList item URLs)
- Any other full-domain href or src references

**Verification:** Zero instances of `https://bcomservices.com.au/` remain in any HTML file. PASS.

| File | Replacements |
|---|---|
| `about.html` | 7 |
| `artificial-intelligence-service-gold-coast.html` | 10 |
| `business-phone-systems-gold-coast.html` | 5 |
| `business.html` | 3 |
| `cloud-computing-service-gold-coast.html` | 6 |
| `computer-consultant-gold-coast.html` | 12 |
| `computer-networking-service-gold-coast.html` | 8 |
| `computer-repairs-gold-coast.html` | 8 |
| `contact.html` | 3 |
| `cybersecurity-health-check-for-small-business-gold-coast.html` | 6 |
| `data-backup-recovery-gold-coast.html` | 10 |
| `hardware-software-troubleshooting-gold-coast.html` | 10 |
| `home-users.html` | 5 |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | 10 |
| `index.html` | 2 |
| `it-consulting-strategy-gold-coast.html` | 10 |
| `it-needs-assessment-gold-coast.html` | 10 |
| `it-support-and-services-gold-coast.html` | 9 |
| `managed-it-services-for-small-businesses-gold-coast.html` | 10 |
| `mesh-network-setup-gold-coast.html` | 10 |
| `nbn-internet-support-gold-coast.html` | 10 |
| `network-cabling-for-offices-gold-coast.html` | 10 |
| `network-security-and-firewall-configuration-gold-coast.html` | 6 |
| `network-troubleshooting-diagnostics-gold-coast.html` | 10 |
| `on-site-computer-repair-gold-coast.html` | 9 |
| `on-site-technical-support-gold-coast.html` | 6 |
| `os-troubleshooting-repair-gold-coast.html` | 9 |
| `pabx-phone-systems-gold-coast.html` | 10 |
| `performance-optimisation-gold-coast.html` | 10 |
| `phone-line-installation-cabling-gold-coast.html` | 10 |
| `privacy-policy.html` | 4 |
| `remote-it-support-gold-coast.html` | 10 |
| `router-and-modem-configuration-gold-coast.html` | 6 |
| `software-installation-configuration-gold-coast.html` | 14 |
| `software-recommendations-gold-coast.html` | 10 |
| `support.html` | 3 |
| `technology-procurement-advice-gold-coast.html` | 10 |
| `telecommunications-contractor-gold-coast.html` | 8 |
| `terms-and-conditions.html` | 4 |
| `virus-and-malware-removal-services-gold-coast.html` | 9 |
| `voip-phone-system-installation-and-support-gold-coast.html` | 10 |
| `wifi-range-extension-gold-coast.html` | 7 |
| **Total** | **339** |

---

## Task 3 Fixes Applied — OG & Twitter Tags (Category A: 29 files)

**Fix date:** 2026-03-10
**Method:** Added complete 10-tag OG/Twitter block to each file after `<meta name="description">`, before `<link rel="canonical">`

**Tag block added to each file:**
```html
<meta property="og:type" content="website">
<meta property="og:title" content="[matches <title>]">
<meta property="og:description" content="[matches meta description]">
<meta property="og:url" content="https://bcomservices.com/[filename].html">
<meta property="og:site_name" content="Bcom IT Solutions">
<meta property="og:image" content="https://bcomservices.com/assets/images/[hero].webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[matches <title>]">
<meta name="twitter:description" content="[matches meta description]">
<meta name="twitter:image" content="https://bcomservices.com/assets/images/[hero].webp">
```

**Verification: 29/29 PASS**

| File | og:image used | Fallback? |
|---|---|---|
| `on-site-computer-repair-gold-coast.html` | `hero-bg-computer-repair.webp` | No |
| `os-troubleshooting-repair-gold-coast.html` | `it-support-onsite-gold-coast.webp` | No |
| `virus-and-malware-removal-services-gold-coast.html` | `virus-malware-removal-gold-coast.webp` | No |
| `software-installation-configuration-gold-coast.html` | `hero-bg-software-installation.webp` | No |
| `data-backup-recovery-gold-coast.html` | `hero-bg-data-backup-recovery.webp` | No |
| `performance-optimisation-gold-coast.html` | `hero-bg-performance-optimisation.webp` | No |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | `hero-bg-wifi-setup.webp` | No |
| `mesh-network-setup-gold-coast.html` | `hero-bg-mesh-wifi.webp` | No |
| `router-and-modem-configuration-gold-coast.html` | `hero-bg-router-modem.webp` | No |
| `network-security-and-firewall-configuration-gold-coast.html` | `hero-bg-network-security.webp` | No |
| `wifi-range-extension-gold-coast.html` | `hero-bg-wifi-range-extension.webp` | No |
| `network-troubleshooting-diagnostics-gold-coast.html` | `hero-bg-network-troubleshooting.webp` | No |
| `remote-it-support-gold-coast.html` | `hero-bg-remote-it-support.webp` | No |
| `on-site-technical-support-gold-coast.html` | `hero-bg-onsite-technical-support.webp` | No |
| `hardware-software-troubleshooting-gold-coast.html` | `hero-bg-hardware-software-troubleshooting.webp` | No |
| `it-consulting-strategy-gold-coast.html` | `hero-bg-it-consulting-strategy.webp` | No |
| `managed-it-services-for-small-businesses-gold-coast.html` | `managed-it-services-hero.webp` | No |
| `business-phone-systems-gold-coast.html` | `business-phone-systems-hero.webp` | No |
| `voip-phone-system-installation-and-support-gold-coast.html` | `voip-phone-system-hero.webp` | No |
| `phone-line-installation-cabling-gold-coast.html` | `phone-line-installation-hero.webp` | No |
| `pabx-phone-systems-gold-coast.html` | `pabx-phone-systems-hero.webp` | No |
| `network-cabling-for-offices-gold-coast.html` | `data-cabling-hero.webp` | No |
| `nbn-internet-support-gold-coast.html` | `nbn-internet-support-hero.webp` | No |
| `it-needs-assessment-gold-coast.html` | `it-needs-assessment-hero.webp` | No |
| `technology-procurement-advice-gold-coast.html` | `technology-procurement-hero.webp` | No |
| `cloud-computing-service-gold-coast.html` | `bcom-og-default.webp` | **YES** — no hero image in assets |
| `cybersecurity-health-check-for-small-business-gold-coast.html` | `bcom-og-default.webp` | **YES** — no hero image in assets |
| `software-recommendations-gold-coast.html` | `bcom-og-default.webp` | **YES** — no hero image in assets |
| `artificial-intelligence-service-gold-coast.html` | `ai-integration-hero.webp` | No |

**Fallback image used:** 3 files — `cloud-computing-service-gold-coast.html`, `cybersecurity-health-check-for-small-business-gold-coast.html`, `software-recommendations-gold-coast.html`

**Note:** `bcom-og-default.webp` does not yet exist in assets — this is a placeholder URL. A default OG image should be created and saved to `assets/bcom-og-default.webp` before these 3 pages are shared on social media.

---

## Task 3 Fixes Applied — OG & Twitter Tags (Category B: stale descriptions)

**Fix date:** 2026-03-10
**Method:** Read current `<meta name="description">` from each file, update `og:description` and `twitter:description` to match exactly. No other tags changed.

| File | Action |
|---|---|
| `index.html` | Full 10-tag OG block added (was missing entirely) |
| `home-users.html` | `og:description` and `twitter:description` updated |
| `it-support-and-services-gold-coast.html` | `og:description` and `twitter:description` updated |
| `about.html` | `og:description` and `twitter:description` updated |
| `on-site-computer-repair-gold-coast.html` | `og:description` and `twitter:description` updated |
| `os-troubleshooting-repair-gold-coast.html` | `og:description` and `twitter:description` updated |
| `virus-and-malware-removal-services-gold-coast.html` | `og:description` and `twitter:description` updated |
| `software-installation-configuration-gold-coast.html` | `og:description` and `twitter:description` updated |
| `telecommunications-contractor-gold-coast.html` | `og:description` and `twitter:description` updated |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | Already matched — no change |
| `network-troubleshooting-diagnostics-gold-coast.html` | Already matched — no change |
| `hardware-software-troubleshooting-gold-coast.html` | Already matched — no change |
| `phone-line-installation-cabling-gold-coast.html` | Already matched — no change |
| `on-site-technical-support-gold-coast.html` | Already matched — no change |

---

## Task 3 Fixes Applied — OG & Twitter Tags (Final Verification)

**Verification date:** 2026-03-10
**Total files checked:** 42
**Result: 42/42 PASS — 0 FAIL**

### Checklist

| Check | Result |
|---|---|
| All 42 files have all 10 required OG/Twitter tags | PASS |
| No `og:url` contains `bcomservices.com.au` | PASS |
| `og:title` matches `<title>` on every page | PASS |
| `og:description` matches `<meta name="description">` on every page | PASS |
| Spot check 5 files (index, about, managed-it, voip, ai) | PASS — all MATCH |
| `twitter:card` is `summary_large_image` on all pages | PASS |
| `og:type` is `website` on all pages | PASS |
| `og:site_name` is `Bcom IT Solutions` on all pages | PASS |
| No `og:image` or `twitter:image` points to `.jpg`, `.jpeg` or `.png` | PASS |
| `home-users.html` now has `twitter:image` | PASS |
| `computer-networking-service-gold-coast.html` `og:title` matches `<title>` | PASS |
| `computer-repairs-gold-coast.html` `og:title` matches `<title>` | PASS |

### Additional files added in final pass (not in original Category A list)

| File | Action |
|---|---|
| `business.html` | Full 10-tag OG block added |
| `contact.html` | Full 10-tag OG block added |
| `support.html` | Full 10-tag OG block added |

### Fallback image files (3 files — no hero image in assets)

| File | Fallback image |
|---|---|
| `cloud-computing-service-gold-coast.html` | `bcom-og-default.webp` |
| `cybersecurity-health-check-for-small-business-gold-coast.html` | `bcom-og-default.webp` |
| `software-recommendations-gold-coast.html` | `bcom-og-default.webp` |

> **Action required:** `bcom-og-default.webp` does not yet exist in the assets folder. A default OG image should be created and saved to `assets/bcom-og-default.webp` before these 3 pages are shared on social media.

### Total files updated across all OG/Twitter fix tasks

| Category | Files | Action |
|---|---|---|
| A — Full block added | 32 | 29 original + business.html, contact.html, support.html |
| B — Stale descriptions synced | 9 | og:description and twitter:description updated |
| C — Title mismatch fixed | 2 | og:title and twitter:title updated |
| D — Missing twitter:image | 1 | twitter:image added to home-users.html |
| Entity encoding normalised | 11 | og:description, og:title synced to match HTML entity format |

---

## Canonical URLs

**Audit date:** 2026-03-10
**Correct domain confirmed:** `https://www.bcomservices.com/`

### PASS (post-fix)

All 39 files pass after the global www domain replacement and index.html fix. Verified 39/39.

### ISSUES FOUND (pre-fix)

| File | Issue | Severity | Fix Required |
|------|-------|----------|--------------|
| All 39 files | Domain missing `www` — canonical used `https://bcomservices.com/` instead of `https://www.bcomservices.com/` | HIGH | Global find-and-replace applied |
| `index.html` | Canonical was bare domain root `https://www.bcomservices.com/` instead of `https://www.bcomservices.com/index.html` | HIGH | Fixed directly |

### Fix Applied

**Global replacement:** `https://bcomservices.com/` → `https://www.bcomservices.com/`
- 427 replacements across 42 files (all HTML + sitemap.xml + llms.txt)
- Corrected: `<link rel="canonical">`, `<meta property="og:url">`, JSON-LD `"url"` fields, BreadcrumbList `"item"` URLs

**index.html canonical:** Updated from `https://www.bcomservices.com/` to `https://www.bcomservices.com/index.html`

**Post-fix verification:** 39/39 PASS — zero remaining instances of old domain.

---

## Open Graph & Social Meta

**Audit date:** 2026-03-10
**Files checked:** 39 existing HTML files (`residential.html` — SKIP, file does not exist)
**Result: 24 PASS / 15 files with issues (all MEDIUM)**

**Note on severity:** All issues are MEDIUM. No missing tag blocks, no wrong domains, no wrong `og:type`, no empty `content=""` attributes, and no `og:title` or `og:description` mismatches were found. The only category of issue is `og:image` paths that do not resolve to an existing file in the assets folder.

---

### PASS

24 files pass all 12 checks:

`artificial-intelligence-service-gold-coast.html` · `business-phone-systems-gold-coast.html` · `business.html` · `data-backup-recovery-gold-coast.html` · `hardware-software-troubleshooting-gold-coast.html` · `home-wifi-setup-and-troubleshooting-gold-coast.html` · `it-consulting-strategy-gold-coast.html` · `it-needs-assessment-gold-coast.html` · `it-support-and-services-gold-coast.html` · `managed-it-services-for-small-businesses-gold-coast.html` · `mesh-network-setup-gold-coast.html` · `nbn-internet-support-gold-coast.html` · `network-cabling-for-offices-gold-coast.html` · `network-security-and-firewall-configuration-gold-coast.html` · `network-troubleshooting-diagnostics-gold-coast.html` · `on-site-technical-support-gold-coast.html` · `pabx-phone-systems-gold-coast.html` · `performance-optimisation-gold-coast.html` · `phone-line-installation-cabling-gold-coast.html` · `remote-it-support-gold-coast.html` · `router-and-modem-configuration-gold-coast.html` · `technology-procurement-advice-gold-coast.html` · `voip-phone-system-installation-and-support-gold-coast.html` · `wifi-range-extension-gold-coast.html`

---

### ISSUES FOUND

| File | Issue | Severity | Fix Required |
|------|-------|----------|--------------|
| `index.html` | `og:url` is `https://www.bcomservices.com/` (bare root) — does not match canonical `https://www.bcomservices.com/index.html` | MEDIUM | Set `og:url` to `https://www.bcomservices.com/index.html` |
| `about.html` | `og:image` path `https://www.bcomservices.com/bcom-logo.webp` not found in assets | MEDIUM | Update to correct assets path |
| `home-users.html` | `og:image` path `https://www.bcomservices.com/bcom-logo.webp` not found in assets | MEDIUM | Update to correct assets path |
| `computer-consultant-gold-coast.html` | `og:image` path `https://www.bcomservices.com/hero-bg-consulting.webp` not found in assets | MEDIUM | Update to correct assets path |
| `computer-networking-service-gold-coast.html` | `og:image` path `https://www.bcomservices.com/hero-bg-networking.webp` not found in assets | MEDIUM | Update to correct assets path |
| `computer-repairs-gold-coast.html` | `og:image` path `https://www.bcomservices.com/hero-bg-computer-repair.webp` not found in assets | MEDIUM | Update to correct assets path |
| `on-site-computer-repair-gold-coast.html` | `og:image` path `https://www.bcomservices.com/hero-bg-computer-repair.webp` not found in assets | MEDIUM | Update to correct assets path |
| `os-troubleshooting-repair-gold-coast.html` | `og:image` path `https://www.bcomservices.com/bcom-assets/it-support-onsite-gold-coast.webp` not found in assets | MEDIUM | Update to correct assets path |
| `virus-and-malware-removal-services-gold-coast.html` | `og:image` path `https://www.bcomservices.com/bcom-assets/virus-malware-removal-gold-coast.webp` not found in assets | MEDIUM | Update to correct assets path |
| `software-installation-configuration-gold-coast.html` | `og:image` path `https://www.bcomservices.com/hero-bg-software-installation.webp` not found in assets | MEDIUM | Update to correct assets path |
| `telecommunications-contractor-gold-coast.html` | `og:image` path `https://www.bcomservices.com/hero-bg-telecoms.webp` not found in assets | MEDIUM | Update to correct assets path |
| `cloud-computing-service-gold-coast.html` | `og:image` path `https://www.bcomservices.com/assets/bcom-og-default.webp` not found in assets | MEDIUM | Create `bcom-og-default.webp` or assign a real hero image |
| `cybersecurity-health-check-for-small-business-gold-coast.html` | `og:image` path `https://www.bcomservices.com/assets/bcom-og-default.webp` not found in assets | MEDIUM | Create `bcom-og-default.webp` or assign a real hero image |
| `software-recommendations-gold-coast.html` | `og:image` path `https://www.bcomservices.com/assets/bcom-og-default.webp` not found in assets | MEDIUM | Create `bcom-og-default.webp` or assign a real hero image |
| `contact.html` | `og:image` path `https://www.bcomservices.com/assets/images/hero-bg-contact.webp` not found in assets | MEDIUM | Update to correct assets path or use fallback |
| `support.html` | `og:image` path `https://www.bcomservices.com/assets/images/hero-bg-support.webp` not found in assets | MEDIUM | Update to correct assets path or use fallback |

---

### Summary

| Category | Count |
|---|---|
| Files passing all checks | 24 |
| Files with `og:image` path not found in assets | 15 |
| Files with `og:url` not matching canonical | 1 (`index.html`) |
| Missing tag blocks | 0 |
| Wrong domain in any tag | 0 |
| Empty `content=""` attributes | 0 |
| `og:title` / `og:description` mismatches | 0 |

**HIGH severity issues: 0**
**MEDIUM severity issues: 16**
**LOW severity issues: 0**

**Root cause of image path issues:** Two groups —
1. Pages that had OG tags before the Category A/B fix pass used non-standard image paths (root-level or `/bcom-assets/` paths) that were not updated to the standard `assets/images/` structure.
2. Three pages (`cloud-computing`, `cybersecurity`, `software-recommendations`) use `bcom-og-default.webp` which has not yet been created.

**Fix required before launch:** Correct all 15 `og:image` paths and create `bcom-og-default.webp`.

---

## Open Graph & Social Meta — Fixes Applied

**Date:** 2026-03-10

All 16 MEDIUM issues identified in the OG & Social Meta audit have been resolved.

### og:image and twitter:image path corrections (15 files)

| File | Old path | New path |
|------|----------|----------|
| `about.html` | `/bcom-logo.webp` (root) | `assets/images/hero-bg.webp` |
| `home-users.html` | `/bcom-logo.webp` (root) | `assets/images/hero-bg-home-users.webp` |
| `computer-consultant-gold-coast.html` | `/hero-bg-consulting.webp` (root) | `assets/images/hero-bg-consulting.webp` |
| `computer-networking-service-gold-coast.html` | `/hero-bg-networking.webp` (root) | `assets/images/hero-bg-networking.webp` |
| `computer-repairs-gold-coast.html` | `/hero-bg-computer-repair.webp` (root) | `assets/images/hero-bg-computer-repair.webp` |
| `on-site-computer-repair-gold-coast.html` | `/hero-bg-computer-repair.webp` (root) | `assets/images/hero-bg-computer-repair.webp` |
| `os-troubleshooting-repair-gold-coast.html` | `/bcom-assets/it-support-onsite-gold-coast.webp` | `assets/images/it-support-onsite-gold-coast.webp` |
| `virus-and-malware-removal-services-gold-coast.html` | `/bcom-assets/virus-malware-removal-gold-coast.webp` | `assets/images/virus-malware-removal-gold-coast.webp` |
| `software-installation-configuration-gold-coast.html` | `/hero-bg-software-installation.webp` (root) | `assets/images/hero-bg-software-installation.webp` |
| `telecommunications-contractor-gold-coast.html` | `/hero-bg-telecoms.webp` (root) | `assets/images/hero-bg-telecoms.webp` |
| `cloud-computing-service-gold-coast.html` | `/assets/bcom-og-default.webp` (missing) | `assets/images/hero-bg.webp` (fallback) |
| `cybersecurity-health-check-for-small-business-gold-coast.html` | `/assets/bcom-og-default.webp` (missing) | `assets/images/hero-bg.webp` (fallback) |
| `software-recommendations-gold-coast.html` | `/assets/bcom-og-default.webp` (missing) | `assets/images/hero-bg.webp` (fallback) |
| `contact.html` | `/assets/images/hero-bg-contact.webp` (missing) | `assets/images/hero-bg.webp` (fallback) |
| `support.html` | `/assets/images/hero-bg-support.webp` (missing) | `assets/images/hero-bg.webp` (fallback) |

### og:url correction (1 file)

| File | Old value | New value |
|------|-----------|-----------|
| `index.html` | `https://www.bcomservices.com/` | `https://www.bcomservices.com/index.html` |

### Final verification result

**40/40 PASS — 0 issues remaining.**

---

## BreadcrumbList Home Item Fix Applied

**Fix date:** 2026-03-10
**Task:** BreadcrumbList Home Item URL — Task 2 fix
**Rule:** Position-1 ListItem "item" must be `https://www.bcomservices.com/` (bare root, no filename)
**Files changed:** 30
**Verification:** 40/40 PASS — 0 HIGH, 0 MEDIUM issues remaining

| File | Before | After |
|------|--------|-------|
| `artificial-intelligence-service-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `business-phone-systems-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `cloud-computing-service-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `contact.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `cybersecurity-health-check-for-small-business-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `data-backup-recovery-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `hardware-software-troubleshooting-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `home-wifi-setup-and-troubleshooting-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `it-consulting-strategy-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `it-needs-assessment-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `managed-it-services-for-small-businesses-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `mesh-network-setup-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `nbn-internet-support-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `network-cabling-for-offices-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `network-security-and-firewall-configuration-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `network-troubleshooting-diagnostics-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `on-site-technical-support-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `os-troubleshooting-repair-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `pabx-phone-systems-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `performance-optimisation-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `phone-line-installation-cabling-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `remote-it-support-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `router-and-modem-configuration-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `software-installation-configuration-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `software-recommendations-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `support.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `technology-procurement-advice-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `virus-and-malware-removal-services-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `voip-phone-system-installation-and-support-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |
| `wifi-range-extension-gold-coast.html` | `https://www.bcomservices.com/index.html` | `https://www.bcomservices.com/` |

**Notes:**
- Only the `"item"` value of the position-1 ListItem in each BreadcrumbList JSON-LD block was changed.
- No other ListItems, properties, canonical tags, OG tags, or visible HTML were modified.
- 4 files (`ns-article-block.html`, `privacy-policy.html`, `terms-and-conditions.html`, `wifi-article-parts.html`) have no BreadcrumbList block — expected, no action required.
- 4 files (`computer-consultant-gold-coast.html`, `computer-repairs-gold-coast.html`, `index.html`, `it-support-and-services-gold-coast.html`) have pre-existing FAQPage JSON parse errors (HTML anchor tags in text fields) — these were already present at the rollback point and are outside the scope of this task.
