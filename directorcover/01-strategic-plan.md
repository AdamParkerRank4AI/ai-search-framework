# DirectorCover — Strategic Plan v1.0

*Master plan: product, positioning, brand, content, regulation, phasing, execution.*

---

## 1. One-Sentence Strategic Commit

DirectorCover is a UK director-insurance publisher and broker directory in Phase 1, built so that every decision — brand, content, partners, contracts, qualifications, and audience data — compounds into a regulated brokerage in Phase 2, without rupturing the entity AI platforms have come to trust.

---

## 2. Two-Phase Strategy

| Phase | Duration | Product | Revenue model | Regulatory status |
|---|---|---|---|---|
| **Phase 1** | Months 0–18 (gated) | UK director-insurance information publisher + broker directory + white-label comparison | Flat directory listing fees, flat per-lead fees, revenue share from Layer-C partner | Unregulated publisher (PERG 8.33 "mere introduction"), financial promotions approved by authorised s.21 partner |
| **Phase 2** | Month 18+ (gate-triggered) | FCA-authorised UK brokerage for director and business insurance, content engine and audience retained | Commission + fees on arranged policies, plus retained directory revenue | Directly FCA-authorised (or AR bridge), CII-qualified principal, SMCR, PI cover, Consumer Duty governance |

Precedent: NerdWallet, MoneySavingExpert, Which?, Cavendish Online, Money to the Masses.

---

## 3. Entity & Brand

**Working name:** DirectorCover

**What we do:**
*DirectorCover is the UK plain-English guide and broker directory for everything a limited company director needs to insure — themselves, their business, and the people in it.*

**Identity Clarity statement (homepage, About, schema, footer):**
*DirectorCover publishes information on UK director and business insurance and lists independent UK brokers who specialise in this area. In partnership with authorised firms we offer indicative product comparison. We are not **currently** an insurer, underwriter, or FCA-authorised firm, and we do not provide regulated financial advice.*

The word *currently* is deliberate — it preserves the Phase 2 pivot without a Signal 01 rupture.

**Brand elements that must hold across both phases:**

| Brand layer | Phase 1 | Phase 2 | Holds? |
|---|---|---|---|
| Name | DirectorCover | DirectorCover | Yes |
| Promise | "Know what cover you need." | "Know what cover you need. We'll arrange it." | Extends |
| Voice | Plain-English, opinionated, publisher | Plain-English, opinionated, broker | Yes |
| Visual system | Editorial (journal feel) | Editorial + transactional | Editorial base stays |
| Entity category | Publisher + broker directory | Authorised brokerage | Shifts |

---

## 4. Three-Layer Commercial Model

| Layer | Function | Regulatory status | Revenue |
|---|---|---|---|
| **A — Content & Authority** | Plain-English guides, Q&A pages, calculators (indicative only) | Unregulated if generic; s.21 approval required when provider-named | Indirect (drives B + C) |
| **B — Broker Directory** | Listings of UK brokers by specialism / region / firm size | Unregulated "mere introduction" (PERG 8.33) if fees are flat and non-contingent | Flat listing fees + flat per-lead fees |
| **C — Comparison / Quote** | Real-time product comparison with quote journeys | Regulated — white-labelled from authorised partners | Revenue share from partner |

**Contract rule:** No exclusivity, no non-compete in Layer C. Maximum 18-month initial term. Explicit exit on DirectorCover FCA authorisation.

---

## 5. Regulation Legend

| Tag | Meaning |
|---|---|
| 🟢 Unregulated | Generic educational content, no provider named, no comparison |
| 🟡 Financial Promotion | Names specific providers / products / prices → s.21 FSMA approval required |
| 🟠 Arranging | Real-time compare / quote / apply → white-label only |
| 🔴 Advising | Recommendation or suitability commentary → do not enter in Phase 1 |

**Disclaimer-by-link pattern:** one canonical `/about-this-information` page + persistent footer link + inline block. Satisfies ICOBS 2.2, Consumer Duty, CAP Code.

---

## 6. Site Architecture (high level)

