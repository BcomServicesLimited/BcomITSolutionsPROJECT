# Bcom IT Solutions — Website Build Knowledge Base

**Project:** BcomITSolutionsNEW  
**Last updated:** 2026-03-04  
**Purpose:** Permanent reference for all bugs encountered, fixes applied, design decisions made, and standards established during the website build. Every future page build must reference this file alongside `CONTROL_RULES.md`.

---

## 1. Asset Standards

| Asset | File | Location | Notes |
|---|---|---|---|
| Logo (original) | `bcom-logo.jpeg` | `/bcom-assets/` | 714 × 296 px, 73.3 KB |
| Logo (WebP) | `bcom-logo.webp` | `/bcom-assets/` | 13.7 KB — 81% smaller, use this on all pages |
| Favicon | `BcomFavicon.gif` | `/bcom-assets/` | Animated GIF, 88 frames, 576 × 576 px |
| Design system | `design-system.css` | `/bcom-assets/` | Single source of truth for all tokens, typography, layout, buttons, cards |
| Nav component | `nav.html` | `/bcom-assets/` | Standalone file — must be **inlined** into each page (see Fix #1) |
| Footer component | `footer.html` | `/bcom-assets/` | Standalone file — must be **inlined** into each page (see Fix #1) |

---

## 1b. WebP Image Format — True WebP Required

All images on this site must be saved and referenced as `.webp` format. The AI image generation tool (`generate_image`) saves files with a `.webp` extension but internally encodes them as **PNG data**. This causes the `file` command to report `PNG image data` even though the filename ends in `.webp`.

**Rule for all future image generation:** After every `generate_image` call, immediately convert the output to true WebP using Pillow:

```python
from PIL import Image
img = Image.open('path/to/image.webp')
img.save('path/to/image.webp', 'WEBP', quality=88)
```

Verify with: `file path/to/image.webp` — output must contain `RIFF` and `Web/P image`, not `PNG image data`.

**Never reference `.jpg`, `.jpeg` or `.png` files in any page HTML.** All `src=` attributes for images must point to `.webp` files only.

---

## 2. Shared Component Integration Rule

### Fix #1 — Nav and Footer Must Be Inlined, Not Referenced as Comments

**Problem:** `nav.html` and `footer.html` were initially inserted into `index.html` as include comments:

```html
<!-- @@include('nav.html') -->
<!-- @@include('footer.html') -->
```

These are build-tool directives (e.g., for Gulp/Parcel preprocessors) and **do not work in plain HTML**. The nav and footer were invisible in the browser.

**Fix:** Use a Python script to read each component file and replace the comment placeholder with the full inlined HTML content. Scripts saved at:

- `/home/ubuntu/inline_nav.py`
- `/home/ubuntu/inline_footer.py`

**Rule for all future pages:** Every new page (`.html`) must have the full contents of `nav.html` pasted directly after the GTM noscript tag, and the full contents of `footer.html` pasted directly before `</body>`. Do not use `@@include` comments or `<link>` imports for these components.

---

## 3. Google Calendar Booking Embed — Critical Bug

### Fix #2 — Escaped Closing Script Tags Break DOM Parsing

**Problem:** The Google Calendar booking button embed was stored with escaped closing script tags:

```html
<script src="...scheduling-button-script.js" async><\/script>
<script>
  ...
<\/script>
```

The `<\/script>` escape is only valid **inside a JavaScript string literal** (to prevent the parser from ending the script block prematurely). When written directly into HTML, the browser treats `<\/script>` as an unknown tag and **does not close the `<script>` block**. As a result, everything after the first booking embed — including the entire Business services column — was consumed as raw script text and never rendered in the DOM.

**Symptom:** The services section showed only one column (Residential). The Business column had zero DOM presence despite being present in the source file.

**Fix:** Replace all `<\/script>` with `</script>` in every embed occurrence. There were three affected embeds in `index.html`:

1. Residential booking (services section)
2. Business booking (services section)
3. Residential booking (service areas section)

**Rule for all future pages:** When pasting Google Calendar embed codes, always verify there are no `<\/script>` escape sequences in the HTML. Use a grep check before finalising any page:

```bash
grep -n '<\\/script>' filename.html
```

The result must return zero matches.

---

## 4. Hero Section Design Standards

### Fix #3 — Hero Height and Overlay Contrast

**Problem:** With the sticky nav bar (utility bar ~28px + main nav 68px = ~96px total), a `min-height: 90vh` hero caused the section to appear excessively tall and pushed down the page. The overlay opacity (`0.88` / `0.75`) was also too dark, creating a harsh contrast against the white nav bar above.

**Fix applied to `index.html`:**

| Property | Before | After |
|---|---|---|
| `.hero` `min-height` | `90vh` | `75vh` |
| `.hero-content` `padding` | `80px 0` | `56px 0` |
| `.hero-overlay` left opacity | `rgba(30,58,95,0.88)` | `rgba(30,58,95,0.72)` |
| `.hero-overlay` right opacity | `rgba(13,31,60,0.75)` | `rgba(13,31,60,0.58)` |

**Rule for all future pages with hero sections:** Use `min-height: 75vh` and overlay opacity values of `0.72` / `0.58` as the baseline. Adjust only if the background image is very light (increase opacity) or very dark (decrease further).

---

## 5. Services Two-Column Layout

The services section uses a CSS Grid with two `.services-col` children inside `.services-columns`. The decorative centre divider (`.services-divider`) must be positioned **outside** the grid flow using `position: absolute` anchored to the `.services-section` container (which must have `position: relative`). If the divider is placed as a third grid child, it consumes a grid column and pushes the business column off-screen.

---

## 6. Suburb Names — Never JavaScript Rendered

All suburb name lists (footer service areas, service areas section pills, LLM entity paragraphs) must be written as **plain HTML text**. They must never be injected via JavaScript (`innerHTML`, template literals, `document.write`, etc.). This is required for:

- Google crawler indexing (Googlebot may not execute all JS)
- LLM entity recognition
- Accessibility (screen readers)

---

## 7. Page Head Template

Every page must include the following in `<head>`, in this order:

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){...})(window,document,'script','dataLayer','GTM-KQRG3BSF');</script>
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
<link rel="icon" type="image/gif" href="BcomFavicon.gif">
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

