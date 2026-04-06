# Technical Build Guide
## Astro + Cloudflare + 301 Redirects + Operations

Generated: 2026-04-06

---

# PART 1: BUILDING ON ASTRO + CLOUDFLARE

## Why Astro (Not WordPress)

| Factor | Astro | WordPress |
|--------|-------|-----------|
| Page speed (Lighthouse mobile) | 95-100 typical | 50-75 typical |
| TTFB | <200ms from CDN | 500ms-2s |
| Security | No server, no database, no attack surface | Constant patching, plugin vulnerabilities |
| Hosting cost | FREE (Cloudflare Pages) | £10-50/month minimum |
| Maintenance | Near zero | Ongoing updates required |
| JavaScript shipped | Zero by default | jQuery + theme + plugins on every page |
| Core Web Vitals | Excellent out of box | Requires optimisation effort |

Zero JavaScript by default = Google crawler sees fully-rendered content immediately. No render-blocking scripts. Perfect for SEO-heavy comparison sites.

## Hosting: Cloudflare Pages (Free)

- Unlimited bandwidth, 500 builds/month free
- UK edge servers (London, Manchester, Edinburgh) = sub-50ms TTFB
- Handles BOTH site hosting AND 301 redirects from aged domains
- SSR via Cloudflare Workers for form submissions
- **Cost: £0/month**

## Site Architecture

```
src/
├── components/
│   ├── ComparisonTable.tsx      # React island — sortable/filterable
│   ├── QuoteForm.tsx            # React island — multi-step form
│   ├── Calculator.tsx           # React island — cost calculator
│   ├── Schema.astro             # JSON-LD schema component
│   ├── SEOHead.astro            # Meta tags, canonical, OG
│   └── ProviderCard.astro       # Static provider summary card
├── content/
│   ├── providers/               # JSON files per provider
│   ├── reviews/                 # Markdown reviews
│   ├── guides/                  # Markdown/MDX guides
│   └── config.ts                # Content collection schemas
├── data/
│   ├── uk-cities.json           # For programmatic location pages
│   └── categories.json          # Comparison categories
├── layouts/
│   └── BaseLayout.astro         # Common layout with analytics, nav, footer
├── pages/
│   ├── index.astro
│   ├── [category]/
│   │   ├── index.astro          # Category comparison page
│   │   └── [provider].astro     # Individual provider page
│   ├── guides/
│   │   └── [...slug].astro      # Guide pages from content collection
│   └── api/
│       └── submit-quote.ts      # Form submission endpoint (SSR)
└── styles/
    └── global.css
```

## Astro Config

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import partytown from '@astrojs/partytown';

export default defineConfig({
  site: 'https://www.yoursite.co.uk',
  output: 'hybrid',           // Static by default, SSR for form endpoints
  adapter: cloudflare(),
  integrations: [sitemap(), mdx(), tailwind(), partytown()],
});
```

## Key Integrations

| Integration | Purpose |
|------------|---------|
| `@astrojs/sitemap` | Auto-generates XML sitemap at build time |
| `@astrojs/mdx` | Markdown + components for content pages |
| `@astrojs/tailwind` | Tailwind CSS |
| `@astrojs/cloudflare` | Cloudflare Pages adapter for SSR endpoints |
| `@astrojs/partytown` | Moves analytics scripts to web worker (better CWV) |
| `astro-seo` | Meta tags, Open Graph component |
| `astro-robots-txt` | Generates robots.txt |
| `schema-dts` | Type-safe JSON-LD schema definitions |

## Schema Markup (Reusable Component)

Create `src/components/Schema.astro`:
```astro
---
const { schema } = Astro.props;
---
<script type="application/ld+json" set:html={JSON.stringify(schema)} />
```

Use on every page:
```astro
---
import Schema from '../components/Schema.astro';

const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": faqs.map(faq => ({
    "@type": "Question",
    "name": faq.question,
    "acceptedAnswer": { "@type": "Answer", "text": faq.answer }
  }))
};
---
<Schema schema={faqSchema} />
```

**Every page needs minimum:** FAQPage + Article + BreadcrumbList. This is what every winning niche site uses.

## Content Collections for Comparison Data

Define typed schemas in `src/content/config.ts`:
```typescript
import { defineCollection, z } from 'astro:content';

