# Quick-CPL Launch Tools

Twelve free utilities that capture leads and route them into affiliate offers. Each is 1–3 days of Astro / Claude Code work for the tool itself, then SEO + email do the rest. They're not businesses — they're cheap traffic feeders that pay their own way and seed email lists for the bigger sites.

These pair with the Master Index entries **CPL-1 through CPL-12** (numbers 83–94 in `niche-shortlist-2026-04.md`).

---

## How they fit the empire

Each tool sits on its own subdomain, OR as a section of a parent site. Examples:
- `invoice.findagym.co.uk` — no, that doesn't work; the right pattern is **standalone domain** OR **section of a finance/agency site**
- The CPL stack drives **email-list growth** which lifts every other site's launch traffic
- Tools that capture business buyers feed the **fleet** (loans, IF, terminals, asset finance)
- Tools that capture homeowners feed **FindATradey** and **Site 1 Home Improvement Hub**
- One tool that captures wedding planners feeds **Site 2 Wedding**

---

## CPL-1 — Free UK invoice generator + quote generator

- **Search demand:** "free invoice generator UK", "free quote template UK" — high volume + repeat-use
- **Tool:** form input → branded PDF download, email captured
- **Affiliate stack:**
  - Xero (£30–80 per signup)
  - FreeAgent (£25–60)
  - QuickBooks UK (£40–100)
  - Sage Business Cloud
  - Crunch Accounting
  - Mazuma
- **Cross-sell:** business loan referral (fleet feed), MTD ITSA software (NEW 5), accountant referral
- **Per-visitor LTV (target):** £2–6 once email funnel mature

## CPL-2 — Free UK company name + domain availability checker

- **Search demand:** "check if company name available UK", "is this domain available" — massive entry-point for new business owners
- **Tool:** Companies House public API + domain WHOIS check, single-page result
- **Affiliate stack:**
  - 123-reg (£8–15/sale)
  - GoDaddy UK
  - Hostinger (£60+ per signup)
  - SiteGround
  - IONOS
- **Cross-sell:** Limited co setup affiliate (RapidFormations / Crunch / Mazuma £20–50), business bank account opens (Tide £40–80, Starling Business £30–60)
- **Why it works:** every UK Ltd founder runs this once, often early in the journey — captures highest-intent stage

## CPL-3 — Free UK salary calculator (PAYE, take-home, employer cost)

- **Search demand:** "UK salary calculator", "take home pay calculator", "employer cost calculator" — massive
- **Tool:** PAYE + NI + pension calc with year-on-year comparison
- **Affiliate stack:**
  - Payroll software (Sage Payroll, Brightpay, IRIS — £30–80)
  - HR services (Peninsula, Citation — £600–5,000 first-year commission, but heavier sales)
  - Recruitment platforms (Reed, CV-Library)
  - Pension auto-enrolment providers
- **Audience:** mixed — employees self-checking AND SME owners checking employer cost. Two affiliate funnels from one tool.

## CPL-4 — Free GDPR cookie banner + privacy policy + terms generator

- **Search demand:** real and rising; high CPC niche
- **Tool:** form-driven generator → downloadable HTML/PDF
- **Affiliate stack:**
  - CookieYes
  - iubenda
  - Termly
  - OneTrust SMB plan
  - GDPR consultant referrals (high-CPL — £100–300 per qualified case)
- **Cross-sell:** cyber/compliance services (parked Cyber Hub), GDPR audit consultancy

## CPL-5 — Free business mileage / expense calculator (HMRC rates)

- **Search demand:** moderate, repeat-use (every UK self-employed person does this monthly)
- **Tool:** HMRC AMAP rates calculator + downloadable expense log
- **Affiliate stack:**
  - Bookkeeping apps (Receipt Bank/Dext, Pleo, Soldo £30–60)
  - Business credit cards
  - Fuel cards (Allstar, BP Plus)
- **Cross-sell:** asset finance for business vehicles, business loan for vehicle purchase

## CPL-6 — Free SEO + site speed audit (DIY, results-page-led)

- **Search demand:** enormous — every business owner has Googled this once
- **Tool:** input URL → backend crawl → score + recommendations on a single results page
- **Affiliate stack (highest CPL on the list):**
  - Ahrefs (£20–60)
  - SEMrush (£50–200 first-month commission)
  - Mangools
  - KeyCDN (CDN affiliate)
- **Cross-sell:** Rank4AI's own A23 AI search audit lead magnet — direct funnel to Rank4AI agency
- **Why it's the strongest:** SEO software has the highest commission rates of any SaaS category

## CPL-7 — Free email signature generator (UK, GDPR-compliant footer)

- **Search demand:** small but very low-competition
- **Tool:** form → HTML email signature with optional GDPR-compliant footer
- **Affiliate stack:**
  - Email marketing platforms (Mailchimp, Brevo, ActiveCampaign, ConvertKit — £20–80)
  - Gmail Workspace reseller (Workspace partners pay £20+)

## CPL-8 — Free CIS calculator (Construction Industry Scheme)

