# AI Search Optimization Guide for Astro Sites

Complete guide for maximizing AI crawler access, citations, and visibility — tailored for Astro.

---

## 1. Astro's Advantage for AI Search

Astro's default SSG (Static Site Generation) is the **gold standard** for AI crawler accessibility:

- Pages pre-rendered at build time into **pure static HTML**
- Zero JavaScript shipped by default
- AI crawlers (GPTBot, ClaudeBot, PerplexityBot) receive fully rendered HTML immediately
- **Critical fact:** Almost no AI crawler executes JavaScript — SPAs are invisible to AI search

**Recommendation:** Use SSG for all public-facing content. Only use SSR for authenticated/dynamic pages.

---

## 2. Recommended Astro Package Stack

```bash
# All-in-one (by Joost de Valk, Yoast creator)
npm install @jdevalk/astro-seo-graph
# Provides: <Seo> component, JSON-LD @graph, IndexNow, llms.txt, FuzzyRedirect, build validation

# OR modular approach:
npm install astro-seo                    # Meta tags + OG
npm install schema-dts astro-seo-schema  # Type-safe JSON-LD

# Sitemap (official)
npx astro add sitemap

# robots.txt
npm install astro-robots-txt

# AI-specific
npm install @4hse/astro-llms-txt         # llms.txt generation
npm install astro-md-alternate           # Markdown alternate for AI agents (10x token reduction)
```

### Package Details

