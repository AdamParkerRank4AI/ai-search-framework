# Free Breaking News APIs & Twitter/X APIs Research

**Date:** 2 April 2026
**Purpose:** Evaluate free-tier APIs for breaking news, Twitter/social media data, political primary sources, and live feeds

---

## Part 1: Free Breaking News APIs

### Top Recommendations

| API | Free Requests | Articles/Req | HTTPS | Best For |
|-----|--------------|-------------|-------|----------|
| **Currents API** | 600/day | ~200 | Yes | Best free volume |
| **NewsAPI.org** | 100/day | 100 | Yes | Dev/prototyping |
| **NewsData.io** | 200/day | 10 | Yes | Multi-country coverage |
| **GNews** | 100/day | 10 | Yes | Simple headline apps |
| **GDELT** | Unlimited | varies | Yes | Research, global monitoring |
| **Google News RSS** | Unlimited* | varies | Yes | Zero-cost, no auth |
| MediaStack | 500/month | 25 | **No** | Budget projects (HTTP-only) |
| Bing News Search | 1,000/month | varies | Yes | High relevance ranking |
| WorldNewsAPI | 500/month | 10 | Yes | Article extraction |
| TheNewsAPI | 3/day | 3 | Yes | Evaluation only |

---

### 1. Currents API (Best Free Volume)

- **URL:** https://currentsapi.services
- **Free Tier:** 600 requests/day
- **Features:** Latest news, search, filtering by language/country/category/keyword/domain/date range. 60+ languages.
- **Auth:** API key (`apiKey` query param or header)
- **Limitations:** Smaller source coverage than NewsAPI. Documentation less polished. Reduced data freshness on free plan.

### 2. NewsAPI.org (Best Feature Set)

- **URL:** https://newsapi.org
- **Free Tier:** 100 requests/day, up to 100 results per request
- **Features:** Top headlines by country/category/source, full-text search across 150k+ sources, language/source/date filtering
- **Auth:** API key (`apiKey` param or `X-Api-Key` header)
- **Limitations:**
  - Free = development only (no commercial use)
  - Results delayed ~15 minutes, limited to 1-month-old articles
  - CORS blocked on free tier (no browser-side JS)
  - No full article body (title, description, snippet, URL only)

### 3. NewsData.io

- **URL:** https://newsdata.io
- **Free Tier:** 200 credits/day (1 credit = 1 API call), 10 results per page
- **Features:** Latest news, crypto news, AI-powered sentiment analysis, 100+ countries, 60+ languages, keyword search
- **Auth:** API key (`apikey` param)
- **Limitations:** Free tier limited to latest news (no history beyond 48h). No full article content. 10 results/page max.

### 4. GNews API

- **URL:** https://gnews.io
- **Free Tier:** 100 requests/day, up to 10 articles per request
- **Features:** Top headlines, full-text search, country/language/category/date filtering. Sources from Google News.
- **Auth:** API key (`apikey` param)
- **Limitations:** Max 10 articles/response. No full content. Rate limit per-day only.

### 5. GDELT Project (Best for Research)

- **URL:** https://api.gdeltproject.org
- **Free Tier:** Completely free, no API key, generous rate limits
- **Features:** Monitors global news across 100+ languages. Full-text search, tone/sentiment filtering, geographic filtering, time-series, TV news monitoring. Billions of records.
- **Auth:** None
- **Limitations:** Not developer-friendly. Academic/research-oriented docs. Returns metadata + links, not full articles. Can be slow.

### 6. Google News RSS (Zero Setup)

- **URL:** https://news.google.com/rss
- **Free Tier:** No rate limit (public RSS), completely free
- **Features:** Top stories, topic feeds (business, tech, sports), search feeds (`/rss/search?q=keyword`), country/language params
- **Auth:** None
- **Limitations:** Not a formal API - no JSON, no SLA. Returns XML (parse yourself). Limited metadata. Aggressive scraping may cause IP blocks.

### 7. MediaStack

- **URL:** https://mediastack.com
- **Free Tier:** 500 requests/month, 25 results/request
- **Features:** Live + historical news, 7,500+ sources, country/language/category/keyword filtering
- **Auth:** API key (`access_key` param)
- **Limitations:** Free plan = **HTTP only** (no HTTPS). No sorting or pagination. Low monthly cap.

### 8. Bing News Search (Azure)

- **URL:** Azure Marketplace (Bing News Search API)
- **Free Tier:** 1,000 transactions/month, 3 req/sec max
- **Features:** Trending news, search, category news, freshness/region filtering. Excellent relevance ranking.
- **Auth:** Azure API key (`Ocp-Apim-Subscription-Key` header)
- **Limitations:** Requires Azure account (credit card for verification). 1,000/month is modest.

### 9. WorldNewsAPI