- **Search demand:** niche but very high-intent (sole trader / construction Ltd co)
- **Tool:** input gross + materials + labour split → CIS deduction calc + Net pay
- **Affiliate stack:**
  - CIS bookkeeping (Crunch, Mazuma)
  - CIS-aware accountants
  - Construction-specific IF (cross-sell to fleet's IF site — A16 Construction CIS IF)
- **Cross-sell:** business loan for cash-flow gaps caused by CIS deductions, asset finance for construction kit

## CPL-9 — Free VAT calculator + reverse VAT + flat-rate scheme calculator

- **Search demand:** large + repeat (every UK SME owner uses this monthly)
- **Tool:** standard VAT, reverse VAT, flat-rate scheme calculator with sector-specific FRS rates
- **Affiliate stack:**
  - MTD-ready accounting software (Xero, FreeAgent, QuickBooks)
  - Accountants (Crunch, Mazuma)
  - VAT specialists for international/import VAT cases

## CPL-10 — Free director's dividend / salary optimiser

- **Search demand:** very specific but high-intent (every UK Ltd director runs this once a year)
- **Tool:** input company profit → output optimal salary + dividend split with tax savings
- **Affiliate stack:**
  - Limited co accountants (Crunch, Mazuma, GoForma)
  - Umbrella companies
  - Contractor brokers
- **Cross-sell:** R&D tax credit specialists (parked but high-CPL), pension planning

## CPL-11 — Free domain / website valuation tool

- **Search demand:** small but pure-intent
- **Tool:** input domain → estimated valuation based on traffic, age, backlinks (proxied)
- **Affiliate stack:**
  - Flippa
  - Empire Flippers
  - GoDaddy Domain Marketplace
  - Sedo (commission on sales)

## CPL-12 — Free wedding budget allocator

- **Search demand:** strong seasonal (Jan–Mar peak)
- **Tool:** total budget input → category breakdown by region (sourced from Site 2 Wedding data)
- **Affiliate stack:**
  - Wedding loan referral (cross-sell to fleet's unsecured personal loan)
  - Compare Wedding Insurance
  - Hitched / Bridebook venue-listing leads
- **Cross-sell:** **direct funnel into Site 2 Wedding** — every visitor to this tool is one click from the wedding-cost programmatic content

---

## Build pattern

All twelve share the same shape:

1. **Single-page tool** built in Astro with a small React island for the calculator/generator UI
2. **Result page** (or dynamic component) that:
   - Shows the result clearly
   - Prompts for email to send the result + optional follow-up tips
   - Routes to 2–4 affiliate offers most relevant to the result
3. **Email sequence** (Beehiiv / Mailchimp / Resend):
   - Day 0: deliver the result
   - Day 2: useful tip + soft affiliate
   - Day 7: deeper guide + cross-sell to a fleet site
   - Day 14: "are you doing X?" affiliate offer
   - Day 30: re-engagement / unsubscribe
4. **Schema markup** (HowTo, SoftwareApplication, FAQPage)
5. **No paid traffic** — SEO + organic share + email-list compounding

---

## Build sequence for v0.1

CPL tools should be built **in waves of 3** while the bigger sites are being built. They're free traffic that lifts everything.

| Wave | Tools | Why this order |
|---|---|---|
| **W3–4** (alongside FindATradey + Pet Hub) | CPL-1 Invoice generator, CPL-2 Domain checker | Fastest to build, broadest audience, biggest affiliate stacks |
| **W5–6** | CPL-3 Salary calc, CPL-9 VAT calc | UK SME volume, paired well with MTD ITSA recency window |
| **W7–8** | CPL-6 SEO audit, CPL-12 Wedding budget allocator | Highest CPL (SEO) + Site 2 cross-sell (wedding) |
| **W9–10** | CPL-4 GDPR generator, CPL-8 CIS calc | Niche but high-intent — light builds |
| **W11–12** | CPL-5 Mileage, CPL-10 Director optimiser | Heavier tax-side tools, lower priority |
| **Phase 2** | CPL-7 Email sig, CPL-11 Domain valuation | Lowest CPL of the list — only build if other waves saturate |

---

## What this stack adds to total revenue

Conservative estimate at 12-month maturity, assuming each tool reaches 5,000 monthly visitors and converts at 2% → 1,200 affiliate clicks/month at average £10 commission = **£12k/month from CPL stack alone**, on top of the bigger sites.

Plus an email list that compounds across all twelve tools — useful for launching every future site without paid acquisition.

---

## Cross-references

- `docs/niche-shortlist-2026-04.md` §6 — master index entries CPL-1 to CPL-12 (#83–#94)
- `docs/reference/lead-resale-model.md` — the three-layer revenue model, of which CPL is layer 3
- `docs/site-builds/findatradey.md` — fleet feeders that link CPL-1, CPL-2, CPL-3 visitors back to fleet products
- `docs/site-builds/gym-hub.md` — Phase 2 cross-sell for fitness-related CPL tools (none in v0.1)