## 8. Completed Pages — index.html Section Order

The homepage (`index.html`) is built with sections in the following order:

1. `<head>` — GTM, meta, Lucide, design-system.css
2. GTM noscript tag
3. **Nav** (inlined from `nav.html`)
4. **Hero** — badge, H1, subheading, buttons, trust strip, availability card
5. **Services** — intro, Residential column, Business column, booking embeds
6. **Trust** — stats bar (count-up), Google reviews (3 cards), trust badges
7. **Service Areas** — intro paragraphs, suburb pills, Google Maps embed, coverage card
8. **FAQ** — accordion, 6 Q&As, FAQPage schema
9. **SEO Content** — editorial text, Article schema
10. **Closing CTA** — angled bg, buttons, reassurance row
11. **Footer** (inlined from `footer.html`)
12. `lucide.createIcons()` script

---

## 9. Schema Inventory — index.html

| Schema Type | Location | Key Values |
|---|---|---|
| `LocalBusiness` | Nav (inlined) | Phone, email, URL, 12 service areas |
| `AggregateRating` | Trust section | `ratingValue: 5.0`, `reviewCount: 47` |
| `Review` (×3) | Review cards | `itemprop` markup on each card |
| `ServiceArea` | Service areas section | 12 suburbs as `City` entities |
| `FAQPage` | FAQ section | 6 Q&As |
| `Article` | SEO content section | `dateModified: 2026-03-01`, `areaServed` |

---

## 10. Colour & Typography Quick Reference

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