- **URL:** https://worldnewsapi.com
- **Free Tier:** 500 requests/month, 10 results/request
- **Features:** News search, top news by country, article body extraction, sentiment/entity analysis
- **Auth:** API key (`x-api-key` header)
- **Limitations:** Low monthly cap. Article extraction counts extra credits.

### 10. Spaceflight News API (Niche)

- **URL:** https://api.spaceflightnewsapi.net
- **Free Tier:** Completely free, no API key, no documented rate limit
- **Features:** Articles, blogs, reports from spaceflight sources
- **Limitations:** Space industry news only.

---

## Part 2: Twitter/X API & Alternatives

### Summary

| Option | Cost | Twitter Data? | Search | Post | Stream | Status (2025) |
|---|---|---|---|---|---|---|
| **X API Free** | $0 | Yes | No | Yes (1,500/mo) | No | Active |
| **X API Basic** | $100/mo | Yes | 7 days | Yes | No | Active |
| **Bluesky API** | $0 | No (alt platform) | Yes | Yes | Yes | Active |
| **Mastodon API** | $0 | No (alt platform) | Yes | Yes | Yes | Active |
| RapidAPI 3rd party | $0-50/mo | Yes | Yes | Varies | No | Fragile |
| Apify Scrapers | $0-49/mo | Yes | Yes | No | No | Fragile |
| X API Pro | $5,000/mo | Yes | Full archive | Yes | Yes | Active |

---

### 1. X/Twitter Official API v2

**URL:** https://developer.x.com

#### Free Tier ($0/month)
- 1,500 tweets posted/month (write-only)
- 1 App Environment
- **No read access** (no search, no timelines, no streaming)
- OAuth 2.0 / OAuth 1.0a / Bearer Token auth
- **Essentially useless for reading data**

#### Basic Tier ($100/month)
- 10,000 tweet reads/month
- 3,000 tweets posted/month
- Recent search (last 7 days)
- Tweet/user lookup
- No streaming

#### Pro Tier ($5,000/month)
- 1M tweet reads/month
- Full-archive search
- Filtered stream (25 rules)
- Full tweet counts

#### Enterprise ($42,000+/month)
- Highest volume, real-time PowerTrack, dedicated support

### 2. Bluesky API (Best Free Alternative)

- **URL:** https://docs.bsky.app (AT Protocol)
- **Cost:** Completely free
- **Features:**
  - Full read/write API
  - **Firehose streaming** (all public posts in real-time)
  - Search posts and profiles
  - Custom algorithmic feeds
  - Labeling and moderation APIs
- **Auth:** App passwords or OAuth
- **Limitations:** Not Twitter data; growing but smaller user base. API still evolving.
- **Verdict:** Best free developer experience among microblogging platforms

### 3. Mastodon/Fediverse API

- **URL:** https://docs.joinmastodon.org/api/
- **Cost:** Completely free
- **Features:** Full read/write API, WebSocket streaming, search, OAuth 2.0
- **Limitations:** Decentralized (must query individual instances), different/smaller user base than Twitter

### 4. RapidAPI Third-Party Twitter APIs

- **URL:** https://rapidapi.com/hub (search "Twitter")
- **Free Tier:** Typically 50-500 requests/month
- **Options:** Twitter154, TwitterAPI.io, Socialdata.tools
- **Limitations:** Fragile, may violate ToS, no uptime guarantees, can break without notice

### 5. Apify Twitter Scrapers

- **URL:** https://apify.com/store
- **Cost:** Free tier gives $5/month in platform credits
- **Features:** Multiple community-built scrapers, structured JSON output, scheduled runs
- **Limitations:** Scrapers break periodically as X changes frontend. Quality varies.

### 6. Threads API (Meta)

- **URL:** https://developers.facebook.com/docs/threads
- **Cost:** Free
- **Features:** Post/reply, read own posts, analytics
- **Limitations:** No public search API. Only access your own content.

### 7. Dead/Broken Tools (Avoid)

| Tool | Status | Reason |
|------|--------|--------|
| **Nitter** | Mostly broken | X killed guest API access; development abandoned 2024 |
| **snscrape** | Broken | X requires auth for all endpoints since mid-2023 |
| **Twint** | Archived | Not updated since 2022, completely non-functional |

---

## Part 3: Political Primary Sources & "Ahead of the News" APIs

These are the sources journalists themselves use. Monitoring them directly puts you ahead of news articles.

### Top "Ahead of the News" Sources (Priority Order)

