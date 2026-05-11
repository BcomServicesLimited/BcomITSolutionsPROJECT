# Rollback Plan — contact.html Option D Redesign

**Date:** 11 May 2026  
**Scope:** `contact.html` body content only (header, footer, nav untouched)  
**Rollback tag:** `contact-pre-redesign-v1`  
**Commit at tag:** see `git show contact-pre-redesign-v1`

---

## What Was Changed

Only the page-specific CSS (`<style>` block inside `<head>`) and the body content sections between the `</nav>` closing tag and the `<footer>` opening tag were modified. The following were **not touched**:

- `<head>` meta tags, schema, GTM, canonical, favicon
- Utility bar (`.utility-bar`)
- Main navigation (`.main-nav`, mega panels, hamburger JS)
- Footer (`.site-footer`)
- `design-system.css` (shared stylesheet — unchanged)

---

## Rollback Options

### Option 1 — Restore single file from Git tag (fastest, ~30 seconds)

```bash
cd /home/ubuntu/BcomITSolutionsPROJECT
git checkout contact-pre-redesign-v1 -- contact.html
git add contact.html
git commit -m "Rollback: restore contact.html to pre-redesign state"
git push origin main
```

Cloudflare Pages will deploy within ~2 minutes.

---

### Option 2 — Full branch revert to tag (if multiple files were affected)

```bash
cd /home/ubuntu/BcomITSolutionsPROJECT
git revert --no-commit HEAD~1..HEAD   # adjust range if needed
git commit -m "Revert: contact.html Option D redesign"
git push origin main
```

---

### Option 3 — Manual restore via GitHub UI

1. Go to: https://github.com/BcomServicesLimited/BcomITSolutionsPROJECT/tags
2. Click `contact-pre-redesign-v1`
3. Browse to `contact.html` → click **Raw** → copy content
4. Paste into the local file and commit

---

## Verification After Rollback

After restoring, confirm the following on the live site:

- [ ] Hero section has dark navy background with centred text
- [ ] Three method cards (Call / Email / Book) render in a 3-column grid
- [ ] Google Maps embed is visible
- [ ] Suburb pills display correctly
- [ ] No console errors in browser dev tools

---

## Notes

- The redesign does **not** affect any other HTML file
- `design-system.css` was not modified — no shared styles were changed
- All content (text, links, phone numbers, email addresses) is identical to the pre-redesign version
