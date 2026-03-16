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
