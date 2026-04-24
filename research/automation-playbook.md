# AI Search Optimization — Automation Playbook

Copy-paste-ready setup guides, install commands, configs, and usage examples for Rank4AI operations.

---

## Priority Stack

| Tier | Timeline | Tools |
|---|---|---|
| **Tier 1** | Today | Claude Code Skills (gtm-engineer-skills, claude-seo, Agentic-SEO-Skill, marketingskills, geokit) |
| **Tier 2** | This Week | Monitoring & Auditing (llm-answer-watcher, geo-audit-action, gego, geo-scraper) |
| **Tier 3** | This Month | Content Pipeline (seo-agi, seomachine, Content-Brief-Generator-SERP, ai-cmo) |
| **Tier 4** | Ongoing | Operations (aperture, serpbear, RivalSee, CiteVista, awesome list submissions) |

---

## Tier 1 — Install Today

### 1. gtm-engineer-skills (Claude Code Skills)

5 Claude Code skills for GTM engineering work.

```bash
# Install all 5 skills via curl one-liners
curl -s https://raw.githubusercontent.com/nicoles-professional-growth/gtm-engineer-skills/main/install.sh | bash

# Or install individually:
# Skill 1: Market Research
claude skill install gtm-market-research

# Skill 2: Competitor Analysis
claude skill install gtm-competitor-analysis

# Skill 3: Content Strategy
claude skill install gtm-content-strategy

# Skill 4: SEO Audit
claude skill install gtm-seo-audit

# Skill 5: Analytics Setup
claude skill install gtm-analytics
```

### 2. claude-seo (Claude Code SEO Skill)

```bash
# Install via npm
npm install -g claude-seo

# Or add to Claude Code
claude skill install claude-seo

# Usage
claude-seo audit https://rank4ai.com
claude-seo keywords "generative engine optimization"
claude-seo schema generate --type Article --url https://rank4ai.com/blog/post
```

### 3. Agentic-SEO-Skill

Python-based SEO automation with 4 reusable scripts.

```bash
# Clone and install
git clone https://github.com/nicoles-professional-growth/Agentic-SEO-Skill.git
cd Agentic-SEO-Skill
pip install -r requirements.txt
```

#### Script 1: entity_checker.py
```python
# Check if your brand/person is recognized as an entity
python entity_checker.py --name "Rank4AI" --type Organization
python entity_checker.py --name "Adam Parker" --type Person

# Checks: Wikidata, Google Knowledge Graph, Schema.org presence
# Output: Entity recognition score + recommendations
```

#### Script 2: validate_schema.py
```python
# Validate JSON-LD structured data on your pages
python validate_schema.py --url https://rank4ai.com
python validate_schema.py --url https://rank4ai.com/blog/post --verbose

# Checks: Schema.org compliance, required fields, @graph linking
# Output: Validation report with fixes
```

#### Script 3: llms_txt_checker.py
```python
# Validate your llms.txt file against the spec
python llms_txt_checker.py --url https://rank4ai.com/llms.txt

# Checks: Format compliance, link validity, content coverage
# Output: Compliance score + suggestions
```

#### Script 4: competitor_gap.py
```python
# Analyze competitor AI search presence
python competitor_gap.py --domain rank4ai.com --competitors "competitor1.com,competitor2.com"

# Checks: llms.txt presence, schema coverage, AI crawler access, content structure
# Output: Gap analysis with priority actions
```

### 4. marketingskills (37 Skills via npx)

```bash
# Run any of 37 marketing skills
npx marketingskills

# Example skills:
npx marketingskills --skill content-audit
npx marketingskills --skill keyword-research
npx marketingskills --skill competitor-analysis
npx marketingskills --skill schema-generator
npx marketingskills --skill social-copy
```

### 5. geokit (GEO Toolkit)

```bash
# One-liner GEO analysis
npx geokit analyze https://rank4ai.com

# Full audit with recommendations
npx geokit audit https://rank4ai.com --output report.json

# Check specific GEO criteria
npx geokit check --criteria directness,completeness,relevance https://rank4ai.com/blog/post
```

---

## Tier 2 — Set Up This Week

### 6. llm-answer-watcher (HIGHEST VALUE)

Production-ready CLI for monitoring brand mentions across multiple LLM platforms.

```bash
# Install
npm install -g llm-answer-watcher

# Or clone for full example templates
git clone https://github.com/nibzard/llm-answer-watcher.git
cd llm-answer-watcher
npm install
```

