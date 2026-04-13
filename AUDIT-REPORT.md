# Bcom IT Solutions — Audit Report
## BcomServicesLimited/BcomITSolutionsPROJECT

---

## Shared & Global Files Audit

### Audit Date: 2026-03-16

| File | Present | Correct | Issues |
|------|---------|---------|--------|
| design-system.css | YES | YES | LOW — `.badge`, `.hero`, `.mega-panel`, `.nav-link`, `.pill`, FAQ classes not in file. These are intentionally defined as inline `<style>` blocks per-page. File size 9,442 chars (just under 10KB threshold). Not a defect. |
| assets/logo/bcom-logo.webp | YES | YES | None |
| assets/logo/bcom-logo-gold-coast-it-services.webp | YES | YES | None |
| assets/logo/BcomFavicon.gif | YES | YES | None |
| bcom-assets/nav.html | YES | YES | None — 25,416 chars, all 7 nav checks pass |
| bcom-assets/footer.html | YES | YES | None — 5,936 chars |
| robots.txt | YES | YES | None — correct domain, disallows, no whole-site block |
| sitemap.xml | YES | YES | None — 65 URLs, valid XML, correct domain, all 8 industry pages present |
| llms.txt | YES | FIXED | HIGH — 53 occurrences of old domain `bcomservices.com.au` replaced with `www.bcomservices.com`. Fixed in commit `2a4cab4`. |
| _redirects | YES | YES | None — 42 rules (41 x 301, 1 x 410), no live page conflicts |
| KNOWLEDGE_BASE.md | YES | MOSTLY | MEDIUM — ABN `92 636 893 108` not present in this file (it is in CONTROL_RULES.md). All other checks pass. |
| CONTROL_RULES.md | YES | MOSTLY | LOW — No explicit `@@include` rule documented. No explicit `.webp only` rule documented. Both rules exist in practice. |
| GTM on all pages | YES | YES | 65 real pages all have GTM-KQRG3BSF (x2 each). bcom-assets/ fragment files correctly excluded. |
| Lucide on all pages | YES | YES | 65 real pages all have Lucide CDN script (`unpkg.com/lucide@latest`). |
| Booking buttons correct | YES | YES | All known business pages have business button. 13 additional business-oriented pages (AI, cloud, cybersecurity, contact, support, etc.) also correctly use business button but were not in the audit list. No residential pages have wrong button. |

### Issues by Severity

**HIGH: 1 (FIXED)**
- `llms.txt` — entire file used old domain `bcomservices.com.au` instead of `www.bcomservices.com`. All 53 occurrences fixed. Commit `2a4cab4`.

**MEDIUM: 1**
- `KNOWLEDGE_BASE.md` — ABN `92 636 893 108` not present. Present in `CONTROL_RULES.md` Brand Reference table but should also appear in the knowledge base for completeness.

**LOW: 3**
- `design-system.css` — File is 9,442 chars (just under 10KB threshold). Component classes (`.badge`, `.hero`, `.mega-panel`, `.nav-link`, `.pill`, FAQ) are intentionally inline per-page, not in this file. Architecture is correct.
- `CONTROL_RULES.md` — No explicit `@@include` prohibition documented.
- `CONTROL_RULES.md` — No explicit `.webp only` image format rule documented.

### Post-Audit Manual Actions

- [ ] Confirm Cloudflare Pages is connected to `BcomServicesLimited/BcomITSolutionsPROJECT` (check Cloudflare dashboard — cannot be verified from the sandbox)
- [ ] Confirm `bcomwebsite` (private repo) is not being deployed anywhere active

### Shared & Global Files Audit: COMPLETE

---

## Industry Pages Pre-Live Audit

### Date: 18 March 2026
### Pages: 7

