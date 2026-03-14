# MANUS CONTROL RULES
> Paste this at the start of EVERY session — no exceptions

## STRICT RULES — READ BEFORE DOING ANYTHING:

1. ONLY change what is explicitly listed in this prompt.
2. Do NOT redesign, restructure, or improve anything not mentioned.
3. Do NOT add new sections, components, or pages unless instructed.
4. Do NOT change fonts, spacing, layout or content unless instructed.
5. Do NOT rename or move any files.
6. Do NOT change any links, hrefs, or file paths.
7. Do NOT modify embed codes (Google Calendar, GTM, Maps, Google Review).
8. Do NOT change any text content unless a specific rewrite is listed.
9. After completing the task, stop. Do not suggest further improvements.
10. If something is unclear, ask one question. Do not make assumptions.

Work file by file. Confirm each file when done before moving to the next.
Do not do anything yet. Wait for my next instruction.

---

## BRAND REFERENCE
*(Paste at the top of every new coding session)*

| Field | Value |
|---|---|
| Business | Bcom Services Pty Ltd |
| ABN | 92 636 893 108 |
| Phone | 07 3041 8993 |
| Email (residential) | hello@bcomservices.com |
| Email (business) | office@bcomservices.com |
| Website | bcomservices.com.au |
| Location | Gold Coast, Queensland |

**Service Areas:** Southport · Burleigh Heads · Robina · Nerang · Helensvale · Coomera · Palm Beach · Varsity Lakes · Coolangatta · Surfers Paradise · Broadbeach

### Brand Colours

| Name | Hex | Usage |
|---|---|---|
| Navy | `#0d1f3c` | Text, logo wordmark, borders ONLY — never a background |
| Slate Blue | `#1e3a5f` | ALL dark backgrounds: hero, footer, CTA banners |
| Cyan | `#00c8e0` | CTAs, highlights, icon accents, links |
| White | `#ffffff` | Nav background, section backgrounds |
| Off-white | `#f8fafb` | Alternate section backgrounds |
| Light cyan | `#f0f9fb` | Utility bar, subtle tints |

- **Nav background:** `#ffffff` (white) — navy links, cyan on hover
- **Hero background:** `#1e3a5f` with background image + gradient overlay
- **Footer:** `#1e3a5f` slate blue

### Typography & Icons
- **Fonts:** DM Sans (body) + DM Mono (labels, code, contact details)
- **Logo:** Toggle switch SVG icon + "BCOM" in navy bold + "IT SOLUTIONS" in cyan
- **Icons:** Lucide SVG — thin line, animated. No emojis anywhere.

---

## SITE URL STRUCTURE
*(Reference for every prompt)*

```
index.html                                              → Home Page
│
├── home-users.html                                     → Residential Hub Page
│   ├── computer-repairs-gold-coast.html                → Computer Repair Service
│   └── computer-networking-service-gold-coast.html    → Networking & WiFi Service
│
├── business.html                                       → Business Hub Page
│   ├── it-support-and-services-gold-coast.html        → IT Support & Services (Primary GBP)
│   ├── telecommunications-contractor-gold-coast.html  → Telecommunications Contractor
│   └── computer-consultant-gold-coast.html            → Computer Consultant / IT Consulting
│
├── support.html                                        → Support Page
├── about.html                                          → About Page
└── contact.html                                        → Contact Page
```

> ⚠️ All internal links must use these exact filenames. Flat .html structure — no folders, no trailing slashes.

---

## EMBED CODES
*(Copy exactly — never retype)*

### RESIDENTIAL BOOKING BUTTON
**Pages:** `home-users.html` · `computer-repairs-gold-coast.html` · `computer-networking-service-gold-coast.html`

