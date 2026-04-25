# AI Search, SEO & AI Overviews — Multilingual Ranking Opportunity

**Research date:** 25 April 2026
**Use case explored:** A UK-based niche site (e.g., card-terminal / merchant-services for independent corner shops) published in a non-English language (e.g., Hindi, Punjabi, Gujarati, Urdu) to capture diaspora demand that English-only competitors are ignoring.

---

## 1. The headline answer

Yes — there is a real, measurable gap. Three forces converge in your favour:

1. **AI search platforms are language- and geo-aware**, but unevenly. Google (AI Overviews / AI Mode) and Microsoft (Copilot) handle multilingual queries well; **ChatGPT, Perplexity and Claude default heavily to English content** even when the user types in another language. That inconsistency *is* the opportunity — and the risk.
2. **Vernacular content on the open web is scarce.** Fewer than 10 languages dominate >90% of indexed pages; English alone is over half. UK-targeted content in Hindi/Punjabi/Gujarati/Urdu for B2B SME topics (card terminals, EPOS, business banking, cash-and-carry, wholesale) is almost non-existent.
3. **Multilingual sites get ~327% more visibility in AI-generated responses** vs. monolingual sites (Weglot data). Initial rankings on low-competition vernacular keywords typically appear in **4–8 weeks**, vs. 6–12+ months in English.

Short version: a UK retailer audience that *speaks* Punjabi/Hindi/Gujarati at home but searches in English (or Hinglish) is being served generic English merchant-services content. A site written natively for them, geo-targeted to the UK, with proper hreflang and local entity signals, can rank fast in Google AI Overviews and AI Mode, and is genuinely novel for ChatGPT/Perplexity to retrieve when the query *is* in that language.

---

## 2. How Google AI Overviews actually work

- AI Overviews (AIO) sit above traditional results and are powered by **Gemini**. They appear on roughly **50% of US queries** and **39.4% of informational queries** vs. 12% for navigational ones.
- Google **does not pick one source** — it blends multiple. **76.1% of URLs cited in AIO also rank in the top 10**, but ranking #1 only gives a **33%** chance of being cited. That means **citation is partially independent of classic ranking** — being one of three cited sources is more achievable than being #1.
- Selection drivers (in order of measured impact):
  1. **Content depth and readability** (sentence/word counts, clear structure).
  2. **Extractable structure** — definitions, FAQ blocks, numbered steps, glossary boxes. AIO extracts *discrete claims*; pages that bury answers in narrative lose.
  3. **Topical clusters**, not single hero pages. Models score a *site's* coverage of a topic. A thin site with one article looks opportunistic.
  4. **E-E-A-T** signals reinforced by Google's March 2026 core update. Brand-entity association with a niche matters more than raw backlinks.
- Traditional SEO metrics (raw traffic, backlink count) had **little measured impact** on AIO citation in 2026 studies — a major shift from classic SEO.

**Implication for a vernacular site:** clean structure + topical depth + native expertise can beat older, larger English competitors on the same topic.

---

## 3. How ChatGPT / Perplexity / Claude search works

- **Two-stage process:** the model rewrites the user query into one or more sub-queries, sends them to a search provider (Bing for ChatGPT, multiple for Perplexity), retrieves a candidate set, *reads* them, then synthesises an answer with inline citations.
- **Retrieval ≠ citation.** Zyppy's 2025 study found **only ~15% of retrieved pages get cited**. The other 85% are read but discarded.
- **Position on page matters massively:** the **first 30% of a page accounts for 44.2% of all LLM citations**, the middle 31.1%, the last 30% only 24.7%. Lead with the answer.
- **Reddit, Wikipedia and review aggregator pages dominate** retrieval but are often quoted without citation — pure brand-mention SEO without a click.
- ChatGPT search uses **IP-based geolocation** automatically (no user prompt), shares it with its search providers, and localises results. UK location is detected automatically with high accuracy at country level.

---

## 4. How AI search handles language + location

This is where the gap lives. Tested behaviour as of 2026:

| Platform | Multilingual handling | Honours `hreflang`? | Geo-aware |
|---|---|---|---|
| **Google AI Overviews / AI Mode** | Strong. AI Mode now covers 53+ languages incl. Hindi (added Sept 2025). Custom Gemini model processes queries in *local context*, draws on regional sources. | Indirectly — Google says it uses algorithmic detection over `hreflang`, but `hreflang` still helps disambiguation. | Yes, via Search infrastructure. |
| **Microsoft Copilot** | Strong. Reuses Bing's mature multilingual stack. | Likely yes (via Bing). | Yes. |
| **ChatGPT** | **Weak.** Frequently returns English URLs even when the query and answer are in another language. | **Probably not** — no evidence it parses `hreflang`. | Yes (IP-based, automatic). |
| **Perplexity** | **Weak / inconsistent.** Sometimes returns the right language, often defaults to English. | Probably not. | Yes. |
| **Claude** | **Weak.** Defaults to English sources. | No. | Limited. |

**Key auto-translate behaviour:** when Google AI Overviews lacks sufficient native-language content for a query, it **auto-translates English content into the user's language** and serves that. This is *exactly* the symptom of an underserved language — and the signal that genuine native content will outrank a translation as soon as it exists.

**For your UK + Indian-language scenario specifically:**

- A UK Indian shop owner querying in English from a UK IP gets UK-localised English results. Standard.
- The same person querying in **Hindi/Punjabi/Gujarati** from a UK IP:
  - **Google AI Mode** — will favour same-language sources, fall back to UK-localised English auto-translation if vernacular content is thin. *This is the gap.*
  - **ChatGPT/Perplexity** — likely retrieve English UK content, may answer *in* the user's language but cite English sources. A native vernacular page with strong on-page structure has a real shot at being one of the few in-language candidates retrieved.
- Google's localisation operates on a **language × country matrix**, so `en-GB`, `hi-GB`, `pa-GB`, `gu-GB`, `ur-GB` are all distinct slots. Almost no one is filling the non-English UK slots for SME B2B topics.

---

## 5. The "card terminals for the corner shop" thesis

You correctly identified a real micro-niche. Why it's promising:

- **Audience size:** UK has ~46,000 convenience/corner shops; the Asian Trader and ACS data show the sector is disproportionately owned by South Asian families (predominantly Gujarati, Punjabi, and Tamil heritage in the UK).
- **Search intent is high-commercial:** card terminal pricing, contract length, chargeback handling, contactless limits, EPOS integration, cash-and-carry payment, wholesale credit terms.
- **Existing English SERP** is dominated by takepayments, Worldpay, SumUp, Square, Zettle, RMS, Elavon — large competitors with high domain authority. **Direct English ranking is hard.**
- **Vernacular SERP is empty.** Searches like "card machine ਛੋਟੀ ਦੁਕਾਨ ਲਈ" (card machine for small shop, Punjabi) or "कॉर्नर शॉप के लिए कार्ड टर्मिनल यूके" (corner shop card terminal UK, Hindi) return mostly auto-translated English pages or Indian domestic results — neither is right for a UK SME.
- **AIO behaviour confirms the gap:** when AIO can't find quality vernacular content, it auto-translates English. Publishing native-quality vernacular content displaces the translation.

### Adjacent niches that share the pattern

The same play works for any UK-diaspora-owned SME vertical where the operator's first language ≠ English:
- EPOS / till systems
- Business insurance (off-licence, takeaway, MOT garage)
- Asset finance and merchant cash advance
- Wholesale / cash-and-carry account setup
- HMRC / VAT / Making Tax Digital basics
- Food hygiene / EHO compliance
- Off-licence / premises licence applications
- Halal / vegetarian supply chain

---

## 6. Strategy to rank fast

If you commit to this, the playbook:

1. **One language per site, or one well-structured subfolder per language.** Use `/hi/`, `/pa/`, `/gu/`, `/ur/` subfolders, not subdomains. Add `hreflang="hi-GB"`, `pa-GB`, `gu-GB`, `ur-GB`, plus `x-default`.
2. **Native writers, not machine translation.** Google AI Mode and AIO can *detect unnatural language patterns* and down-rank. Hire diaspora writers — they exist and are cheap relative to the moat they create.
3. **Lead every page with the answer.** First 30% of the page does 44% of the LLM-citation work. Definition box, then FAQ, then depth.
4. **Build topical clusters, not islands.** Around "card terminals for UK corner shops" you want: pricing comparison, contract gotchas, chargebacks, contactless limits, integration with common EPOS, PCI-DSS basics, what to do when terminal fails on a Friday night, etc. Ten interconnected pages outrank one hero page.
5. **Geo-target deliberately.** UK address in schema, UK phone, UK case studies with named towns (Southall, Leicester, Hounslow, Wembley, Birmingham, Bradford, Glasgow). Local entity signals are what convince Google your `hi-GB` page is *for* the UK.
6. **Get cited by aggregators.** ChatGPT and Perplexity heavily retrieve from Reddit, Wikipedia, review sites and trade press (Asian Trader, BetterRetailing). Seed presence there.
7. **Schema markup:** `LocalBusiness`, `Product`, `FAQPage`, `HowTo`, `Article` with `inLanguage` set per page.
8. **Test actively.** Run the same query in Hindi/Punjabi/Gujarati from a UK IP across Google AI Mode, ChatGPT, Perplexity, Copilot weekly. Track which platforms cite you and which auto-translate around you.
9. **Don't cannibalise English.** Keep the English site if you have one — different URL, different language, hreflang linked. They feed each other.
10. **Time horizon:** expect first AIO appearances on long-tail vernacular queries in **4–8 weeks**. Meaningful traffic in **3–6 months**.

---

## 7. Risks and caveats

- **Audience behaviour reality check.** UK-born second/third-generation South Asians overwhelmingly search in English. The buyer of card terminals is more often the *child* running the shop's admin than the first-generation owner. Validate with actual search-volume data and customer interviews before committing.
- **Hinglish/Punglish is real.** Many users mix scripts and languages in one query. Plan for transliterated keywords (Roman script Hindi, e.g. "card machine kitne ka aata hai") alongside Devanagari/Gurmukhi.
- **Auto-translation arms race.** Google is improving its on-the-fly translation. If you publish thin vernacular content, you'll be replaced by a better English page auto-translated. Quality and depth are non-negotiable.
- **ChatGPT/Perplexity may answer in the user's language but never click through to you.** Brand mention without traffic is a real GEO outcome — measure mentions, not just clicks.
- **Don't conflate "Indian language" with one language.** Hindi, Punjabi, Gujarati, Urdu, Tamil, Bengali are different audiences with different scripts and different UK concentrations.

---

## 8. Open questions worth answering before building