| Check | Hospitality | Healthcare | Real Estate | Restaurants | Retail | Trades | Small Biz |
|---|---|---|---|---|---|---|---|
| Title | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Meta description | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Canonical | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| GTM | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| CSS linked | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| BreadcrumbList | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| BC parent = industries | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| LocalBusiness | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| email = hello@ | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| serviceType correct | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| FAQPage schema | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| HowTo schema | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| H1 correct | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Hero image present | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Hero no lazy | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Content image present | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Business button x 3 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| No residential button | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| No placeholder text | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ABN present | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Last updated | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| In sitemap (0.8) | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Not blocked robots | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| In llms.txt | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

### Issues Fixed

HIGH: 1
- `it-support-small-business-gold-coast.html`: CTA email button used `support@bcomservices.com` — changed to `hello@bcomservices.com`

MEDIUM: 0

LOW: 0

### Post-Deploy Actions

- [ ] Submit sitemap in Google Search Console
- [ ] Request indexing for all 7 URLs via URL Inspection tool
- [ ] Run Google Rich Results Test on all 7 pages
- [ ] Verify Industries appears in nav on live site
- [ ] Check Search Console for crawl errors after 48 hours
- [ ] Monitor for indexing within 2 weeks

### Audit: COMPLETE

---

## New Service Pages Pre-Deployment Audit

**Date:** March 2026
**Pages audited:** `microsoft-365-setup-gold-coast.html`, `hardware-procurement-setup-gold-coast.html`, `business-wifi-gold-coast.html`

### Audit Results

| Task | Description | Result |
|------|-------------|--------|
| Task 1 | Full automated audit (47 checks per page) | 152/159 checks passed |
| Task 2 | Fix HIGH issues | 4 false positives resolved (HTML entity decoding in audit script) |
| Task 3 | Fix MEDIUM issues | 3 meta descriptions shortened to 120–160 chars |
| Task 4 | Schema deep validation | All schemas valid; 2 duplicate schemas removed from hardware page |
| Task 5 | Final verification | 3/3 pages pass all 27 genuine checks |
| Task 6 | Audit report | Appended to AUDIT-REPORT.md |

### Issues Found and Fixed

| Severity | Page | Issue | Fix Applied |
|----------|------|-------|-------------|
| MEDIUM | `microsoft-365-setup-gold-coast.html` | Meta description 165 chars (limit 160) | Shortened to 148 chars |
| MEDIUM | `hardware-procurement-setup-gold-coast.html` | Meta description 173 chars (limit 160) | Shortened to 149 chars |
| MEDIUM | `business-wifi-gold-coast.html` | Meta description 168 chars (limit 160) | Shortened to 146 chars |
| LOW | `hardware-procurement-setup-gold-coast.html` | Duplicate FAQPage and HowTo schemas in head | 2 duplicate blocks removed |

### Schema Summary (all pages)

| Schema | M365 | Hardware | WiFi |
|--------|------|----------|------|
| BreadcrumbList (3 items, pos2=business.html) | OK | OK | OK |
| LocalBusiness (email=hello@, correct serviceType) | OK | OK | OK |
| FAQPage (5 questions, no HTML in answers) | OK | OK | OK |
| HowTo (4 steps) | OK | OK | OK |

### Commits

| Commit | Description |
|--------|-------------|
| `c816840` | Fix meta descriptions — new service pages pre-deployment audit |
| `0f7ddec` | Remove duplicate FAQPage and HowTo schemas from hardware procurement page |

### Post-Deploy Actions

- [ ] Submit updated sitemap in Google Search Console
- [ ] Request indexing for all 3 URLs via URL Inspection tool
- [ ] Run Google Rich Results Test on all 3 pages
- [ ] Monitor Search Console for crawl errors after 48 hours

### Audit: COMPLETE

---

## Full Site Review
### Date: 2026-04-12
### Result: CLEAN (0 real issues remaining)

