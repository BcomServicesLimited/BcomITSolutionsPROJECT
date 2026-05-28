# Bcom IT Solutions — Website Build Knowledge Base

**Project:** BcomITSolutionsPROJECT  
**Last updated:** 2026-05-28  
**Purpose:** Permanent reference for all bugs encountered, fixes applied, design decisions made, and standards established during the website build. Every future page build must reference this file alongside `CONTROL_RULES.md`.

---

## 1. REPOSITORY — SINGLE SOURCE OF TRUTH

**GitHub repository:** BcomServicesLimited/BcomITSolutionsPROJECT  
**Branch:** main  
**URL:** https://github.com/BcomServicesLimited/BcomITSolutionsPROJECT

There is ONE repository for this project. Do not create, reference or push to any other repository. All work must be committed to this repository before ending any session. The local sandbox is temporary and resets — GitHub is the only persistent storage.

- **Nav source of truth:** `index.html` (nav block)
- **Footer source of truth:** `index.html` (footer block)

---

## 2. BRAND REFERENCE

| Field | Value |
|---|---|
| Business Name | Bcom Services Pty Ltd |
| Trading Name | Bcom IT Solutions |
| ABN | 92 636 893 108 |
| Phone | 07 3041 8993 |
| Email | support@bcomservices.com |
| Website | https://www.bcomservices.com |
| Location | Gold Coast, Queensland |

**Service Areas:** Southport · Burleigh Heads · Robina · Nerang · Helensvale · Coomera · Palm Beach · Varsity Lakes · Coolangatta · Surfers Paradise · Broadbeach

---

## 3. ASSET STANDARDS

| Asset | File | Location | Notes |
|---|---|---|---|
| Logo (original) | `bcom-logo.jpeg` | `/assets/logo/` | 714 × 296 px, 73.3 KB |
| Logo (WebP) | `bcom-logo.webp` | `/assets/logo/` | 13.7 KB — 81% smaller, use this on all pages |
| Favicon | `BcomFavicon.gif` | `/assets/logo/` | Animated GIF, 88 frames, 576 × 576 px |
| Design system | `design-system.css` | `/` (root) | Single source of truth for all tokens, typography, layout, buttons, cards |

### WebP Image Format — True WebP Required

All images on this site must be saved and referenced as `.webp` format. Never reference `.jpg`, `.jpeg` or `.png` files in any page HTML. All `src=` attributes for images must point to `.webp` files only.

If using AI image generation tools, the output must be converted to true WebP using Pillow or similar tools, as some generators save PNG data with a `.webp` extension.

---

## 4. SHARED COMPONENT INTEGRATION RULE

### Nav and Footer Must Be Inlined, Not Referenced as Comments

**Rule for all future pages:** Every new page (`.html`) must have the full contents of the nav block pasted directly after the GTM noscript tag, and the full contents of the footer block pasted directly before `</body>`. 

Do not use `@@include` comments or `<link>` imports for these components. They must be plain HTML inlined into every file.

---

## 5. GOOGLE CALENDAR BOOKING EMBED — CRITICAL BUG

### Escaped Closing Script Tags Break DOM Parsing

**Problem:** The Google Calendar booking button embed was previously stored with escaped closing script tags (`<\/script>`). When written directly into HTML, the browser treats `<\/script>` as an unknown tag and does not close the `<script>` block, breaking the page layout.

**Rule for all future pages:** When pasting Google Calendar embed codes, always verify there are no `<\/script>` escape sequences in the HTML. Use `</script>` only.

---

## 6. HERO SECTION DESIGN STANDARDS

**Rule for all future pages with hero sections:** Use `min-height: 75vh` and overlay opacity values of `0.72` (left) / `0.58` (right) as the baseline. Adjust only if the background image is very light (increase opacity) or very dark (decrease further).

---

## 7. SUBURB NAMES — NEVER JAVASCRIPT RENDERED

All suburb name lists (footer service areas, service areas section pills, LLM entity paragraphs) must be written as **plain HTML text**. They must never be injected via JavaScript (`innerHTML`, template literals, `document.write`, etc.). This is required for Google crawler indexing, LLM entity recognition, and accessibility.

---

## 8. PAGE HEAD TEMPLATE

