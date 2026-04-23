# LLM SEO & GEO Audit Report: Bcom IT Solutions (April 2026)

This report evaluates the Bcom IT Solutions website against the latest 2026 Generative Engine Optimization (GEO) and LLM SEO best practices. It covers how ChatGPT, Perplexity, Claude, and Google Gemini discover, evaluate, and cite local businesses, followed by a specific audit of the Bcom website and a prioritised improvement plan.

## 1. The 2026 LLM SEO Landscape: What Actually Matters

Recent data from 2025-2026 studies (including Profound's analysis of 3.25 billion citations and Search Engine Land's citation trait research) reveals exactly how LLMs choose which local businesses to recommend:

### A. The "Answer Capsule" is King
The single strongest predictor of a ChatGPT citation is the presence of an "answer capsule" [1]. This is a concise, self-contained explanation of roughly 120 to 150 characters (20-25 words) placed directly after an H2 question. LLMs extract these blocks because they are easy to parse and attribute without following complex HTML structures.

### B. Turn 1 is Everything
Users' opening questions trigger web searches; follow-ups rarely do. Turn 1 is 2.5× more likely to trigger citations than turn 10 [2]. Local businesses must optimize for the "first question" (e.g., "Who does business IT support on the Gold Coast?"), not just deep technical queries.

### C. Entity Authority & Co-Citation
LLMs prioritize trust over keyword density. They look for "triplets" of information (Subject, Predicate, Object) confirmed across multiple sources [3]. If your website, your Google Business Profile, and a local directory all confirm you do "Emergency IT Support in Southport," your entity authority rises. Furthermore, sources travel in packs; ChatGPT cites competitors side-by-side [2].

### D. The Cloudflare Bot Blocking Issue
A major issue in 2026 is that Cloudflare's "AI Scrapers and Crawlers" toggle silently blocks `OAI-SearchBot` (ChatGPT's live search crawler) and `PerplexityBot` [4]. While blocking `GPTBot` (the training crawler) is fine, blocking the search crawlers makes a site invisible to live AI queries.

### E. Schema Markup is the AI API
Schema doesn't guarantee citations, but it helps AI understand entities [5]. FAQPage schema improves AI citation rates by 30% on average [6]. LocalBusiness and Organization schema are non-negotiable for establishing the business entity.

---

## 2. Bcom Website Audit Findings

I audited all 71 pages of the Bcom IT Solutions website against these 2026 LLM SEO standards. Here is how the site currently performs:

### The Good (What's Working Well)
*   **FAQ Schema:** 61 out of 71 pages have valid `FAQPage` schema. This is excellent and directly contributes to the site's current visibility in ChatGPT.
*   **Entity Links (sameAs):** 62 pages have `sameAs` links in their schema pointing to the Google Business Profile, Facebook, LinkedIn, and local directories (TrueLocal, YellowPages). This perfectly builds the "Entity Authority" LLMs look for.
*   **Review Schema:** 62 pages feature `AggregateRating` schema, providing the structured social proof LLMs need to categorize the business positively.
*   **Comparison Content:** 30 pages contain "vs" or comparison content (e.g., "On-site vs Workshop repairs"). This is highly citable by LLMs when users ask for recommendations.

### The Gaps (Areas for Improvement)
*   **Missing Answer Capsules:** Only 10 pages currently feature the optimal "Answer Capsule" pattern (an H2 question followed immediately by a concise 20-30 word paragraph). Most pages have H2s, but the text beneath them is either too long, too short, or starts with a bulleted list.
*   **Incomplete LocalBusiness Schema:** Only 7 pages currently use `LocalBusiness` (or related) schema. The rest use `HowTo` or `FAQPage` but lack the core entity definition on the page itself. Only 1 page has `Organization` schema.
*   **Thin Content on Some Pages:** 14 pages have fewer than 800 words of core content. LLMs prefer comprehensive, authoritative pages to extract data from.
*   **Robots.txt Optimization:** The current `robots.txt` explicitly allows `OAI-SearchBot` and `PerplexityBot`, which is perfect. However, it also allows `GPTBot` and `ClaudeBot` (training crawlers). Best practice in 2026 is to allow search/citation bots but block training bots to protect intellectual property [7].

---

## 3. Prioritised Improvement Plan

To make Bcom IT Solutions the most LLM-friendly IT company on the Gold Coast, I recommend the following action plan:

### Phase 1: The "Answer Capsule" Injection (High Impact, Low Effort)
**Action:** Rewrite the first paragraph under the primary H2 on the top 20 highest-traffic pages to form a perfect "Answer Capsule."
**Execution:** Ensure the H2 is phrased as a question (e.g., "Need IT Support on the Gold Coast?"). The immediate paragraph below it must be exactly 20-30 words, containing the brand name, the core service, and the location, with no links.

### Phase 2: Universal Entity Schema (High Impact, Medium Effort)
**Action:** Inject a comprehensive `LocalBusiness` JSON-LD schema block into the `<head>` of every single page, not just the current 7.
**Execution:** This schema must include the business name, exact address, phone number, `sameAs` links, price range, opening hours, and geographic service area (listing all 11 Gold Coast suburbs). This acts as a universal API for LLMs.

### Phase 3: Robots.txt Refinement (Medium Impact, Low Effort)
**Action:** Update `robots.txt` to explicitly block training crawlers while ensuring search crawlers remain allowed.
**Execution:** Change `Allow: /` to `Disallow: /` for `GPTBot`, `Google-Extended`, and `ClaudeBot`. Keep `Allow: /` for `OAI-SearchBot` and `PerplexityBot`. Also, verify in the Cloudflare dashboard that "AI Scrapers and Crawlers" is disabled so Cloudflare doesn't override these rules.

### Phase 4: "Why Choose Us" Expansion (Medium Impact, High Effort)
**Action:** Expand the "Why Choose Us" sections across the site. Currently, 43 pages have this content.
**Execution:** LLMs use sentiment analysis to categorize businesses [3]. Ensure these sections explicitly use phrases that LLMs look for, such as "no hidden fees," "independent advice," "no vendor commissions," and "same-day service."

### Phase 5: Content Density Boost (Long Term)
**Action:** Expand the 14 pages that currently have fewer than 800 words.
**Execution:** Add detailed, structured paragraphs (not just bullet points) covering specific local scenarios, troubleshooting steps, and expanded FAQs to give LLMs more context to extract.

---

## References
[1] Search Engine Land (2026). *How to get cited by ChatGPT: The content traits LLMs quote most*.
[2] Profound (2026). *How ChatGPT sources the web*.
[3] BrandLume (2026). *AI Local SEO: How To Dominate Local Recommendations In 2026*.
[4] Reddit r/SEO (2026). *Cloudflare has been quietly blocking GPTBot and PerplexityBot*.
[5] Search Engine Land (2026). *How schema markup fits into AI search — without the hype*.
[6] Stackmatix (2026). *Structured Data AI Search: Schema Markup Guide*.
[7] Technology Checker (2026). *We Analyzed robots.txt Across Cloudflare's Network*.
