# Press Coverage for AI Search — Research Brief

**Author:** Research working document for Rank4AI
**Branch:** `claude/press-coverage-research-AbeLW`
**Date:** 24 April 2026
**Purpose:** Inform an AI search product focused on press / earned media, and help trim a 100+ outlet list down to a defensible 30–50.

---

## 1. Types of Press Coverage

The industry groups coverage into three families — **Paid, Earned, Owned** (the PESO / trifecta model) — with five practical sub-types that matter for AI visibility.

| Type | Paid? | Editorial control | Typical signal for AI | Example |
|------|-------|-------------------|------------------------|---------|
| **Press release (wire)** | Paid distribution | Company writes it | Weak. Syndicated copies are deduped. | Company announces funding on Business Wire → picked up by Yahoo Finance, MSN. |
| **Sponsored / advertorial / branded content** | Paid | Brand-supplied, lightly edited | Weak-to-neutral. Marked "sponsored"; LLMs discount it. | "Paid content" slot on Forbes/Bloomberg. |
| **Editorial feature / article** | Not paid | Journalist-written | **Strongest.** Independent, cited. | Sifted feature on a funded startup. |
| **Expert quote / contributor mention** | Not paid | Journalist chooses quote | Strong. Builds entity–subject association. | CEO quoted as analyst in a TechCrunch piece. |
| **Guest post / op-ed / byline** | Usually unpaid, occasionally paid | Author-supplied, editor-approved | Moderate. Good for topical authority; weaker than independent editorial. | Op-ed in City A.M. by a named founder. |

**Key distinctions to encode in a product:**
- Byline type: **staff journalist** vs **contributor** vs **brand byline** vs **sponsored**.
- Placement type: **news**, **analysis/feature**, **opinion**, **listicle**, **sponsored**.
- Link attribute: **dofollow** vs **nofollow** vs **sponsored rel** vs **ugc rel**.
- Mention depth: **passing mention**, **named source**, **focus of piece**.

---

## 2. Does Syndication Count as Multiple? (Short answer: **No**)

This is the single biggest misconception sold on newswire ratecards.

- Analysis of **4M+ AI citations** across ChatGPT, Google AI Overviews, Google AI Mode and Gemini found syndicated press releases (Yahoo Finance, MSN, Globe Newswire, etc.) accounted for **0.04%** of all AI citations.
- On Google: syndicated press accounts for ~0.32% of *news* citations and 0.04% of the total dataset.
- Google explicitly indexes **one canonical version** across Google News and Search when content is duplicated across outlets. AI engines behave the same way — they dedupe on near-identical text and prefer the source that carries the authority signals (Reuters original) over the aggregator (Yahoo Finance copy).
- Newswires typically set **nofollow** on embedded links anyway, so even the backlink value is minimal.

**Implication for the product / ratecard:** a press release "guaranteed" across 200 outlets is effectively **one** signal to an LLM, not 200. The 98% "AI Visibility" score on MSN in the ratecard is likely measuring appearance on the MSN domain, not independent citation weight.

**When syndication *does* help:**
- Tier-1 pickup where a journalist rewrites with original commentary (becomes new editorial, new signal).
- Presence in trade databases (AP, Reuters wire) that licensed LLM training data includes.
- Press release on the **company's own newsroom** page (treated as owned content; Signal 03 Meaning Architecture applies).

---

## 3. How Each AI Search Engine Pulls Press

### ChatGPT / SearchGPT / Copilot
- Live retrieval via Bing's index + partner feeds.
- **~87% of SearchGPT citations match Bing's top organic results.** Rank in Bing first; AI citation follows.
- Microsoft Bing Webmaster Tools now exposes an **AI Performance dashboard** (launched Feb 2026) showing citation counts per page for Copilot, AI Bing summaries, and partner integrations.
- Notable: ChatGPT is the **most willing** to cite company-owned newsroom pages (~18% of citations vs ~3% for Google AI).

### Google AI Overviews / AI Mode / Gemini
- Pulls from the standard Google index. **78% of AI Overview citations come from the top 10 organic results.**
- Out of **18.4M domains in Google's index**, only **274,455 have ever appeared in AI Overviews** — extreme selectivity.
- Top 3 publishers capture **31% of news citations**; top 10 capture **~80%**.
- Paywalled coverage counts: **96% of NYT citations** and **99% of Washington Post citations** in AI Overviews come from behind paywalls.
- Reddit (2.2%) and YouTube (1.9%) are the single biggest domains.

