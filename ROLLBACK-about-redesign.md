# Rollback Plan — about.html Options A+B+C Redesign

**Date:** 11 May 2026  
**Scope:** `about.html` page-specific CSS only (header, footer, nav untouched)  
**Rollback tag:** `about-pre-redesign-v1`  
**Changes applied:** Accent colour swap (teal → brand blue), typography tightening, visual noise reduction

---

## What Was Changed

Only the `<style>` block inside `<head>` (lines 143–243) was modified. The following were **not touched**:

- All HTML structure, content, links, and text
- `<head>` meta tags, schema, GTM, canonical, favicon
- Utility bar, main navigation, mega panels
- Footer HTML and footer CSS
- `design-system.css` (shared stylesheet)
- Modal HTML and modal JS

---

## Changes Applied (Options A+B+C)

| Option | Change |
|---|---|
| **A** | Reduced heavy drop shadows; removed thick `border-top: 3px solid` accent lines from cards |
| **B** | Swapped all `#00c8e0` (teal) accent references to `#1a3fbe` (brand blue) |
| **C** | Reduced heading font-weight from 700 to 600 on section headings; increased letter-spacing on labels; increased body line-height |

---

## Rollback Options

### Option 1 — Restore single file from Git tag (fastest, ~30 seconds)

```bash
cd /home/ubuntu/BcomITSolutionsPROJECT
git checkout about-pre-redesign-v1 -- about.html
git add about.html
git commit -m "Rollback: restore about.html to pre-redesign state"
git push origin main
```

Cloudflare Pages will deploy within ~2 minutes.

---

### Option 2 — Manual restore via GitHub UI

1. Go to: https://github.com/BcomServicesLimited/BcomITSolutionsPROJECT/tags
2. Click `about-pre-redesign-v1`
3. Browse to `about.html` → click **Raw** → copy content
4. Paste into the local file and commit

---

## Verification After Rollback

After restoring, confirm the following on the live site:

- [ ] Hero badge has teal border and teal icon
- [ ] Team cards have `border-top: 3px solid #00c8e0` (teal top border)
- [ ] Team photo has teal ring border
- [ ] Why cards have teal top border
- [ ] Service areas section has teal background (`#e6fafd`)
- [ ] CTA banner has teal top border and teal label text
- [ ] No console errors in browser dev tools