const providers = defineCollection({
  type: 'data',
  schema: z.object({
    name: z.string(),
    slug: z.string(),
    category: z.enum(['invoice-finance', 'business-loans', 'green-energy', 'health']),
    rating: z.number().min(0).max(5),
    minRate: z.string(),
    maxRate: z.string(),
    features: z.array(z.string()),
    pros: z.array(z.string()),
    cons: z.array(z.string()),
    logo: z.string(),
    lastUpdated: z.coerce.date(),
  })
});

export const collections = { providers };
```

Editors update JSON files in `src/content/providers/`. Build-time validation catches errors.

## Content Editing: Keystatic CMS (Free)

For non-technical editors:
- **Keystatic** = Git-based CMS with admin UI
- Editors update comparison data through a web interface at `/keystatic`
- Content stored as files in your repo (version controlled)
- No external service, no vendor lock-in, free and open source
- Works natively with Astro Content Collections

## Lead Capture Forms (Astro Islands)

Multi-step forms built as React/Svelte components, hydrated independently:

```astro
---
import QuoteForm from '../components/QuoteForm.tsx';
---
<QuoteForm client:load />
```

Only the form loads JavaScript. Rest of page = static HTML, zero JS.

Form submissions go to Astro API endpoint (SSR on Cloudflare Workers) → CRM (HubSpot, Pipedrive) or email/Google Sheets.

**Research finding:** Multi-step forms (4-6 steps) convert 86-300% better than single forms. Promise "up to 3-4 free quotes." Suppress phone numbers to force form completions.

## Comparison Tables

Use React/Svelte Island with `client:visible` for sortable/filterable tables:

```astro
---
import ComparisonTable from '../components/ComparisonTable.tsx';
import { getCollection } from 'astro:content';
const providers = await getCollection('providers');
---
<ComparisonTable client:visible providers={providers.map(p => p.data)} />
```

Data fetched at build time, component hydrates only when user scrolls to it.

## Programmatic Page Generation

Generate hundreds of pages from data using `getStaticPaths()`:

```astro
---
// src/pages/providers/[slug].astro
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const providers = await getCollection('providers');
  return providers.map(p => ({
    params: { slug: p.data.slug },
    props: { provider: p.data },
  }));
}
const { provider } = Astro.props;
---
<h1>{provider.name} Review</h1>
```

Same pattern for `[treatment]-in-[city].astro` location pages (what WhatClinic, Checkatrade, Bark all do to generate thousands of indexed pages).

## Analytics

**GA4:** Use Partytown to offload to web worker:
```html
<script type="text/partytown" src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
```

**Microsoft Clarity (free):** Add script tag in base layout. Free heatmaps and session recordings.

---

# PART 2: 301 REDIRECT TECHNICAL SETUP

## The Cloudflare Free Method (2 Minutes Per Domain)

**Step 1:** Add aged domain to Cloudflare (free plan)

**Step 2:** Update nameservers at registrar to Cloudflare's

**Step 3:** Add DNS records:
- A record: `@` → `192.0.2.1` (dummy IP, orange cloud proxy ON)
- CNAME: `www` → `oldsite.co.uk` (orange cloud ON)

**Step 4:** Go to Rules → Redirect Rules → Create rule:
- If: All incoming requests
- Then: Static URL redirect → `https://www.yournewsite.co.uk` → Status **301**

**Step 5:** Verify: `curl -I http://oldsite.co.uk` — should see `301 Moved Permanently`

**No hosting needed. Free forever. 2 minutes setup.**

## How Many 301s Per Site?

| Number | Risk Level |
|--------|-----------|
| 1-3 | Very low — looks like normal business consolidation |
| 4-7 | Low — still plausible |
| 8-15 | Moderate — ensure all topically relevant |
| 15-30 | Higher — likely triggers review |
| 30+ | Risky |

**Start with 2-3** in first 3 months. Add 1-2 more every 2-3 months. Cap at 8-10 per site.

**Stagger setup** — don't redirect 5 domains on the same day. Space 2-4 weeks apart.

## Critical Rules

1. **Always use 301** (not 302) — verify with `curl -I`
2. **Redirect ALL variants** — http, https, www, non-www
3. **No redirect chains** — A→B→C loses equity. Go A→C directly
4. **Check Wayback Machine** for spam/adult history before buying
5. **Audit backlinks** in Ahrefs/Moz — toxic profiles import penalties
6. **Keep redirects active forever** — £5/yr per domain is worth it
7. **Use GSC Change of Address tool** — speeds up equity transfer (takes 3-6 months for full transfer)
8. **Domains must be relevant** to destination site — factoring → factoring comparison = safe

