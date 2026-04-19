# DirectorCover — Site Build Spec ("Perfect at Launch")

*What the site has to be on Day 1 for Phase 1 to start compounding.*

---

## 1. Definition of "Perfect at Launch"

A DirectorCover launch is "perfect" when every one of the following is true on Day 1:

- Entity, compliance, and legal foundations are fully in place.
- Site architecture is live with both sides, journal, directory, compare layer, tools, glossary, and legal pages.
- Minimum content inventory is published (at least 20 product explainers + 10 problem-led pages + 5 journal pieces).
- Every page carries a regulation tag (🟢🟡🟠🔴) and a disclaimer link.
- Schema is complete and matches visible text (Signal 03).
- Layer B directory shell is live with at least 5 vetted brokers on each side.
- Layer C compare widgets are live on at least one page per side (see `04-activequote-integration.md` for the Side 2 ActiveQuote plan).
- Newsletter signup is functional and tagged by entry point.
- Named author pages are live with `Person` schema + LinkedIn links.
- Analytics, consent, cookie banner, lead tracking, and AI referral tracking are working.
- `llms.txt`, `robots.txt`, `sitemap.xml` published.
- AI-visibility baseline benchmark recorded.
- Trust signals present — Companies House filed, Wikidata claimed, LinkedIn company page live, Trustpilot account set up.

Nothing below here contradicts those — it operationalises them.

---

## 2. Full Site Wireframe