| Package | What it does | Stars/Downloads |
|---|---|---|
| [@jdevalk/astro-seo-graph](https://joost.blog/astro-seo-complete-guide/) | All-in-one: meta, OG, JSON-LD graph, IndexNow, llms.txt, FuzzyRedirect | By Yoast creator |
| [astro-seo](https://github.com/jonasmerlin/astro-seo) | Lightweight `<SEO />` component for meta/OG | Most popular |
| [astro-seo-schema](https://github.com/codiume/orbit/tree/main/packages/astro-seo-schema) | `<Schema>` component with TypeScript defs via `schema-dts` | v6.0.0, active |
| [@4hse/astro-llms-txt](https://github.com/4hse/astro-llms-txt) | Generates /llms.txt, /llms-small.txt, /llms-full.txt | 19 stars |
| [astro-llms-md](https://github.com/tfmurad/astro-llms-md) | Zero-config llms.txt + individual .md files | Auto-detects |
| [astro-md-alternate](https://github.com/gxjansen/astro-md-alternate) | `.md` endpoints + `<link rel="alternate" type="text/markdown">` for AI agents | 10x token reduction |
| [@astrojs/sitemap](https://docs.astro.build/en/guides/integrations-guide/sitemap/) | Official sitemap generation | Official |
| [astro-robots-txt](https://www.npmjs.com/package/astro-robots-txt) | Auto-generated robots.txt from config | 12,629 weekly downloads |
| [astro-navigation](https://www.npmjs.com/package/astro-navigation) | Breadcrumbs with auto JSON-LD structured data | |

### Astro Starters/Templates

| Starter | Description |
|---|---|
| [schema-driven-astro-starter](https://github.com/greynewell/schema-driven-astro-starter) | Production-ready with WebSite schema, auto JSON-LD, Decap CMS, TypeScript |
| [astro-seo-blog-template](https://github.com/Apatero-Org/astro-seo-blog-template) | Auto Schema.org (BlogPosting, FAQ, HowTo, Review), sitemap, RSS, 100 Lighthouse |

---

## 3. robots.txt for AI Crawlers

### All Known AI Crawler User-Agents (2026)

**OpenAI (3 bots):**
| User Agent | Purpose | Allow? |
|---|---|---|
| `GPTBot` | Training + retrieval | Optional (training) |
| `OAI-SearchBot` | ChatGPT real-time search index | **YES — critical for citations** |
| `ChatGPT-User` | User-initiated browsing | **YES** |

**Anthropic (3 bots, updated Feb 2026):**
| User Agent | Purpose | Allow? |
|---|---|---|
| `ClaudeBot` | Training crawler | Optional (training) |
| `Claude-SearchBot` | Search/retrieval for Claude answers | **YES — critical** |
| `Claude-User` | User-initiated browsing | **YES** |

**Perplexity (2 bots):**
| User Agent | Purpose | Allow? |
|---|---|---|
| `PerplexityBot` | Indexes web for Perplexity search | **YES** |
| `Perplexity-User` | Real-time retrieval | **YES** |

**Google:**
| User Agent | Purpose | Allow? |
|---|---|---|
| `Googlebot` | Standard search (AI Overviews use this) | **YES** |
| `Google-Extended` | Gemini training + grounding | Optional |

**Others:**
| User Agent | Purpose | Allow? |
|---|---|---|
| `Bingbot` | Bing index — **ChatGPT relies on Bing** | **YES — critical** |
| `Applebot-Extended` | Apple Intelligence | Optional |
| `DuckAssistBot` | DuckDuckGo AI | Yes |
| `Bytespider` | ByteDance/TikTok (poor compliance) | Block |
| `CCBot` | Common Crawl training data | Block |
| `meta-externalagent` | Meta AI | Optional |

**Deprecated (remove if present):** `Claude-Web`, `anthropic-ai`

### Recommended robots.txt (Maximum AI Citation Visibility)

```
# === AI SEARCH BOTS (ALLOW for citations) ===
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: DuckAssistBot
Allow: /

# === AI TRAINING BOTS (BLOCK to prevent training use) ===
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /

User-agent: meta-externalagent
Disallow: /

# === TRADITIONAL SEARCH (always allow) ===
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: *
Allow: /

Sitemap: https://example.com/sitemap-index.xml
```

### Astro Implementation

**Option A: Static file** — place in `public/robots.txt`

**Option B: Dynamic** — create `src/pages/robots.txt.ts`:
```typescript
import type { APIRoute } from 'astro';
export const GET: APIRoute = () => {
  const robotsTxt = `
User-agent: OAI-SearchBot
Allow: /
...
Sitemap: ${import.meta.env.SITE}/sitemap-index.xml
  `.trim();
  return new Response(robotsTxt, { headers: { 'Content-Type': 'text/plain' } });
};
```

### CDN WARNING

**Cloudflare blocks AI crawlers by default** since July 2025. Over 1 million sites affected. If you use Cloudflare, you MUST go to dashboard → **AI Crawl Control** and explicitly allow AI crawlers, or your robots.txt Allow directives are overridden at the infrastructure level. **27% of B2B SaaS sites are unknowingly blocking AI crawlers at CDN level.**

---

## 4. llms.txt Implementation

The `/llms.txt` standard tells AI systems which pages to read first — a curated table of contents for LLMs.

### Astro Options

**@4hse/astro-llms-txt:**
```bash
npm install @4hse/astro-llms-txt
```
```javascript
// astro.config.mjs
import llmsTxt from '@4hse/astro-llms-txt';
export default defineConfig({
  integrations: [llmsTxt({
    docSet: [{ include: 'blog/**', promote: ['blog/best-posts/**'] }],
    mainSelector: 'main',
    ignoreSelectors: ['nav', 'footer', '.sidebar']
  })]
});
```
Generates `/llms.txt`, `/llms-small.txt`, `/llms-full.txt`.

**astro-llms-md (zero-config):**
```bash
npm install -D astro-llms-md
```
Auto-detects site URL, generates llms.txt + llms-full.txt + individual .md files. Requires valid `<h1>` and `<main>` elements per page.

**astro-md-alternate (markdown for AI agents):**
```bash
npm install astro-md-alternate
```
Generates `.md` endpoints for each content page (e.g., `/post/my-article.md`). Adds `<link rel="alternate" type="text/markdown">` for auto-discovery. Claims **10x reduction in token usage** for LLM consumption.

---

## 5. Structured Data / JSON-LD for Astro

### Best Practice: Linked @graph (not flat snippets)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebSite", "@id": "https://example.com/#website", "name": "Rank4AI" },
    { "@type": "WebPage", "@id": "https://example.com/page/#webpage", "isPartOf": { "@id": "https://example.com/#website" } },
    { "@type": "BlogPosting", "mainEntityOfPage": { "@id": "https://example.com/page/#webpage" }, "author": { "@id": "https://example.com/#person" } },
    { "@type": "Person", "@id": "https://example.com/#person", "name": "Adam Parker" },
    { "@type": "BreadcrumbList", "itemListElement": [...] }
  ]
}
```

`@jdevalk/astro-seo-graph` handles this automatically with linked entities.

### Schema Types Ranked by AI Citation Impact

| Schema Type | Impact | Detail |
|---|---|---|
| **FAQPage** | Highest — 28-40% higher citation probability | Q&A format matches how AI delivers answers |
| **Article/BlogPosting** | High — used by 26% of AI Overview cited pages | Include author, datePublished, dateModified |
| **Organization** | High — used by 34% of AI Overview cited pages | Establishes entity identity |
| **BreadcrumbList** | Medium — used by 20% of AI Overview cited pages | Helps AI understand site hierarchy |
| **Person** | Medium | Author expertise signals, links to verifiable experts |
| **HowTo** | Medium | Step-by-step content AI can directly extract |
| **Product/Review** | For e-commerce | Rich results + AI extraction |
| **SpeakableSpecification** | Emerging | Marks content suitable for voice/AI playback |

**Key stat:** Sites with comprehensive schema receive **3.2x more AI citations**. 82.5% of AI citations come from pages with structured data.

---

## 6. Crawl Rate Optimization

### Speed Targets

- **Under 200ms server response time (TTFB)** — AI crawlers abandon after ~10 seconds
- Pages with FCP under 0.4s earn **3.2x more ChatGPT citations** than slower pages
- AI crawlers generated **50 billion requests/day** across Cloudflare's network in March 2025

### Sitemap Optimization

```javascript
// astro.config.mjs
import sitemap from '@astrojs/sitemap';
export default defineConfig({
  site: 'https://rank4ai.com',
  integrations: [sitemap({
    filter: (page) => !page.includes('/admin/'),
    serialize(item) {
      if (item.url.includes('/blog/')) {
        item.changefreq = 'weekly';
        item.priority = 0.8;
      }
      return item;
    },
  })],
});
```

Add to HTML `<head>`:
```html
<link rel="sitemap" type="application/xml" href="/sitemap-index.xml" />
```

### IndexNow (Critical for ChatGPT)

**87% of ChatGPT citations match Bing's top 10 results.** IndexNow instantly notifies Bing when content changes → accelerates ChatGPT discoverability.

`@jdevalk/astro-seo-graph` includes IndexNow support built-in. Otherwise implement manually:
- Submit up to 10,000 URLs per HTTP POST request
- Supported by: Bing, ChatGPT (via Bing), Yandex, Naver
- Free, no limits, no spam risk

### Bing Webmaster Tools

**Treat Bing with the same priority as Google.** ChatGPT relies on Bing's index. Submit your sitemap to both Google Search Console AND Bing Webmaster Tools.

---

## 7. Content Formatting for AI Citations

### What AI Models Prefer to Cite

| Factor | Impact | Detail |
|---|---|---|
| **Content length** | 59% more likely to be cited | Content over 2,900 words vs under 800 |
| **Section length** | 70% more citations | 120-180 word sections vs sub-50-word sections |
| **First 100 words** | Critical | Lead with the answer — AI extracts the opening |
| **Statistics** | 3.7x citation boost | Include original data, cited statistics |
| **H2 as questions** | High | Maps to how users query AI systems |
| **40-word definitions** | High | Direct definitions AI can extract verbatim |
| **Comparison tables** | High | Clean HTML tables AI extracts well |
| **FAQ sections** | 30% citation rate improvement | Matches AI Q&A delivery format |
| **Freshness** | 76.4% of ChatGPT's most-cited pages updated in last 30 days | Update high-value content every 2-3 months |

### Content Structure Template

```markdown
# [Topic] — [Clear, Specific Title]

[40-60 word direct answer to the main question. This is what AI will extract first.]

## What is [Topic]?

[Direct 40-word definition. Self-contained paragraph.]

## How Does [Topic] Work?

[120-180 word explanation with specific steps or process.]

## [Topic] vs [Alternative]: Key Differences

| Feature | [Topic] | [Alternative] |
|---|---|---|
| ... | ... | ... |

## Frequently Asked Questions

### [Question matching user query]?
[Direct 40-60 word answer.]

### [Question matching user query]?
[Direct 40-60 word answer.]
```

### The Nerdwallet Principle

From the LinkedIn post you shared — "AI Overviews absorb the average but they cannot absorb your experience."

**Content that gets cited has:**
- Original research and proprietary data
- Named experts with verifiable credentials
- First-person experience and case studies
- Specific numbers, not generic claims
- A perspective that requires domain expertise

**Content that gets replaced by AI Overviews:**
- Generic definitions available everywhere
- Listicles with no original insight
- Content that any AI could generate itself

---

## 8. Entity Optimization

### How to Become a Recognized Entity

1. **Schema markup:** Organization + Person schemas with `sameAs` links to social profiles, Wikipedia, Wikidata
2. **Google Knowledge Panel:** Claim via Google Search Console or create a Wikidata entry
3. **Consistent NAP:** Name, Address, Phone consistent across every mention on the web
4. **Author bios:** Named authors with verifiable credentials on every article
5. **Brand mentions:** PR coverage, community discussions, earned media — brand mentions correlate **3x more strongly** with AI citations than backlinks

### What Matters More Than Domain Authority for AI

| Factor | Correlation with AI Citation |
|---|---|
| E-E-A-T signals | 96% of AI Overview citations have strong E-E-A-T |
| Brand mentions / entity recognition | 3x stronger than backlinks |
| Original data / research | 3.7x more likely to be cited |
| Content freshness | 25.7% fresher than organic results |
| Topical authority (hub-and-spoke) | 31-35% citation chance |
| Domain Authority | Correlation dropped to r=0.18 for AI |

---

## 9. Getting Indexed by Each AI Platform

### ChatGPT Search
1. Submit sitemap to **Bing Webmaster Tools** (87% of citations match Bing top 10)
2. Implement **IndexNow** for instant Bing indexing
3. Optimize for Bing SEO (Bing weighs exact-match keywords more than Google)
4. Allow `OAI-SearchBot` and `ChatGPT-User` in robots.txt
5. Sites with 190K+ monthly visitors are 2x more likely to be cited

### Perplexity
1. Allow `PerplexityBot` in robots.txt
2. Indexing typically takes **1-7 days** with proper sitemap
3. Perplexity does **live retrieval** on every query (not just static index)
4. Favors: recently published content, clear author bios, structured answer formatting
5. Lead with the answer in the **first 100 words**

### Google AI Overviews
1. Same index as Google Search — if you rank, you're eligible
2. Allow `Google-Extended` for Gemini grounding
3. 96% of citations come from sources with strong E-E-A-T
4. Pages ranking #6-#10 with strong E-E-A-T are cited **2.3x more** than #1 with weak authority

### General Timeline
**Expect first AI citations 60-120 days after optimization begins.**

---

## 10. Internal Linking for AI Understanding

- **Hub-and-spoke model:** Pillar pages linked from multiple cluster pages — AI recognizes this as the citation-worthy source
- **Descriptive anchor text:** Semantically rich, not "click here"
- **Shallow crawl depth:** Important pages within 2-3 clicks of homepage
- **Bidirectional linking:** Pillar → cluster AND cluster → pillar
- **Contextual placement:** Links within body content, not just nav/footer

---

## 11. SaaStorm Content Brief Workflow (Replicable)

From the LinkedIn post — SaaStorm's 5-phase workflow is **proprietary but replicable** using public tools.

### Closest Open-Source Starting Points

| Tool | What it covers | URL |
|---|---|---|
| n8n Bright Data SERP Brief | Phases 1+3 (SERP analysis → brief) | [n8n.io/workflows/8053](https://n8n.io/workflows/8053-create-data-driven-seo-content-briefs-with-ai-analysis-of-serp-data-using-bright-data/) |
| n8n Keyword to Google Doc | Phase 5 (output to Docs) | [n8n.io/workflows/8289](https://n8n.io/workflows/8289-create-seo-content-brief-from-keyword-to-google-doc/) |
| agniiva/Content-Brief-Generator-SERP | Python/Streamlit SERP brief | [GitHub](https://github.com/agniiva/Content-Brief-Generator-SERP) |
| gbessoni/seo-agi | DeerFlow-based, DataForSEO, 500-token chunks | [GitHub](https://github.com/gbessoni/seo-agi) |
| TheCraigHewitt/seomachine | Claude Code workspace, full pipeline | [GitHub](https://github.com/TheCraigHewitt/seomachine) |

### Build Your Own (Architecture)

**Stack:** n8n (self-hosted) + DataForSEO/SerpAPI + Claude Sonnet + Google Docs API

**Phase 1 — SERP Intelligence:** HTTP Request → DataForSEO → Loop top 5 URLs → Firecrawl scrape → Python parse headings/word count/structure

**Phase 2 — Audience Research:** DataForSEO PAA endpoint → Vector Store search (ICP knowledge base) → Claude classify intent + synthesize

**Phase 3 — Brief Generation:** Claude prompt with Phase 1+2 data → H1, meta, word count, heading structure, narrative spine

**Phase 4 — Writing Directives:** Claude generate per-section instructions grounded in ICP pain points

**Phase 5 — Output:** Liquid templating (AI-assisted vs human writer formats) → Google Docs API

**Estimated cost per brief:** $0.10-0.50 (SERP ~$0.05-0.15, scraping ~$0.02-0.10, LLM ~$0.05-0.25)

---

## 12. Priority Action Checklist

### Do Today
- [ ] Check CDN (Cloudflare) is not blocking AI crawlers
- [ ] Configure robots.txt to Allow all AI search bots
- [ ] Submit sitemap to Bing Webmaster Tools
- [ ] Implement IndexNow (or install `@jdevalk/astro-seo-graph` which includes it)
- [ ] Run `npx @glincker/geo-audit https://yoursite.com` for baseline score

### Do This Week
- [ ] Install `@jdevalk/astro-seo-graph` OR modular package stack
- [ ] Add FAQPage, Article/BlogPosting, Organization JSON-LD schemas
- [ ] Create `/llms.txt` via `@4hse/astro-llms-txt` or `astro-llms-md`
- [ ] Install `astro-md-alternate` for markdown AI endpoints
- [ ] Verify TTFB is under 200ms

### Do This Month
- [ ] Restructure top 10 pages: H2 questions, 120-180 word sections, answers-first
- [ ] Add author bios with Person schema to all articles
- [ ] Build hub-and-spoke internal linking with descriptive anchors
- [ ] Update dateModified on all high-value content
- [ ] Set up Bing IndexNow for automatic submission on deploy

### Ongoing
- [ ] Update high-value content every 2-3 months
- [ ] Publish original research with proprietary data
- [ ] Monitor AI crawler activity in server logs
- [ ] Track citations across ChatGPT, Perplexity, Gemini, Google AI Overviews
- [ ] Submit to GEO agency directories and awesome lists