- What's the *actual* monthly UK search volume for the top 20 vernacular queries in this niche? (Free: Google Keyword Planner with UK + Hindi/Punjabi locale. Paid: Ahrefs / Semrush, but coverage in vernacular is thin — verify with Google Trends.)
- Do the target merchants prefer voice or text? (Voice search adoption among Indian-language users in the UK is high and growing — this changes content format.)
- Is the goal traffic, leads, or brand mentions in AI answers? Each implies a different content shape.
- Would a pure directory/aggregator play (like India's Mobile Ki Dukaan) outperform a brand-led content site? Aggregators are heavily retrieved by ChatGPT/Perplexity.

---

---

## 9. Language × geography × niche — where vernacular content can actually win

The pattern that works has four ingredients: **(a)** a diaspora or migrant audience large enough to matter, **(b)** concentrated in a specific country/region, **(c)** doing a B2B or high-stakes task where the *operator* is first-generation and not English-confident, **(d)** dominated in English-language SERPs by a few high-DA national players who'll never localise.

### UK matrix (your starting market)

| Audience | Language(s) | UK concentration | Niches with the strongest gap |
|---|---|---|---|
| Indian / Pakistani / Bangladeshi corner-shop & off-licence owners | Punjabi (Gurmukhi + Shahmukhi), Hindi, Gujarati, Urdu, Bengali | Southall, Hounslow, Wembley, Leicester, Birmingham, Bradford, Tower Hamlets, Glasgow | Card terminals, EPOS, business banking, off-licence/premises licence, alcohol wholesale, tobacco track-and-trace, MTD/VAT, business insurance, refrigeration finance, lottery terminal setup |
| Polish small-business owners (builders, mechanics, beauticians, food shops) | Polish | Ealing, Slough, Boston (Lincs), Crewe, Northampton | CIS/self-assessment, van insurance, MOT/garage compliance, food hygiene, payroll for 1–3 staff |
| Romanian / Bulgarian | Romanian, Bulgarian | Harrow, Edmonton, Wood Green, Luton | Self-employed registration, UTR, settled-status linked banking, car-wash compliance |
| Turkish / Kurdish (kebab, barber, mini-mart) | Turkish, Kurdish (Kurmanji) | Haringey, Enfield, Hackney | Catering insurance, EHO food hygiene, barber licensing, EPOS for restaurants |
| Chinese (takeaway, Chinese supermarket, nail bar) | Simplified + Traditional Chinese, Cantonese | Manchester, Birmingham, Soho, Cricklewood | Restaurant compliance, supplier wholesale accounts, Alipay/WeChat Pay UK, work-permit/visa-linked employment law |
| Vietnamese (nail bar) | Vietnamese | Hackney, Deptford, Croydon | Salon insurance, COSHH compliance, lease assignments |
| Somali / Eritrean (mini-cab, mini-mart, money transfer) | Somali, Tigrinya | Whitechapel, Streatham, Cardiff | PHV licensing, money-service-business compliance, Uber/Bolt onboarding |
| Nigerian / Ghanaian (logistics, freight, food import, beauty) | English mostly, but Yoruba/Igbo/Twi for community trust signals | Peckham, Thamesmead, Dagenham | UK-Africa freight, halal/cultural food import, hair/beauty wholesale |
| Filipino (care work, nursing agency) | Tagalog | Barking, Ilford, Manchester | Care-home compliance, sponsor-licence guidance, NMC pin maintenance |
| Brazilian / Portuguese (cleaning, construction, beauty) | Brazilian Portuguese | Brent, Bayswater, Stockwell | Self-employed registration, CIS, public liability insurance |
| Ukrainian (post-2022) | Ukrainian | Nationwide, dispersed | Banking with limited credit history, recognition of foreign qualifications, business setup under Homes-for-Ukraine |

### The same pattern outside the UK

The framework is portable. A few high-confidence examples:

- **USA** — Spanish for bodega/taquería/auto-shop owners (NY, LA, Miami, Texas); Vietnamese for nail salons (CA, TX); Korean for dry-cleaners and BBQ (LA, NJ); Mandarin for restaurants and freight forwarders; Hindi/Gujarati for motel owners (notably the Patel motel network).
- **Canada** — Punjabi for trucking and freight (Brampton, Surrey); Tagalog for care agencies; Mandarin for property management.
- **Australia** — Mandarin/Cantonese for hospitality and import; Punjabi for trucking and farming labour (Sydney, Melbourne); Vietnamese for bakeries and nail salons.
- **Germany** — Turkish for kebab and trades (Berlin, Köln, Duisburg); Polish for trades and cleaning; Russian/Ukrainian for IT contracting.
- **France** — Arabic / Maghrebi for halal supply, taxi and auto trades; Portuguese for construction.
- **UAE / Gulf** — Malayalam, Tamil, Bengali, Urdu for restaurant labour, taxi, salon and small-trade owners — vast underserved B2B vernacular market in a wealthy economy.
- **Singapore / Malaysia** — Tamil and Bahasa for SME compliance, especially F&B.

**Filter test before picking one:** if the *English* version of the niche keyword has 5+ entrenched national brands ranking on page 1 with high DA, AND the audience is concentrated in 3–10 known postcodes/cities, AND the buyer is the first-generation operator (not the kid running admin), AND the topic involves regulation, money or contracts where mistakes are expensive — you have a proper gap. The card-terminal-for-corner-shop hits all four.

---

## 10. Pages or websites? And how much to translate?

### Short answer

- **A single translated page bolted onto an English site does almost nothing.** AI Overviews and AI Mode score *site-level* topical depth and entity association. One Hindi page on an English domain reads as opportunistic.
- **The minimum that works is a "language section" — a clustered subfolder** (e.g., `yoursite.co.uk/hi/...`) with **at least 8–12 interconnected pages** covering the topic from multiple angles, plus proper hreflang back to the English equivalents.
- **A standalone vernacular site can also work** and is sometimes faster (no English baggage, every signal is in-language), but you forfeit the consolidated authority of an existing English domain.
- **Whole site translated 1:1 is usually wasteful.** You don't need a Punjabi version of your investor page. Translate the *commercial cluster* the audience cares about.

### Subfolder vs subdomain vs separate domain

| Option | Best for | Watch-outs |
|---|---|---|
| `yoursite.co.uk/hi/` (subfolder) — **recommended** | Inheriting domain authority; cleanest hreflang; cheapest to maintain. | Must have proper hreflang and `lang` attributes; can't easily host on different infra. |
| `hi.yoursite.co.uk` (subdomain) | When you need a separate tech stack or CMS per language. | Google treats it as more of a separate property; less authority transfer. |
| `yoursite.in` / `yoursite.co.in` (separate ccTLD) | Strong country signal, e.g., targeting India itself. | Doesn't help "Hindi-speakers in UK" — wrong country signal. |
| Single dedicated brand (`punjabicardterminals.co.uk`) | Pure-play vernacular brand; full focus; can rank without English baggage. | Builds authority from zero; needs its own backlinks and citations. |

For "UK + Indian-language SME" the realistic shapes are: **(1)** add a `/hi/`, `/pa/`, `/gu/` subfolder to an existing English site, **OR (2)** build a dedicated UK vernacular brand on a `.co.uk`. Don't use an Indian ccTLD — it's a country mismatch.

### What "ranking-ready vs bolted-on" looks like

A cluster that's actually citation-ready in one language has roughly:

- 1 pillar page (e.g., "Card terminals for UK corner shops, in Punjabi")
- 4–6 supporting commercial pages (pricing comparison, contract gotchas, contactless limits, integration with EPOS, chargebacks, what to do when terminal fails)
- 4–6 informational/FAQ pages (PCI-DSS in plain Punjabi, contactless limit changes, refund handling, what is a chargeback)
- All cross-linked, all with FAQ schema, all with the answer in the first 30% of the page
- Hreflang clusters back to English equivalents
- Local entity signals (UK address, UK phone, named UK case studies)

Eight to twelve pages is roughly the threshold where the model treats your site as a topical authority in that language for that niche. Below that, you're a translated landing page.

---

## 11. Does the same strategy work for classic SEO and AI search? And does *everything* need to be in the language?

### Strategy overlap

Yes — about **80% of the work is shared**. AI search and classic SEO both reward: clear structure, topical clusters, native-quality language, geo-signals, schema, fast pages, internal linking, citations from trusted sources. The 20% that differs:

- **Classic SEO** still rewards backlinks and exact-match keywords; both matter much less for AIO/LLM citation.
- **AI search** rewards "extractable" formats (definitions, lists, FAQ blocks, tables) and answer-first structure far more aggressively. The first 30% of a page does ~44% of LLM citation work.
- **AI search** rewards being mentioned across the wider web (Reddit, Wikipedia, trade press, forums). LLMs heavily retrieve aggregator content. Classic SEO doesn't lean on this as hard.
- **AI search** doesn't always send a click — your KPI mix shifts toward *brand mentions in answers*, not just sessions.

So: build for AI search and you mostly get classic SEO for free. The reverse is no longer true.

### What needs to be translated

Anything that the search engine, the LLM, *or* the user reads. Practically:

| Element | Translate? | Why |
|---|---|---|
| Visible body content | **Yes — natively, by a human** | The single biggest signal. Machine translation is detectable and down-ranked. |
| H1, H2, H3 headings | **Yes** | Structural extraction signals; AIO pulls from headings. |
| Title tag | **Yes** | Click-through and language-detection signal. |
| Meta description | **Yes** | Click-through; appears in SERP snippets in target language. |
| URL slug | **Yes** (in target script or transliterated Roman) | "mysite.co.uk/hi/कार्ड-टर्मिनल" or "mysite.co.uk/hi/card-terminal-corner-shop" — both acceptable, transliterated Roman is often more practical because of CMS and link-sharing constraints. |
| Image `alt` text | **Yes** | Accessibility + image search + AIO image grounding. |
| Image filenames (where reasonable) | Optional | Marginal benefit. |
| Schema / structured data (`name`, `description`, `offers`, FAQ Q&A) | **Yes** | LLMs read JSON-LD heavily. Mixed-language schema confuses both Google and the model. |
| `<html lang="hi">` (or `lang="pa"`, etc.) | **Yes — set per page** | Primary language signal Google uses now that it leans away from hreflang for detection. |
| `hreflang` cluster | **Yes — bidirectional** | `hi-GB`, `pa-GB`, `gu-GB`, `ur-GB`, plus `en-GB` and `x-default`. Every page in the cluster must reference every other. |
| Open Graph / Twitter card metadata | **Yes** | Social previews drive aggregator pickup, which feeds LLM retrieval. |
| Breadcrumbs | **Yes** | Both visible and in schema. |
| Internal anchor text | **Yes** | Topical entity signal in target language. |
| Form labels, button text, error messages | **Yes** | Trust + bounce-rate signal. |
| Reviews and testimonials | **Yes if possible — keep originals too** | Native reviews are gold for AIO local snippets. |
| Privacy policy / T&Cs / cookie banner | **Yes** | Trust signal; affects E-E-A-T. |
| Phone number, address, opening hours | Keep UK format — don't "translate" the data | Localise *presentation* (script of digits is fine in most languages) but keep the entity data as the canonical UK NAP. |
| Currency | **GBP — never convert to INR/PKR** | Country signal. The whole point is "UK in Hindi", not "India in Hindi". |
| Sitemap.xml | **Yes — list both language URLs with proper `xhtml:link` hreflang annotations** | Helps Google index every variant. |
| robots.txt | No translation needed | It's only directives. |
| `canonical` | **Self-referencing per language version** | Don't canonicalise the Hindi page to the English page — that wipes it from the index. |

### Is there one tag that flags "this page is in language X" to all three (Google AIO, ChatGPT, Perplexity, Copilot)?

**No single magic tag.** There isn't a universal "I am in Hindi" flag. Each system reads a different combination, and **none of them rely solely on the markup — they all also detect language from the actual content.** The robust pattern is to send the same signal through five different channels so that whichever one a given AI reads, you're covered.

The five signals to ship together on every translated page:

1. **`<html lang="hi-GB">`** (or `pa-GB`, `gu-GB`, `ur-GB`)
   The primary HTML language attribute. Google has confirmed this is now its main programmatic language signal — it's leaning *away* from hreflang for detection. Always include the country suffix to lock the geo target.
2. **`<link rel="alternate" hreflang="hi-GB" href="..." />`** in the `<head>`
   Plus a matching set for every other language version of that page, plus `x-default`. Bidirectional — every page in the cluster references every other. Google AIO and Bing/Copilot use this for *which version to serve* once language is known.
3. **`Content-Language: hi-GB`** HTTP response header
   Older standard, still honoured. Costs nothing to set in the server config.
4. **JSON-LD schema with `"inLanguage": "hi-GB"`** on every entity (Article, FAQPage, LocalBusiness, Product)
   This is the one most sites miss — and it's the most useful for *LLM* retrievers (ChatGPT, Perplexity, Claude), which lean heavily on structured data.
5. **`<meta property="og:locale" content="hi_IN">`** (note the underscore + ISO country code; `og:locale` doesn't accept GB-suffixed Hindi cleanly, so use the closest standard locale and rely on the other four signals for the UK targeting)
   Picked up by social aggregators, which feed LLM training and retrieval indirectly.

Plus the **sitemap.xml** entries with `<xhtml:link rel="alternate" hreflang="..." />` annotations so Google's crawler sees the cluster from the index side.

How each platform actually uses these:

- **Google AI Overviews / AI Mode** — reads all five, plus runs its own content-based detection. `<html lang>` and hreflang carry the most weight.
- **Bing / Copilot** — reads hreflang and `<html lang>` reliably.
- **ChatGPT / Perplexity / Claude** — there's **no public evidence they parse hreflang at all**. They infer language primarily from the content itself, the URL, and to some extent the JSON-LD `inLanguage` field. This is why **the content has to be unmistakably native** — the markup alone won't save a machine-translated page.

**Punchline:** ship all five signals (it's <30 minutes of work per template once), but treat them as a backup. The 90% signal is that the visible content, headings, schema and meta description are all in clean, native, human-written target language. If you only do one thing, set `<html lang="hi-GB">` and write the page itself in fluent Punjabi/Hindi/Gujarati. Everything else is reinforcement.

### Things people get wrong

- Translating the body but leaving the title tag, meta description and schema in English. Result: SERP snippet shows in English, click-through tanks, language signal becomes mixed, AI Mode often serves the English version even on a Hindi query.
- Auto-translating with a plugin and shipping it. Detectable, down-ranked, and AIO will prefer the auto-translated *English* original over a clearly machine-translated "native" page.
- Pointing canonical from `/hi/page` back to `/en/page`. This deindexes the Hindi version. Use self-canonical + hreflang.
- Mixing scripts in one URL or page (e.g., body in Devanagari, navigation in English). Pick one primary language per page and stick to it.
- Forgetting `<html lang="...">`. It's the most reliable signal Google currently uses for language detection.
- Translating brand names. Don't. "Visa" stays "Visa". "takepayments" stays "takepayments".

---

---

## 12. The basic plan — read this first

Plain-English playbook. If you only read one section, read this one.

### Step 1 — Pick the target before you build anything

Pick **one** language × one country × one niche to start. Do not start with three. Filter:

- Audience is **first-generation, not English-confident**, and is the actual buyer (not their kid).
- Concentrated in **3–10 known towns or postcodes** so geo-signals are easy.
- English SERP is dominated by **3+ big national brands** you can't outrank in English.
- Topic involves **money, regulation or contracts** where mistakes cost real money — that's what makes the user actually search.

Example: "UK + Punjabi + card terminals for corner shops" passes all four. "UK + French + general accountancy" fails — French speakers in the UK skew professional and English-fluent.

### Step 2 — Decide pages vs site

There are three realistic shapes. Pick one.

| Shape | When to pick it | Effort |
|---|---|---|
| **A. Subfolder on an existing English site** — e.g., `yoursite.co.uk/pa/...` | You already have a site with some authority you want to extend. Cheapest, fastest, best link equity. **Default choice.** | Low |
| **B. Standalone vernacular brand** — e.g., `punjabicardterminals.co.uk` | You want a pure-play, no English baggage, sharper brand for the audience. Slower to build authority but cleaner positioning. | Medium |
| **C. Subdomain** — e.g., `pa.yoursite.co.uk` | Only if you genuinely need separate tech/CMS per language. Otherwise don't bother. | Medium |

**Don't** use a foreign country domain (`.in`, `.pk`) — that signals India/Pakistan, not the UK. Always `.co.uk` for a UK audience.

### Step 3 — Decide what to translate (NOT the whole site)

Translate the **commercial cluster** that the audience actually buys from. Leave the rest in English.

A cluster is roughly **8–12 interconnected pages**:

- 1 pillar page: "Card terminals for UK corner shops" (in Punjabi)
- 4–6 commercial pages: pricing, contracts, contactless limits, EPOS integration, chargebacks, terminal failure
- 4–6 informational/FAQ pages: PCI-DSS in plain Punjabi, refunds, what is a chargeback, etc.

Don't translate your About page, investor page, blog archive. Waste of money.

### Step 4 — Same page twice in different languages? Yes — that's the model

This is exactly how multilingual sites work. You have:

- `yoursite.co.uk/card-terminals` (English)
- `yoursite.co.uk/pa/card-terminals` (Punjabi version of the same thing)
- `yoursite.co.uk/hi/card-terminals` (Hindi version)

These are **not duplicate content** as far as Google is concerned, *as long as the body is genuinely translated*. They link to each other via hreflang, each has its own self-canonical, and each ranks in its own language. This is the standard pattern.

Critical rules:

- Each version has a **self-canonical** (`/pa/card-terminals` canonicalises to itself, NOT to the English page). Pointing canonicals back to English deindexes the translated versions — common, fatal mistake.
- All versions reference each other via `hreflang` in the `<head>` and in the sitemap.
- Each version has its own `<html lang="...">` set correctly.
- You don't need 1:1 page parity. It's fine if the English site has 200 pages and the Punjabi cluster has 12. Map the 12 to their English equivalents and that's enough.

### Step 5 — Language switcher? Yes, but build it the right way

You DO want a visible "EN | ਪੰਜਾਬੀ | हिन्दी" switcher in the header — it's good UX and a strong language signal. But how you implement it matters a lot:

**Do this:**

- The switcher is a set of **actual links** to actual translated URLs (`/en/card-terminals`, `/pa/card-terminals`, `/hi/card-terminals`).
- Clicking it changes the URL. The new page is genuinely indexed and crawlable.
- Remember the user's choice in a cookie so they don't have to pick again next visit.
- Auto-suggest a language based on `Accept-Language` header *with* their permission, but never auto-redirect — Google's John Mueller has repeatedly said auto-redirect on language breaks crawling.

**Don't do this:**

- ❌ **Google Translate widget** — JavaScript translation that doesn't change the URL. Search engines and LLMs see the original English page only. Zero ranking benefit. Looks like effort but does nothing.
- ❌ Any **client-side JS translation** for the same reason.
- ❌ **Auto-redirect** based on IP or browser language — confuses crawlers, traps users in the wrong version.
- ❌ A **single page that toggles language with a button** but keeps the URL the same. The translated version is invisible to search.

Test: visit your translated page in Chrome incognito with JS disabled. If the translated text is gone, your switcher is broken for SEO and AI search. The translation has to be in the HTML the server returns, not injected by the browser.

### Step 6 — Translate everything on the translated page

On every translated page, translate:

- Body, headings, title tag, meta description, URL slug, image alt text, schema (especially `inLanguage`), Open Graph, breadcrumbs, internal anchor text, form labels, button text, T&Cs link text.

Keep the entity data canonical (UK address, GBP, UK phone). You're "UK in Punjabi", not "Punjab in Punjabi".

### Step 7 — Ship the five language signals

On every translated page, all of these:

1. `<html lang="pa-GB">`
2. `<link rel="alternate" hreflang="pa-GB" href="...">` cluster, bidirectional, plus `x-default`
3. `Content-Language: pa-GB` HTTP header
4. JSON-LD schema with `"inLanguage": "pa-GB"`
5. `<meta property="og:locale" content="pa_IN">` (use `pa_IN` because OG locales don't take GB-suffixed Punjabi cleanly; the other four signals carry the UK targeting)

Plus sitemap.xml entries with `<xhtml:link rel="alternate" hreflang="...">` annotations.

### Step 8 — Hire a native writer, not a translator

Machine translation is detectable and down-ranked by Google AI Mode. A "translator" who works word-by-word produces stiff text. You want a **native speaker who lives in the UK diaspora context** — someone who knows the audience says "card machine" and "PDQ" and not the textbook word for "payment terminal". For Punjabi specifically, decide which script (Gurmukhi vs Shahmukhi) up front based on audience research — Sikh-heritage UK Punjabi audiences mostly read Gurmukhi.

Plan for **Hinglish/Punglish/Romanised script**: many users type "card machine kitne ka hai" in Roman letters. Cover both the script version and a transliterated Roman version of high-value keywords.

### Step 9 — Get listed where AIs actually look

Google AI Overviews and ChatGPT both heavily retrieve from a small set of trusted aggregators. For UK SME niches, get presence on:

- Asian Trader, Better Retailing, Convenience Store (trade press)
- Reddit (r/CasualUK, r/UKPersonalFinance, niche subs) — even short comments help
- Wikipedia (where genuinely relevant)
- Local trade directories
- YouTube — short native-language explainers; AI Overviews increasingly cite video transcripts

### Step 10 — Measure the right things

Don't just track sessions. Track:

- AI Overview impressions / clicks (Search Console)
- Brand mentions in ChatGPT, Perplexity and Google AI Mode answers — run the top 20 vernacular queries weekly from a UK IP and screenshot
- Click-through rate on translated SERP snippets (low CTR = title/meta need work)
- Conversion rate vs the English version

**Time horizon:** first AIO appearances on long-tail vernacular queries in 4–8 weeks. Meaningful traffic in 3–6 months. Real moat in 9–12 months.

---

## 13. Target list — language × audience × niches

Don't be precious about stereotyping; this is straight from ONS, ACS and trade-association data on who actually owns what kind of UK business. Pick combos where **all three** boxes are true: (1) audience is concentrated, (2) operator is first-generation, (3) topic is regulated/financial/contractual.

### UK — primary targets

| # | Language | Audience | Where in UK | Niches worth targeting |
|---|---|---|---|---|
| 1 | **Punjabi (Gurmukhi)** | Sikh-heritage corner-shop, off-licence, taxi, transport owners | Southall, Hounslow, Wolverhampton, Birmingham (Handsworth), Glasgow, Bradford, Leicester (Belgrave) | Card terminals, EPOS, off-licence/premises licence, alcohol & tobacco wholesale, lottery terminal, taxi PHV licensing, business insurance, MTD/VAT, refrigeration finance |
| 2 | **Hindi (Devanagari)** | Indian-origin corner-shop, pharmacy, restaurant, motel/B&B owners | Wembley, Harrow, Leicester, Croydon, Manchester | Card terminals, EPOS, pharmacy compliance, NHS contracting, food hygiene, premises licence, business banking, commercial mortgages |
| 3 | **Gujarati** | Newsagent, off-licence, post-office, jewellery, pharmacy owners (large historic UK community) | Leicester, Wembley, Harrow, Bolton, North London | Newsagent supply, post-office sub-postmaster compliance, jewellery hallmarking, pharmacy ownership, card terminals, business insurance |
| 4 | **Urdu (Shahmukhi script)** | Pakistani-origin taxi, restaurant, mini-mart, halal butcher, takeaway owners | Bradford, Birmingham (Sparkbrook), Manchester (Rusholme), Luton, East London | Taxi PHV licensing, halal certification, food hygiene, takeaway compliance, business insurance, money-service-business compliance |
| 5 | **Bengali** | Bangladeshi-origin restaurant (curry house), mini-mart owners | Tower Hamlets, Camden, Oldham, Luton | Restaurant compliance, EHO food hygiene, alcohol licence, employment law (kitchen staff), business banking |
| 6 | **Tamil** | Sri Lankan-origin convenience store, takeaway, pharmacy, accountancy SMEs | Wembley, Tooting, East Ham, Croydon | Convenience-store ops, pharmacy ownership, accountancy practice setup |
| 7 | **Polish** | Tradespeople, mechanics, beauticians, food shop owners, cleaners | Ealing, Hammersmith, Slough, Boston (Lincs), Crewe, Northampton, Southampton | CIS/self-assessment, van insurance, MOT/garage compliance, public liability, food hygiene, payroll for 1–3 staff, building regs basics |
| 8 | **Romanian** | Self-employed builders, car-wash operators, drivers | Harrow, Edmonton, Wood Green, Luton, Wembley | Self-employed registration, UTR, banking with limited credit history, car-wash compliance, CIS |
| 9 | **Bulgarian** | Drivers, cleaners, small builders | Same areas as Romanian, plus Reading, Slough | Self-employed registration, ride-hail onboarding, cleaning-business setup |
| 10 | **Turkish / Kurdish (Kurmanji)** | Kebab shops, barbers, mini-marts, bakers | Haringey, Enfield (Green Lanes), Hackney, Lewisham | Catering insurance, EHO food hygiene, barber/salon licensing, premises licence, EPOS for restaurants |
| 11 | **Mandarin (Simplified)** | Takeaways, Chinese supermarkets, freight forwarders, property landlords | Manchester, Birmingham, Soho, Cricklewood, Cambridge | Restaurant compliance, supplier wholesale accounts, Alipay/WeChat Pay UK acceptance, employment law for sponsored workers, freight forwarding compliance |
| 12 | **Cantonese / Traditional Chinese** | Older Hong Kong–origin restaurant and takeaway owners | Soho, Manchester Chinatown, Birmingham, Newcastle | Same as Mandarin but cultural language preference for older operators |
| 13 | **Vietnamese** | Nail-bar owners, bakers (banh mi shops), small restaurants | Hackney, Deptford, Croydon, Birmingham | Salon insurance, COSHH compliance, lease assignments, EHO food hygiene |
| 14 | **Korean** | Restaurants, beauty stores, K-pop retail | New Malden, central London | Restaurant compliance, import paperwork, EPOS, employment law |
| 15 | **Arabic (Modern Standard / Levantine / Maghrebi)** | Restaurants, shisha lounges, halal butchers, mini-marts, money-transfer | Edgware Road, Whitechapel, Birmingham (Alum Rock), Manchester (Rusholme) | Halal certification, shisha licensing, money-service-business compliance, restaurant compliance |
| 16 | **Somali** | Mini-cab firms, mini-marts, money-transfer (hawala-related), cafes | Whitechapel, Streatham, Tower Hamlets, Cardiff (Butetown), Bristol (Easton), Birmingham (Small Heath) | PHV licensing, money-service-business compliance, mini-mart setup, employment law |
| 17 | **Tigrinya / Amharic** | Cafes, mini-cabs | Camden, Wood Green, Brixton | Same as Somali, smaller volume |
| 18 | **Yoruba / Igbo / Twi** | Logistics, freight, food import, hair & beauty wholesale, salons (mostly English-speaking but vernacular trust signals work) | Peckham, Thamesmead, Dagenham, Leyton | UK–West Africa freight, halal/cultural food import, hair/beauty wholesale, salon licensing |
| 19 | **Tagalog (Filipino)** | Care workers, nursing-agency staff, cleaners | Barking, Ilford, Manchester, Earls Court | Care-home compliance, sponsor-licence guidance, NMC pin maintenance, nursing-agency setup |
| 20 | **Brazilian Portuguese** | Cleaners, builders, beauticians, food trucks | Brent, Bayswater, Stockwell, Willesden | Self-employed registration, CIS, public liability insurance, food-hygiene cert |
| 21 | **Portuguese (European)** | Construction, restaurants | Stockwell, Vauxhall, Reading | CIS, restaurant compliance |
| 22 | **Spanish (Latin American)** | Cleaners, food vendors, hospitality | Elephant & Castle, Seven Sisters, Brixton | Self-employed registration, market-stall licensing, food hygiene |
| 23 | **Russian / Ukrainian** | IT contractors, beauty industry, small import/export, post-2022 Ukrainian small businesses | Dispersed, with concentrations in West London, Manchester | Banking with limited credit history, recognition of foreign qualifications, IT contracting via umbrella, business setup under Homes-for-Ukraine |
| 24 | **Nepali** | Ex-Gurkha small businesses, restaurants, care workers | Aldershot, Folkestone, Reading | Pension and resettlement, restaurant compliance, care-home setup |
| 25 | **Albanian** | Construction, car washes, small import | North London (Wood Green), Luton | Self-employed registration, car-wash compliance, construction insurance |

### Tier-1 starting candidates (highest gap × highest value)

If you want to pick the three strongest plays to test first:

1. **Punjabi → corner-shop card terminals & EPOS** — exactly your original thesis. Concentrated audience, regulated topic, English SERP locked up by national brands, almost zero vernacular competition.
2. **Polish → CIS, van insurance, MOT garage compliance** — huge audience (~700k Polish-born in UK), genuinely first-generation operator, English SERP dominated by big insurers, vernacular content thin.
3. **Urdu → taxi PHV licensing & halal food compliance** — Bradford/Birmingham/Luton, regulated topic, first-generation audience, English content is generic council-website material that doesn't speak the operator's language.

### Outside the UK (same framework)

- **USA**: Spanish (bodega, taquería, auto-shop in NY/LA/Texas/Miami), Vietnamese (nail salons in CA/TX), Korean (dry cleaners in NJ/LA), Mandarin (restaurants/freight), Hindi/Gujarati (motels — the "Patel motel" network).
- **Canada**: Punjabi (trucking & freight in Brampton/Surrey), Tagalog (care agencies), Mandarin (property management).
- **Australia**: Mandarin/Cantonese (hospitality/import), Punjabi (trucking/farming labour), Vietnamese (bakeries/nails).
- **Germany**: Turkish (kebab/trades in Berlin/Köln/Duisburg), Polish (trades/cleaning), Russian/Ukrainian (IT contracting).
- **France**: Arabic/Maghrebi (halal supply, taxi, auto), Portuguese (construction).
- **UAE / Gulf**: Malayalam, Tamil, Bengali, Urdu (restaurant labour, taxi, salon SMEs — wealthy economy, vast vernacular audience).
- **Singapore / Malaysia**: Tamil and Bahasa for SME compliance, especially F&B.

The framework is the same wherever you point it: pick the diaspora, find their concentration, find the regulated topic, write natively, ship the five signals.

---

## 14. Covering all three — when the play is mostly SEO + Google AI Overviews

You're right that this is realistically a **Google-led play** for vernacular UK content. Google AI Mode handles Hindi/Punjabi/Gujarati natively and respects `hreflang` + `<html lang>`. ChatGPT, Perplexity and Claude default to English sources even when the query and answer are in another language — they're a smaller, less reliable channel. But the marginal cost of also covering them is low if you've already done the Google work, and the **brand-mention upside** in AI answers is real even without clicks.

### Realistic effort split

| Channel | Share of effort | Why |
|---|---|---|
| Google (classic SEO + AI Overviews + AI Mode) | **~70%** | Largest audience, best language handling, respects all your signals, returns clicks. |
| Microsoft (Bing + Copilot) | **~15%** | Free wins; Bing handles multilingual properly; Copilot inherits it. Most of the work is already done. |
| ChatGPT / Perplexity / Claude | **~15%** | Defaults to English, smaller share of vernacular search, but generates brand mentions in answers. Worth doing for visibility, not for traffic. |

### What you do *once* that covers all three

These are signals every modern AI search system reads. Doing them gives you Google + Bing + LLMs together:

1. **Native-quality content in target language**, answer-first, in the top 30% of every page. (Highest single-factor signal across all three.)
2. **The five language tags** from §11: `<html lang>`, hreflang, `Content-Language` header, JSON-LD `inLanguage`, `og:locale`.
3. **JSON-LD schema** on every page: `Article`, `FAQPage`, `HowTo`, `LocalBusiness`, `Product` — with all string fields in the target language. **LLMs read JSON-LD heavily.** This is the single biggest "covers all three" signal that most sites skip.
4. **Topical cluster** of 8–12 interconnected pages, internally linked with native-language anchor text.
5. **Real URL-based language switcher** (no JS-only translation, no auto-redirect).

### What's specific to Google AI Overviews + classic SEO

- `hreflang` cluster, bidirectional, plus `x-default`. (Critical for Google; ChatGPT ignores it.)
- Search Console set up per language version, sitemaps with `<xhtml:link>` annotations.
- `LocalBusiness` schema with UK address, UK phone, named UK case studies.
- Google Business Profile in the local language (you can set the primary language of a GBP listing).
- Internal linking from your strongest existing English pages into the new vernacular cluster.
- Backlinks from UK trade press (Asian Trader, Better Retailing, Convenience Store, ACS).

### What's specific to Bing + Copilot

Mostly piggybacks on the Google work, but worth ten minutes:

- **Bing Webmaster Tools** — submit the site, submit each language sitemap separately. Bing supports hreflang and uses it.
- **IndexNow** — Bing-led protocol for instant URL submission. If you're on Cloudflare or a modern CMS, it's a one-click toggle.
- **LinkedIn presence** in target language. Bing/Copilot weight LinkedIn content heavily.

### What's specific to ChatGPT, Perplexity and Claude

This is where the work is genuinely different. These LLMs don't respect `hreflang`, they detect language from content/URL/schema, and they retrieve heavily from a small set of trusted aggregators. So:

1. **Allow the bots in `robots.txt`.** This is the single most missed step. Don't block them or you get zero exposure.
   ```
   User-agent: GPTBot
   Allow: /

   User-agent: ChatGPT-User
   Allow: /

   User-agent: OAI-SearchBot
   Allow: /

   User-agent: PerplexityBot
   Allow: /

   User-agent: Perplexity-User
   Allow: /

   User-agent: ClaudeBot
   Allow: /

   User-agent: Claude-Web
   Allow: /

   User-agent: Google-Extended
   Allow: /

   User-agent: Applebot-Extended
   Allow: /
   ```
   `Google-Extended` controls whether Gemini training and AI Overviews can use your content; `Applebot-Extended` does the same for Apple Intelligence. If you want to *opt out* of training but still appear in answers, you need a more nuanced setup — but for a publisher trying to be cited, allow all of them.

2. **Ship an `llms.txt` file** at `yoursite.co.uk/llms.txt`. Emerging convention (~2025) — a curated map of your site's content for LLMs, in plain English. Even where it's not formally honoured, it's harmless and well-structured pages get cited more often. List your pillar pages and a one-line summary of each.

3. **URL slugs in target language**, or transliterated Roman script. LLMs use the URL as a strong language hint when they don't read hreflang.

4. **JSON-LD `inLanguage` on every entity.** Cannot stress this enough — this is how ChatGPT/Perplexity infer the page's language when they parse structured data.

5. **Get into the aggregators LLMs retrieve.** For UK SME niches in vernacular languages:
   - **Reddit** — diaspora subs (r/sikh, r/IndiansInUK, r/PolesInTheUK, r/london), niche subs (r/UKPersonalFinance, r/CasualUK, r/sysadmin if relevant). Reddit is heavily retrieved by ChatGPT, often without citation — but the brand mention still seeds the model's "associations". Post in target language where the sub allows.
   - **Wikipedia** — only where genuinely relevant. Cite your source pages from existing Wikipedia articles where editors agree it's appropriate.
   - **YouTube** — short native-language explainers (60–180s) with auto-generated captions in the same language. AI Overviews cites YouTube transcripts; LLMs increasingly index them.
   - **Quora** in target language (yes, it still gets retrieved).
   - **Trade press digital**: Asian Trader, Better Retailing, Convenience Store, Caterer, MotorTrader. A single quote in a trade article gives you brand-entity reinforcement across all three platforms.
   - **Local trade-association directories**: ACS (corner shops), NFRN (newsagents), British Takeaway Campaign, NRLA (landlords).

6. **English shadow page in the same cluster.** Because ChatGPT/Perplexity default to English, having a parallel English page (`/card-terminals` mirroring `/pa/card-terminals`) gives the LLM a path to cite *you* even when it ignores the vernacular version. The English page rides on the same brand entity. This is the highest-leverage single thing you can do specifically for ChatGPT/Perplexity.

7. **Brand mentions, not just backlinks.** LLMs weight unlinked brand mentions almost as heavily as linked ones. PR placements that name the brand without linking still help.

8. **Lead with the answer.** First 30% of the page = 44% of LLM citations (Zyppy 2025). FAQ block above the fold, with the question as a heading and a 1–2 sentence answer.

### Per-platform monitoring (10 minutes a week)

Run the top 20 vernacular queries from a UK IP, weekly, and screenshot:

| Platform | What to capture |
|---|---|
| Google Search (vernacular query, UK IP) | AIO box appears? Are you cited? Position in 10 blue links? |
| Google AI Mode (vernacular query, UK IP) | Are you cited? Is the answer in the right language? |
| Bing Search → Copilot | Same as Google. |
| ChatGPT (web search on, UK IP) | Are you cited inline? Is the answer in target language or English? |
| Perplexity (UK IP) | Are you in the source list? |
| Claude (with web search) | Are you cited? |

Track over 12 weeks. The pattern reveals which channel actually returns value for your niche, and you can re-allocate effort.

### One-line summary

The vernacular play is **Google-first by design**, **Bing free-ride**, and **LLMs as a brand-mention layer**. Native content + the five language tags + schema + an English shadow page covers all three with one production cycle.

---

## 15. Tips, tricks and gotchas

Things that don't fit cleanly into the plan above but move the needle. Grouped by area.

### Content craft

- **Voice search dominates first-gen audiences.** Older Punjabi/Gujarati/Polish users dictate searches into their phone. Write the way the audience *speaks*, not the way it would be written formally. Add long, conversational headings ("ਕੋਨਰ ਸ਼ਾਪ ਲਈ ਕਾਰਡ ਮਸ਼ੀਨ ਕਿੰਨੇ ਦੀ ਮਿਲਦੀ ਹੈ?" / "How much does a card machine cost for a corner shop?").
- **Hinglish / Punglish / Roman-script versions matter.** A non-trivial slice of the audience types the language phonetically in Roman letters: "card machine kitne ka aata hai", "corner shop ke liye terminal". Have a transliterated keyword set as well as the native script set. Map both to the same page where appropriate.
- **Comparative tables are LLM gold.** Side-by-side comparison ("Worldpay vs takepayments vs SumUp for a corner shop, in Punjabi") is one of the most-cited formats in AI Overviews and ChatGPT answers. Build at least one per pillar topic.
- **Lead with original data or a unique quote.** Both Google AI Overviews and LLMs prefer pages that contribute something new ("we surveyed 47 Leicester shopkeepers and found..."). It doesn't have to be a big study — a quote from a named UK shopkeeper, a price you got over the phone, a screenshot of a contract clause is enough.
- **Numbered checklists and definition boxes near the top.** AIO extracts discrete claims. A "What's included" list with 5–8 items will be quoted verbatim.
- **AI-written prose gets down-ranked.** Use AI for outlines, keyword expansion and editing. Have a human native speaker write the prose. Google's March 2026 core update reinforced this. Caveat — pure AI content can rank short-term but degrades fast.
- **"Last updated" date visible** on every page, in target language. Both Google and LLMs weight freshness.
- **Author bio with photo and credentials** at the top or bottom of every commercial page. Real name, real expertise, link to LinkedIn/About page. E-E-A-T signal that matters more than ever.

### Language and script details

- **Punjabi has two scripts: Gurmukhi (Sikh-heritage UK audiences) and Shahmukhi (Pakistani-heritage).** Pick one as primary based on audience research. UK Punjabi for corner shops skews Gurmukhi.
- **Urdu and Arabic are right-to-left.** Your CSS needs `dir="rtl"` on those pages. Get a native QA pass on the layout — buttons, icons, breadcrumbs and tables all need flipping. Forms break in RTL if you don't test.
- **Numerals: stick with Western 0–9 for prices, dates and phone numbers.** Native numerals (Devanagari ०१२, Gurmukhi ੦੧੨, Eastern Arabic ٠١٢) are linguistically correct but cause copy/paste, OCR and CTR issues. Use them sparingly in body text only.
- **Date format: DD/MM/YYYY.** Never US format on a UK-targeted page.
- **Currency: always GBP.** Don't show INR/PKR conversions even for first-gen audiences. The whole point is "UK in your language", not "back home in your language".
- **Don't translate brand names, product names, or established UK acronyms** like HMRC, VAT, MTD, EHO, PHV, PCI-DSS, NMC, CIS, CQC. Transliterate or leave in English.

### Technical SEO

- **Self-canonical, always.** `<link rel="canonical" href="/pa/card-terminals">` on the Punjabi page. Pointing canonicals at the English version deindexes the translated cluster. This is the most common fatal mistake.
- **Sitemap with `<xhtml:link>` hreflang annotations.** Don't just list URLs; annotate language/region pairs.
- **Speed matters more in vernacular markets.** First-gen audience is more likely on older Android phones with patchy 4G. Get to a 90+ Lighthouse score on mobile. Lazy-load images, AVIF/WebP, modest JS.
- **Mobile-first design is non-negotiable** — vernacular UK audiences are 80%+ mobile.
- **Internal anchor text variety.** Don't always link with the same phrase. Mix native-script, transliterated, and English brand-name anchors.
- **Bridge English pages to the vernacular cluster.** Add a subtle "Read this in ਪੰਜਾਬੀ / हिन्दी" link on relevant English pages. Helps crawlers find the cluster and signals language equivalence.
- **Set up Google Business Profile per location with primary language in target.** GBP supports a primary language. Posts in target language drive AIO local citations.

### Off-page / authority

- **Local community media is a free goldmine.** Sunrise Radio (Asian community), Polish Radio London, Asian Sound Manchester, Akash Radio, Lyca Radio, Kismat Radio. A 30-second mention on community radio drives both real customers and named brand mentions LLMs eventually pick up.
- **Diaspora trade press**: Garavi Gujarat, Eastern Eye, Asian Trader, Polish Express, Cooltura. Smaller circulation but the audience is *exactly* your buyer.
- **Place of worship newsletters and noticeboards.** Gurdwaras (Sikh temples), Mandirs (Hindu temples), Mosques, Polish parishes, Pentecostal churches. First-gen owners trust community channels more than ads. Sponsor or contribute content.
- **Reviews in native language are massive trust signals.** Encourage Google Reviews in target script; reply in the same language. Trustpilot supports multiple languages.
- **WhatsApp link sharing is the dominant channel for diaspora communities.** Test how your URLs preview on WhatsApp (OG image, OG title in target language). A great preview spreads through community groups for free.
- **Influencer/community Facebook groups** — search "Sikhs in Leicester", "Polish in Boston Lincs", "Tamils in Tooting" on Facebook. These groups have tens of thousands of members and dwarf any paid acquisition channel for niche audiences.

### UX and trust

- **Owner photo, named team members, real UK address visible.** Trust signals.
- **Click-to-call phone number** in header, in target language, formatted UK. First-gen audiences call before buying.
- **WhatsApp Business contact** as a primary CTA. Diaspora audiences strongly prefer WhatsApp over email or web forms.
- **Live chat / chatbot that responds in target language.** Even a basic flow boosts conversion 2–3x for first-gen audiences.
- **Geographic sub-pages.** "Card terminals for corner shops in Leicester", "...in Southall", "...in Bradford". Each ranks on its own city long-tail. Cheap content with high commercial intent.
- **Named UK case studies.** "Mr Singh's shop in Hounslow saved £600/year." First-gen audience trusts community proof over generic stats.

### Operational

- **Phone hours that match audience hours.** A corner shop owner is busy 6am–11pm and free between rushes. Not 9–5. Out-of-hours WhatsApp coverage wins.
- **Onboarding paperwork in target language.** Translate the contract or at least the summary one-pager. Reduces drop-off massively.
- **Bilingual customer support staff are a moat.** Hire one Punjabi-speaker, one Polish-speaker, one Urdu-speaker. Hard for big competitors to replicate.

### Common errors to avoid

1. **Pointing the canonical from the translated page back to the English page.** Wipes the translated version from the index. Most common fatal mistake.
2. **Using Google Translate widget or any JS that translates without changing the URL.** Search engines see the original English. Zero ranking benefit.
3. **Auto-redirect on IP or browser language.** Breaks crawling, traps users, against Google guidelines.
4. **Machine translation shipped without native-speaker review.** Detectable, down-ranked, kills trust.
5. **Forgetting `<html lang="xx-GB">`.** Removes the strongest single language signal.
6. **Translating only the body, leaving title tag and meta description in English.** SERP snippet shows in English; CTR collapses.
7. **Not setting `inLanguage` in JSON-LD.** Single biggest miss for LLM citation.
8. **Mixing scripts in one page** (English navigation + Punjabi body). Pick one primary language per page.
9. **Treating "Indian languages" as one bucket.** Hindi, Punjabi, Gujarati, Urdu, Tamil, Bengali are different audiences with different scripts and different UK concentrations.
10. **Translating UK acronyms** (HMRC, VAT, MTD, EHO). Confuses both users and the search engine. Leave in English.
11. **Using a foreign country domain (`.in`, `.pk`, `.pl`) for a UK audience.** Country signal contradicts geo target.
12. **Auto-redirect on the language switcher.** It must change the URL on click; users (and crawlers) must be able to bookmark and share each language version.
13. **Blocking `GPTBot` / `ClaudeBot` / `PerplexityBot` / `Google-Extended` in robots.txt by default.** Many CMS templates do this. Check.
14. **Cookie-walls or aggressive consent banners that block crawlers.** Both Google AIO and LLMs choke on these.
15. **Chasing head keywords.** Vernacular search volume is in the long tail. Build for "card terminal corner shop Leicester contract gotchas in Punjabi", not "card terminals in Punjabi".

---

## 16. Consolidated target list — language × area × niche (final summary)

If you only read one table, this is it. Pick a row, build the cluster, ship.

### Tier 1 — start here

| # | Language (script) | Audience | UK concentration | Primary niches |
|---|---|---|---|---|
| 1 | **Punjabi (Gurmukhi)** | Sikh-heritage corner-shop, off-licence, taxi, transport | Southall, Hounslow, Wolverhampton, Birmingham (Handsworth), Glasgow, Leicester (Belgrave), Bradford | **Card terminals, EPOS, off-licence/premises licence, alcohol & tobacco wholesale, lottery terminal, taxi PHV licensing, refrigeration finance** |
| 2 | **Polish** | Tradespeople, mechanics, beauticians, food shop owners, cleaners | Ealing, Hammersmith, Slough, Boston (Lincs), Crewe, Northampton, Southampton | **CIS / self-assessment, van insurance, MOT/garage compliance, public liability, food hygiene, payroll for 1–3 staff** |
| 3 | **Urdu (Shahmukhi)** | Pakistani-origin taxi, restaurant, mini-mart, halal butcher, takeaway | Bradford, Birmingham (Sparkbrook), Manchester (Rusholme), Luton, East London | **Taxi PHV licensing, halal certification, food hygiene, takeaway compliance, money-service-business compliance** |

### Tier 2 — strong follow-ons

| # | Language | Audience | UK concentration | Primary niches |
|---|---|---|---|---|
| 4 | **Hindi (Devanagari)** | Indian-origin corner-shop, pharmacy, restaurant, motel/B&B | Wembley, Harrow, Leicester, Croydon, Manchester | Card terminals, EPOS, pharmacy compliance, NHS contracting, food hygiene, premises licence, business banking, commercial mortgages |
| 5 | **Gujarati** | Newsagent, off-licence, post-office, jewellery, pharmacy | Leicester, Wembley, Harrow, Bolton, North London | Newsagent supply, post-office sub-postmaster compliance, jewellery hallmarking, pharmacy ownership, card terminals |
| 6 | **Bengali** | Bangladeshi-origin restaurant (curry house), mini-mart | Tower Hamlets, Camden, Oldham, Luton | Restaurant compliance, EHO food hygiene, alcohol licence, employment law (kitchen staff), business banking |
| 7 | **Romanian** | Self-employed builders, car-wash operators, drivers | Harrow, Edmonton, Wood Green, Luton, Wembley | Self-employed registration, UTR, banking with limited credit history, car-wash compliance, CIS |
| 8 | **Turkish / Kurdish (Kurmanji)** | Kebab shops, barbers, mini-marts, bakers | Haringey (Green Lanes), Enfield, Hackney, Lewisham | Catering insurance, EHO food hygiene, barber/salon licensing, premises licence, EPOS for restaurants |
| 9 | **Mandarin (Simplified)** | Takeaways, Chinese supermarkets, freight forwarders, landlords | Manchester, Birmingham, Soho, Cricklewood, Cambridge | Restaurant compliance, supplier wholesale accounts, Alipay/WeChat Pay UK, employment law for sponsored workers, freight forwarding |
| 10 | **Tamil** | Sri Lankan-origin convenience store, takeaway, pharmacy, accountancy SMEs | Wembley, Tooting, East Ham, Croydon | Convenience-store ops, pharmacy ownership, accountancy practice setup |

### Tier 3 — niche but viable

| # | Language | Audience | UK concentration | Primary niches |
|---|---|---|---|---|
| 11 | **Arabic** | Restaurants, shisha lounges, halal butchers, mini-marts, money-transfer | Edgware Road, Whitechapel, Birmingham (Alum Rock), Manchester (Rusholme) | Halal certification, shisha licensing, money-service-business compliance, restaurant compliance |
| 12 | **Vietnamese** | Nail-bar owners, bakers, small restaurants | Hackney, Deptford, Croydon, Birmingham | Salon insurance, COSHH compliance, lease assignments, EHO food hygiene |
| 13 | **Somali** | Mini-cab firms, mini-marts, money-transfer, cafes | Whitechapel, Streatham, Cardiff (Butetown), Bristol (Easton), Birmingham (Small Heath) | PHV licensing, money-service-business compliance, mini-mart setup |
| 14 | **Tagalog (Filipino)** | Care workers, nursing-agency staff | Barking, Ilford, Manchester, Earls Court | Care-home compliance, sponsor-licence guidance, NMC pin maintenance, nursing-agency setup |
| 15 | **Brazilian Portuguese** | Cleaners, builders, beauticians, food trucks | Brent, Bayswater, Stockwell, Willesden | Self-employed registration, CIS, public liability insurance, food-hygiene cert |
| 16 | **Bulgarian** | Drivers, cleaners, small builders | Harrow, Edmonton, Reading, Slough | Self-employed registration, ride-hail onboarding, cleaning-business setup |
| 17 | **Cantonese / Traditional Chinese** | Older HK-origin restaurant and takeaway owners | Soho, Manchester Chinatown, Birmingham, Newcastle | Restaurant compliance, employment law, EPOS — same as Mandarin but for older operators |
| 18 | **Korean** | Restaurants, beauty stores, K-pop retail | New Malden, central London | Restaurant compliance, import paperwork, EPOS, employment law |

### Tier 4 — smaller but interesting

| # | Language | Audience | UK concentration | Primary niches |
|---|---|---|---|---|
| 19 | **European Portuguese** | Construction, restaurants | Stockwell, Vauxhall, Reading | CIS, restaurant compliance |
| 20 | **Spanish (Latin American)** | Cleaners, food vendors, hospitality | Elephant & Castle, Seven Sisters, Brixton | Self-employed registration, market-stall licensing, food hygiene |
| 21 | **Russian / Ukrainian** | IT contractors, beauty industry, post-2022 Ukrainian SMEs | Dispersed, West London, Manchester | Banking with limited credit history, recognition of foreign qualifications, IT contracting via umbrella, business setup under Homes-for-Ukraine |
| 22 | **Tigrinya / Amharic** | Cafes, mini-cabs | Camden, Wood Green, Brixton | PHV licensing, MSB compliance, mini-mart setup |
| 23 | **Yoruba / Igbo / Twi** | Logistics, freight, food import, hair & beauty wholesale (mostly English-speaking but vernacular trust signals work) | Peckham, Thamesmead, Dagenham, Leyton | UK–West Africa freight, halal/cultural food import, hair/beauty wholesale, salon licensing |
| 24 | **Nepali** | Ex-Gurkha small businesses, restaurants, care workers | Aldershot, Folkestone, Reading | Pension and resettlement, restaurant compliance, care-home setup |
| 25 | **Albanian** | Construction, car washes, small import | North London (Wood Green), Luton | Self-employed registration, car-wash compliance, construction insurance |

### The portable framework outside the UK

Same pattern, different markets:

- **USA**: Spanish (bodega, taquería, auto-shop, NY/LA/TX/FL), Vietnamese (nail salons, CA/TX), Korean (dry cleaners, NJ/LA), Mandarin (restaurants, freight), Hindi/Gujarati (motels — the historical "Patel motel" network).
- **Canada**: Punjabi (trucking & freight, Brampton/Surrey), Tagalog (care agencies), Mandarin (property management).
- **Australia**: Mandarin/Cantonese (hospitality/import), Punjabi (trucking, farming labour), Vietnamese (bakeries, nails).
- **Germany**: Turkish (kebab, trades, Berlin/Köln/Duisburg), Polish (trades, cleaning), Russian/Ukrainian (IT contracting).
- **France**: Arabic / Maghrebi (halal supply, taxi, auto), Portuguese (construction).
- **UAE / Gulf**: Malayalam, Tamil, Bengali, Urdu (restaurant labour, taxi, salon SMEs).
- **Singapore / Malaysia**: Tamil and Bahasa for SME compliance, especially F&B.

**Selection rule everywhere:** first-generation operator, geographically concentrated, regulated/financial topic, English SERP locked up by big brands.

---

## Sources

- [How Google's AI Overviews Are Changing SEO In 2026 — EnFuse Solutions](https://www.enfuse-solutions.com/how-googles-ai-overviews-are-changing-seo-in-2026/)
- [Google AI Overview SEO Impact: 2026 Data & Statistics — Stackmatix](https://www.stackmatix.com/blog/google-ai-overview-seo-impact)
- [How to Rank in Google AI Overviews in 2026 — Analytics Insight](https://www.analyticsinsight.net/seo/how-to-rank-in-google-ai-overviews-in-2026-a-tactical-seo-framework)
- [How to Rank in AI Overviews — Ahrefs](https://ahrefs.com/blog/how-to-rank-in-ai-overviews/)
- [Only 15% of pages retrieved by ChatGPT appear in final answers — Search Engine Land](https://searchengineland.com/chatgpt-retrieved-vs-citations-study-471606)
- [ChatGPT Ranking Factors in 2026 — AiBoost](https://aiboost.co.uk/chatgpt-ranking-factors-in-2026-what-actually-influences-citations/)
- [Inside ChatGPT's Citation Engine: 2026 Blueprint — SEO Smoothie](https://seosmoothie.com/blog/inside-chatgpts-citation-engine-the-2026-blueprint-behind-its-search-logic/)
- [AI Search, hreflang, and translated content — GSQI](https://www.gsqi.com/marketing-blog/ai-search-hreflang-multilingual-queries/)
- [The web is multilingual — so why does search still speak just a few languages? — Search Engine Land](https://searchengineland.com/web-multilingual-search-few-languages-460026)
- [Multilingual SEO & Keyword Research for Search and AI Discovery — Sitebulb](https://sitebulb.com/resources/guides/multilingual-seo-keyword-research-for-search-and-ai-discovery/)
- [Multilingual GEO Visibility Guide — Weglot](https://www.weglot.com/blog/multilingual-geo-guide)
- [Google May Rely Less On Hreflang, Shift To Auto Language Detection — Search Engine Journal](https://www.searchenginejournal.com/google-may-rely-less-on-hreflang-shift-to-auto-language-detection/523224/)
- [Google Is Stealing Your International Search Traffic With Automated Translations — Ahrefs](https://ahrefs.com/blog/google-is-stealing-your-international-search-traffic-with-automated-translations/)
- [Google AI Mode Expands to 53 Languages — ALM Corp](https://almcorp.com/blog/google-ai-mode-expands-53-languages-analysis/)
- [AI Mode is now available in more languages and locations — Google blog](https://blog.google/products-and-platforms/products/search/ai-mode-expands-languages-locations/)
- [How ChatGPT (and similar services) figure out where you are — CometAPI](https://www.cometapi.com/how-does-chatgpt-determine-user-location/)
- [The ChatGPT IP address mystery — Simon Willison](https://simonwillison.net/2024/Nov/4/chatgpt-location/)
- [SEO for Regional Languages in India: Hindi, Tamil & Vernacular Content Guide (2026) — Gaurav Tiwari](https://gauravtiwari.org/seo-for-regional-languages-in-india/)
- [Local SEO Keyword Research for Indian Businesses — ContentSERP](https://contentserp.in/local-seo-keyword-research-for-indian-businesses/)
- [Mobile Ki Dukaan Platform Helps India's Small Mobile Shops Get Discovered on ChatGPT — Business Upturn](https://www.businessupturn.com/brand-post/mobile-ki-dukaan-platform-helps-indias-small-mobile-shops-get-discovered-on-chatgpt-and-ai-search-at-zero-cost/)
- [10 card payment machines ideal for small business — Small Business UK](https://smallbusiness.co.uk/10-card-payment-machines-ideal-for-small-business-2558598/)
- [Card Machines for Businesses — takepayments](https://www.takepayments.com/card-machines/)