```
DIRECTORCOVER.CO.UK
│
├── /                                        HOME
│   • 4-register hero, two-side split, popular guides, tools, find-broker | compare
│
├── /business-insurance/                     SIDE 1 — Commercial GI
│   ├── public-liability/
│   │   ├── what-is-public-liability-insurance
│   │   ├── how-much-public-liability-cover-do-i-need
│   │   ├── public-liability-for-consultants
│   │   ├── public-liability-for-trades
│   │   ├── public-liability-for-home-based-business
│   │   └── compare / find-a-broker
│   ├── employers-liability/
│   │   ├── what-is-employers-liability-insurance
│   │   ├── minimum-5m-cover-explained
│   │   ├── do-i-need-el-if-only-contractors
│   │   ├── el-for-one-person-ltd
│   │   └── compare / find-a-broker
│   ├── professional-indemnity/
│   │   ├── what-is-pi-insurance
│   │   ├── pi-for-consultants
│   │   ├── pi-for-tech-and-saas
│   │   ├── pi-claims-made-vs-occurrence
│   │   ├── pi-run-off-cover
│   │   └── compare / find-a-broker
│   ├── directors-and-officers/
│   │   ├── what-does-d-and-o-actually-cover
│   │   ├── what-d-and-o-does-not-cover   (wrongful trading etc)
│   │   ├── d-and-o-for-startups-with-investors
│   │   ├── side-a-side-b-side-c-explained
│   │   └── compare / find-a-broker
│   ├── cyber/
│   │   ├── what-is-cyber-insurance
│   │   ├── ransomware-and-business-interruption
│   │   ├── cyber-for-data-heavy-businesses
│   │   ├── cyber-for-saas-companies
│   │   ├── first-party-vs-third-party-cyber
│   │   └── compare / find-a-broker
│   ├── business-interruption/
│   ├── contents-and-equipment/
│   ├── product-liability/
│   ├── legal-expenses/
│   └── commercial-property/
│
├── /director-protection/                    SIDE 2 — Life & Protection
│   ├── relevant-life/
│   │   ├── what-is-a-relevant-life-policy
│   │   ├── relevant-life-for-sole-director
│   │   ├── relevant-life-vs-death-in-service
│   │   ├── relevant-life-trust-explained
│   │   ├── hmrc-anderson-rules-and-relevant-life
│   │   ├── relevant-life-for-llp-members
│   │   └── compare / find-a-broker      ← ACTIVEQUOTE integration (see 04)
│   ├── key-person/
│   │   ├── what-is-key-person-cover
│   │   ├── how-much-key-person-cover-do-i-need
│   │   ├── key-person-for-tech-founders
│   │   ├── key-person-tax-treatment-bim45525
│   │   └── compare / find-a-broker
│   ├── shareholder-protection/
│   │   ├── what-is-shareholder-protection
│   │   ├── company-owned-vs-own-life-in-trust
│   │   ├── cross-option-agreements-explained
│   │   ├── shareholder-protection-for-property-spv
│   │   ├── shareholder-protection-and-emi-schemes
│   │   └── compare / find-a-broker
│   ├── partnership-protection/
│   │   ├── llp-partnership-protection
│   │   ├── general-partnership-protection
│   │   ├── dental-and-gp-practice-partnerships
│   │   ├── scottish-partnerships
│   │   └── compare / find-a-broker
│   ├── income-protection/
│   │   ├── executive-income-protection
│   │   ├── ip-for-directors-on-dividends
│   │   ├── ip-for-self-employed-vs-ltd
│   │   └── compare / find-a-broker       ← ACTIVEQUOTE integration
│   ├── critical-illness/
│   │   ├── what-is-critical-illness-cover
│   │   ├── ci-payout-claims-stats
│   │   └── compare / find-a-broker       ← ACTIVEQUOTE integration
│   ├── director-life-insurance/
│   │   ├── personal-life-insurance-vs-relevant-life
│   │   └── compare / find-a-broker       ← ACTIVEQUOTE integration
│   └── personal-guarantee-cover/
│       ├── what-is-personal-guarantee-insurance
│       ├── how-pg-cover-protects-the-family-home
│       └── compare / find-a-broker
│
├── /guides/                                 CROSS-CUTTING (problem-led, 🟢)
│   ├── director-insurance-checklist
│   ├── what-insurance-does-a-uk-ltd-company-need
│   ├── insurance-by-business-type/
│   │   ├── consultants
│   │   ├── tech-and-saas
│   │   ├── agencies
│   │   ├── ecommerce
│   │   ├── property-spv-landlords
│   │   ├── professional-practices
│   │   └── startups-with-investors
│   └── insurance-by-business-stage/
│       ├── pre-revenue-startup
│       ├── first-employee
│       ├── series-a
│       └── exit-and-succession
│
├── /journal/                                TRUST CONTENT (35% allocation)
│   ├── /incidents/
│   ├── /regulation/
│   ├── /case-analysis/
│   ├── /claims-data/
│   ├── /interviews/
│   └── /myths/
│
├── /find-a-broker/                          LAYER B — DIRECTORY
│   ├── /commercial/
│   │   ├── /by-region/{london, manchester, ...}
│   │   ├── /by-specialism/{pi, d-and-o, cyber, ...}
│   │   └── /by-business-type/{tech, agency, trade, ...}
│   ├── /protection/
│   │   ├── /by-region/...
│   │   ├── /by-specialism/{relevant-life, shareholder, key-person, ...}
│   │   └── /by-business-type/...
│   └── /broker-profile/{slug}/
│
├── /compare/                                LAYER C — WHITE-LABEL
│   ├── /business-insurance/
│   │   ├── /public-liability/
│   │   ├── /professional-indemnity/
│   │   ├── /d-and-o/
│   │   └── /cyber/
│   └── /director-protection/
│       ├── /relevant-life/                  ← ACTIVEQUOTE
│       ├── /critical-illness/               ← ACTIVEQUOTE
│       ├── /income-protection/              ← ACTIVEQUOTE
│       ├── /life-insurance/                 ← ACTIVEQUOTE
│       ├── /key-person/                     (different partner — advised)
│       └── /shareholder-protection/         (different partner — advised)
│
├── /tools/
│   ├── what-cover-do-i-need/  (quiz → routes to S1, S2, or both)
│   ├── relevant-life-savings-calculator
│   ├── key-person-cover-calculator
│   └── shareholder-protection-cover-calculator
│
├── /glossary/                               4-REGISTER REFERENCE
│
├── /about/
│   ├── /how-we-make-money/
│   ├── /our-editorial-policy/
│   ├── /authors/{founder, guest contributors}
│   ├── /our-broker-vetting-policy/
│   └── /careers/
│
├── /about-this-information/                 CANONICAL DISCLAIMER
├── /compliance-and-approvals/
│   ├── /financial-promotions-approver/
│   ├── /complaints/
│   ├── /accessibility-statement/
│   └── /vulnerable-customer-policy/
├── /privacy/
├── /cookies/
├── /terms/
└── /sitemap.xml  +  /robots.txt  +  /llms.txt
```

---

## 3. User Flow Map (How Traffic Moves to Revenue)

```
AI SEARCH / GOOGLE
"what happens if my business partner dies"
        │
        ▼
/journal/incidents/business-partner-died-without-cover
(problem-led, layman's H1, RAG-extractable)
        │
        ▼
/director-protection/shareholder-protection/
(product explainer, 4 registers, schema-marked)
        │
        ├──→ /find-a-broker/protection/by-specialism/shareholder  (LAYER B)
        └──→ /compare/director-protection/shareholder-protection/ (LAYER C)

Trust loop feeds both: /journal/case-analysis/  +  /journal/claims-data/
Owned audience: newsletter capture at every step (transferable to Phase 2)
```

