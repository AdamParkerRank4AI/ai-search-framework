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
