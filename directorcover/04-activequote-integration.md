# DirectorCover — ActiveQuote Integration Plan

*The Side 2 Layer C compare partner. Gets DirectorCover a live, regulated product-comparison capability on Day 1 without needing FCA authorisation.*

---

## 1. Why ActiveQuote

ActiveQuote is a UK FCA-authorised protection and health insurance comparison firm (FRN 501109), based in Cardiff. They run their own consumer-facing comparison site and also operate a white-label / partner programme that lets third-party brands embed their quote-and-apply journey.

For DirectorCover this is attractive because:

- **They are authorised.** DirectorCover stays on the publisher side of the perimeter; ActiveQuote holds the arranging permissions.
- **Protection-panel depth.** ActiveQuote compares quotes across the major UK life, critical illness, and income protection insurers — Aviva, Legal & General, Royal London, Vitality, AIG Life, LV=, Zurich, Scottish Widows, Guardian, and others.
- **White-label/API available.** The partnership model supports embedded compare widgets on DirectorCover's domain under DirectorCover branding, with ActiveQuote handling the regulated journey.
- **Established tech.** Live since 2009, mature quote engine, good conversion data.
- **Commercial terms** are typically revenue-share or per-lead, negotiable by volume.

---

## 2. Product Coverage — ActiveQuote vs DirectorCover Side 2

| DirectorCover Side 2 product | ActiveQuote covers? | Notes |
|---|---|---|
| **Life Insurance (personal / director)** | ✅ Yes | Direct fit — comparison across the full panel |
| **Relevant Life** | ✅ Yes | ActiveQuote sells relevant life directly; good partner fit |
| **Critical Illness** | ✅ Yes | Core product |
| **Executive Income Protection** | ✅ Personal income protection yes; executive IP — to confirm scope during setup | Check whether the API surfaces executive IP specifically, or if it is retail IP only |
| **Key Person** | ⚠️ Likely not (advised-only business product) | Source a different partner (LifeSearch, Drewberry, Cavendish) |
| **Shareholder Protection** | ⚠️ Likely not (advised-only with legal overlay) | Source a different partner |
| **Partnership Protection** | ⚠️ Likely not | Same as above |
| **Personal Guarantee Cover** | ❌ Not typically | Specialist niche — different partner |

**Practical implication:** ActiveQuote covers the non-advised-viable subset of Side 2 — life, critical illness, personal IP, and relevant life. The advised products (key person, shareholder, partnership, PG) need a separate Layer C partner, either:

- **LifeSearch Partner Programme** — referral handoff to advised brokers
- **Drewberry** — specialist business protection advisers
- **Cavendish Online** — execution-only route (limited for shareholder/keyperson)
- **A bespoke IAR arrangement** with a protection broker if volumes justify it

The ActiveQuote page plan therefore covers the 4 products above; the other 4 route to find-a-broker (Layer B) or to a different compare partner.

---

## 3. The ActiveQuote-Powered Pages on DirectorCover

Four compare pages on Day 1 of Side 2 launch:

```
/compare/director-protection/life-insurance/            ← ActiveQuote
/compare/director-protection/relevant-life/             ← ActiveQuote
/compare/director-protection/critical-illness/          ← ActiveQuote
/compare/director-protection/income-protection/         ← ActiveQuote
```

Plus embedded compare CTAs on the relevant product explainer pages:

```
/director-protection/relevant-life/         →  embed compare widget
/director-protection/critical-illness/      →  embed compare widget
/director-protection/income-protection/     →  embed compare widget
/director-protection/director-life-insurance/  →  embed compare widget
```

### Compare page template (ActiveQuote-powered)