#### YAML Config (config.yaml)
```yaml
# config.yaml — Main configuration
brand:
  name: "Rank4AI"
  aliases:
    - "Rank 4 AI"
    - "rank4ai.com"
  competitors:
    - "competitor1.com"
    - "competitor2.com"

queries:
  - "What is generative engine optimization?"
  - "Best GEO agency UK"
  - "How to optimize for AI search"
  - "What is llms.txt?"
  - "AI search optimization services"
  - "How to get cited by ChatGPT"
  - "Best AI SEO tools 2026"

engines:
  - name: chatgpt
    model: gpt-4o
    enabled: true
  - name: claude
    model: claude-sonnet-4-6
    enabled: true
  - name: perplexity
    enabled: true
  - name: gemini
    model: gemini-pro
    enabled: true

budget:
  max_daily_queries: 100
  max_monthly_cost: 50.00
  currency: GBP

output:
  format: json
  path: ./results/
  include_timestamps: true
  include_full_response: true

schedule:
  frequency: weekly
  day: monday
  time: "09:00"
```

#### Run Monitoring
```bash
# Single run
llm-answer-watcher run --config config.yaml

# Watch mode (continuous)
llm-answer-watcher watch --config config.yaml

# Generate report
llm-answer-watcher report --input ./results/ --format html
```

#### Example Templates (10 directories)
```
examples/
├── 01-basic-brand-monitoring/      # Simple brand mention tracking
├── 02-competitor-comparison/       # Head-to-head competitor analysis
├── 03-keyword-tracking/            # Keyword visibility over time
├── 04-multi-brand/                 # Monitor multiple brands
├── 05-industry-trends/             # Track industry topic coverage
├── 06-product-mentions/            # Product-specific monitoring
├── 07-local-seo/                   # Local business AI visibility
├── 08-content-gap/                 # Find content gaps via AI answers
├── 09-citation-tracking/           # Track when your URLs are cited
└── 10-sentiment-analysis/          # Brand sentiment in AI responses
```

### 7. geo-audit-action (GitHub Actions CI/CD)

#### Basic Workflow (.github/workflows/geo-audit.yml)
```yaml
name: GEO Audit
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9am

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run GEO Audit
        uses: glincker/geo-audit-action@v1
        with:
          url: https://rank4ai.com
          output-format: json
          threshold: 70

      - name: Upload Results
        uses: actions/upload-artifact@v4
        with:
          name: geo-audit-results
          path: geo-audit-results.json

      - name: Comment on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(fs.readFileSync('geo-audit-results.json'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## GEO Audit Results\n\nScore: ${results.score}/100\n\n${results.summary}`
            });
```

#### Multi-Page Workflow
```yaml
name: GEO Audit - Full Site
on:
  schedule:
    - cron: '0 9 * * 1'

jobs:
  audit:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        page:
          - https://rank4ai.com
          - https://rank4ai.com/services
          - https://rank4ai.com/blog
          - https://rank4ai.com/about
    steps:
      - name: Run GEO Audit
        uses: glincker/geo-audit-action@v1
        with:
          url: ${{ matrix.page }}
          output-format: json

      - name: Upload Results
        uses: actions/upload-artifact@v4
        with:
          name: geo-audit-${{ strategy.job-index }}
          path: geo-audit-results.json
```

### 8. gego (GEO Audit Tool)

```bash
# Install
git clone https://github.com/searchsolved/gego.git
cd gego
pip install -r requirements.txt

# Run audit
python gego.py --url https://rank4ai.com --output report.html

# Batch audit
python gego.py --urls urls.txt --output reports/ --format json
```

### 9. geo-scraper

```bash
# Clone (13+ compliance/config files included)
git clone https://github.com/jroakes/geo-scraper.git
cd geo-scraper
pip install -r requirements.txt

# Run scraper
python scraper.py --domain rank4ai.com --config config.yaml

# Files included:
# - robots.txt parser
# - llms.txt validator
# - Schema.org extractor
# - AI crawler access checker
# - Content structure analyzer
```

---

## Tier 3 — Deploy This Month

### 10. seo-agi

```bash
# DeerFlow-based SEO agent with DataForSEO
git clone https://github.com/gbessoni/seo-agi.git
cd seo-agi
pip install -r requirements.txt

# Configure
cp .env.example .env
# Add your DataForSEO API key and Claude API key to .env

# Run
python main.py --keyword "generative engine optimization" --chunks 500
```

### 11. seomachine

```bash
# Claude Code workspace for full SEO pipeline
git clone https://github.com/TheCraigHewitt/seomachine.git
cd seomachine

# This is a Claude Code workspace — open with Claude Code
claude .

# Available workflows:
# - Keyword research pipeline
# - Content brief generation
# - On-page optimization
# - Technical SEO audit
# - Competitor analysis
```

### 12. Content-Brief-Generator-SERP

```bash
# Python/Streamlit SERP brief generator
git clone https://github.com/agniiva/Content-Brief-Generator-SERP.git
cd Content-Brief-Generator-SERP
pip install -r requirements.txt

