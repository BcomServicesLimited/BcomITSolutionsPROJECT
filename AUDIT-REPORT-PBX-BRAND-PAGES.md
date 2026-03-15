# Audit Report — PBX Brand Pages
**Project:** Bcom IT Solutions — BcomITSolutionsPROJECT  
**Pages audited:** 4 PBX brand pages  
**Audit date:** March 2026  
**Auditor:** Manus AI  

---

## Pages Audited

| Page | File |
|---|---|
| LG Ericsson PBX Gold Coast | `lg-ericsson-pbx-gold-coast.html` |
| Alcatel-Lucent PBX Gold Coast | `alcatel-lucent-pbx-gold-coast.html` |
| Panasonic PBX Gold Coast | `panasonic-pbx-gold-coast.html` |
| NEC PBX Gold Coast | `nec-pbx-gold-coast.html` |

---

## Task 1 — Head Tags

**Result: PASS (with LOW notes — no fixes applied)**

All critical head tag elements are present and correct on all 4 pages: canonical URL, OG tags, Twitter tags, GTM (head + noscript). The following LOW-severity observations were noted but left unchanged per user instruction:

| Page | Title length | Meta description length | Note |
|---|---|---|---|
| LG Ericsson | 46 chars | 154 chars | Title slightly short of 50-char target |
| Alcatel-Lucent | 49 chars | 166 chars | Meta 11 chars over 155-char guideline |
| Panasonic | 44 chars | 173 chars | Title short; meta 18 chars over |
| NEC | 38 chars | 167 chars | Title short; meta 12 chars over |

No fixes applied. No commit.

---

## Task 2 — BreadcrumbList Schema

**Result: ALL PASS — no fixes required**

All 4 pages have a valid BreadcrumbList with depth 4:
- Position 1: Home → `https://www.bcomservices.com/`
- Position 2: Business → `https://www.bcomservices.com/business.html`
- Position 3: Business Phone Systems → `https://www.bcomservices.com/business-phone-systems-gold-coast.html`
- Position 4: Brand-specific page (unique per page)

No commit.

---

## Task 3 — LocalBusiness Schema

**Result: ALL PASS — no fixes required**

All 4 pages have a valid `["LocalBusiness","ProfessionalService"]` schema block with correct:
- `name` (brand-specific)
- `serviceType` (brand-specific)
- `telephone`: `+61730418993`
- `email`: `hello@bcomservices.com`
- `url` (brand-specific, correct domain)
- `areaServed`: Gold Coast, QLD, AU
- `provider.name`: Bcom IT Solutions Pty Ltd
- `provider.taxID`: 92 636 893 108

No commit.

---

## Task 4 — FAQPage Schema

**Result: 2 issues found and fixed — commit `f519360`**

### Issue 1 — Alcatel-Lucent: HTML in JSON-LD answer text (HIGH)
The FAQPage Q1 answer contained `<a href="tel:0730418993">07 3041 8993</a>` inside the JSON-LD `text` field. HTML tags inside JSON-LD answer text cause the block to fail JSON parsing entirely, meaning Google cannot read the schema.

**Fix:** Replaced with plain text `07 3041 8993`.

### Issue 2 — NEC: Insufficient model specificity in question text (MEDIUM)
Only 1 of 5 FAQ question texts referenced a specific model number (Q1: SV8100/SV9100). The audit target was 2+ questions referencing model numbers in the question text itself.

**Fix:** Q3 updated from "Can you add DT series handsets to my existing NEC system?" to "Can you add DT820 or DT830 handsets to my existing NEC system?" — updated in both JSON-LD schema and visible HTML accordion.

All other checks passed: 5 questions per page, all ending with `?`, no HTML in answers, no duplicate questions across pages.

---

## Task 5 — HowTo Schema

**Result: ALL PASS — no fixes required**

All 4 pages have a valid HowTo schema with:
- Brand-specific `name` (unique per page)
- Non-empty `description`
- Exactly 4 steps with correct `position` values (1–4)
- No HTML tags in step text
- All HowTo names unique across pages

No commit.

---

## Task 6 — On-Page SEO Essentials

**Result: ALL PASS — no fixes required**

| Check | All 4 pages |
|---|---|
| 1× H1, correct text, left-aligned | ✅ |
| No H4/H5/H6 | ✅ |
| 8× H2s, all brand-specific | ✅ |
| ABN 92 636 893 108 (×5 per page) | ✅ |
| Last updated: March 2026 | ✅ |
| Phone as tel: link (×7–8 per page) | ✅ |
| Badge "Business IT · Gold Coast" | ✅ |
| No emojis | ✅ |
| Hero image — CSS background (no lazy) | ✅ |
| Body image — loading="lazy" | ✅ |
| All img src = .webp | ✅ |
| All img have alt text | ✅ |
| Business booking button × 3 | ✅ |
| No residential booking | ✅ |
| Parent page linked | ✅ |
| Additional internal links present | ✅ |
| No .com.au in href attributes | ✅ |
| Page not in nav menu | ✅ |

No commit.

---

## Task 7 — Duplicate Content Analysis

**Result: PASS — no fixes required**

Overall text similarity scores (8-gram method):

| Pair | Similarity | Assessment |
|---|---|---|
| LG Ericsson vs Alcatel-Lucent | 25.3% | Acceptable |
| LG Ericsson vs Panasonic | 25.5% | Acceptable |
| LG Ericsson vs NEC | 25.1% | Acceptable |
| Alcatel-Lucent vs Panasonic | 30.0% | Acceptable |
| Alcatel-Lucent vs NEC | 32.1% | Acceptable |
| Panasonic vs NEC | 31.0% | Acceptable |