| Source | Why It's "Ahead" | Cost |
|---|---|---|
| **Federal Register API** (public inspection) | Tomorrow's executive actions today | Free, no auth |
| **Congress.gov API** | Bill actions before media coverage | Free, API key |
| **docs.house.gov** | Committee docs before congress.gov | Free, no auth |
| **FEC API** | Campaign finance filings in real-time | Free, API key |
| **CourtListener/RECAP** | Court filings before media coverage | Free |
| **Polymarket / Kalshi** | Market prices shift pre-news | Free |
| **Bluesky Firehose** | Real-time political speech | Free |
| **Senate Lobbying API** | Lobbying registrations reveal upcoming fights | Free, no auth |
| **LegiScan** | 50-state legislation tracking | Free tier |
| **Regulations.gov API** | Federal rulemaking before finalized | Free, API key |

---

### Government/Legislative APIs

#### US Congress API
- **URL:** https://api.congress.gov/v3/
- **Free Tier:** Completely free, API key required (free registration)
- **Rate Limit:** 5,000 requests/hour
- **Data:** Bills, amendments, summaries, actions, cosponsors, committees, hearings, nominations, treaties, Congressional Record, member info, roll-call votes
- **Key Endpoints:** `/bill/{congress}/{type}`, `/member`, `/committee`, `/nomination`
- **Why ahead:** Bills and actions appear here before news coverage

#### Federal Register API
- **URL:** https://www.federalregister.gov/developers/api/v1
- **Free Tier:** Completely free, NO API key required
- **Data:** Executive orders, proposed rules, final rules, presidential documents, agency notices
- **Key Feature:** `/public-inspection-documents` shows what will be published TOMORROW
- **Why ahead:** Journalists check the public inspection endpoint daily

#### GovInfo API (US Government Publishing Office)
- **URL:** https://api.govinfo.gov/
- **Free Tier:** Free, API key required
- **Data:** Federal Register, Congressional reports, bills, public laws, Supreme Court decisions, CFR, GAO reports, budget documents

#### LegiScan API (State + Federal)
- **URL:** https://legiscan.com/legiscan
- **Free Tier:** 30,000 API calls/month, covers all 50 states + federal
- **Auth:** API key (free registration)
- **Data:** Bill text, status, sponsors, votes, amendments for all state legislatures + Congress
- **Why ahead:** State legislation often flies under the radar of national media

#### UK Parliament API
- **URL:** https://developer.parliament.uk/
- **Free Tier:** Completely free, no auth for most endpoints
- **Data:** MPs/Lords info, bills, votes, Hansard (debate transcripts), written questions, committee inquiries

#### EU Parliament Open Data
- **URL:** https://data.europarl.europa.eu/
- **Free Tier:** Free, no auth
- **Data:** MEP info, legislative procedures, plenary votes, parliamentary questions
- **Format:** RDF/SPARQL, CSV, JSON

#### GOV.UK Content API
- **URL:** https://www.gov.uk/api/content/
- **Free Tier:** Free, no auth
- **Data:** All UK government publications, press releases, policy papers, speeches

---

### Campaign Finance & Lobbying

#### FEC API (Federal Election Commission)
- **URL:** https://api.open.fec.gov/
- **Free Tier:** Completely free, API key required (instant free registration)
- **Rate Limit:** 1,000 requests/hour
- **Data:** Campaign contributions, expenditures, candidate filings, PAC data, independent expenditures
- **Why ahead:** New filings appear here before journalists write about them. Quarterly deadline filings are goldmines.

#### OpenSecrets API
- **URL:** https://www.opensecrets.org/api/
- **Free Tier:** Free with API key (non-commercial use), 200 calls/day
- **Data:** Legislator finances, industry contributions, lobbying data, revolving door

#### Senate Lobbying Disclosure API
- **URL:** https://lda.senate.gov/api/
- **Free Tier:** Free, no auth required
- **Data:** Lobbying registrations and activity reports under the Lobbying Disclosure Act
- **Why ahead:** New registrations reveal corporate/interest group priorities before they become public issues

---

### Courts & Legal

#### CourtListener / RECAP
- **URL:** https://www.courtlistener.com/api/rest/v4/
- **Free Tier:** Free, token auth for higher limits (free account), 5,000 req/day unauthenticated
- **Data:** Federal court opinions, oral arguments, PACER docket entries (via RECAP), judge info
- **Coverage:** Supreme Court, Circuit Courts, District Courts, Bankruptcy Courts
- **Why ahead:** Court filings in high-profile cases appear here before media coverage

#### Oyez (Supreme Court)
- **URL:** https://api.oyez.org/
- **Free Tier:** Free, no auth
- **Data:** Structured SCOTUS case data, oral argument audio

---

### Prediction Markets (Prices Move Before News)

#### Polymarket
- **URL:** https://docs.polymarket.com/
- **Free Tier:** Free, no auth for market data
- **Data:** Market prices (implied probabilities), order books, trade history
- **WebSocket:** Real-time price updates available
- **Why ahead:** Political event markets move on information before it's widely reported