---

## 4. Launch Readiness Checklist

### Entity & legal

- [ ] DirectorCover Ltd registered at Companies House (Registered Entity alignment for Signal 01)
- [ ] Trademark filed: Class 35 (advertising/directory), Class 36 (insurance/financial), Class 41 (publishing)
- [ ] Domain portfolio: `.co.uk`, `.com`, `.uk` defensively
- [ ] ICO registration as data controller (Fee Band A)
- [ ] Privacy policy, cookie policy, PECR-compliant opt-in mechanics
- [ ] Terms of use, accessibility statement, complaints policy, vulnerable-customer policy
- [ ] Signed s.21 financial promotions approver contract in hand (external approver or via Layer C partner)
- [ ] DirectorCover's own PI + cyber insurance bought and active
- [ ] `/about-this-information/` canonical disclaimer page live and linked from every footer

### Compliance governance artefacts

- [ ] Evidence Register spreadsheet set up with review workflow
- [ ] Tone-of-voice guideline (including vulnerable-customer handling)
- [ ] Complaints handling process documented
- [ ] Regulation-tag policy (🟢🟡🟠🔴) embedded in CMS workflow
- [ ] Financial promotion approval log (every 🟡 page with date, approver, review date)

### Site & technical

- [ ] Framework / CMS chosen and deployed (recommendation: Astro + Sanity, or Webflow + Sanity, or Ghost for journal + custom product pages)
- [ ] Site theme built — editorial feel, mobile-first, WCAG 2.2 AA compliant
- [ ] Core Web Vitals passing: LCP < 2.5s, INP < 200ms, CLS < 0.1
- [ ] Internal site search working
- [ ] Sitemap XML generated, robots.txt reviewed, `llms.txt` published with canonical URLs + identity statement
- [ ] 301 redirect policy in place for any URL changes post-launch
- [ ] HTTPS with HSTS, HTTP/2 or HTTP/3
- [ ] CDN + UK data residency for analytics/logs
- [ ] Automated backups

### Schema stack (all pages)

- [ ] `Organization` site-wide with `knowsAbout` listing product areas
- [ ] `WebPage` + `Article` on guides
- [ ] `FAQPage` on every Q&A block
- [ ] `HowTo` on decision tools and calculators
- [ ] `ItemList` + `LocalBusiness` on directory listings
- [ ] `Person` + `author` on every article
- [ ] `Dataset` on any original aggregated data (e.g. broker coverage map)
- [ ] Visible text matches schema content exactly (Signal 03)
- [ ] `datePublished` and `dateModified` on every article

### Content inventory (minimum at launch)

- [ ] 10 Side 1 product explainer pages (one per GI product)
- [ ] 10 Side 2 product explainer pages (one per protection product)
- [ ] 10 problem-led cross-cutting pages (the priority list in the strategic plan)
- [ ] 5 journal pieces (mix: 1 incident, 1 regulation decode, 1 case analysis, 1 claims-data, 1 myth-buster)
- [ ] Glossary page (one page mapping formal ↔ SEO ↔ AI ↔ layman for all products)
- [ ] "What cover do I need?" quiz tool live
- [ ] Author page for founder with CII plan + LinkedIn + photo
- [ ] Guest author pages for at least one external contributor if secured
- [ ] Every page tagged 🟢 / 🟡 / 🟠

### Layer B — directory

- [ ] Directory schema (broker profile template) built
- [ ] At least 5 vetted brokers listed per side (10 total minimum)
- [ ] FCA Register cross-check process for every listed broker
- [ ] Listing contract template with flat-fee terms + 90-day change notice clause
- [ ] Broker application page live

### Layer C — comparison

- [ ] ActiveQuote partnership signed (see `04-activequote-integration.md`) — at least one compare widget live
- [ ] Side 1 Layer C partner contacted and terms in negotiation (Simply Business / Superscript / affiliate alternative acceptable at launch)
- [ ] Tracking parameters passed to partner + attribution back to DirectorCover

### Analytics & measurement

- [ ] GA4 with consent mode v2
- [ ] Server-side tracking (recommended: Stape or Cloudflare Workers)
- [ ] Cookie banner (Cookiebot / Osano / CookieYes)
- [ ] Event taxonomy: page_view, outbound_broker_click, compare_widget_start, compare_widget_complete, newsletter_signup, contact_broker, quiz_complete
- [ ] AI referral tracking set up (capture `Referer` from AI platforms where available + UTM tagging on any placements)
- [ ] Lead tracking: Contact State-style ID on every outbound broker referral
- [ ] Dashboard set up (Looker Studio or similar) with daily refresh

