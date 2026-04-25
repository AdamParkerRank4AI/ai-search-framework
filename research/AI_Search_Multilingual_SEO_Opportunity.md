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
