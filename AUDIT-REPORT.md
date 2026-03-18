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