### Email / owned audience

- [ ] Newsletter platform live (Ghost, Beehiiv, ConvertKit, or equivalent)
- [ ] Double opt-in flow
- [ ] Signup CTAs on every page (footer minimum; inline on guides)
- [ ] Welcome sequence (3–5 emails)
- [ ] Tagging by entry point for future segmentation

### Trust signals / Signal 04 priming

- [ ] LinkedIn company page live with consistent entity description
- [ ] Founder LinkedIn bio updated with DirectorCover
- [ ] Trustpilot account claimed for DirectorCover entity
- [ ] Wikidata entry claimed and populated
- [ ] Crunchbase entry
- [ ] OpenCorporates record
- [ ] Companies House public description aligned with site tagline
- [ ] At least 3 outbound links to HMRC / ABI / FCA / legislation.gov.uk per long-form page

### AI-search readiness

- [ ] `llms.txt` published with: (a) one-paragraph identity statement, (b) canonical URLs for the 20 priority Q&A pages, (c) contact email
- [ ] Baseline AI-visibility benchmark recorded before launch — the 8 prompts run across Claude, ChatGPT, Gemini, Perplexity, Google AIO with scores noted (Inclusion Rate, Citation Frequency, Sentiment Alignment, Misclassification Rate)
- [ ] Sitemap submitted to Google Search Console + Bing Webmaster Tools
- [ ] IndexNow ping set up for new content (fast Bing indexing = fast ChatGPT / Copilot visibility)

---

## 5. Technical Stack Recommendation

For fastest defensible launch:

| Layer | Recommended | Alternative |
|---|---|---|
| Framework / CMS | Astro + Sanity (headless) | Webflow + Sanity; or Ghost (journal) + Next.js (product pages) |
| Hosting | Vercel or Netlify | Cloudflare Pages |
| Newsletter | Ghost (if using Ghost for journal) | Beehiiv, ConvertKit |
| Analytics | GA4 + Stape (server-side) | Plausible for privacy-light deployment |
| Cookie banner | CookieYes | Cookiebot, Osano |
| Schema | `schema-dts` typings if using TS, or Sanity schemas with JSON-LD embedders | Manual JSON-LD blocks |
| Search | Algolia DocSearch or Pagefind (static) | Native Sanity search |
| Directory | Custom build on Sanity | Directorist (WordPress) if you pivot to WP |
| Forms / lead capture | Formspree, Basin, or native (Sanity actions) | Typeform for quiz |
| Monitoring | Sentry (errors) + Better Uptime (availability) | Cronitor |

---

## 6. Page Template (Signal 03-compliant)

Every product page and problem-led page uses this skeleton:

```
[H1] — Layman's term or problem phrasing
    "The director's life hack: when can your company pay your life insurance?"

[Lead paragraph — 100–150 words]
    Primary answer. No pronouns. Full entity names.
    "A relevant life policy is a single-life, term-only life insurance policy
     paid for by a UK limited company on behalf of a director or employee..."

[Disclaimer inline block]
    "This is general information, not regulated financial advice — [read more]"

[H2 — SEO register]
    "What is a relevant life policy in the UK?"
    [200–500 token passage]

[H2 — AI-search register]
    "Can a UK limited company pay for your life insurance?"
    [200–500 token passage]

[H2 — further sub-questions in conversational phrasing]
    Each with a 200–500 token passage.

[FAQ block — FAQPage schema]
    Q: Who can take out a relevant life policy?
    Q: Is the premium tax-deductible?
    Q: Does it pay into a trust?
    (etc.)

[Sources block]
    Outbound links to HMRC BIM, legislation.gov.uk, ABI.

[Evidence stamp]
    "Last reviewed [date] · Author: [name] · Sources: [count]"

[CTA block — ONE product + two routes]
    "Find a broker who specialises in relevant life"  →  Layer B
    "Compare relevant life policies"                   →  Layer C
```

---

## 7. Gap Items — Confirm Before Launch

- Final brand name (lock `DirectorCover` or pivot)
- Layer C partner agreement for Side 1 (Simply Business / Superscript / other)
- Named editor / compliance reviewer in post
- First guest author secured
- Budget and runway confirmed
- Investment posture decided (bootstrap / friends-and-family / seed)
- Media-first vs insurance-first posture formally committed

See `01-strategic-plan.md` §15 for the full open-decisions list.
