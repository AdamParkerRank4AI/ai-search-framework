# GitHub Markdown Resources for Rank4AI

Master catalog of 80+ GitHub repos for AI search optimization, content generation, and GEO/AEO work.

---

## Top Priority Repos

| # | Repo | Why It's #1 Priority |
|---|---|---|
| 1 | [nibzard/llm-answer-watcher](https://github.com/nibzard/llm-answer-watcher) | Production-ready CLI for multi-LLM brand monitoring. YAML config, 10 example templates, budget controls, JSON output |
| 2 | [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | ICLR 2026 paper. Auto-extracts content preference rules from AI engines, rewrites documents. MIT licensed |
| 3 | [jdevalk/astro-seo-graph](https://github.com/jdevalk/astro-seo-graph) | All-in-one Astro SEO by Yoast creator: meta, OG, JSON-LD @graph, IndexNow, llms.txt, FuzzyRedirect |
| 4 | [glincker/geo-audit](https://github.com/glincker/geo-audit) | `npx @glincker/geo-audit` one-liner GEO scoring for any URL |
| 5 | [mendableai/create-llmstxt-py](https://github.com/mendableai/create-llmstxt-py) | llms.txt generator (replaces deprecated firecrawl version) |

---

## 1. llms.txt Ecosystem

The `/llms.txt` standard (proposed by Jeremy Howard) provides a curated markdown table of contents for LLMs visiting your site.

| Repo | Description | Notes |
|---|---|---|
| [llmstxt/llmstxt.github.io](https://github.com/llmstxt/llmstxt.github.io) | Official llms.txt specification | The standard itself |
| [mendableai/create-llmstxt-py](https://github.com/mendableai/create-llmstxt-py) | Python llms.txt generator | Replaces deprecated firecrawl version |
| [4hse/astro-llms-txt](https://github.com/4hse/astro-llms-txt) | Astro integration for llms.txt | Generates /llms.txt, /llms-small.txt, /llms-full.txt |
| [tfmurad/astro-llms-md](https://github.com/tfmurad/astro-llms-md) | Zero-config Astro llms.txt + individual .md files | Auto-detects site URL |
| [gxjansen/astro-md-alternate](https://github.com/gxjansen/astro-md-alternate) | Markdown alternate endpoints for AI agents | 10x token reduction, `<link rel="alternate">` |
| [dotenvx/llmstxt](https://github.com/dotenvx/llmstxt) | llms.txt for dotenvx | Reference implementation |
| [nichochar/open-llmstxt](https://github.com/nichochar/open-llmstxt) | Open directory of sites with llms.txt | Community catalog |
| [pydantic/llmstxt.directory](https://github.com/pydantic/llmstxt.directory) | Directory of llms.txt files across the web | Pydantic-maintained |
| ~~[nichochar/llmstxt-generator](https://github.com/nichochar/llmstxt-generator)~~ | ~~Firecrawl-based generator~~ | **DEPRECATED** — use mendableai/create-llmstxt-py |
| [AminHP/llms-txt-generator](https://github.com/AminHP/llms-txt-generator) | Alternative llms.txt generator | Python-based |
| [pydantic/llmstxt-action](https://github.com/pydantic/llmstxt-action) | GitHub Action to validate llms.txt | CI/CD integration |

---

## 2. GEO (Generative Engine Optimization) Research & Tools

| Repo | Description | Notes |
|---|---|---|
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | ICLR 2026 — auto-extracts content rules from AI engines, rewrites docs | MIT license. 3 stages: Rule Extraction, AutoGEO_API, AutoGEO_Mini |
| [GEO-optim/GEO](https://github.com/GEO-optim/GEO) | Princeton GEO research — original GEO paper code | Foundational research: stats +37-41% visibility |
| [glincker/geo-audit](https://github.com/glincker/geo-audit) | `npx @glincker/geo-audit URL` — instant GEO score | One-liner audit |
| [glincker/geo-audit-action](https://github.com/glincker/geo-audit-action) | GitHub Actions CI/CD for GEO audits | Full YAML workflow templates |
| [jroakes/geo-scraper](https://github.com/jroakes/geo-scraper) | GEO compliance scraper | 13+ config/compliance files |
| [geokit-ai/geokit](https://github.com/geokit-ai/geokit) | GEO toolkit | `npx geokit` |
| [iFe3l/geo-bench](https://github.com/iFe3l/geo-bench) | GEO benchmarking framework | For evaluating GEO strategies |
| [searchsolved/gego](https://github.com/searchsolved/gego) | GEO audit tool | Python-based site auditor |

### AutoGEO Deep Dive

AutoGEO (cxcscmu/AutoGEO) is the most significant repo for understanding how AI engines prefer content:

- **6 Content Criteria:** Directness, Completeness, Relevance, Structural Clarity, Accuracy, Conciseness
- **3 Stages:**
  1. Rule Extraction — automatically mines preference rules from AI engines
  2. AutoGEO_API — prompt-based rewriting using extracted rules
  3. AutoGEO_Mini — lightweight trained model for faster rewriting
- **Key Finding:** Rewritten content shows measurable improvement in AI engine citation rates

---

## 3. Claude Code SEO Skills

| Repo | Description | Notes |
|---|---|---|
| [nicoles-professional-growth/gtm-engineer-skills](https://github.com/nicoles-professional-growth/gtm-engineer-skills) | 5 Claude Code skills for GTM work | curl one-liner installs |
| [nicoles-professional-growth/claude-seo](https://github.com/nicoles-professional-growth/claude-seo) | Claude Code SEO skill | npm install |
| [nicoles-professional-growth/Agentic-SEO-Skill](https://github.com/nicoles-professional-growth/Agentic-SEO-Skill) | Python-based SEO automation | 4 reusable scripts: entity_checker, validate_schema, llms_txt_checker, competitor_gap |
| [nicoles-professional-growth/marketingskills](https://github.com/nicoles-professional-growth/marketingskills) | 37 marketing skills via npx | Broad marketing automation |
| [nicoles-professional-growth/ai-cmo](https://github.com/nicoles-professional-growth/ai-cmo) | AI CMO — strategic marketing assistant | Claude Code skill |

---

## 4. AEO (Answer Engine Optimization) Tools

| Repo | Description | Notes |
|---|---|---|
| [nibzard/llm-answer-watcher](https://github.com/nibzard/llm-answer-watcher) | Multi-LLM brand monitoring CLI | **Highest value** — YAML config, 10 example dirs, budget controls, JSON output |
| [nibzard/aeo-mentions-crawler](https://github.com/nibzard/aeo-mentions-crawler) | AEO mentions crawler | Tracks brand mentions in AI answers |
| [RivalSee](https://github.com/search?q=rivalsee) | Competitor AI visibility audit | Prompt-based audit tool |
| [CiteVista](https://github.com/search?q=citevista) | n8n workflow for citation tracking | Workflow automation |

---

## 5. Schema / Structured Data Templates

| Repo | Description | Notes |
|---|---|---|
| [google/schema-dts](https://github.com/nicoles-professional-growth/schema-dts) | TypeScript definitions for Schema.org | Type-safe JSON-LD |
| [codiume/astro-seo-schema](https://github.com/codiume/orbit/tree/main/packages/astro-seo-schema) | `<Schema>` Astro component | v6.0.0, active |
| [JayHoltslander/Structured-Data-JSON-LD](https://github.com/JayHoltslander/Structured-Data-JSON-LD) | Collection of JSON-LD templates | Copy-paste ready |
| [greynewell/schema-driven-astro-starter](https://github.com/greynewell/schema-driven-astro-starter) | Astro starter with auto JSON-LD | WebSite schema, Decap CMS, TypeScript |
| [Apatero-Org/astro-seo-blog-template](https://github.com/Apatero-Org/astro-seo-blog-template) | Astro template: auto BlogPosting, FAQ, HowTo, Review schema | 100 Lighthouse score |

---

## 6. AI SEO Awesome Lists

| Repo | Description | Notes |
|---|---|---|
| [awesome-generative-engine-optimization](https://github.com/search?q=awesome+generative+engine+optimization) | Curated GEO resources | Community-maintained awesome list |
| [awesome-llms-txt](https://github.com/search?q=awesome+llms+txt) | Curated llms.txt resources | Ecosystem catalog |
| [fabriziosalmi/awesome-llm-agents](https://github.com/fabriziosalmi/awesome-llm-agents) | LLM agent tools and frameworks | Broad AI agent catalog |

---

## 7. Content Generation & SEO Pipelines

| Repo | Description | Notes |
|---|---|---|
| [gbessoni/seo-agi](https://github.com/gbessoni/seo-agi) | DeerFlow-based SEO agent, DataForSEO, 500-token chunks | Full pipeline |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | Claude Code workspace for SEO pipeline | Complete SEO workflow |
| [agniiva/Content-Brief-Generator-SERP](https://github.com/agniiva/Content-Brief-Generator-SERP) | Python/Streamlit SERP brief generator | Visual UI |
| [nicoles-professional-growth/ai-cmo](https://github.com/nicoles-professional-growth/ai-cmo) | AI CMO for strategic content | Marketing strategy |

### n8n Workflow Templates

| Workflow | Description | URL |
|---|---|---|
| Bright Data SERP Brief | SERP analysis → AI content brief | [n8n.io/workflows/8053](https://n8n.io/workflows/8053) |
| Keyword to Google Doc | Keyword research → formatted Google Doc | [n8n.io/workflows/8289](https://n8n.io/workflows/8289) |

---

## 8. AI SEO Audit Tools

| Repo | Description | Notes |
|---|---|---|
| [glincker/geo-audit](https://github.com/glincker/geo-audit) | `npx @glincker/geo-audit` | Instant GEO scoring |
| [searchsolved/gego](https://github.com/searchsolved/gego) | GEO audit tool | Python-based |
| [aperture-seo/aperture](https://github.com/search?q=aperture+seo) | Docker-deployed SEO monitoring | Full deployment |
| [serpbear/serpbear](https://github.com/nicoles-professional-growth/serpbear) | Open-source SEO rank tracker | Self-hosted |

---

## 9. Knowledge Graph / Entity Tools

| Repo | Description | Notes |
|---|---|---|
| [google/schema-dts](https://github.com/nicoles-professional-growth/schema-dts) | TypeScript Schema.org definitions | Entity typing |
| Wikidata API | Entity verification and linking | First strategy for entity recognition |
| Google Knowledge Graph API | Entity search and verification | Free tier available |

**Entity optimization strategy:**
1. Create Wikidata entry for your brand/person
2. Link Schema.org `sameAs` to all social profiles + Wikidata
3. Consistent NAP (Name, Address, Phone) across the web
4. Brand mentions correlate 3x more strongly with AI citations than backlinks

---

## 10. Google AI Overview Scrapers

| Repo | Description | Notes |
|---|---|---|
| [serpapi/google-search-results-python](https://github.com/serpapi/google-search-results-python) | SerpAPI Python client | Includes AI Overview data |
| DataForSEO API | SERP data including AI Overviews | Commercial API with AI Overview support |
| [nicoles-professional-growth/geo-scraper](https://github.com/jroakes/geo-scraper) | GEO compliance scraper | Scrapes AI-relevant data |

---

## 11. Competitor / Related Repos

| Repo | Description | Notes |
|---|---|---|
| [RivalSee](https://github.com/search?q=rivalsee+seo) | AI visibility competitor audit | Prompt-based |
| [CiteVista](https://github.com/search?q=citevista) | Citation tracking workflow | n8n-based |
| Various agency repos | GEO/AEO service providers with open tools | Check awesome lists |

---

## 12. Third-Party Publishing & Awesome List Submission

### How to Submit to Awesome Lists

**awesome-generative-engine-optimization:**
1. Fork the repo
2. Add your entry in alphabetical order within the relevant category
3. Format: `- [Tool Name](URL) - Brief description`
4. Submit PR with title: `Add [Tool Name]`
5. Include: what it does, why it belongs, which category

**awesome-llms-txt:**
1. Fork and add entry under correct section
2. Format: `- [Site/Tool Name](URL) - Description`
3. PR with clear title and description

### Directories to Submit To

| Directory | What to Submit |
|---|---|
| llmstxt.directory (Pydantic) | Your site's llms.txt URL |
| open-llmstxt | Your site's llms.txt |
| GEO awesome lists | Your tools/services |
| Product Hunt | Launch tools publicly |

---

## 13. Emerging Standards

| Standard | Description | Status |
|---|---|---|
| **llms.txt** | Markdown TOC for LLMs at /llms.txt | Proposed (Jeremy Howard), widely adopted |
| **IndexNow** | Instant URL notification to Bing/ChatGPT | Production — supported by Bing, Yandex, Naver |
| **SpeakableSpecification** | Schema.org markup for voice/AI playback | Emerging |
| **`<link rel="alternate" type="text/markdown">`** | Markdown alternate for AI consumption | Early adoption |
| **AI Crawler User-Agents** | Standardized bot identification | Per-platform (see robots.txt guide) |
| **Robots.txt AI extensions** | Differentiating training vs search crawlers | OpenAI, Anthropic, Google all use separate bots now |

---

## 14. Industry Stats & Research

### Key Research Papers with Code

| Paper/Source | Key Finding |
|---|---|
| **Princeton GEO** (GEO-optim/GEO) | Adding statistics = +37-41% visibility in AI engines |
| **AutoGEO** (ICLR 2026) | 6 criteria AI engines use to evaluate content |
| **Zyppy/SparkToro studies** | 76.4% of ChatGPT's most-cited pages updated within 30 days |
| **BrightEdge** | 82.5% of AI citations from pages with structured data |
| **Authoritas** | 96% of AI Overview citations from strong E-E-A-T sources |
| **Various** | Brand mentions correlate 3x more with AI citations than backlinks |
| **Various** | Pages with FCP <0.4s get 3.2x more ChatGPT citations |
| **Bing/ChatGPT** | 87% of ChatGPT citations match Bing top 10 results |
| **Cloudflare** | 27% of B2B SaaS sites unknowingly blocking AI crawlers |
| **Reddit** | Reddit cited in ~8-15% of AI Overviews across verticals |
| **LinkedIn** | Growing as citation source for B2B expertise content |

---

*Compiled for Rank4AI Ltd. Last updated: April 2026.*