### Perplexity
- Operates its own crawler: **PerplexityBot**. Respects robots.txt absolutely — block it and you cannot be cited.
- Runs real-time crawl per query; freshness-led. Breaking stories can reach citation within hours.
- Citation count per response is lower (~5 per answer vs ~10 for ChatGPT, ~9 for AI Overviews), so each citation is heavier.
- Over-indexes on **academic, primary news, and technical documentation**. Reddit = 6.6% of total citations.

### Claude
- Less freshness-driven; weights **consistent entity description across multiple independent sources**.
- Favours encyclopedic / long-form / reference material.
- Press works here through **ecosystem consistency**: the same entity description on BBC + Reuters + Wikipedia + LinkedIn compounds trust.

### General mechanism (all engines)
1. Query is rewritten/expanded.
2. Retrieval layer fetches candidate passages (from index or live crawl).
3. **Deduplication** collapses near-identical syndicated copies.
4. Authority ranking: domain authority, entity graph position, freshness, E-E-A-T signals, schema.
5. Passage extraction: clean 200–500 token chunks become the cited source.
6. Synthesis into answer with citation attribution.

**Does the AI look at your site first?** For **branded / navigational** queries — yes, it will often hit your own domain. For **unbranded exploratory / transactional** queries — no, it starts from the retrieval index and your site only surfaces if it already ranks. This is why press is leverage: it gets you into the retrieval set for queries where your own site would never compete.

---

## 4. Citation Patterns — Who Actually Gets Picked Up

### Cross-engine dominant domains
The top 5 domains account for ~**38%** of all AI citations; top 20 account for ~**66%**.

**Tier-0 (universal, non-press):** Wikipedia, Reddit, YouTube, LinkedIn, Google properties.

**Tier-1 news/editorial cited across every engine:**
- **Reuters** — cross-engine. Licensed to multiple LLMs.
- **Axios** — disproportionately cited by Gemini + ChatGPT (Nieman Lab study).
- **Forbes** — the *only* traditional outlet cited across all 11 major B2B/B2C sectors in the ALM 30M-source study. 10,000+ mentions.
- **Financial Times**
- **Time**
- **Bloomberg** — dominates finance queries.
- **The New York Times** — dominant on Google AI Overviews despite paywall.
- **The Washington Post** — same paywall pattern.
- **BBC News** — strong in Claude due to entity consistency.
- **Associated Press** — the *original* AP wire (not syndicated mirrors).
- **The Verge** — media/tech queries.
- **TechCrunch** — startup/tech.
- **Wired** — tech, long-form.
- **The Guardian** — UK + global.

**Tier-2 trade/vertical (cited when relevant):**
Gartner, Forrester, HBR, MIT Tech Review, Nature, Crunchbase, G2, Capterra, Sifted (startups EU/UK), The Information, Stratechery.

### Pattern observations
- **Journalistic content = 49% of citations** for any query phrased with "latest / recent / current".
- **Corporate blogs + owned content = majority of citations** for subjective/advisory queries ("how do I…", "best way to…").
- Finance queries → Bloomberg + SEC filings. Media queries → NYT + Reuters + Verge. Tech queries → TechCrunch + Verge + Wired.
- AI citation sets are **3–6 domains per query**, vs ~10 for a Google SERP. Concentration is the game.

---

## 5. Review of the PR Fire Ratecard (Your Spreadsheet)

**What's in the sheet** — 13 publications priced £49–£400, with DA, "AI Visibility %", indexed status, and link type.

**Critical read:** most of these are **paid syndication slots** on the domains of large outlets. Several patterns to flag:

| Outlet | Notes |
|--------|-------|
| MSN (£210, 98% AI Vis, dofollow) | MSN is itself an aggregator; content here is almost always a syndicated copy. The "AI Visibility" score measures that the URL shows up, not that it wins the citation. LLMs dedupe to the original. |
| Yahoo Finance (£210, 88%, nofollow) | Same story — aggregator placement of wire content. |
| Associated Press News (£100, 50%, **not indexed**, nofollow) | An un-indexed AP page is effectively invisible to retrieval. Almost certainly a third-party-operated "AP News" subdomain, not the actual AP wire. High risk of misrepresentation. |
| Benzinga (£110, 97%, **not indexed**, nofollow) | Not indexed = not retrievable by Google AI. Only useful if ChatGPT/Bing indexes it separately. |
| Street Insider (£49, 98%, nofollow) | Heavy aggregator. |
| Business Insider (£199, 90%, nofollow) | Legit outlet but nofollow + likely a "contributor"/sponsored slot. |
| USA Today (£200, 80%, nofollow) | As above. |
| IB Times UK (£400, 50%, nofollow) | Expensive for 50% visibility. |
| MarketWatch (£200, **10%** AI Vis, nofollow) | 10% — under-performing. |
| ABC Money (£125, 72%, **dofollow**) | Dofollow is notable; smaller outlet. |
| London Loves Business (£340, 84%, dofollow) | Dofollow + UK vertical, but pricey. |
| News Anyway (£75, 68%, dofollow) | Low DA, clearly a syndicate site. |
| News Today (£100, 69%, dofollow) | DA 36 — network syndicate site. |