| Task | Check | Result |
|---|---|---|
| Task 1 | Repository cleanup | CLEAN — no backup files, no duplicates, no untracked files |
| Task 2/3 | Image audit | FIXED — 6 PNG files converted to WebP (~26MB → ~1.4MB) |
| Task 4 | Metadata consistency | FIXED — 8 title tags corrected (1 HIGH truncated brand, 7 MEDIUM over-length) |
| Task 5 | Phone/contact consistency | CLEAN — all pages use correct phone and support@bcomservices.com |
| Task 6 | Brand name/copy | CLEAN — "Bcom Services Pty Ltd" in schema/footer is correct legal name |
| Task 7 | Schema integrity | CLEAN — all JSON-LD valid, GTM present on all pages |
| Task 8 | Internal links/navigation | FIXED — 24 broken links resolved across 4 pages |
| Task 9 | Form/button consistency | CLEAN — all business pages use IT support modal, resi pages use Google Calendar |
| Task 10 | CSS/design system | CLEAN — all pages have design-system.css, no emojis, no @@include |
| Task 11 | Sitemap/robots/llms | FIXED — business-wifi-gold-coast.html added to sitemap (71 URLs total) |
| Task 12 | Final summary | 72 pages — all GTM, canonical, meta desc, design-system, nav, no emojis, no PNG refs |

**Commits in this audit:**
- `1cf070a` — Task 2/3: Convert PNG images to WebP
- `24be97c` — Task 4: Fix 8 page title tags
- `442179a` — Task 8: Fix 24 broken internal links across 4 pages
- `615bd36` — Task 11: Add business-wifi-gold-coast.html to sitemap

**Note:** `index.html` reports 4 `</footer>` tags — 3 are valid HTML5 `<footer>` elements inside `<article>` review cards. Not an error.

---

## SEO Improvements — April 2026

**Date:** 2026-04-13

### Changes Deployed

| Commit | Description |
|--------|-------------|
| `2abb867` | Priority 1: Add street address (9 Ferny Avenue, Surfers Paradise QLD 4217) and `openingHours: Mo-Su 00:00-23:59` to LocalBusiness schema on all 69 applicable HTML pages |
| `cb95886` | Priority 2–4: Title/meta CTR fixes, new content sections, llms.txt update |
| `e1bad7d` | Swap Trust Badges and Google Reviews order on homepage (credentials before testimonials) |

### Priority 1 — LocalBusiness Schema
- Added `"streetAddress"`, full `PostalAddress`, and `"openingHours": "Mo-Su 00:00-23:59"` to all 69 applicable pages
- Improves Google Local Pack eligibility and LLM entity recognition

### Priority 2 — Title/Meta CTR Fixes
- `it-support-and-services-gold-coast.html`: new title `IT Support Gold Coast | Same-Day On-Site | Bcom IT Solutions`
- `it-support-small-business-gold-coast.html`: new title `Small Business IT Support Gold Coast | Bcom IT Solutions`
- `microsoft-365-setup-gold-coast.html`: meta updated to lead with "migration" keyword

### Priority 3 — Content Push
- `it-support-and-services-gold-coast.html`: ~280-word section targeting "IT support Gold Coast", 24/7, no fix no fee, address mention
- `managed-it-services-for-small-businesses-gold-coast.html`: ~250-word section targeting "managed IT services Gold Coast" and "fully managed IT services Gold Coast"

### Priority 4 — llms.txt
- Added address and 24/7 hours to header entity block
- Updated descriptions for 4 strengthened pages

### Google Search Console — www vs non-www
- The "Preferred Domain" setting in GSC was removed by Google years ago. Google determines canonical automatically via 301 redirects, sitemaps, and canonical tags.
- Cloudflare `_redirects` already has non-www → www 301. All canonical tags point to `https://www.bcomservices.com/...`. Sitemap URLs all use www. Code is correct.
- **User action required:** Add a Domain Property for `bcomservices.com` in GSC (aggregates all variants). Submit sitemap under the www prefix property. Use URL Inspection to verify Google-selected canonical on key pages.

### Post-Deploy Actions
- [ ] Add Domain Property for `bcomservices.com` in Google Search Console
- [ ] Submit sitemap under www.bcomservices.com property
- [ ] URL Inspection on key pages — verify Google-selected canonical is www version
- [ ] Request Indexing on any pages still showing non-www canonical
- [ ] Recheck GSC Performance in 2–4 weeks for CTR and position improvements

