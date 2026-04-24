# Really Cheap B2B Outreach Stack — GitHub + DIY Research

A survey of open-source / low-cost tools for the full B2B outbound loop:
**find leads → enrich + verify → send → track**. Optimized for cost first.

## TL;DR — cheapest viable stack

| Stage | Pick | Cost |
|---|---|---|
| Lead sourcing | Scrape + Bright Data free tier / LinkedIn scrapers | $0–$20/mo |
| Email finding | Hunter free (50/mo) + pattern guessing | $0 |
| Verification | Reacher / Trumail / `umuterturk/email-verifier` (self-host) | $0 |
| Sending infra | Mailforge mailboxes (~$2.50/mbx) OR your own DNS + Postal/Mox | $0–$30 |
| Sequencer | `PaulleDemon/Email-automation` or Woodpecker ($20/mo) | $0–$20 |
| Campaign mgr | listmonk (self-hosted) | $0 |
| Inbox cleanup | `elie222/inbox-zero` | $0 |

Rough floor: **~$0–$40/mo** if you self-host and do DNS yourself; ~$60–$80/mo if you want managed warmup + a sequencer.

---

## 1. Lead sourcing (GitHub repos worth bookmarking)

- **[eracle/OpenOutreach](https://github.com/eracle/OpenOutreach)** — describe your product + ICP, it discovers leads on LinkedIn and reaches out. Self-hosted.
- **[brightdata/ai-lead-generator](https://github.com/brightdata/ai-lead-generator)** — Streamlit app: Bright Data scrapes, OpenAI qualifies, spits out outreach-ready rows.
- **[IsaacBell/leads-db](https://github.com/IsaacBell/leads-db)** — AI-powered B2B lead gen system (private preview at time of writing).
- **[linkdAPI/linkedin-leads-discover](https://github.com/linkdAPI/linkedin-leads-discover)** — LinkedIn profile discovery + export.
- **[josephlimtech/LinkedIn-Scraper-1](https://github.com/josephlimtech/LinkedIn-Scraper-1)** — scrape up to ~10k profiles from company links, pulls email if public.
- **[sm00v/LinkedIn_Email_Scraper](https://github.com/sm00v/LinkedIn_Email_Scraper)** — Selenium scraper, outputs to an email-format template.
- **GitHub topics to browse:** [`lead-generation`](https://github.com/topics/lead-generation), [`leadgeneration`](https://github.com/topics/leadgeneration), [`linkedin-scraper`](https://github.com/topics/linkedin-scraper), [`email-scraper`](https://github.com/topics/email-scraper).

**Cheapskate pattern:** scrape company lists (Crunchbase, YC, Product Hunt, Apollo free exports), pull employees with a LinkedIn scraper, pattern-guess emails (`{first}.{last}@domain`), verify.

⚠️ LinkedIn scraping violates their ToS. Use rotating proxies, your own cookies, and understand the risk — account bans are real.

## 2. Email finding + verification (free/open-source)

- **[umuterturk/email-verifier](https://github.com/umuterturk/email-verifier)** — free Docker-packaged validator, doesn't store data. Hosted at `rapid-email-verifier.fly.dev`.
- **[trumail/trumail](https://github.com/trumail/trumail)** — Go lib + public API + Docker image for SMTP/regex/DNS verification.
- **[Reacher](https://reacher.email/)** — open-source verification API, self-hostable.
- **[KnowEmail](https://openinitia.github.io/knowemail/)** — bulk verifier/validator, syntax + domain + deliverability.
- **Hunter.io free tier** — 50 searches/mo, cleanest for domain-to-email if you want managed.

**Commercial fallbacks with free credits:** Lusha (50 credits), Enrich (100 API credits).

## 3. Sending infrastructure (the actual bottleneck)

Your deliverability is dominated by **domain reputation + DNS + warmup**, not the tool. Don't send cold mail from your primary domain.

**Self-hosted mail servers:**
- **[mjl-/mox](https://github.com/mjl-/mox)** — modern secure mail server, low-maintenance.
- **[Billionmail/BillionMail](https://github.com/Billionmail/BillionMail)** — full self-hosted stack (server + newsletter + marketing).
- **[muety/mailwhale](https://github.com/muety/mailwhale)** — BYO-SMTP relay with REST API.
- **[vitorfs/colossus](https://github.com/vitorfs/colossus)** — self-hosted email marketing, any SMTP.

**Managed cheap:** Mailforge (~$2.50/mailbox) is the cheapest if you're willing to manage DNS/warmup yourself. InboxKit (~$39/mo) is cheaper once you factor in domain burn.

**Rule of thumb:** buy 3–10 throwaway domains (~$10/yr each), 2–3 mailboxes per domain, warm up for 2 weeks before blasting. Cap at ~30 cold sends/mailbox/day.

## 4. Sending / sequencing

- **[PaulleDemon/Email-automation](https://github.com/PaulleDemon/Email-automation)** — scheduled cold outreach with dynamic templates + follow-ups. Self-hosted, configurable SMTP.
- **[catin-black/meteor-emails](https://github.com/catin-black/meteor-emails)** — simple SendGrid-based cold sender.
- **[listmonk](https://listmonk.app/)** ([GitHub](https://github.com/knadh/listmonk)) — Go, multi-SMTP, rate-limited, handles high volume. Best pure sender if you don't need sequences.
- **[Mautic](https://github.com/mautic/mautic)** — full automation platform (scoring, workflows, CRM). Heavier: 2–4GB RAM, PHP + MySQL, real maintenance burden.
- **[Keila](https://www.keila.io/)** — Elixir, ergonomic newsletter tool.

**listmonk vs Mautic:** listmonk wins for raw sending + simplicity. Mautic wins if you need multi-step nurture workflows and lead scoring. For cold outreach specifically, listmonk + a sequencer is usually enough.

**Managed cheap:** Woodpecker ($20/mo), Saleshandy ($25/mo), Apollo ($49/user/mo — includes their DB).

## 5. Inbox / reply management

- **[elie222/inbox-zero](https://github.com/elie222/inbox-zero)** — AI inbox assistant, OSS. Handy when replies start landing.

---

## Recommended starter path (practical)

1. **Domains:** buy 3 lookalikes of your main domain on Namecheap/Cloudflare (~$30/yr total).
2. **Mailboxes:** Google Workspace ($7/mbx) or Mailforge (~$2.50/mbx). Set SPF + DKIM + DMARC before anything else.
3. **Warmup:** 2 weeks, gradually ramping. `instantly` or `smartlead` have warmup included; if self-hosting, use a warmup pool like [Mailivery](https://mailivery.io/) or build one with a few real inboxes + scripted replies.
4. **Leads:** pull an ICP list from Apollo's free export (10k contacts/mo on free tier), enrich gaps with Hunter free + `email-verifier` for verification.
5. **Sequencer:** `PaulleDemon/Email-automation` if DIY, Woodpecker if you want something that just works.
6. **Tracking:** turn **off** open tracking (hurts deliverability in 2026). Track replies and booked meetings only.

## Unit economics sanity check

- Domains + mailboxes: **$20–$40/mo**
- Data + verification: **$0–$20/mo** (free tiers stitched together)
- Sequencer: **$0–$25/mo**
- **Total: ~$20–$85/mo** to run 1,000–3,000 cold emails/day with reasonable deliverability.

Compare to Apollo + Outreach + ZoomInfo stack: $500–$2,000/mo starting point.

---

## Sources

- [lead-generation GitHub topic](https://github.com/topics/lead-generation)
- [OpenOutreach](https://github.com/eracle/OpenOutreach)
- [Bright Data AI Lead Generator](https://github.com/brightdata/ai-lead-generator)
- [IsaacBell/leads-db](https://github.com/IsaacBell/leads-db)
- [HuggingFace: Top 30 OSS lead-gen projects](https://huggingface.co/blog/samihalawa/automating-lead-generation-with-ai)
- [PaulleDemon/Email-automation](https://github.com/PaulleDemon/Email-automation)
- [catin-black/meteor-emails](https://github.com/catin-black/meteor-emails)
- [listmonk](https://listmonk.app/)
- [BillionMail](https://github.com/Billionmail/BillionMail)
- [mox mail server](https://github.com/mjl-/mox)
- [mailwhale](https://github.com/muety/mailwhale)
- [Colossus](https://github.com/vitorfs/colossus)
- [inbox-zero](https://github.com/elie222/inbox-zero)
- [Keila](https://www.keila.io/)
- [sm00v/LinkedIn_Email_Scraper](https://github.com/sm00v/LinkedIn_Email_Scraper)
- [linkdAPI/linkedin-leads-discover](https://github.com/linkdAPI/linkedin-leads-discover)
- [josephlimtech/LinkedIn-Scraper-1](https://github.com/josephlimtech/LinkedIn-Scraper-1)
- [umuterturk/email-verifier](https://github.com/umuterturk/email-verifier)
- [trumail](https://github.com/trumail/trumail)
- [Reacher](https://reacher.email/)
- [KnowEmail](https://openinitia.github.io/knowemail/)
- [listmonk vs Mautic (openalternative.co)](https://openalternative.co/compare/listmonk/vs/mautic)
- [Listmonk vs Mautic (Sequenzy)](https://www.sequenzy.com/versus/listmonk-vs-mautic)
- [Cheapest Cold Email Infrastructure 2026 (InboxKit)](https://www.inboxkit.com/learn/cheapest-cold-email-infrastructure-2026)
- [Best Cold Email Stack 2026 (Mailpool)](https://www.mailpool.ai/blog/the-best-cold-email-stack-in-2026-infrastructure-sending-tool-tracking)
- [Apollo.io alternatives (Skrapp)](https://skrapp.io/blog/apollo-io-alternatives/)
- [Apollo free alternatives (Alex Berman)](https://alexberman.com/apollo-alternative-free)

---

# Part 2 — Deeper tactics

## 6. AI-driven enrichment (the "Clay" replacement)

Clay.com charges $167+/mo for waterfall enrichment. You can get 80% of it with:

- **[mendableai/fire-enrich](https://github.com/mendableai/fire-enrich)** — open-source Clay-like tool. Point it at an email/domain, it uses AI + web search to enrich firmographics, tech stack, funding, headcount.
- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** (110k+ stars) — scrape any page to clean markdown/JSON. Great for "given a company homepage, return: pricing, tech stack, customer logos, careers page headcount signal."
- **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** (50k+ stars) — LLM-friendly Python scraper; cheaper than Firecrawl at scale, self-hosted.
- **[kaymen99/ai-web-scraper](https://github.com/kaymen99/ai-web-scraper)** — Crawl4AI-based lead extractor that pulls structured business data (names, phones, addresses) from directory sites.

**Waterfall pattern (DIY):**
```
email input
  -> Hunter free API
     -> (miss) Apollo free CSV lookup
        -> (miss) Firecrawl domain scrape + GPT to infer pattern
           -> email-verifier to confirm SMTP-valid
```
Each step only runs if the prior misses. Costs: $0–$0.002 per lead versus Clay's ~$0.10–$0.50.

## 7. Warmup (the thing that actually decides deliverability)

- **[WKL-Sec/Warmer](https://github.com/WKL-Sec/Warmer)** — Selenium Python script that automates warmup sends + replies. Only OSS option that actually works.
- **Paid budget picks:** Warmy, Mailreach, Warmforge — $29–$79/mo per mailbox, include placement tests (where the email lands: inbox vs spam vs promotions).
- **DIY warmup pool:** set up 10 Gmail/Outlook mailboxes across different providers, run a script that has them exchange ~20 emails/day with realistic reply chains for 14 days. The `Warmer` repo above is a starting point.

**Non-negotiables before you send a single cold email:**
1. SPF record on sending domain.
2. DKIM signing enabled.
3. DMARC set to `p=none` (monitor mode) minimum.
4. Custom tracking domain (or skip open tracking entirely — recommended in 2026).
5. Google Postmaster Tools + Microsoft SNDS accounts set up to monitor reputation.

If any of those are missing, buying more fancy tools is a waste of money.

## 8. SMTP providers ranked by $/email (and cold-email fitness)

| Provider | Cost | Free tier | Cold email? |
|---|---|---|---|
| Amazon SES | $0.10 per 1k | 3k/mo (12mo) | ✅ allowed but you must BYO deliverability |
| SMTP2GO | $15/mo for 10k | 1k/mo | ✅ decent cold-email reputation |
| Brevo (ex-Sendinblue) | ~$25/mo 20k | 300/day | ⚠️ stricter on cold |
| Postmark | $15/mo 10k | trial only | ❌ bans cold email explicitly |
| SendGrid | $20/mo 50k | 100/day | ❌ risky for cold, accounts get banned |
| Mailgun | $15/mo 10k | trial | ⚠️ warns against cold |

**SES is cheapest per email** ($1 = 10k sends), but you own deliverability entirely: warmup, IP reputation, bounce handling. Combine with dedicated IP ($24.95/mo extra) only after consistent ~50k/mo.

For cold outreach specifically, **don't use transactional providers** (Postmark/Mailgun/SendGrid) — they police cold email aggressively and will suspend you. Use dedicated mailboxes on Google Workspace, Outlook 365, or Mailforge.

## 9. AI personalization (the compounding edge)

Generic cold email reply rates in 2026 hover around 0.5–2%. Personalized-opener emails hit 5–12%. The marginal cost is a few cents per lead.

- **[takuyadev/personalize-ai](https://github.com/takuyadev/personalize-ai)** — mass-generates first-line openers from LinkedIn/website keywords.
- **[The-Pocket/PocketFlow-Tutorial-Cold-Email-Personalization](https://github.com/The-Pocket/PocketFlow-Tutorial-Cold-Email-Personalization)** — end-to-end tutorial: Google search → scrape → Claude/GPT opener.
- **[cupel-cloud/ai-cold-email-campaign-kit](https://github.com/cupel-cloud/ai-cold-email-campaign-kit)** — ICP scoring + sequence generation with natural language prompts.
- **[harshmriduhash/Cold-Emailer](https://github.com/harshmriduhash/Cold-Emailer)** — full-stack n8n + OpenAI + Sheets agent.

**Minimum viable personalization prompt:**
```
Given this LinkedIn/company snippet:
<snippet>

Write a 12-word opener for a cold email that:
- references ONE specific detail (not "saw you work at X")
- is not a compliment
- reads like a human typed it
- ends without punctuation
```

Run it with `claude-haiku-4-5` or `gpt-4o-mini` — costs ~$0.0003/lead.

## 10. LinkedIn channel (risky but free)

LinkedIn DMs get 3–5x reply rates vs. cold email, but automation violates ToS and account bans are real. Mitigations: rotating residential proxies, human-like delays (30–120s between actions), daily caps (20 connection requests, 10 DMs).

- **[linkoutapp/linkout-scraper](https://github.com/linkoutapp/linkout-scraper)** — Puppeteer, comprehensive actions incl. messaging. Updated 2026.
- **[y0k4i-1337/puppetin](https://github.com/y0k4i-1337/puppetin)** — scrape employees by company, infer emails.
- **[juliatan/linkedin-scraper](https://github.com/juliatan/linkedin-scraper)** — clean Puppeteer base to fork.
- **[josephlimtech/linkedin-profile-scraper-api](https://github.com/josephlimtech/linkedin-profile-scraper-api)** — headless API returning JSON.

**Safer paid alternatives:** Dripify ($39/mo), Heyreach ($79/mo), Expandi ($99/mo) — they manage the browser fingerprint and throttling for you. Still ToS-violating but less likely to get you banned.

## 11. No-code orchestration with n8n (free, self-hosted)

n8n is the free Zapier. Workflows chain lead sources → enrichment → AI → CRM → sender. A few production-ready templates to copy:

- **[Awaisali36/50k-lead-generation-system](https://github.com/Awaisali36/50k-lead-generation-system)** — Apollo + Google Search + LinkedIn scraping + Gemini qualification, all in n8n + Airtable. Generates and scores thousands of leads.
- [Apollo → Airtable one-click qualification](https://n8n.io/workflows/3435-get-qualified-leads-in-one-click-from-apollo-to-airtable/)
- [Apollo + Apify scraping + GPT personalization](https://n8n.io/workflows/9393-automate-b2b-lead-generation-and-personalized-cold-emails-with-apollo-apify-and-gpt/)
- [Full AI BDR: Apollo → Instantly.ai with enrichment](https://n8n.io/workflows/6983-automate-lead-generation-and-personalized-outreach-with-apollo-ai-and-instantlyai/)

Self-host n8n on a $5 Hetzner box via Docker; total infra for the automation layer is $5–10/mo.

---

## 12. Concrete 30-day playbook (cheap build)

**Week 1 — Infrastructure**
- Buy 3 domains (lookalikes, not your primary). ~$30/yr.
- Set up Google Workspace, 2 mailboxes per domain = 6 mailboxes at $7 each = $42/mo. (Or Mailforge at ~$15 total.)
- Configure SPF/DKIM/DMARC on all 3 domains.
- Register Google Postmaster + Microsoft SNDS.
- Start warmup on all 6 mailboxes (Warmy $49/mo OR `WKL-Sec/Warmer` self-hosted).

**Week 2 — Data layer**
- Define ICP in one sentence: "(Role) at (company size) in (industry) who (signal)."
- Pull 5k matching contacts from Apollo free tier (10k/mo export limit).
- Run through `umuterturk/email-verifier` to drop invalid (~15–25% fail).
- Enrich with Fire Enrich or a Firecrawl + GPT-4o-mini prompt: company 1-liner, tech stack, recent news.

**Week 3 — Copy + sends**
- Write one 3-email sequence, 60–80 words per email, no open tracking.
- Generate first-line personalization per lead with `gpt-4o-mini` (~$1.50 per 5k leads).
- Load into sequencer (Woodpecker $20/mo or self-hosted `PaulleDemon/Email-automation`).
- Cap at 25 sends/mailbox/day × 6 mailboxes = 150 sends/day, 1,050/week.

**Week 4 — Iterate**
- Measure: reply rate, positive-reply rate, booked-meeting rate.
- Benchmarks: >1% reply = infra fine. <1% = deliverability issue, check Postmaster.
- Benchmarks: <10% positive of total replies = copy problem, rewrite subject + first line.
- Re-warmup any mailbox that dips below 95% inbox placement.

**Total cost for month 1:** ~$50 (Mailforge) to ~$130 (Google Workspace + Woodpecker + Warmy). Beats a $500/mo Apollo + Outreach stack for <5k/month outreach volume.

---

## 13. What I'd skip

- **Open tracking pixels** — big deliverability hit in 2026 post-iOS-MPP, and most ESPs now block them. Track link clicks + replies only.
- **SendGrid / Mailgun / Postmark for cold** — they'll suspend you; use mailboxes.
- **Buying lists** — >50% bounce rates, torch your reputation in a day.
- **Scraping LinkedIn from your real account** — use burners or don't do it at all.
- **Paying for ZoomInfo** — $15k/yr minimum, Apollo gives 90% of the data for $49/user.

## 14. Additional sources

- [Fire Enrich (Clay alternative)](https://github.com/mendableai/fire-enrich)
- [Firecrawl](https://github.com/firecrawl/firecrawl)
- [Crawl4AI](https://github.com/unclecode/crawl4ai)
- [kaymen99/ai-web-scraper](https://github.com/kaymen99/ai-web-scraper)
- [WKL-Sec/Warmer (OSS warmup)](https://github.com/WKL-Sec/Warmer)
- [takuyadev/personalize-ai](https://github.com/takuyadev/personalize-ai)
- [PocketFlow Cold Email Personalization tutorial](https://github.com/The-Pocket/PocketFlow-Tutorial-Cold-Email-Personalization)
- [cupel-cloud/ai-cold-email-campaign-kit](https://github.com/cupel-cloud/ai-cold-email-campaign-kit)
- [harshmriduhash/Cold-Emailer](https://github.com/harshmriduhash/Cold-Emailer)
- [Awaisali36/50k-lead-generation-system](https://github.com/Awaisali36/50k-lead-generation-system)
- [linkoutapp/linkout-scraper](https://github.com/linkoutapp/linkout-scraper)
- [y0k4i-1337/puppetin](https://github.com/y0k4i-1337/puppetin)
- [juliatan/linkedin-scraper](https://github.com/juliatan/linkedin-scraper)
- [n8n lead-generation workflow library](https://n8n.io/workflows/categories/lead-generation/)
- [Brevo: free SMTP servers comparison](https://www.brevo.com/blog/free-smtp-servers/)
- [EmailToolTester: best transactional email 2026](https://www.emailtooltester.com/en/blog/best-transactional-email-service/)
