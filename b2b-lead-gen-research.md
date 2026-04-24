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