Shared content is limited to structural boilerplate (nav, footer, suburb pill list, How It Works process steps, related links). All unique body content — models, services, FAQ, body paragraphs — is fully differentiated across all 4 pages. No duplicate paragraphs in body copy. No duplicate H2 headings. No duplicate service cards.

No commit.

---

## Task 8 — Images WebP Audit

**Result: 5 images compressed — commit `5569e80`**

All 8 PBX images confirmed as true WebP (RIFF/VP8 header). 5 images were oversized (>300KB) and compressed using Pillow at reduced quality. Dimensions unchanged (2752×1536 on all images).

| Image | Before | After | Quality |
|---|---|---|---|
| `lg-ericsson-pbx-gold-coast-hero.webp` | 303KB | 114KB | 80 |
| `lg-ericsson-pbx-gold-coast-installation.webp` | 554KB | 249KB | 70 |
| `alcatel-lucent-pbx-gold-coast-hero.webp` | 730KB | 249KB | 40 |
| `panasonic-pbx-gold-coast-hero.webp` | 320KB | 195KB | 80 |
| `panasonic-pbx-gold-coast-installation.webp` | 453KB | 201KB | 80 |
| `alcatel-lucent-pbx-gold-coast-installation.webp` | 271KB | — | Already OK |
| `nec-pbx-gold-coast-hero.webp` | 286KB | — | Already OK |
| `nec-pbx-gold-coast-installation.webp` | 267KB | — | Already OK |

---

## Task 9 — Sitemap, robots.txt and llms.txt

**Result: 1 issue fixed — commit `29217c2`**

### Sitemap.xml — PASS
All 4 pages present with `lastmod=2026-03-01`, `changefreq=monthly`, `priority=1.0`. No duplicates. Total: 57 URLs.

### robots.txt — PASS
File exists. References `sitemap.xml`. None of the 4 PBX pages are blocked.

### llms.txt — Fixed
The PBX Brand section was using relative paths (`/lg-ericsson-pbx-gold-coast.html`) instead of full absolute URLs. Updated to full `https://www.bcomservices.com/` URLs with descriptive text for each page, matching the format used throughout the rest of the file.

---

## Task 10 — Internal Link and Nav Verification

**Result: ALL PASS — no fixes required**

All 4 pages:
- Link to parent page (`business-phone-systems-gold-coast.html`)
- Have multiple additional internal links (nav + footer + body)
- Do not use `.com.au` in href attributes
- All linked `.html` files exist on disk
- Do not appear in the nav menu
- Are linked from the parent page brand cards (confirmed `href` values)

No commit.

---

## Task 11 — Additional SEO Checks

**Result: ALL PASS — no fixes required**

| Check | LG Ericsson | Alcatel-Lucent | Panasonic | NEC |
|---|---|---|---|---|
| Word count (target 1500+) | 2,337 | 2,081 | 2,071 | 2,120 |
| Primary keyword in first paragraph | ✅ | ✅ | ✅ | ✅ |
| geo.region / geo.placename | ✅ | ✅ | ✅ | ✅ |
| `<html lang="en">` | ✅ | ✅ | ✅ | ✅ |
| charset UTF-8 | ✅ | ✅ | ✅ | ✅ |
| viewport meta | ✅ | ✅ | ✅ | ✅ |
| design-system.css | ✅ | ✅ | ✅ | ✅ |
| Favicon | ✅ | ✅ | ✅ | ✅ |
| lucide.createIcons() | ✅ | ✅ | ✅ | ✅ |
| No @@include | ✅ | ✅ | ✅ | ✅ |
| No `<\/script>` | ✅ | ✅ | ✅ | ✅ |
| All phones as tel: links | ✅ | ✅ | ✅ | ✅ |
| No non-brand inline colours | ✅ | ✅ | ✅ | ✅ |
| Suburb pills (Southport, Burleigh, Robina, Nerang) | ✅ | ✅ | ✅ | ✅ |
| Service areas section | ✅ | ✅ | ✅ | ✅ |
| Closing CTA section | ✅ | ✅ | ✅ | ✅ |
| No unclosed HTML comments | ✅ | ✅ | ✅ | ✅ |
| Exactly 4 JSON-LD blocks | ✅ | ✅ | ✅ | ✅ |

No commit.

---

## Summary of All Fixes Applied

| Task | Issue | Severity | Fix | Commit |
|---|---|---|---|---|
| Task 4 | Alcatel-Lucent FAQPage Q1 answer contained HTML `<a>` tag in JSON-LD — broke schema parsing | HIGH | Replaced with plain text phone number | `f519360` |
| Task 4 | NEC FAQ Q3 question text used "DT series" — insufficient model specificity | MEDIUM | Updated to "DT820 or DT830 handsets" in JSON-LD and HTML | `f519360` |
| Task 8 | 5 of 8 PBX images oversized (303KB–730KB) | MEDIUM | Compressed to ≤249KB using Pillow; dimensions unchanged | `5569e80` |
| Task 9 | llms.txt PBX Brand section used relative paths instead of full URLs | MEDIUM | Updated to full `https://www.bcomservices.com/` URLs with descriptions | `29217c2` |

**Total issues fixed: 4**  
**Total commits: 3**  
**Files modified: 2 HTML pages, 5 image files, 1 llms.txt**  
**Files not modified: sitemap.xml, robots.txt, nav, footer, any other pages**

---

## Commits

| Commit | Description |
|---|---|
| `f519360` | Fix FAQPage schema — PBX brand pages audit |
| `5569e80` | Compress oversized PBX hero/installation images — audit Task 8 |
| `29217c2` | Fix llms.txt PBX Brand section — use full absolute URLs |
