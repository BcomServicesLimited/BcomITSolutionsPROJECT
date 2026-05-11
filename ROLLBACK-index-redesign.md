# Rollback Plan — index.html Options A+B+C Redesign

**Tag:** `index-pre-redesign-v1`
**Date tagged:** 11 May 2026
**Scope:** CSS-only changes to `index.html` — accent colour, typography, shadow reduction. No HTML structure, content, links, or embeds were changed.

---

## What was changed

- All `#00c8e0` (teal) accent colours replaced with `#1a3fbe` (brand blue)
- All `rgba(0,200,224,...)` teal rgba values replaced with brand blue equivalents
- `--cyan` CSS variable overridden to `#1a3fbe`
- `font-weight: 700` on section headings reduced to `font-weight: 600`
- `line-height` on body text increased from 1.7 to 1.85
- `box-shadow` values reduced (less spread, lower opacity)
- Card hover lift reduced from 5–6px to 3–4px translateY
- Section label `letter-spacing` increased slightly

---

## To roll back instantly

Run the following two commands from the repo root:

```bash
git checkout index-pre-redesign-v1 -- index.html
git add index.html && git commit -m "Rollback: restore index.html to pre-redesign state" && git push origin main
```

This restores `index.html` exactly as it was before any A+B+C changes were applied. All other files are unaffected.

---

## To roll back the about page (separate tag)

```bash
git checkout about-pre-redesign-v1 -- about.html
git add about.html && git commit -m "Rollback: restore about.html to pre-redesign state" && git push origin main
```
