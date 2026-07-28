# LLM / AI-Search Citation Audit — 28 July 2026

Method: web-search probes of the money queries, recording which businesses are
recommended in AI-summarised answers and which sources those answers cite.
Repeat quarterly (next due: late October 2026) and compare.

## Query 1 — "best IT support companies Gold Coast managed IT services"

- Cited source driving the answer: **GoodFirms Gold Coast listicle** (goodfirms.co/it-services/gold-coast)
- Recommended: First Focus, GCIT, Hutchison IT, Teamwork Technology, F1 Solutions, Sharp EIT, Gray Area Consulting, **bcom ICT (last, via own homepage)**
- Note: bcom present but not via the listicle → get listed on GoodFirms.
- Bug found and fixed same day: homepage title glyph rendered as "55-star Rated" (5★ → 5-Star, commit 9c8e607).

## Query 2 — "managed IT services provider Gold Coast small business recommendation"

- Recommended: GCIT (160+ reviews, ISO 27001 — dominant), SEQ IT Services (SMB1001 certified), **"Bcom IT Solutions"**, Techwell, BITS Technology Group
- ⚠ bcom appears under the OLD brand name "Bcom IT Solutions" and via the legacy
  .html URL (managed-it-services-for-small-businesses-gold-coast.html) — the search
  index is serving a stale snippet. The 301 + canonical are in place; expect this
  to correct as Google recrawls. Watch next audit; if still stale, request
  recrawl of the canonical in GSC.
- Competitive reality: GCIT's review count (160+) and certifications are what
  dominance looks like — reinforces review-velocity as bcom's #1 lever.

## Query 3 — "business wifi installation Gold Coast installer"

- Recommended: GC Data Cabling, COLETEK, M-Techs, **bcom ICT (cited twice — business-wifi + networking pages, with accurate segmentation/PCI descriptions)**, Smart WiFi, In Connect
- bcom's strongest citation performance — the WiFi cluster copy is working.

## Standing observations

1. Directory listicles (GoodFirms) are the citation backbone for "best X" queries → directory presence = recommendation presence.
2. bcom is present in all three answers — the entity work is landing. Position within answers tracks review volume and third-party corroboration, not on-page factors.
3. Old-brand ("Bcom IT Solutions") snippets persist in the index — monitor.

## Actions spawned from this audit
- GoodFirms + Cloudtango + Clutch listings (Royce to submit; profiles drafted on request)
- Review velocity push (g.page/r/CSc3yhyrbZCaEBM/review after every job)
- Re-audit late October 2026