**Honest takeaway:** this list is a **syndication network, not an editorial network**. AI citation value of paid syndicated placement is empirically ~0.04%. The ratecard's "AI Visibility %" is almost certainly a domain-appearance metric, not an AI-citation metric.

**What the sheet is missing for an AI-era product:**
- Editorial vs sponsored vs contributor labelling.
- Whether the outlet is in known LLM training corpora (Common Crawl, C4, OpenWebText, licensed feeds).
- Whether PerplexityBot, GPTBot, ClaudeBot, Google-Extended are allowed in robots.txt.
- Whether the outlet has a **canonical pointing back to the origin** (most syndicates do — this is the kill switch for AI citation).
- Schema coverage (Article, NewsArticle, Person for bylines).
- Entity density (does the placement name the client entity consistently vs a passing mention?).

---

## 6. Framework: Trimming 100s of Outlets to 30–50

Recommended scoring model. Each outlet scored 0–5 per dimension; minimum threshold to include, e.g. 18/30.

| Dimension | What it measures | Why it matters |
|-----------|------------------|----------------|
| **1. Citation evidence** | Has the outlet been observed in AI citation studies (Ahrefs, Semrush, Peec, Otterly, ALM)? | Direct proof of pickup. |
| **2. LLM training inclusion** | Known in Common Crawl / C4 / licensed OpenAI/Anthropic deals (Reuters, AP, FT, Axel Springer, News Corp, Condé Nast, Vox, Guardian). | Persistent authority beyond live retrieval. |
| **3. Original vs syndicated** | Is content original to this domain, or a mirror of wire copy (with `rel="canonical"` pointing elsewhere)? | Dedup kills syndicated mirrors. |
| **4. Editorial control** | Staff-written / independent feature vs paid/contributor slot. | AI weighs independent editorial far higher. |
| **5. Crawler access** | GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot all allowed? Paywall behaviour? | No access = no citation. |
| **6. Domain authority + entity graph position** | DA/DR, brand recognition, Wikipedia presence. | Authority is a direct LLM ranking input. |
| **7. Vertical relevance** | Does the outlet cover the client's category meaningfully? | Concentration beats breadth. |
| **8. Freshness velocity** | Is content re-crawled and promoted fast enough for Perplexity / AI Overviews on time-sensitive queries? | Required for "latest"-type queries. |

### Suggested final tier structure (target 30–50 outlets)

**Tier 1 — Anchor outlets (8–10):** The few that show up across AI engines and multiple verticals. Reuters, Bloomberg, FT, NYT, WaPo, Forbes, Axios, BBC, The Guardian, AP (the genuine wire).

**Tier 2 — Category leaders (10–15):** Vertical-dominant, cited when the query is in their lane. For B2B tech: TechCrunch, The Verge, Wired, The Information, MIT Tech Review, HBR, Stratechery. For finance: MarketWatch, CNBC, WSJ, Barron's. For UK: Sifted, City A.M., The Times, Sky News.

**Tier 3 — Trade / analyst (6–10):** Gartner, Forrester, IDC, McKinsey Insights, sector-specific trade press (e.g. The Grocer, Retail Week, Campaign, Computer Weekly).

**Tier 4 — Validation platforms (4–8):** Wikipedia (if eligibility achieved), Crunchbase, G2, Capterra, LinkedIn News, YouTube (long-form / interview slots).

**Tier 5 — Optional UK regional / niche (3–5):** Only where a client's footprint justifies it.

**Total: 31–48 outlets.** The discipline is to reject anything that is primarily a syndication aggregator (MSN, Yahoo Finance, Street Insider, News Anyway, News Today) unless the client is *specifically* paying for the SERP-trust halo rather than AI citation.

---

## 7. Implications for the Product

If the product is an **AI-era press placement / tracking tool** built on the Rank4AI framework:

1. **Reframe the metric.** Replace "AI Visibility %" (which reads as domain-appearance) with two separate scores:
   - **AI Citation Probability** (modelled from public citation studies + live LLM prompt testing).
   - **Signal Density** (entity mention depth × link type × editorial independence).