Every page must include the following in `<head>`, in this order:

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KQRG3BSF');</script>
<!-- End Google Tag Manager -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Geo meta -->
<meta name="geo.region" content="AU-QLD">
<meta name="geo.placename" content="Gold Coast">
<!-- Page-specific title and description -->
<title>...</title>
<meta name="description" content="...">
<link rel="canonical" href="https://www.bcomservices.com/...">
<!-- Favicon -->
<link rel="icon" type="image/gif" href="assets/logo/BcomFavicon.gif">
<!-- Lucide icons -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<!-- Design system -->
<link rel="stylesheet" href="design-system.css">
```

And at the very bottom of `<body>`, before `</body>`:

```html
<script>lucide.createIcons();</script>
```

---

## 9. SCHEMA INVENTORY

| Schema Type | Location | Key Values |
|---|---|---|
| `LocalBusiness` | Nav (inlined) | Phone, email, URL, 12 service areas |
| `AggregateRating` | Trust section | `ratingValue: 5.0`, `reviewCount: 47` |
| `Review` (×3) | Review cards | `itemprop` markup on each card |
| `ServiceArea` | Service areas section | 12 suburbs as `City` entities |
| `FAQPage` | FAQ section | 6 Q&As |
| `Article` | SEO content section | `dateModified`, `areaServed` |

---

## 10. COLOUR & TYPOGRAPHY QUICK REFERENCE

| Token | Value | Usage |
|---|---|---|
| Primary Navy | `#0d1f3c` | Headings, nav text, dark backgrounds |
| Accent Cyan | `#00c8e0` | Links, icons, borders, CTA buttons |
| Slate Blue | `#1e3a5f` | Stats bar, footer background |
| Light Cyan BG | `#e6fafd` | Service areas section, response callout |
| Off-white BG | `#f8fafb` | Cards, FAQ answer panels |
| Muted text | `#4a5568` | Body paragraphs |
| Very muted | `#94a3b8` | LLM entity paragraphs, helper text |
| Body font | DM Sans | All paragraph and heading text |
| Mono font | DM Mono | Labels, ABN, utility bar, FAQ headings |

---

## 11. RECENT SESSION HISTORY & DECISIONS (APRIL 2026)

### Task A: Google Calendar to IT Support Modal Conversion
- **Decision:** The Google Calendar embed (`AcZssZ21JsFI`) was removed from all 35 business-oriented pages.
- **Replacement:** Replaced with a custom IT Support Request Modal (`#it-support-modal`) triggered by the "Book an appointment" buttons.
- **Reason:** To capture more detailed lead information (name, email, phone, company, issue description) before booking, rather than just a calendar slot.
- **Note:** The 22 residential pages still use the residential Google Calendar embed (`AcZssZ2z99t5`).

### Task B: FormSpree Integration
- **Decision:** The IT Support Request Modal was wired up to FormSpree (`https://formspree.io/f/xpwqkywd`).
- **Implementation:** Added JavaScript to handle form submission, prevent default behaviour, send data via fetch, and display a success/error message within the modal.

### Task C: SEO Content Injection (Page 2 Boosts)
- **Decision:** Added targeted body content and FAQ entries to 4 pages ranking on page 2 of Google to push them to page 1.
- **Pages Updated:**
  - `it-consulting-strategy-gold-coast.html` (Target: "it consulting gold coast")
  - `software-installation-configuration-gold-coast.html` (Target: "software installation and troubleshooting")
  - `cybersecurity-health-check-for-small-business-gold-coast.html` (Target: "ransomware protection gold coast")
  - `microsoft-365-setup-gold-coast.html` (Target: "hybrid work it solutions gold coast")
- **Implementation:** Added 300-400 words of highly relevant, locally-optimised content to each page, matching the existing design system.

### Task D: Computer Repairs Content
- **Decision:** Added a comprehensive body content section to `computer-repairs-gold-coast.html`.
- **Implementation:** Covered hardware/software repairs, on-site vs workshop options, and what to expect from a visit, including local suburb mentions.

### Task E: Site Audit & Cleanup
- **Decision:** Ran a full 12-point site audit across all 72 HTML pages.
- **Fixes Applied:**
  - Converted 6 PNG images to WebP (saving ~25MB).
  - Fixed 8 title tags (truncated brand names, over-length).
  - Fixed 24 broken internal links across 4 pages.
  - Added `business-wifi-gold-coast.html` to `sitemap.xml`.
  - Updated `llms.txt` descriptions for modified pages.
- **Result:** Site is 100% clean with 0 remaining issues.

### Global Rules Enforced
- **Email:** All pages use `support@bcomservices.com` (including schema).
- **Domain:** All pages use `https://www.bcomservices.com`.
- **Social Media:** No social media icons or links exist on the site.
- **Emojis:** No emojis are used anywhere; only Lucide SVGs.
- **Language:** UK English spelling (e.g., "optimisation", "defence").