```
[H1 — layman's register]
    "Compare relevant life policies paid by your company"

[Lead paragraph — 100 words]
    Primary answer: what the comparison shows, how pricing works,
    why relevant life is different to personal life insurance.
    Full entity names, no pronouns.

[Disclaimer inline block]
    "This comparison is provided in partnership with ActiveQuote,
     an FCA-authorised firm (FRN 501109). DirectorCover publishes
     information and does not itself provide regulated advice —
     [read more]"

[ActiveQuote widget embed]
    Pre-filled for a director / UK limited company context.
    Quote journey runs under ActiveQuote's permissions and compliance.

[Below the widget]
    "How to think about the numbers"
    — plain-English guidance on what to compare (premium, sum assured,
      term length, policy definitions, provider financial strength).

[FAQ block — FAQPage schema]
    Q: Who underwrites these policies?
    Q: Is the quote an indication or a full quote?
    Q: Who do I speak to if I have questions before applying?
    Q: Can I make changes after I've bought the policy?

[Evidence stamp + Sources]
    Partner: ActiveQuote (FRN 501109)
    Last reviewed [date] · Author [name]

[Related reading]
    Links to /director-protection/relevant-life/ guide pages
    (pure content, no compare)
```

### Tracking and attribution

- Unique tracking ID per DirectorCover page passed to ActiveQuote on widget load
- Callback / postback from ActiveQuote on quote start, quote complete, policy bound
- Event names in GA4: `compare_widget_view`, `compare_widget_start`, `compare_widget_complete`, `policy_bound` (if ActiveQuote returns this event)
- Revenue reconciliation monthly against ActiveQuote partner report

---

## 4. Getting It Sorted — Partnership Process

### Step 1 — Initial contact (Week 0–2)

- Email: ActiveQuote partnerships team via the `Partners` or `B2B` contact on their website
- Alternative: LinkedIn outbound to Head of Partnerships / Commercial Director
- What to include in the first email:
  - Who DirectorCover is (one-paragraph entity description from `01-strategic-plan.md`)
  - Target audience (UK limited company directors, estimated monthly traffic or early-stage equivalent)
  - Products we want to compare (life, relevant life, critical illness, income protection)
  - Integration mode preferred (embedded widget under DirectorCover branding)
  - Indicative launch timing

### Step 2 — Discovery call (Week 2–4)

Expected topics they will want to discuss:
- Estimated volumes (be honest — pre-launch or early-launch)
- Brand alignment — they will assess whether DirectorCover's editorial content sits comfortably alongside their compliance posture
- Our s.21 financial promotions approver (they may offer to approve, which simplifies things)
- Lead-handling — what happens after a user starts a quote
- Data sharing — what we pass to them, what they pass back
- Reporting cadence

### Step 3 — Commercial terms (Week 3–6)

Typical models:
- **Revenue share** — percentage of commission / retail price paid back to DirectorCover on policies bound via our traffic. Common range: 20–50% depending on volume.
- **Per-lead / per-quote** — flat payment per qualified lead or completed quote, regardless of binding.
- **Hybrid** — smaller per-lead + rev-share on bound policies.

Our negotiation priorities:
- Non-exclusive (we can bring other partners later or become authorised ourselves)
- **Maximum 18-month initial term** with exit on DirectorCover FCA authorisation
- No "most favoured partner" clauses that limit what we publish
- Clear data-sharing rules — we own our user data; ActiveQuote owns the regulated interaction data
- Reporting cadence (monthly minimum)

### Step 4 — Compliance alignment (Week 4–8)

- Confirm whether ActiveQuote acts as our s.21 financial promotions approver for pages that reference their comparison or feature provider-specific content — if yes, this simplifies our compliance stack materially.
- Agree brand-safety rules — what DirectorCover can and cannot say adjacent to the widget (e.g. no implied advice, clear exclusion statement, accurate product descriptions).
- Align disclaimers — the `/about-this-information/` canonical page needs to accurately describe the ActiveQuote relationship.
- Decide on vulnerable-customer handling — what happens if a user starts a quote and the questions suggest vulnerability.

### Step 5 — Technical integration (Week 6–10)

- Receive ActiveQuote's embed spec / API docs
- Implement widget on the four compare pages (and the inline CTAs on product explainers)
- Implement tracking parameter passing + postback reception
- QA in staging with test journeys
- Agree go-live window

### Step 6 — Launch (Week 10–12)

- Soft launch on one page first (recommended: `/compare/director-protection/relevant-life/`) — highest DirectorCover editorial strength and lowest ambiguity
- Monitor first 2 weeks for funnel behaviour, drop-off points, and any regulatory issues
- Roll out to the other three compare pages once the first is stable
- Enable inline compare CTAs on product explainer pages
- Fire IndexNow + GSC requests; add compare pages to `llms.txt`