2. **Label every placement** by type: Editorial / Feature / Quote / Contributor / Sponsored / Syndication. Price and score differently.
3. **Run live citation probes** against ChatGPT, Perplexity, Google AI Mode, Gemini post-placement to measure whether the placement actually surfaces for target prompts (this is Rank4AI's measurement philosophy applied to press).
4. **Track canonicals + robots.txt per outlet** — flip a red flag if `rel=canonical` points elsewhere or if GPTBot/PerplexityBot/ClaudeBot is blocked.
5. **Tie to Signal 04 (Ecosystem Validation):** each outlet placement should reinforce the same identity language across independent sources to prevent graph drift.
6. **Sell tiered campaigns**, not outlet-by-outlet SKUs. A tier-1 editorial win + 3 tier-2 category placements beats 15 syndicated copies.

---

## 8. Open Questions / Next Steps

- [ ] Prompt-test the PR Fire outlets live in ChatGPT + Perplexity + Google AI Mode on 5–10 representative queries; record whether each outlet actually gets cited. Compare to the ratecard's stated AI Visibility %.
- [ ] Pull robots.txt for each of the 13 ratecard outlets; record GPTBot / PerplexityBot / ClaudeBot / Google-Extended / CCBot status.
- [ ] Inspect canonical behaviour on a sample syndicated press release across MSN / Yahoo Finance / Street Insider — confirm dedup hypothesis.
- [ ] Build the 30–50 outlet master list using the scoring model in Section 6.
- [ ] Decide whether the product positions as **placement broker** (buy editorial) or **measurement tool** (track AI citation) — different GTM, different tech.

---

## Sources

- [Cision — Types of Earned Media](https://www.cision.com/resources/insights/types-of-earned-media/)
- [PR Newswire — Earned Media Strategy](https://www.prnewswire.com/resources/articles/earned-media-strategy-2025/)
- [Bastion — Earned, Paid, and Owned Media](https://us.bastionagency.com/news-views/three-different-types-of-media-coverage/)
- [Search Engine Journal — AI Search Barely Cites Syndicated News](https://www.searchenginejournal.com/ai-search-barely-cites-syndicated-news-or-press-releases/569854/)
- [ALM Corp — AI Search Cites Press Releases 0.04% of the Time](https://almcorp.com/blog/ai-search-press-release-citations/)
- [ALM Corp — Top Domains Cited by AI Search (30M sources)](https://almcorp.com/blog/top-domains-cited-by-ai-search/)
- [Seer Interactive — 87% of SearchGPT Citations Match Bing](https://www.seerinteractive.com/insights/87-percent-of-searchgpt-citations-match-bings-top-results)
- [PPC Land — Bing AI Citation Data for Publishers](https://ppc.land/bing-gives-publishers-first-look-at-how-ai-systems-cite-their-content/)
- [Trysight — How Perplexity AI Selects Sources](https://www.trysight.ai/blog/how-perplexity-ai-selects-sources)
- [Otterly — AI Citation Economy 2026](https://otterly.ai/blog/the-ai-citations-report-2026/)
- [Search Engine Journal — Google AI Overviews Favor Major News Outlets](https://www.searchenginejournal.com/google-ai-overviews-favor-major-news-outlets-study-reveals/548359/)
- [Stackmatix — How Google Selects AI Overview Sources](https://www.stackmatix.com/blog/ai-overview-source-selection)
- [Nieman Lab — AI Models Love to Cite Reuters and Axios](https://www.niemanlab.org/2025/07/generative-ai-models-love-to-cite-reuters-and-axios-study-finds/)
- [Ahrefs — Top 10 Most-Cited Domains in AI](https://ahrefs.com/blog/top-10-most-cited-domains-ai-assistants/)
- [Semrush — Most-Cited Domains in AI](https://www.semrush.com/blog/most-cited-domains-ai/)
- [Peec AI — Top Domains Cited by AI Search (30M sources)](https://peec.ai/blog/top-domains-cited-by-ai-search-analysis-based-on-30m-sources)
- [Meltwater — Importance of Earned Media for GEO](https://www.meltwater.com/en/blog/earned-media-geo)
- [Businesswire — Press Releases and SEO](https://blog.businesswire.com/everything-you-need-to-know-about-press-releases-and-seo)
- [PR.co — Do Press Release and Newswire Services Help with AI Visibility](https://pr.co/blog/do-press-release-and-newswire-services-help-with-ai-visibility)
- [Authority Tech — Which Publications Get Cited Most by AI](https://authoritytech.io/blog/which-publications-get-cited-most-ai-search-engines-2026)