## Google Processing Timeline

- Discovery: 1-4 weeks
- Full equity transfer: 3-6 months
- Ranking changes visible: 2-8 weeks
- Keep redirect active: minimum 1 year, ideally forever

---

# PART 3: WHAT THE TOP NICHE SITES DO (Competitor Cheat Sheet)

## Content Patterns That Work

1. **Cost/price guide pages** = #1 format. 3,000-4,500 words with tables, FAQs, expert bylines. (The Eco Experts, Heatable, Rated People)
2. **"X vs Y" comparison pages** — "Funding Circle vs iwoca", "Heat Pumps vs Gas Boilers". Big sites ignore these.
3. **Industry-specific pages** — "Best Lenders for Recruitment Agencies" — zero competition from MoneySupermarket
4. **Calculator/tool pages** — cost calculators, eligibility checkers. AI can't replicate = forces clicks
5. **Programmatic location pages** — `[service]-in-[city]` generates thousands of pages (WhatClinic, Checkatrade, Bark)

## Schema Markup (Universal Across Successful Sites)

| Site | Schema Types |
|------|-------------|
| The Eco Experts | Article, FAQPage, BreadcrumbList, Organization, Person, VideoObject |
| Heatable | FAQPage (8 Q&As), Article, Organization |
| iwoca | Product, AggregateRating (4.8/5, 5,895 reviews), Review |
| Invoice-funding.co.uk | Organization, FAQPage (4 Q&As), WebPage |
| Funding Agent | Organization, FAQPage, BreadcrumbList, FundingAgency |
| WhatClinic | Organization, AggregateRating, ServiceScore |

**FAQPage schema = the single most common type.** Used by virtually every site studied.

## Lead Capture Patterns

- Multi-step forms (4-6 steps): Heatpumps.co.uk uses 6 steps
- Promise "up to 3-4 free quotes"
- Suppress phone numbers — force form completions
- CTA above fold + sticky + inline throughout page
- WhatsApp emerging as booking channel (Treatwell)

## Trust Signals (Even Small Sites)

- Trustpilot rating on every page (iwoca 4.8/5, Heatable 4.9/5)
- "As featured in" media logos (Guardian, Telegraph, BBC)
- Named author with registration numbers (Gas Safe, MCS, FCA)
- "More than X homeowners helped" social proof
- Free tools as trust builders (calculators, eligibility checkers)

## Monetisation Models

| Model | Example | Revenue |
|-------|---------|---------|
| Pay per lead (shared) | Boiler Guide, GreenMatch | £30-50/lead |
| Credit-based | Bark | £6-60 per response |
| Commission | Treatwell | 35% first booking, 0% repeats |
| Subscription | Checkatrade, Rated People | £30-180/month |
| Affiliate | FundInvoice | Commission on placements |

## AI Overview Tactics

- **59.6% of AI citations** come from URLs NOT in top 20 organic — niche sites have a real shot
- **44.2% of citations** come from first 30% of page text — front-load answers
- Pages not updated in 3+ months are **3x more likely to lose AI visibility**
- Definition-first sections, question-as-heading format, neutral factual language

---

# PART 4: LEGAL/COMPLIANCE (UK)

## FCA (Financial Conduct Authority)

If comparing FCA-regulated products (loans, insurance, credit):
- May need FCA authorisation or Appointed Representative status
- All financial promotions must be "fair, clear, not misleading"
- **Budget £500-1,500 for solicitor consultation — not optional**

## GDPR

- Register with ICO: **£40/year** for small sites
- Cookie consent must be **opt-in** (not just a notification banner)
- Data Processing Agreements with all third parties
- Right to deletion — must delete user data on request

## ASA (Advertising Standards Authority)

- All comparison content earning commission = advertising
- Must label clearly: "affiliate", "sponsored", "ad"
- "Best" and "cheapest" claims must be provable with evidence

## Must-Have Pages Before Launch