#### Kalshi
- **URL:** https://trading-api.kalshi.com/v2/
- **Free Tier:** Free for market data (read-only), auth for trading
- **Data:** Government shutdown odds, Fed decisions, policy outcomes
- **WebSocket:** Real-time market data feed

#### Metaculus
- **URL:** https://www.metaculus.com/api/
- **Free Tier:** Free, no auth for public questions
- **Data:** Community forecasts on geopolitical/policy questions

#### Manifold Markets
- **URL:** https://docs.manifold.markets/api
- **Free Tier:** Completely free, no auth for reading
- **Data:** Play-money prediction markets with active political market creation

---

### Regulatory & Transparency

#### Regulations.gov API
- **URL:** https://api.regulations.gov/v4/
- **Free Tier:** Free, API key required
- **Data:** All federal rulemaking comments and documents, proposed rules during comment period
- **Why ahead:** Proposed rules appear here well before becoming final

#### MuckRock API (FOIA Tracking)
- **URL:** https://www.muckrock.com/api/
- **Free Tier:** Free to browse
- **Data:** FOIA request tracking and released documents

#### DocumentCloud API
- **URL:** https://www.documentcloud.org/help/api
- **Free Tier:** Free
- **Data:** Primary source documents uploaded by journalists

#### EveryCRSReport.com
- **URL:** https://www.everycrsreport.com/
- **Data:** Congressional Research Service reports (normally restricted to Congress)

---

## Part 4: Live Feeds & Real-Time Streaming

### WebSocket / Streaming Feeds

| Feed | Protocol | Data | Cost |
|------|----------|------|------|
| **Bluesky Firehose** | WebSocket | All public posts real-time | Free |
| **Polymarket** | WebSocket | Political market prices | Free |
| **Kalshi** | WebSocket | Regulated event contracts | Free |
| **Mastodon Streaming** | WebSocket | Instance activity | Free |

#### Bluesky Firehose
- **WebSocket:** `wss://bsky.network/xrpc/com.atproto.sync.subscribeRepos`
- All public posts in real-time. Filter for political accounts/keywords client-side.

### Government Live Feeds
- **House Floor XML:** https://clerk.house.gov/floor/ (near-real-time during session)
- **Senate Floor:** https://www.senate.gov/legislative/floor_activity_pail.htm
- **C-SPAN Live Streams:** Free via website and YouTube (House/Senate floor + hearings)
- **docs.house.gov:** Committee documents posted BEFORE they appear on congress.gov

### RSS Feeds Worth Monitoring
- **White House:** https://www.whitehouse.gov/feed/ (press releases, executive orders)
- **State Department:** https://www.state.gov/rss-feeds/
- **Department of Justice:** Press releases via RSS
- **Pentagon/DoD:** https://www.defense.gov/ (releases, contracts, casualty reports)
- **Treasury:** Sanctions announcements via RSS
- **Google News Politics RSS:** https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFZ4ZERBU0FtVnVLQUFQAQ

---

## Key Takeaways

### For Breaking News:
1. **Start with Currents API** (600 req/day) for the best free volume
2. **Use Google News RSS** for zero-setup, no-auth headline access
3. **GDELT** is unbeatable for research-scale global monitoring
4. **NewsAPI.org** has the richest features but is dev-only on free tier

### For Twitter/Social Data:
1. **X Free tier is write-only** - useless for reading/searching tweets
2. **$100/month Basic tier** is the minimum for any meaningful X data access
3. **All open-source scraping tools are broken** as of 2025
4. **Bluesky API is the best free alternative** with full firehose streaming
5. **RapidAPI third-party APIs** are the cheapest Twitter read option but are fragile

### For Political "Ahead of News":
1. **Monitor primary government sources** (Federal Register, Congress.gov, FEC, court filings) - this is what journalists do
2. **Federal Register public inspection** endpoint shows tomorrow's executive actions today
3. **Prediction markets** (Polymarket, Kalshi) move on information before it's widely reported
4. **Senate Lobbying API** reveals upcoming political fights early
5. **LegiScan** catches state-level legislation that national media misses

### For Live Feeds:
1. **Bluesky Firehose** is the only free real-time social media stream available
2. **Polymarket/Kalshi WebSockets** for real-time political probability shifts
3. **Government RSS feeds** (White House, State Dept, DoJ, DoD) for official announcements
4. **House/Senate floor XML feeds** for live congressional activity

### Recommended Full Stack (Budget):
- **News:** Currents API + Google News RSS + GDELT
- **Social:** Bluesky API (free) + X API Basic ($100/mo if needed)
- **Political Primary Sources:** Congress.gov API + Federal Register API + FEC API + CourtListener
- **Prediction/Probability:** Polymarket + Kalshi + Metaculus
- **Live Streaming:** Bluesky Firehose + Polymarket WebSocket + Government RSS feeds
