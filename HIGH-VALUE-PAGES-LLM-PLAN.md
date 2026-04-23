# High-Value Pages LLM SEO Refinement Plan

Based on the Google Search Console data and the 2026 LLM SEO best practices, we are pivoting away from padding low-value hub pages. Instead, we will refine the pages that are already generating impressions and clicks, but need structural adjustments to dominate AI citations (ChatGPT, Perplexity, Google AI Overviews).

## The 2026 LLM SEO Requirements
1.  **The "Extractable Unit":** Every H2/H3 must be immediately followed by a 40-60 word direct answer.
2.  **Attributed Evidence:** Content must include specific statistics, local context, and clear attribution.
3.  **Entity Consistency:** Local signals (suburbs, specific local scenarios) must be woven naturally into the text.
4.  **Depth Over Breadth:** Pages must comprehensively cover the topic without fluff.

## Target Pages & GSC Insights

### 1. IT Consulting & Strategy (`it-consulting-strategy-gold-coast.html`)
*   **GSC Data:** 580 impressions, Position 48.5, 1 click.
*   **Top Queries:** "it consultant gold coast", "it consulting gold coast", "it advisory and consulting gold coast".
*   **Current State:** 2,170 words. Good structure, but lacks specific local case studies and concrete statistics on ROI.
*   **Refinement Plan:**
    *   Inject 40-60 word direct answers under each H3 in the "IT Consulting & Strategy Services" section.
    *   Add a new section detailing a hypothetical (but realistic) Gold Coast business case study (e.g., a Southport law firm migrating to the cloud).
    *   Include statistics on the cost of IT downtime for small businesses.

### 2. Cybersecurity Health Check (`cybersecurity-health-check-for-small-business-gold-coast.html`)
*   **GSC Data:** 274 impressions, Position 17.6, 0 clicks.
*   **Top Queries:** "cyber security risk assessment gold coast", "managed it security gold coast", "ransomware protection gold coast".
*   **Current State:** 2,795 words. Strong word count, but needs to directly address the specific queries.
*   **Refinement Plan:**
    *   Ensure the H2s explicitly use the terms "risk assessment", "managed IT security", and "ransomware protection".
    *   Add an "Extractable Unit" defining exactly what a "cyber security risk assessment" entails for a Gold Coast business.
    *   Include recent statistics on ransomware attacks targeting Australian SMEs.

### 3. AI Services (`artificial-intelligence-service-gold-coast.html`)
*   **GSC Data:** 220 impressions, Position 8.0, 4 clicks.
*   **Top Queries:** Interestingly, this page is ranking for "computer repairs gold coast" (Pos 49.9) and "seo training gold coast" (Pos 38.6).
*   **Current State:** 3,322 words. Very comprehensive.
*   **Refinement Plan:**
    *   The page is suffering from keyword confusion. We need to tighten the semantic focus on "AI consulting", "AI automation", and "AI integration".
    *   Review the content to ensure it isn't inadvertently targeting "computer repairs" or "SEO".
    *   Ensure all H3s under "AI Integration Services" have clear, 40-60 word extractable summaries.

### 4. Data Backup & Recovery (`data-backup-recovery-gold-coast.html`)
*   **GSC Data:** 207 impressions, Position 16.2, 1 click.
*   **Top Queries:** "data recovery services gold coast insurance reports" (416 impr, Pos 9.8), "cloud backup gold coast".
*   **Current State:** 2,378 words.
*   **Refinement Plan:**
    *   **Crucial Addition:** Create a dedicated H2 section specifically for "Data Recovery Insurance Reports". This is a high-impression, page-1 query that needs direct targeting.
    *   Add an "Extractable Unit" explaining the process of getting an insurance report for data loss.
    *   Ensure "cloud backup solutions" is prominently featured with a direct answer.

### 5. Microsoft 365 Setup (`microsoft-365-setup-gold-coast.html`)
*   **GSC Data:** 0 impressions in the general view, but the query data shows "microsoft 365 migration in gold coast" (145 impr, Pos 4.1) and "office 365 setup gold coast" (37 impr, Pos 7.3).
*   **Current State:** 1,805 words.
*   **Refinement Plan:**
    *   The page needs to explicitly target "migration" as well as "setup".
    *   Add an H2 section: "Microsoft 365 Migration Services Gold Coast".
    *   Include an "Extractable Unit" detailing the migration process (zero downtime, data integrity).

### 6. The WiFi Cluster
*   **Pages:** `home-wifi-setup-and-troubleshooting-gold-coast.html` (4,073 words), `mesh-network-setup-gold-coast.html` (3,138 words), `wifi-range-extension-gold-coast.html` (4,132 words), `business-wifi-gold-coast.html` (1,360 words).
*   **GSC Data:** "mesh wifi installation gold coast" (119 impr, Pos 9.2), "wifi installation gold coast" (87 impr, Pos 11.2).
*   **Refinement Plan:**
    *   These pages are already very long (except Business WiFi). The focus here is *formatting for extraction*.
    *   Audit every H2/H3 to ensure it is immediately followed by a 40-60 word direct answer.
    *   For `business-wifi-gold-coast.html`, expand the content to >1,800 words by adding specific scenarios (e.g., guest portals for hospitality, high-density coverage for offices).

## Execution Workflow
For each target page:
1.  Read the current HTML structure.
2.  Draft the required "Extractable Units" (40-60 words) and new sections based on the GSC query data.
3.  Inject the new content using precise string replacement or DOM manipulation, strictly adhering to the formatting rules (no emojis, UK English, keep existing headings).
4.  Commit, push, and submit to IndexNow.