```html
<!-- Google Calendar Appointment Scheduling begin -->
<link href="https://calendar.google.com/calendar/scheduling-button-script.css" rel="stylesheet">
<script src="https://calendar.google.com/calendar/scheduling-button-script.js" async></script>
<script>
(function() {
  var target = document.currentScript;
  window.addEventListener('load', function() {
    calendar.schedulingButton.load({
      url: 'https://calendar.google.com/calendar/appointments/schedules/AcZssZ2z99t5yQNIRoRT8rNM3Jv7-WC-MNC35owGsga-okvZmEIG167e9iLOAco3_vHaX44r6eYmGFRA?gv=true',
      color: '#039BE5',
      label: 'Book an appointment',
      target,
    });
  });
})();
</script>
<!-- end Google Calendar Appointment Scheduling -->
```

---

### BUSINESS BOOKING BUTTON
**Pages:** `business.html` · `it-support-and-services-gold-coast.html` · `telecommunications-contractor-gold-coast.html` · `computer-consultant-gold-coast.html` · `support.html`

```html
<!-- Google Calendar Appointment Scheduling begin -->
<link href="https://calendar.google.com/calendar/scheduling-button-script.css" rel="stylesheet">
<script src="https://calendar.google.com/calendar/scheduling-button-script.js" async></script>
<script>
(function() {
  var target = document.currentScript;
  window.addEventListener('load', function() {
    calendar.schedulingButton.load({
      url: 'https://calendar.google.com/calendar/appointments/schedules/AcZssZ21JsFI48SyH1NJO3oZkyuch15utQ__rWaeHMgfxSppgM_GaVeKRe6Kn0v2oN4XjRgl5D256Up7?gv=true',
      color: '#039BE5',
      label: 'Book an appointment',
      target,
    });
  });
})();
</script>
<!-- end Google Calendar Appointment Scheduling -->
```

---

### GOOGLE MAPS EMBED
**Page:** `index.html` — Service Areas section only

```html
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d451109.88017319166!2d153.36936139999997!3d-27.9542216!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2bf15c9da94c225d%3A0x9a906dab1cca3727!2sBcom%20IT%20Solutions%20%7C%20IT%20Support%20and%20Services%20Gold%20Coast!5e0!3m2!1sen!2sau!4v1772527730869!5m2!1sen!2sau"
  width="100%" height="450" style="border:0; border-radius:12px;"
  allowfullscreen="" loading="lazy"
  referrerpolicy="no-referrer-when-downgrade">
</iframe>
```

---

### GOOGLE REVIEW BUTTON
**Location:** Footer — centred above bottom copyright bar — every page

```html
<a href="https://g.page/r/CSc3yhyrbZCaEBM/review"
   target="_blank"
   rel="noopener noreferrer"
   aria-label="Leave a Google review for Bcom IT Solutions">
  Leave us a Google Review
</a>
```

**Style:** bg white, colour `#0d1f3c`, border-radius 8px, padding 10px 20px, font-weight 600, 0.88rem. Hover: bg `#00c8e0`, colour `#0d1f3c`. Lucide star icon left of text.

**Helper text below** (mono, 0.68rem, muted): *"Your review helps Gold Coast locals find us — thank you!"*

---

### GOOGLE TAG MANAGER
**Both tags on EVERY page.** Container: `GTM-KQRG3BSF` · GA4: `G-RD7XPVP0Z3`

**TAG 1 — First item inside `<head>`:**
```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KQRG3BSF');</script>
<!-- End Google Tag Manager -->
```

**TAG 2 — First item after `<body>`:**
```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KQRG3BSF"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

---

## PAGE HEAD TEMPLATE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google Tag Manager — FIRST in head -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-KQRG3BSF');</script>
  <!-- End Google Tag Manager -->

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="geo.region" content="AU-QLD">
  <meta name="geo.placename" content="Gold Coast">
  <title>Page Title | Bcom IT Solutions</title>
  <meta name="description" content="...">
  <link rel="canonical" href="https://bcomservices.com.au/[filename].html">
  <link rel="stylesheet" href="design-system.css">
</head>
<body>
  <!-- Google Tag Manager (noscript) — FIRST in body -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KQRG3BSF"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

  <!-- nav, content, footer here -->

  <script>lucide.createIcons();</script>
</body>
</html>
```