| Page | Why |
|------|-----|
| Privacy Policy | GDPR legal requirement |
| Terms and Conditions | Limit liability |
| Cookie Policy + consent banner | UK PECR regulations |
| "How We're Funded" | ASA requirement for comparison sites |
| About Us | E-E-A-T — real names, photos, credentials |
| Contact Us | Address, email, phone — Google Quality Rater Guidelines |
| Editorial Policy / How We Review | E-E-A-T + ASA compliance |
| Disclaimer | Especially for financial content |

---

# PART 5: DAILY/WEEKLY/MONTHLY OPERATIONS

## Automated (Set and Forget)

| Task | Tool | Cost |
|------|------|------|
| Site backups | Git-based (Astro = files in repo) | Free |
| Uptime monitoring | UptimeRobot | Free (50 monitors) |
| Form → CRM | Zapier / Make.com | Free tier / £9/mo |
| Social posting | Blog2Social | Free / £5/mo |
| Security | Static site = no attack surface | Free |
| Rank tracking | SERPRobot | Free (5 keywords) |
| Backlink monitoring | Ahrefs Alerts / Monitor Backlinks | Free tier |
| Competitor changes | Visualping | Free (5 pages) |

## Weekly Schedule

| Day | Task | Manual/Auto |
|-----|------|-------------|
| Monday | Write 1 comparison/guide page (AI-assisted, human-reviewed) | Manual |
| Tuesday | Publish → triggers automation | Semi-auto |
| Wednesday | Review auto-generated video (YouTube = Rank4AI stack) | Manual review |
| Thursday | LinkedIn post (convert page highlights to post) | Manual |
| Friday | Engage on Reddit (genuine, not spam) | Manual |

## Monthly Tasks

- [ ] Update all comparison tables with current rates
- [ ] Add "Last updated: [month] 2026" to all pages
- [ ] Check AI Overview citations (Semrush AI Visibility or Otterly.ai)
- [ ] Run RDAP checker on snipe list domains
- [ ] Review lead capture form conversion rates
- [ ] Check competitor content changes (Visualping)
- [ ] Review which pages are getting GSC impressions — double down on those topics

## LinkedIn Manual Repurposing Checklist

For each new comparison page published:
1. Hook: surprising stat from the comparison ("63% of invoice finance providers charge under 2%")
2. 3-5 bullet takeaways
3. CTA: "Full comparison with rates at [link]"
4. Tag relevant industry connections
5. Post Tuesday-Thursday, 8-10am UK time

**YouTube/Podcasts** = covered by Rank4AI stack. No duplication needed.

---

# PART 6: FIRST-YEAR COST SUMMARY

| Item | Cost |
|------|------|
| Domains (.co.uk registration, ~20 domains) | £100-150 total |
| Cloudflare Pages hosting | £0 |
| Cloudflare 301 redirects | £0 |
| Domain renewals (ongoing) | £100-150/year |
| Keystatic CMS | £0 (open source) |
| Astro + all integrations | £0 (open source) |
| ICO registration | £40/year |
| Semrush or SE Ranking (SEO tracking) | £250-600/year |
| Microsoft Clarity (heatmaps) | £0 |
| Zapier/Make.com (automation) | £0-108/year |
| Legal consultation (one-time) | £500-1,500 |
| Sniped domains (auction, if won) | £100-5,000+ each |
| **Total first year (DIY content)** | **~£1,000-2,500** |
| **Total first year (outsourced content)** | **~£3,000-15,000** |

---

# PART 7: LAUNCH TIMELINE

| Week | Action |
|------|--------|
| **1** | Register domains. Set up Cloudflare account. Init Astro project. |
| **2** | Build site structure, components, layouts. Deploy to Cloudflare Pages. |
| **3** | Create legal pages, about page, editorial policy. Set up GSC + Bing + GA4. |
| **4** | Publish first 3 comparison pages + 2 guides. Set up Keystatic for editors. |
| **5** | Buy first aged domain. Audit backlinks. Set up 301 via Cloudflare. Add to GSC. |
| **6-8** | Continue publishing 3-4 pages/week. Monitor GSC for first impressions. |
| **8-10** | Buy second aged domain if first showed positive signals. Start Reddit engagement. |
| **10-12** | Review analytics. Update comparison pages. Plan month 4-6 calendar. |
| **Month 4-6** | Scale to 5-8 pages/week. Add 1-2 more redirect domains. Start digital PR. |
| **Month 6-12** | Full content scaling. Regular freshness updates. Evaluate new verticals. |