Two vertical sides + cross-cutting hubs + journal + directory + compare + tools + legal.

- **/business-insurance/** — Side 1 Commercial GI (launch first, lower regulation)
- **/director-protection/** — Side 2 Life & Protection (launch second, higher regulation)
- **/guides/** — Cross-cutting problem-led and stage-led hubs
- **/journal/** — Trust / editorial content (35% allocation)
- **/find-a-broker/** — Layer B directory (Side 1 and Side 2 splits)
- **/compare/** — Layer C white-label comparison widgets
- **/tools/** — Calculators + "what cover do I need?" quiz
- **/glossary/** — 4-register reference (formal ↔ SEO ↔ AI ↔ layman)
- **/about/**, **/about-this-information/**, **/compliance-and-approvals/**, **/privacy/**, **/cookies/**, **/terms/**

Full wireframe tree in `02-site-build-spec.md`.

---

## 7. Product Matrix (4 Registers)

Each product is targeted across four linguistic registers simultaneously.

### Side 1 — Business Insurance (Commercial GI) · 🟢→🟠

| Product | SEO query | AI-search query | Layman's term |
|---|---|---|---|
| Public Liability | *public liability insurance small business* | "Do I need insurance if a client trips in my office?" | Visitor-and-bystander cover |
| Employers' Liability | *employers liability insurance* | "What insurance do I need when I hire my first employee?" | First-employee cover |
| Professional Indemnity | *professional indemnity insurance consultant* | "What if my advice costs my client money?" | Bad-advice cover |
| Directors & Officers | *directors and officers insurance UK* | "Can I be sued personally as a director?" | Personal director cover |
| Cyber | *cyber insurance small business* | "What do I do if my business gets hacked?" | Hack-and-ransomware cover |
| Business Interruption | *business interruption insurance UK* | "What happens if my business can't trade for a while?" | Lost-trade cover |
| Contents & Equipment | *business contents insurance* | "What if my laptop is stolen from the office?" | Kit-and-laptop cover |
| Product Liability | *product liability insurance UK* | "What if a product I sell harms someone?" | Faulty-product cover |
| Legal Expenses | *legal expenses insurance* | "How do I pay for lawyers if I get into a dispute?" | Lawyer-bill cover |
| Commercial Property | *commercial property insurance UK* | "What insurance do I need if I own my business premises?" | Own-the-building cover |

### Side 2 — Director Protection (Life & Protection) · 🟢→🟠

| Product | SEO query | AI-search query | Layman's term |
|---|---|---|---|
| Relevant Life | *relevant life policy* | "Can my company pay for my life insurance?" | Company-paid life cover |
| Key Person | *key person insurance UK* | "What happens to my business if I die or can't work?" | Founder-safety-net cover |
| Shareholder Protection | *shareholder protection insurance* | "What happens if my business partner dies?" | Partner-buyout cover |
| Partnership Protection | *partnership protection insurance* | "What happens to our partnership if a partner dies or leaves?" | Partner-exit cover |
| Executive Income Protection | *executive income protection* | "What if I can't work for months — how do I pay myself?" | Still-paid-if-I'm-off cover |
| Critical Illness | *critical illness cover UK* | "What happens financially if I get cancer or have a stroke?" | Serious-illness lump sum |
| Director Life Insurance | *life insurance UK director* | "How do I make sure my family is ok if I die?" | Family safety net |
| Personal Guarantee Cover | *personal guarantee insurance UK* | "What if I can't pay the personal guarantee I signed?" | PG safety net |

### Cross-Cutting Problem-Led Hubs · 🟢

| Theme | AI-search query | Layman's term |
|---|---|---|
| Whole-stack checklist | "What insurance does a UK Ltd company director need?" | The director insurance starter kit |
| First-employee event | "What insurance do I need when I hire my first employee?" | First-hire cover checklist |
| Investor round event | "What insurance do I need when I take on investors?" | Post-raise cover checklist |
| Consultant setup | "What insurance does a consultant through a Ltd need?" | Consultant cover checklist |
| SaaS setup | "What insurance does a UK SaaS startup need?" | SaaS cover checklist |
| Property SPV setup | "What insurance do I need for a property SPV Ltd?" | SPV landlord cover checklist |
| Business-partner event | "What happens if my business partner dies without cover?" | Partner-loss playbook |
| Personal-sue event | "I've been sued personally as a director — what now?" | The director's legal playbook |
| Ransomware event | "Our company just got hit by ransomware — what do we do?" | Ransomware first 24 hours |
| Serious-illness event | "If I get seriously ill, what happens to my Ltd?" | Founder-illness playbook |

---

## 8. Content Strategy

| Content type | Allocation | Purpose |
|---|---|---|
| Product explainers (formal register) | 25% | Own formal queries, schema targets, AI entity graph |
| Problem-led pages (SEO + AI register) | 25% | Top-of-funnel; incumbents weakest here |
| Cross-cutting / scenario hubs | 15% | Route mixed intent to right product |
| Trust / journal (35%) | 35% | Domain authority, E-E-A-T, AI citation, Signal 04 |

### Signal 03 page template

```
H1 — layman's term or problem phrasing
Lead paragraph (first 150 words) — primary answer, full entity names, no pronouns
H2 — SEO query phrasing
H2 — AI-search query phrasing
Body — 200–500 token passages with sub-question headings
FAQ block — FAQPage schema, conversational questions
Footer — disclaimer link + ONE product CTA + one layer routing
```

### Voice rules (journal/blog)

First person where possible · short opening sentence · varied sentence length · specific numbers over vague claims · one clear take per post · date + author + review stamp · no corporate hedging · outbound links to HMRC / ABI / FCA · entity density.

### Author strategy

Named primary author (founder) with full bio, photo, LinkedIn, `/author/[name]` page, `Person` + `author` schema. Guest contributors (broker, insolvency lawyer, accountant) widen Signal 04. Never publish under "Team" byline. Display CII qualifications as earned.

---

## 9. Stats and Evidence Discipline

Three regulatory layers apply: ICOBS 2.2 (fair/clear/substantiated), CAP Code 3.7 (documentary evidence held at publication), Consumer Duty (no selective presentation).

**Source hierarchy:**
- Tier 1 — ABI, FCA, PRA, HMRC manuals, ONS, Companies House, legislation.gov.uk
- Tier 2 — L&G, Aviva, Royal London, Vitality, Swiss Re, Zurich, LV= published research
- Tier 3 — FSB, Beazley, Coalition, Marsh specialist reports
- Tier 4 — FT Adviser / Cover Magazine / Money Marketing (as pointer to primary source)
- Tier 5 — never use competitor blogs or AI-generated stats as primary

**Evidence Register** — single spreadsheet: stat, source, URL, date captured, tax year if relevant, review date. Reviewed quarterly.

**Tax-year tags** on every tax fact.

---

## 10. AI-Search Specifics

**Schema stack:** Organization, WebPage, Article, FAQPage, HowTo, ItemList, LocalBusiness (directory), Person (authors). Visible text must match schema content exactly.

**Terminology lock (Signal 05):** one canonical term per product.

**Citation targets:** HMRC BIM outbound links, MoneyHelper inclusion, AccountingWEB / ICAEW / ACCA guest content, Law Society Gazette / STEP Journal, Wikidata, Crunchbase, OpenCorporates, Companies House alignment, Trustpilot, LinkedIn founder cadence.

**llms.txt** adopted early.

**AI visibility benchmark** (run monthly) — 8 prompts across Claude / ChatGPT / Gemini / Perplexity / Google AIO, scored on Inclusion Rate, Citation Frequency, Sentiment Alignment, Misclassification Rate.

---

## 11. Phase 1 Success Gates (evidence-triggered, not time-triggered)

| Gate | Directional threshold |
|---|---|
| Organic traffic | 75k–150k sessions / month |
| AI-search inclusion rate | ≥40% across benchmark prompt set |
| Email list | 10k+ engaged subscribers |
| Branded search volume | Measurable organic demand for "DirectorCover" |
| Commercial viability | Profitable on Phase 1 revenue |
| Content inventory | 200–300 published pages |
| Broker relationships | ≥20 live broker relationships |
| Consumer Duty evidence | 12+ months of documented governance |
| Qualified principal | Founder holds CII R05 minimum (ideally R01 + R05 + R06) |

Hit all nine → trigger Phase 2 authorisation application.

---

## 12. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Signal 01 rupture on pivot | Use "publisher + directory + comparison" framing; include *currently* in exclusion statement |
| Directory partners turn hostile post-authorisation | Keep directory small, vetted, non-exclusive |
| FCA authorisation takes longer than planned | Start pre-app Month 12; budget 18-month bridge |
| Phase 1 content reads wrong post-authorisation | Write "here's how to think about this" not "we can't tell you" |
| Audience feels suddenly commercialised | Frame Phase 2 as "grown into"; keep 35% trust content |
| Exclusive Layer C deals lock you in | Max 18-month term, exit on authorisation |
| Qualification gap at transition | Founder starts CII R01 from Month 1 |
| Stats rot | Evidence Register + tax-year tagging + quarterly review |
| Vulnerable customer handling (bereavement/illness content) | Tone guideline, signpost Cruse / Samaritans / MoneyHelper |

---

## 13. Timeline

| Month | Phase 1 | Phase 2 prep (parallel) |
|---|---|---|
| 0–3 | Register DirectorCover Ltd, domain, trademark, launch shell, first 20 guides, ICO registration, privacy/cookies, own PI + cyber cover, sign s.21 approver | Founder books CII R01 |
| 3–6 | Scale content, launch directory, sign Side 1 Layer C (see `04-activequote-integration.md`), newsletter | R01 study |
| 6–12 | Launch Side 2 content, sign Side 2 Layer C, 100 pages published, newsletter 3k+ subs, monthly AI benchmark | R01 complete, start R05 |
| 12–15 | Hit gates, begin FCA pre-application dialogue | R05 complete, start R06 |
| 15–18 | Submit FCA authorisation application | R06 complete, PI + capital + business plan |
| 18–24 | FCA processes application; prep new promotion regime | Phase 2 staffing + tech |
| 24+ | **Phase 2 launches** as authorised brokerage with content, audience, directory intact | Ongoing |

---

## 14. Decisions Locked (doctrine)

1. Phase-neutral where possible, phase-differentiated only where necessary
2. Every page carries a regulation tag at build time
3. Never enter 🔴 in Phase 1
4. Flat fees only in Layer B — no contingent commissions
5. No exclusive partner deals in Layer C
6. One product named per problem-led page, with two CTAs (find-a-broker OR compare)
7. 35% trust content from day one
8. Named authors only
9. Terminology lock — one canonical term per product
10. Evidence Register for every stat
11. Tax-year tags on every tax fact
12. Founder on the CII clock from Month 1

---

## 15. Open Questions / To Decide

1. Final brand name — confirm DirectorCover or alternative
2. Layer C partners — confirm ActiveQuote for Side 2 (see `04-activequote-integration.md`); Side 1 shortlist
3. Editorial hire — named editor with sign-off authority
4. First guest contributors — broker / insolvency lawyer / accountant
5. Media-first vs insurance-first posture — recommendation: media-first, commit explicitly
6. Budget / runway — cash needed to reach Phase 1 gates
7. Investment posture — bootstrapped, friends-and-family, or seed raise at P1→P2

---

## 16. Key References

FCA PERG 5 · FCA PERG 8.33 · FCA ICOBS 2.2 · FCA Consumer Duty · FCA Financial Promotions Gateway (s.21 FSMA) · FCA AR regime · ASA / CAP Code rule 3.7 · HMRC BIM45525 · HMRC BIM45530 (Anderson rules) · Employers' Liability (Compulsory Insurance) Act 1969 · Companies Act 2006 s.172 · Insolvency Act 1986 s.214 · Chartered Insurance Institute R01 / R05 / R06 · Rank4AI Five Signal Model.