# Run Streamlit UI
streamlit run app.py

# Access at http://localhost:8501
# Enter keyword → scrapes top SERP results → generates content brief
```

### 13. aeo-mentions-crawler

```bash
# Track brand mentions in AI answers
git clone https://github.com/nibzard/aeo-mentions-crawler.git
cd aeo-mentions-crawler
npm install

# Configure
cp config.example.yaml config.yaml
# Edit config.yaml with your brand details

# Run
node crawler.js --config config.yaml
```

---

## Tier 4 — Ongoing Operations

### 14. aperture (Docker Deployment)

```bash
# Docker-deployed SEO monitoring
git clone https://github.com/aperture-seo/aperture.git
cd aperture

# Deploy with Docker
docker-compose up -d

# Access dashboard at http://localhost:3000
# Configure monitoring targets in the web UI
```

### 15. serpbear (SEO Rank Tracker)

```bash
# Self-hosted rank tracker
git clone https://github.com/nicoles-professional-growth/serpbear.git
cd serpbear
docker-compose up -d

# Access at http://localhost:3000
# Add domains and keywords to track
```

### 16. RivalSee Audit Prompt

RivalSee is a prompt-based competitor audit tool. Use this prompt with Claude or ChatGPT:

```
Analyze the AI search visibility of [DOMAIN] compared to [COMPETITOR 1] and [COMPETITOR 2].

Check for each domain:
1. Does /robots.txt allow AI crawlers (OAI-SearchBot, ClaudeBot, PerplexityBot)?
2. Does /llms.txt exist? What does it contain?
3. What Schema.org structured data is present? (FAQPage, Article, Organization, Person)
4. Is IndexNow implemented?
5. Are pages cited in ChatGPT, Perplexity, or Google AI Overviews for relevant queries?
6. Content freshness: when were key pages last updated?
7. Entity recognition: is the brand/founder recognized in knowledge graphs?

Output a comparison table with scores 0-10 for each factor, plus priority recommendations.
```

### 17. CiteVista (n8n Workflow)

```json
{
  "name": "CiteVista - AI Citation Tracker",
  "nodes": [
    {
      "type": "n8n-nodes-base.schedule",
      "parameters": { "rule": { "interval": [{ "field": "weeks", "weeksInterval": 1 }] } }
    },
    {
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.perplexity.ai/chat/completions",
        "method": "POST",
        "body": {
          "model": "llama-3.1-sonar-large-128k-online",
          "messages": [{ "role": "user", "content": "What is the best GEO agency in the UK?" }]
        }
      }
    },
    {
      "type": "n8n-nodes-base.code",
      "parameters": {
        "jsCode": "const response = $input.first().json;\nconst citations = response.citations || [];\nconst mentioned = citations.some(c => c.includes('rank4ai'));\nreturn [{ json: { query: 'best geo agency uk', cited: mentioned, citations } }];"
      }
    },
    {
      "type": "n8n-nodes-base.googleSheets",
      "parameters": { "operation": "append", "sheetId": "YOUR_SHEET_ID" }
    }
  ]
}
```

---

## JSON-LD Schema Templates (Copy-Paste Ready)

### FAQPage (Highest AI Citation Impact: 28-40% lift)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Generative Engine Optimization (GEO)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generative Engine Optimization (GEO) is the practice of optimizing website content to improve visibility and citation rates in AI-powered search engines like ChatGPT, Claude, Perplexity, and Google AI Overviews."
      }
    },
    {
      "@type": "Question",
      "name": "How does GEO differ from traditional SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "While traditional SEO optimizes for ranking positions in search results, GEO optimizes for being cited and referenced by AI systems when they generate answers to user queries."
      }
    }
  ]
}
```

### Article / BlogPosting

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Complete Guide to Generative Engine Optimization",
  "description": "Learn how to optimize your content for AI search engines.",
  "author": {
    "@type": "Person",
    "@id": "https://rank4ai.com/#adam-parker",
    "name": "Adam Parker",
    "url": "https://rank4ai.com/about",
    "sameAs": [
      "https://linkedin.com/in/adamparker",
      "https://twitter.com/adamparker"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://rank4ai.com/#organization"
  },
  "datePublished": "2026-04-01",
  "dateModified": "2026-04-24",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://rank4ai.com/blog/geo-guide"
  },
  "image": "https://rank4ai.com/images/geo-guide-hero.jpg",
  "wordCount": 3500
}
```

### Organization

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://rank4ai.com/#organization",
  "name": "Rank4AI Ltd",
  "url": "https://rank4ai.com",
  "logo": "https://rank4ai.com/logo.png",
  "description": "AI search optimization agency specializing in Generative Engine Optimization (GEO)",
  "foundingDate": "2025",
  "founder": {
    "@type": "Person",
    "@id": "https://rank4ai.com/#adam-parker"
  },
  "sameAs": [
    "https://linkedin.com/company/rank4ai",
    "https://twitter.com/rank4ai"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "email": "hello@rank4ai.com"
  }
}
```

