# Website SEO, GEO & AI Search: Tips, Tricks & Weird Findings (2026)

> Research compiled from LinkedIn posts, articles, and industry sources. May 2026.
> Focused on **website/on-site optimization** only.

---

## Table of Contents

1. [The New Search Landscape](#the-new-search-landscape)
2. [GEO - Generative Engine Optimization](#geo---generative-engine-optimization)
3. [AEO - Answer Engine Optimization](#aeo---answer-engine-optimization)
4. [LLMO - Large Language Model Optimization](#llmo---large-language-model-optimization)
5. [AI Search Visibility & Brand Citations](#ai-search-visibility--brand-citations)
6. [Local SEO in the AI Era](#local-seo-in-the-ai-era)
7. [Schema Markup & Structured Data](#schema-markup--structured-data)
8. [Weird & Wonderful Findings](#weird--wonderful-findings)
9. [Google's "Searchable Index" Patent](#googles-searchable-index-patent-us20250217356a1-july-2025)
10. [Parasite SEO & Social Signal Stacking](#parasite-seo--social-signal-stacking)
11. [AI Overview Tracking: What Actually Works](#ai-overview-tracking-what-actually-works-daniel-foley-carter)
12. [AI Search Is Probabilistic, Not Deterministic](#ai-search-is-probabilistic-not-deterministic)
13. [llms.txt: The File AI Agents Actually Read Now](#llmstxt-the-file-ai-agents-actually-read-now-david-kaufman--siteline)
14. [Writing for RAG: H1s, First Paragraphs & Zero Anaphora](#writing-for-rag-h1s-first-paragraphs--zero-anaphora)
15. [Claude Code .claude/ Folder for Marketers](#claude-code-claude-folder-for-marketers-vicky-lalwani)
16. [Flipbook: Post-GUI Web Experiences](#flipbook-post-gui-web-experiences)
17. [Actionable Site Playbook](#actionable-site-playbook)

---

## The New Search Landscape

The search world in 2026 has fractured into **five overlapping layers** - all requiring on-site work:

| Layer | What It Means for Your Site |
|-------|----------------------------|
| **SEO** | Ranking pages on Google (traditional on-page & technical) |
| **GEO** | Structuring site content so generative AI engines (ChatGPT, Perplexity, Gemini) cite it |
| **AEO** | Winning zero-click answers and featured snippets with on-page Q&A formatting |
| **AIO** | Feeding AI with structured data (schema, metadata) so it understands your brand |
| **SXO** | Aligning on-site UX with user intent for trust & conversions |

### Key Stats

- **31.3%** of the US population will use generative AI search in 2026
- Gartner predicts traditional search volume will drop **25%** by 2026
- Organic search traffic could decrease by **over 50%** as consumers embrace AI-powered search
- When an AI summary appears in Google, users click external links only **8%** of the time (vs 15% without)
- Google still sends **190x** more traffic to websites than ChatGPT
- ChatGPT processes approximately **2.5 billion** prompts daily
- About **65%** of ChatGPT usage qualifies as traditional search behaviour

---

## GEO - Generative Engine Optimization

GEO focuses on structuring your **site content** so AI engines **cite** it rather than competitors.

### On-Site Content Principles

1. **Topic Authority Over Keywords**: Build deep, comprehensive content clusters around broader subjects instead of chasing individual keyword phrases. Generative engines synthesise information from sources they consider authoritative on a topic.

2. **Citation-Worthy Content**: Publish original research, proprietary data, benchmarks, and expert commentary on your site. If your site has something no one else does (a benchmark study, a unique dataset, a framework), AI engines have a reason to cite you over alternatives.

3. **Content Structure for AI Extraction**:
   - Concise paragraphs (2-3 sentences max)
   - Bullet points and numbered lists
   - Clear H2/H3 headers phrased as questions
   - **40-60 word answers** directly after question headers
   - Key information placed **early** in pages - AI models prioritise information that appears near the top

4. **Brand Consistency**: Your site's brand description, positioning, and value proposition should be consistent with what appears on directories, review platforms, and industry listings. AI systems use cross-platform consistency to categorise brands with confidence.

5. **On-Site Citation Strategy**: Include statistics, data points, and references within your content. Cite credible sources and include "As seen in" or media mention sections to signal authority.

### GEO Trends for 2026

- Shift from keyword targeting to **topic targeting** across your site
- Focus on **brand mentions** across the web - the more your brand is mentioned elsewhere, the more AI cites your site
- **40-60% of cited sources change month-to-month** across Google AI Mode and ChatGPT - visibility is volatile, so keep content fresh
- Only **7.2%** of domains get cited in both LLMs and Google's AI Overviews - you need to optimise for each separately

**Sources:**
- [GEO Guide 2026: Generative Engine Optimization Explained](https://www.digitalapplied.com/blog/geo-guide-generative-engine-optimization-2026)
- [Rising GEO Trends for 2026](https://www.seo.com/blog/geo-trends/)
- [Mastering GEO in 2026 - Search Engine Land](https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142)
- [GEO Best Practices 2026 - Firebrand](https://www.firebrand.marketing/2025/12/geo-best-practices-2026/)

---

## AEO - Answer Engine Optimization

AEO is about structuring your **on-page content** so AI assistants and voice search deliver it as a direct answer.

### On-Site Techniques

- **Question-and-answer page structure**: Use H2s phrased as questions, with concise direct answers immediately below
- **Add statistics and citations** within your content to build authority signals
- **Implement structured data** (FAQPage, HowTo schema) to help AI engines parse your content
- **Include FAQ sections** on key pages to answer related questions directly
- **Write conversationally** - match how people actually ask questions in AI search

### Why This Matters for Your Site

Instead of just returning links, search engines now deliver direct answers powered by LLMs. The site content that wins isn't the most keyword-optimised - it's the most **clearly structured and authoritative**. Your pages need to be formatted so AI can easily extract a clean, quotable answer.

**Sources:**
- [Answer Engine Optimization (AEO) Is The New SEO - Rob Pickering](https://www.linkedin.com/posts/robjpickering_answer-engine-optimization-aeo-is-the-new-activity-7326520056534695937-15e-)
- [AEO Strategy Guide - Hassan Tariq Malik](https://www.linkedin.com/pulse/answer-engine-optimization-aeo-strategy-guide-hassan-tariq-malik-y3pff)
- [FAQ on GEO and AEO - eMarketer](https://www.emarketer.com/content/faq-on-geo-aeo--where-ai-search-seo-overlap-2026)

---

## LLMO - Large Language Model Optimization

LLMO is about aligning your site content to how LLMs **process, interpret, and prioritise** information.

### How LLMO Differs from Traditional On-Site SEO

1. **Semantic chunking** replaces keyword density - organise content into clear, self-contained sections
2. **Vector alignment** matters more than backlink profiles - your content needs to be semantically close to the queries it should answer
3. **Retrieval optimization** over crawl optimization - make content easy to retrieve and quote
4. **Machine-citable trust signals** - structured data, author credentials, publication dates
5. Focus on being **synthesised** rather than ranked - your content will be blended into AI answers
6. Content **freshness signals** work differently - include explicit dates and "updated" timestamps
7. Make content **quotable in 1-2 sentences** - AI needs clean, extractable snippets

### What's Actually Working On-Site

- Structuring pages with clear question/answer pairs
- Publishing original data and research that can't be found elsewhere
- Extensive **schema markup** implementation
- Creating content that's **quotable in 1-2 sentences** per key point
- **Semantic chunking** - clear H2/H3 sections that each stand alone as a complete answer

**Sources:**
- [7 Ways LLMO Differs from SEO - Jim Liu](https://www.linkedin.com/pulse/7-ways-llmo-llm-optimization-differs-from-seo-jim-liu-tkrsc)
- [SEO/LLM Optimization Tips - Benjamin Goodey](https://www.linkedin.com/posts/benjamingoodey_latest-observations-things-i-see-working-activity-7335981580076634112-2J0i)

---

## AI Search Visibility & Brand Citations

### The Citation Economy

The biggest shift for websites in 2026 is from **rankings to citations**. AI engines don't rank your pages - they cite them. Your site content needs to be worth citing.

### Key Research Findings

| Metric | What It Means for Your Site |
|--------|----------------------------|
| **Brand mentions correlation** | 0.664 correlation strength with AI visibility (Ahrefs study) - the more your brand is mentioned across the web, the more AI cites your site |
| **ChatGPT citation diversity** | 90% of citations come from pages outside Google's top 20 - your lower-ranking pages can still get cited |
| **Conversion rates** | AI-cited visitors convert **4.4x** better than traditional organic visitors |
| **Long-form content** | Cited in ~50-66% of AI responses - longer, deeper pages get cited more |
| **Brand mention impact** | Brands with most web mentions appear up to **10x** more often in AI results |
| **Small site opportunity** | AI engines cited over **160 unique websites** vs Google's usual 10-15 top domains |

### What Makes a Page Get Cited

- **Original data or research** that doesn't exist elsewhere
- **Clear, extractable answers** (40-60 words answering a specific question)
- **Expert authorship** with visible credentials (Author schema)
- **Recent publication/update dates** shown on the page
- **Statistics and data points** within the content
- **"As seen in" sections** highlighting media mentions and credibility

### Tracking Your Site's AI Visibility

Monitor whether your site pages are being cited across:
- ChatGPT responses
- Perplexity citations
- Google AI Overviews / AI Mode
- Claude responses
- Gemini responses

**Sources:**
- [500 AI Searches Later: Which Brands LLMs Actually Cite - Jacob Penn](https://www.linkedin.com/pulse/how-ai-search-reshaping-content-landscape-jacob-penn-g3edf)
- [Ahrefs Study: Brand Mentions Most Correlated with AI Overviews - Chris Long](https://www.linkedin.com/posts/chris-long-marketing_seo-data-study-an-analysis-from-ahrefs-found-activity-7334185782213033986-NI0k)
- [How to Get Cited in AI Answers - Madhav Mistry](https://www.linkedin.com/posts/madhav-mistry-999349164_seo-isnt-dead-its-just-fragmented-in-activity-7369339276188225537-FMuI)

---

## Local SEO in the AI Era

### The Geolocation Problem

Generative AI **doesn't know where you're searching from** - at least not without being told explicitly. This lack of geolocation leads to generic, irrelevant answers. Traditional search still wins for queries with clear local intent. This makes **on-site local optimization** even more critical.

### Local Ranking Factors (2026)

| Signal Group | Weight |
|-------------|--------|
| Google Business Profile | 32% |
| Reviews | 20% |
| On-page signals | 15% |
| Behavioural signals | 9% |
| Other factors | 24% |

### On-Site Local SEO Actions

1. **Location-Specific Pages**:
   - Create genuinely useful pages for each location served
   - Include real local information, not just templated content
   - Use question-and-answer format for local queries
   - Add LocalBusiness and GeoCoordinates schema markup

2. **On-Page Local Signals**:
   - Consistent NAP (Name, Address, Phone) on every relevant page
   - Embed Google Maps where appropriate
   - Include local landmarks, area descriptions, and service area details
   - Add location-specific FAQ sections

3. **Google Business Profile Optimization** (feeds your site's local visibility):
   - Complete and accurate information
   - Real photos regularly (exterior, interior, team, work, before/after)
   - Seed Q&A sections with real questions and clear answers

4. **Multi-Platform Directory Consistency**:
   - Apple Business Connect (Maps, Siri, Wallet)
   - Bing Places for Business (feeds into Copilot)
   - Ensure your site's NAP matches all directory listings exactly

5. **Review Strategy**: Reviews are the 2nd most important signal group at 20% - have a strategy to earn and respond to them

**Sources:**
- [How to Optimize for AI Search: Local SEO Best Practices 2026](https://brightly.com/blog/how-to-optimize-for-ai-search-local-seo-best-practices-in-2026/)
- [Local SEO Optimization Guide 2026](https://www.266seo.com/local-seo-optimization-guide/)
- [Why Local SEO Is Thriving in the AI-First Search Era](https://searchengineland.com/local-seo-ai-search-462083)

---

## Schema Markup & Structured Data

### Why Schema Matters More Than Ever for Your Site

Structured data makes your site content **machine-readable and AI-friendly**. Schema markup helps LLMs understand your content's structure, context, and authority - directly influencing whether your pages get cited.

### Priority Schema Types for AI

| Schema Type | Use Case | AI Impact |
|------------|----------|-----------|
| **FAQPage** | Q&A content on pages | Highly cited by AI - makes answers directly extractable |
| **HowTo** | Step-by-step guides | Structured steps are easy for AI to quote |
| **Article** | Blog posts and news | Signals content type, author, date |
| **Product** | E-commerce listings | Helps AI recommend products |
| **Review** | Customer reviews and ratings | Social proof signals for AI |
| **Organization** | Brand information | Helps AI identify and categorise your brand |
| **Author** | Expertise and authority | Critical for E-E-A-T signals |
| **LocalBusiness** | Local SEO pages | Geolocation and service info for local AI answers |
| **Speakable** | Voice search optimization | Marks content suitable for voice/audio playback |

### Implementation Tips

- Focus on schema types that **answer questions directly** - FAQPage and HowTo are the highest-impact
- Use **Author schema** to establish expertise (critical for E-E-A-T signals in AI)
- Combine multiple schema types on a single page where relevant
- Include **datePublished** and **dateModified** in Article schema - freshness signals matter
- Add **Speakable schema** to content you want surfaced in voice search
- Rewrite product descriptions to include **scientific data and specifications** - AI engines favour data-rich content

**Sources:**
- [Schema Markup in 2026: What Product Data AI Actually Reads](https://www.linkedin.com/pulse/schema-markup-2026-what-product-data-ai-actually-reads-ansari-cue9f)
- [Matt Diggity's 2026 SEO Strategy](https://www.linkedin.com/posts/mattdiggityseo_heres-my-2026-seo-strategy-stop-chasing-activity-7404443723511623681--Dk9)

---

## Weird & Wonderful Findings

The surprising, counterintuitive, and sometimes bizarre findings that affect your website strategy:

### 1. Your Low-Ranking Pages Might Be Your Best AI Assets
**90% of ChatGPT citations come from pages outside Google's top 20**. A page ranking #50 in Google might be the #1 cited source in ChatGPT for the same topic. Don't neglect or remove pages just because they rank poorly in traditional search.

### 2. Small Sites Can Beat Giants
While Google consistently offers the same 10-15 domains, AI search engines cited **over 160 unique websites** including small players like Thrifty Traveler, Fang Wallet, and Finance Buzz. Quality, citable content matters more than domain authority in AI search.

### 3. AI-Cited Traffic Converts 4.4x Better
Visitors arriving via AI citations convert at **4.4 times** the rate of traditional organic visitors. AI pre-qualifies the recommendation, so users arrive with higher intent and trust. Fewer visits, much higher quality.

### 4. The Click-Through Collapse
CTR from ChatGPT is approximately **96% lower** than Google's. Users get answers directly in the chat. The traffic game is shifting from volume to quality - optimise for conversions on the traffic you do get.

### 5. Monthly Citation Volatility
**40-60%** of cited sources change month-to-month. Unlike traditional SEO where rankings are relatively stable, AI visibility is highly volatile. Keep content fresh and updated - stale pages drop out fast.

### 6. Content Freshness Is a Cheat Code
Adding specific dates (e.g., "The top AI tools for 2026") to page titles and headers helps AI systems recognise content as current. Pages with explicit dates and "last updated" timestamps get cited significantly more.

### 7. The "Quotable Snippet" Effect
AI engines need to extract a clean 1-2 sentence answer. Pages that provide **clear, self-contained statements** near the top of each section are cited far more than pages requiring synthesis across multiple paragraphs. Write each key section so the first 1-2 sentences could stand alone as a complete answer.

### 8. "As Seen In" Sections Actually Work
Adding credibility sections showing media mentions, awards, and expert endorsements on your pages boosts AI citation rates. It acts as a trust signal that AI can verify across the web.

### 9. Scientific Data in Product Descriptions
Rewriting product descriptions to include measurable specs, scientific data, and comparison data makes them significantly more likely to be cited by AI shopping assistants and product comparison queries.

### 10. Only 7.2% of Sites Win in Both AI and Traditional Search
The vast majority of sites that get cited by AI engines are **not** the same ones that rank well in Google. These are nearly separate games requiring separate on-site strategies.

---

## Google's "Searchable Index" Patent (US20250217356A1, July 2025)

A Google patent published July 2025 reveals how the index actually works under the hood. This is not speculation - it's straight from the patent filing.

### The Core Idea

Instead of running keyword retrieval and ML ranking as two separate steps, **Google bakes the ML predictions directly into the index**. Each entry pairs a document with a probability score for a specific user context.

### What Goes Into "User Context"

Not just keywords. The patent lists tokens for:
- **Location**
- **Language**
- **Bandwidth** (connection speed)
- **Device type**
- **View history** (what the user has seen before)

Every combination changes which documents Google considers relevant **before ranking even happens**.

### Two Critical Signals from the Patent

1. **Duration Prediction**: The outcome probability includes how long a user is expected to interact with the content. Dwell time isn't a rumour - it's named in the patent as a training signal.

2. **Repeat Access**: Whether users come back is its own ranking signal, separate from CTR. Return visits are explicitly tracked.

### What This Means for Your Site

- **Stop treating one URL as one ranking.** The same page has different relevance scores for different user contexts. Check rankings per device, country, and language separately, not in aggregate.

- **Page speed on slow connections matters more than lab scores suggest.** The index has a bandwidth token. A page that loads fine on fibre but struggles on 4G is a **different document** to Google.

- **Localisation beats translation.** A page that just translates English content scores differently than one written for local search behaviour, because the language token interacts with location and query patterns.

- **Build for return visits, not just first clicks.** Newsletter signups, useful tools, deep reference content. "Repeat access" rewards pages people bookmark. Design content people will come back to.

- **Watch dwell time as a real metric.** If users bounce in 5 seconds, that signal feeds back into the index. Create content that keeps people engaged.

---

## Parasite SEO & Social Signal Stacking

A strategy being shared on LinkedIn (#parasiteseo) that uses high-authority third-party platforms to rank for your brand terms, then funnels that authority back to your site.

### The Tactic

1. Create branded profiles on major platforms: YouTube, Facebook (Groups rank better than Pages), LinkedIn, X (Premium articles rank better), Instagram, Threads, Pinterest, TikTok, Reddit (create your own subreddit)

2. **Post multiple times per day** across all platforms. Doesn't need to be video - text/image posts work. Volume and consistency matter.

3. What happens: Your social posts start appearing on page one for your brand terms. Then longtail keywords start appearing on page one.

4. **Create AI pages on Perplexity, Qwen, and similar** for your brand - these index and rank too.

5. Once social posts are indexing and ranking, **purchase press releases** that link back to your website AND the social posts that are already ranking. This stacks authority.

6. Claimed result: increasing organic traffic in Google Search Console and leads within two weeks of consistent posting.

### Why This Matters for Your Site

This isn't just social media strategy - it's about creating a **web of brand signals** that AI and search engines pick up. The more consistent your brand appears across platforms, the more confidently AI systems cite and recommend your site. It directly feeds the brand mention correlation (0.664) with AI visibility found in the Ahrefs study.

---

## AI Overview Tracking: What Actually Works (Daniel Foley Carter)

Insights from Daniel Foley Carter (25+ years SEO experience) on the reality of tracking AI Overviews and AI search visibility.

### The Uncomfortable Truths

- **AI Overviews are unstable.** They vary daily, by location, and by device. They don't remain consistent.
- **CTR is up by average 22%** on days where AI Overviews appear frequently - but that's not great considering the space an AIO takes up. Users likely scan the initial answer before scrolling.
- **Personalisation changes output** - different users see different AI Overviews
- **Location changes output** - geography shifts what appears
- **LLMs are not linear** - you can't predict or guarantee appearances

### What to Actually Track

**Track end clicks, not visibility.** The only reliable measurement is what happens at the end - actual clicks and conversions. The journey to an AI citation is almost impossible to piece together.

This applies to:
- AI Overviews
- AI Mode
- AI Searches (LLMs)

### What Doesn't Work

- **LLM prompt search volume data** - described as "utter bollocks" - unreliable
- **LLM prompt tracking visibility %** - doesn't consistently align with GA4 referral traffic from LLMs. Visibility can go up massively while GA4 referral traffic stays the same.
- Most AI/LLM searches are **5+ words**, making them highly personalised. The probability of the same search happening more than once goes down because conversational search lets people be very specific.

### The Priority

**AI Overviews and AI Mode should be the priority** over chasing LLM prompt visibility. They're attached to Google (where the traffic still is) and are more measurable through end clicks.

---

## AI Search Is Probabilistic, Not Deterministic

A critical mental model shift for anyone optimising their site for AI search.

### The Two Core Concepts of AEO

**1. AI search is probabilistic.**
The same question asked twice - even by the same person, even in the same session - will return a different result. This is a feature, not a bug.

What this means: **Your brand won't show up 100% of the time for any given prompt.** The best brands only show up ~60% of the time. (Useful stat for when the CEO asks why they didn't appear in their random AI search.)

**How to measure performance:** Don't think in rankings. Think in **trends over time** - for a given set of prompts you care about, is your brand showing up more frequently and in a positive light?

**2. Zero-click UX changes everything.**
Traditional search: Search > Click > Read > Repeat.
AI search collapses that into one step. Agents do the visiting, discovery, evaluation, and recommendation for the user.

**What this means for your site:** If you're only looking at referral traffic from AI platforms as a success metric, you're missing the bigger picture. Your site content is being consumed and synthesised by AI even when no one clicks through. The value is in being **recommended and cited**, not just visited.

---

## llms.txt: The File AI Agents Actually Read Now (David Kaufman / Siteline)

Originally dismissed as a gimmick, llms.txt has quietly become a real thing.

### What Changed

llms.txt files were pitched early as a robots.txt for AI agents - a place to describe your product and brand. SEO heads noticed Googlebot wasn't crawling it and moved on. **That was a fair read for a while, but it changed in the last few weeks.**

### The Numbers

Across sites tracking with Siteline, requests for llms.txt and llms-full.txt are **up more than 10x** since the start of 2026, mostly driven by Claude.

**Top platforms requesting llms.txt and llms-full.txt:**
- Anthropic (Claude): **52%**
- OpenAI: **25%**
- Amazon: **4%**
- Google: **4%**

### The Real Use Case

The use case is different than what was originally pitched. Instead of treating it as a brand summary, companies are using llms.txt as a **table of contents for their documentation**, so the AI agent can figure out which docs to read next.

A typical example:

```
[Product overview](docs.example.com/overview)
[Quickstart](docs.example.com/quickstart)
[API functionality A](docs.example.com/api/endpointA)
[API functionality B](docs.example.com/api/endpointB)
```

After hitting the file, the agent picks 2-3 pages from the index and goes straight to those.

### What This Means for Your Site

Claude and other AI agents are using llms.txt as a **jumping-off point** to figure out where to go next on your website and docs. If you have a docs-heavy or technical product, the highest leverage move is making sure your llms.txt is a clean, structured index of your content. **Skip the marketing copy** - treat it like a sitemap for AI agents.

---

## Writing for RAG: H1s, First Paragraphs & Zero Anaphora

How LLMs actually parse your pages, and why the first paragraph matters more than the H1.

### The Rule

LLMs (ChatGPT, Claude, Gemini, Perplexity) parse top-to-bottom and weight the first chunk of any page heavily. But the **H1 should name the thing, not explain it**. The explanation belongs in the **first paragraph immediately after the H1** - ideally a single plain-prose sentence that states what it is and what it does, before any sub-headings, lists, or front-matter.

### Why This Matters (Two Technical Reasons)

**1. RAG Chunking.**
Retrieval pulls 200-500 token passages. The first passage on a page is the one most likely to be cited. If the H1 is the only thing carrying meaning, the chunk has nothing to extract. If the purpose is in paragraph 1, the chunk is self-contained.

**2. Zero Anaphora / Standalone Passages.**
The opening sentence should use the **full entity name** and state the function. For example:

- GOOD: *"Rank4AI is a framework for X that does Y"*
- BAD: *"This document outlines..."* (subject only resolvable via the H1)

When AI extracts a passage, it rips it out of context. If your opening sentence uses "this" or "it" referring back to the H1, the extracted passage is meaningless on its own. Use the full name. State the function. Make every paragraph capable of standing alone.

### Practical On-Site Rules

1. **H1** = Name the thing (short, specific)
2. **First paragraph** = One sentence explaining what it is and what it does, using the full entity name
3. **No anaphora** in opening sentences of any section - always restate the subject
4. **Every H2 section** should have a self-contained opening sentence that makes sense without reading anything above it

---

## Claude Code .claude/ Folder for Marketers (Vicky Lalwani)

An emerging approach using Claude Code's project structure specifically for SEO and marketing automation.

### The Blueprint

A `.claude/` folder structure designed for marketers, with SEO-specific skills and hooks:

**Skills (on-demand, model-invokable):**
- `schema-gen/` - JSON-LD generation for any page
- `redirect-map/` - Old URL to new URL mapper
- `faq-block/` - FAQ schema + visible block generator
- `hero-rewrite/` - Headline + CTA generator

**Agents (subagents, isolated context):**
- `reviewer.md` - Checks diffs against brand rules
- `researcher.md` - Pulls competitor patterns
- `log-analyzer.md` - Parses GSC + GA errors

**Hooks (deterministic, fire every time):**
- `PostToolUse.sh` - Auto-commit after every edit
- `SessionStart.sh` - Load client context on startup
- `PreCompact.sh` - Save state before compaction

**Slash commands:**
- `/ship` - Lint, build, deploy in one go
- `/audit` - Full SEO check before commit

**Rules (path-scoped):**
- `seo.md` - Loads only for `content/**` files

**MCP integrations:**
- `.mcp.json` with GSC + GTM + Semrush connections

### Why This Matters for Your Site

This represents a shift toward **automated, AI-assisted SEO workflows** built into the development process. Schema generation, redirect mapping, FAQ blocks, and SEO audits happen as part of the code workflow rather than as separate manual processes. The hooks ensure SEO checks run automatically before any content goes live.

---

## Flipbook: Post-GUI Web Experiences

An early signal of where the web is heading - relevant for how your site might need to adapt.

Flipbook (flipbook.page) generates entire screen experiences live via AI instead of rendering through HTML, CSS, and layout engines. Using LTX Studio's video model to deliver live 1080p at 24fps over WebSockets on serverless GPUs.

### Why This Matters

The implication for websites: interfaces that can be anything you describe, on demand. Coding environments, data dashboards, travel planners, creative tools - all potentially reimagined as fluid, adaptive experiences. This is early, but it signals a future where **static page structures may give way to dynamically generated interfaces** - which would fundamentally change how AI interacts with and cites web content.

---

## Actionable Site Playbook

### Quick Wins (Do This Week)

- [ ] Add **FAQPage, HowTo, Author, and Organization schema** to key pages
- [ ] Add **specific dates** to content page titles and headers (e.g., "Best X for 2026")
- [ ] Add **datePublished and dateModified** to Article schema on all content pages
- [ ] Restructure top 10 pages with **H2 questions and 40-60 word answers**
- [ ] Add **"As seen in" credibility sections** to key landing pages
- [ ] Check **NAP consistency** across your site and all directory listings
- [ ] Add an **llms.txt** file to your site root as a structured index of your key content
- [ ] Rewrite **first paragraphs** on key pages: full entity name + what it does, no anaphora

### Medium-Term (This Month)

- [ ] Audit **brand mentions** across the web and identify gaps (Ahrefs/Semrush)
- [ ] Create **citation-worthy original research** pages (surveys, benchmarks, data studies)
- [ ] Implement **AI visibility tracking** - focus on **end clicks** not prompt visibility %
- [ ] Rewrite **product descriptions** with scientific data, specs, and comparison data
- [ ] Build **location-specific pages** with real local content and LocalBusiness schema
- [ ] Optimise **Apple Business Connect** and **Bing Places** listings to match site NAP
- [ ] Test page speed on **slow connections (4G)** - Google's index has a bandwidth token
- [ ] Audit every page: can the **first 200-500 tokens** stand alone as a self-contained passage?

### Strategic (This Quarter)

- [ ] Develop **topic authority content clusters** (broader subjects, not just individual keywords)
- [ ] Publish **proprietary datasets or frameworks** that AI engines need to cite
- [ ] Build a **PR and brand mention strategy** to increase web mentions (0.664 correlation with AI visibility)
- [ ] Add **Speakable schema** to content optimised for voice search
- [ ] Set up **monthly AI citation trend tracking** for key prompts (trending up/down, not absolute %)
- [ ] Review and **don't kill low-ranking pages** - they may be your best AI citation assets
- [ ] Explore **Claude Code .claude/ workflows** for automated schema generation and SEO auditing
- [ ] Build for **repeat access** - tools, references, resources people bookmark and return to
- [ ] Localise content for key markets (don't just translate - **rewrite for local search behaviour**)
- [ ] Check rankings per **device, country, and language separately** (same URL = different scores per context)

---

## Key Takeaway

> Your site needs to be **citable, not just rankable**. AI search is probabilistic - the best brands only show up ~60% of the time. Structure every key page so the first paragraph stands alone as a complete, self-contained answer using the full entity name. Add an llms.txt file. Publish original data no one else has. Test on 4G, not just fibre. Track end clicks and citation trends, not prompt visibility percentages. And build for return visits - Google's patent confirms repeat access is a ranking signal.

---

*Research compiled May 2026. Sources from LinkedIn articles, posts, Google patent filings, and industry publications. Focused on website/on-site optimization only.*