### Step 7 — Ongoing (post-launch)

- Monthly revenue reconciliation with ActiveQuote
- Quarterly performance review — conversion rates, funnel analysis, new product coverage
- Content updates aligned with any ActiveQuote panel changes (new insurers added, products changed)
- Watch for Phase 2 readiness — this contract is explicitly built to expire / convert when DirectorCover becomes authorised

---

## 5. Pre-Partnership Checklist

Before first contacting ActiveQuote, have ready:

- [ ] DirectorCover Ltd registered at Companies House
- [ ] Domain and branding live (at least a landing page describing the proposition)
- [ ] One-paragraph entity description (from `01-strategic-plan.md`)
- [ ] Traffic estimate or target (honest — pre-launch is fine; they partner with early-stage brands too)
- [ ] Target audience brief (UK Ltd directors, role, likely products)
- [ ] Clear statement that DirectorCover is unauthorised and intends to stay so in Phase 1
- [ ] Preferred integration mode (embedded widget vs API)
- [ ] Financial promotions approval plan (ideally ActiveQuote covers this)
- [ ] DirectorCover's own PI + cyber insurance in force (due diligence signal)

---

## 6. Fallback / Complementary Partners

If ActiveQuote is not the right fit, or for the advised-only products they do not cover:

| Partner | For | Model |
|---|---|---|
| **LifeSearch — Partner Programme** | Advised business protection (keyperson, shareholder, partnership) | Referral |
| **Drewberry** | Specialist business protection advisers | Referral / commercial partnership |
| **Cavendish Online** | Execution-only life, IP, CI | Referral / co-brand |
| **UnderwriteMe** (B2B) | Quote engine for protection across the panel | API license (higher build cost) |
| **iPipeline Solution Builder** | Adviser-focused platform (B2B2C) | License via one of their re-sellers |
| **Simply Business** affiliate | Side 1 Commercial GI (PI, PL, EL, cyber for SMEs) | Affiliate programme |
| **Superscript** affiliate | Side 1 SME subscription commercial | Affiliate programme |

For DirectorCover's Side 1, the launch assumption is an affiliate programme with Simply Business or Superscript (low integration, immediate revenue) — see `02-site-build-spec.md` §4.

---

## 7. Risks Specific to the ActiveQuote Partnership

| Risk | Mitigation |
|---|---|
| ActiveQuote's product panel does not cover relevant life or executive IP fully | Confirm the panel scope in Step 2 before signing; fill gaps via LifeSearch / Drewberry |
| Exclusive or aggressive non-compete clauses | Negotiate out in Step 3 — non-negotiable for DirectorCover |
| s.21 approval bottleneck | Agree turnaround SLA in Step 4 |
| Brand dilution (ActiveQuote branding showing through on our pages) | Negotiate embedded-widget styling that preserves DirectorCover branding above the fold |
| Phase 2 transition | 18-month term + authorisation exit clause agreed up front |
| Attribution disputes | Tracking IDs per page, postback verification, monthly reconciliation |

---

## 8. Success Signals for the Partnership

- First 100 quotes started via DirectorCover within 90 days of launch
- Conversion rate (quote start → bind) at least at ActiveQuote's internal benchmark
- No compliance flags raised in the first 6 months
- Partner revenue ≥ a meaningful share of Phase 1 income within 6 months of Side 2 launch
- Clean handover path documented for the Phase 2 transition

---

## 9. Open Items to Confirm

1. Exact product scope ActiveQuote will serve for DirectorCover (relevant life, IP, CI, life — all confirmed feasible; executive IP and business protection TBC)
2. Whether ActiveQuote can also serve as DirectorCover's s.21 financial promotions approver for provider-named content
3. Commercial terms — rev share % vs per-lead rate
4. Non-exclusivity and 18-month exit terms
5. Timeline to first live compare page (target: 10–12 weeks from first contact)
6. Second Layer C partner for the advised-only business protection products (key person, shareholder, partnership, PG) — recommended shortlist: LifeSearch, Drewberry