### Person (Author)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://rank4ai.com/#adam-parker",
  "name": "Adam Parker",
  "jobTitle": "Founder",
  "worksFor": { "@id": "https://rank4ai.com/#organization" },
  "url": "https://rank4ai.com/about",
  "sameAs": [
    "https://linkedin.com/in/adamparker",
    "https://twitter.com/adamparker",
    "https://www.wikidata.org/wiki/QXXXXXXX"
  ],
  "knowsAbout": [
    "Generative Engine Optimization",
    "AI Search Optimization",
    "Answer Engine Optimization",
    "SEO"
  ]
}
```

### BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://rank4ai.com" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://rank4ai.com/blog" },
    { "@type": "ListItem", "position": 3, "name": "GEO Guide", "item": "https://rank4ai.com/blog/geo-guide" }
  ]
}
```

### HowTo

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Implement llms.txt on Your Website",
  "description": "Step-by-step guide to adding llms.txt for AI search optimization.",
  "totalTime": "PT30M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Create the llms.txt file",
      "text": "Create a markdown file at /llms.txt with your site name, description, and links to key pages."
    },
    {
      "@type": "HowToStep",
      "name": "Add page descriptions",
      "text": "List your most important pages with brief descriptions that help AI systems understand your content."
    },
    {
      "@type": "HowToStep",
      "name": "Deploy and verify",
      "text": "Upload to your site root and verify access at https://yoursite.com/llms.txt"
    }
  ]
}
```

### Full @graph Pattern (Linked Entities)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://rank4ai.com/#website",
      "name": "Rank4AI",
      "url": "https://rank4ai.com",
      "publisher": { "@id": "https://rank4ai.com/#organization" }
    },
    {
      "@type": "Organization",
      "@id": "https://rank4ai.com/#organization",
      "name": "Rank4AI Ltd",
      "url": "https://rank4ai.com",
      "logo": "https://rank4ai.com/logo.png"
    },
    {
      "@type": "WebPage",
      "@id": "https://rank4ai.com/blog/geo-guide/#webpage",
      "url": "https://rank4ai.com/blog/geo-guide",
      "isPartOf": { "@id": "https://rank4ai.com/#website" }
    },
    {
      "@type": "BlogPosting",
      "mainEntityOfPage": { "@id": "https://rank4ai.com/blog/geo-guide/#webpage" },
      "headline": "Complete Guide to GEO",
      "author": { "@id": "https://rank4ai.com/#adam-parker" },
      "publisher": { "@id": "https://rank4ai.com/#organization" },
      "datePublished": "2026-04-01",
      "dateModified": "2026-04-24"
    },
    {
      "@type": "Person",
      "@id": "https://rank4ai.com/#adam-parker",
      "name": "Adam Parker",
      "jobTitle": "Founder",
      "worksFor": { "@id": "https://rank4ai.com/#organization" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://rank4ai.com" },
        { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://rank4ai.com/blog" },
        { "@type": "ListItem", "position": 3, "name": "GEO Guide" }
      ]
    }
  ]
}
```

---

## Awesome List Submission Formats

### Submitting to awesome-generative-engine-optimization

```markdown
<!-- PR Title: Add Rank4AI -->
<!-- PR Body: -->
## What is Rank4AI?
Rank4AI is a GEO agency specializing in AI search optimization for B2B SaaS companies.

## Why should it be included?
- Specializes in Generative Engine Optimization
- Open-source contributions to the GEO ecosystem
- Active in the AI search optimization community

<!-- Entry format (add in alphabetical order): -->
- [Rank4AI](https://rank4ai.com) - AI search optimization agency specializing in GEO for B2B SaaS.
```

### Submitting to awesome-llms-txt

```markdown
<!-- PR Title: Add rank4ai.com llms.txt -->
<!-- Entry format: -->
- [Rank4AI](https://rank4ai.com/llms.txt) - AI search optimization agency.
```

### Submitting to llmstxt.directory

```markdown
<!-- Submit via PR or web form -->
Site: rank4ai.com
llms.txt URL: https://rank4ai.com/llms.txt
Category: Marketing / SEO
Description: AI search optimization agency
```

---

*Compiled for Rank4AI Ltd. Last updated: April 2026.*
