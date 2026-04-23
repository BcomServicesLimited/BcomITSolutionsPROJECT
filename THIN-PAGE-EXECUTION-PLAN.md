# LLM SEO Execution Plan: Thin Page Content Expansion

## 1. The 2026 LLM SEO Landscape for Local Service Pages

Based on the latest 2026 research from Search Engine Land, Averi AI, and Google's March 2026 Core Update, the requirements for local service pages have shifted dramatically:

*   **The "Zero-Click" Reality:** Over 51% of searches now end without a click. LLMs (ChatGPT, Perplexity, Google AI Overviews) extract answers directly from pages.
*   **Depth Over Breadth:** The March 2026 Core Update heavily penalised "thin, templated location pages" that just swap city names. Pages under 1,500 words are struggling to provide enough entity signals and semantic depth for LLMs to confidently cite them.
*   **The "Extractable Unit":** LLMs look for 40-60 word direct answers immediately following descriptive H2/H3 headings.
*   **Attributed Evidence:** Content with specific statistics, local context, and clear attribution gets 30-40% higher visibility in AI citations.
*   **Entity Consistency:** LocalBusiness schema (which we've already implemented) must be supported by in-text local signals (suburbs, specific local scenarios).

## 2. Audit of the 10 Thin Pages

We identified 10 core pages that fall under the 1,500-word threshold (excluding policy/utility pages). These pages lack the semantic depth required for consistent LLM citation.

| Page | Current Words | Target Words | Primary Gap |
| :--- | :--- | :--- | :--- |
| `contact.html` | 1,021 | 1,500+ | Needs detailed location info, parking, service area map context, and expected response times. |
| `industries.html` | 1,045 | 1,500+ | Needs specific IT challenges and solutions for each of the 6 target industries. |
| `support.html` | 1,092 | 1,500+ | Needs detailed SLA definitions, remote vs. on-site criteria, and escalation paths. |
| `home-users.html` | 1,094 | 1,500+ | Needs expanded descriptions of common home IT issues (NBN dropouts, mesh WiFi limits). |
| `business.html` | 1,195 | 1,500+ | Needs deeper explanation of managed vs. break-fix, and proactive maintenance benefits. |
| `about.html` | 1,336 | 1,500+ | Needs more company history, technician qualifications, and community involvement. |
| `business-wifi-gold-coast.html` | 1,360 | 1,800+ | Needs specific scenarios (e.g., guest portals, high-density office coverage). |
| `asus-wifi-gold-coast.html` | 1,385 | 1,800+ | Needs detailed model comparisons (ZenWiFi vs. ROG) and specific home layouts. |
| `hardware-procurement-setup-gold-coast.html` | 1,431 | 1,800+ | Needs lifecycle management details, warranty handling, and specific brand partnerships. |
| `aruba-instant-on-wifi-gold-coast.html` | 1,464 | 1,800+ | Needs cloud management explanation and specific small business use cases. |

## 3. Execution Strategy: Zero Duplicate Content Risk

To expand these pages without triggering duplicate content penalties or diluting existing signals, we will follow a strict, structured approach:

### Rule 1: Expand, Don't Replace
We will keep all existing H1 and H2 headings intact. New content will be written *beneath* existing headings to expand on the current topics, rather than rewriting what is already there.

### Rule 2: The "Extractable Unit" Format
Every new section will begin with a 40-60 word direct answer or summary, followed by detailed paragraphs. This caters directly to LLM extraction patterns.

### Rule 3: Local Specificity (No Generic Filler)
Instead of generic IT advice, we will inject local context. For example, instead of "We fix internet issues," we will write "We resolve NBN dropouts common in older Southport apartment buildings and extend WiFi coverage through multi-level homes in Burleigh Heads."

### Rule 4: Strict Formatting Constraints
*   **75-85% Paragraph Text:** Bullet points will be used sparingly. LLMs prefer well-structured paragraphs for context.
*   **No Emojis:** Professional tone only.
*   **UK English:** Strict adherence to UK spelling (e.g., optimisation, tailored).
*   **No Competitor Bashing:** Focus solely on Bcom's value proposition.

## 4. Step-by-Step Implementation Plan

We will execute the expansion in three batches to ensure quality control and allow for IndexNow submission after each batch.

### Batch 1: The Core Hub Pages
1.  `business.html`
2.  `home-users.html`
3.  `industries.html`

### Batch 2: The Brand/Specific Service Pages
4.  `business-wifi-gold-coast.html`
5.  `hardware-procurement-setup-gold-coast.html`
6.  `asus-wifi-gold-coast.html`
7.  `aruba-instant-on-wifi-gold-coast.html`

### Batch 3: The Trust/Utility Pages
8.  `about.html`
9.  `support.html`
10. `contact.html`

For each page, the workflow will be:
1.  Read the current HTML structure.
2.  Draft new, highly specific paragraphs for each existing H2 section.
3.  Inject the new content using precise string replacement or DOM manipulation.
4.  Verify word count exceeds the 1,500+ target.
5.  Commit, push, and submit to IndexNow.
