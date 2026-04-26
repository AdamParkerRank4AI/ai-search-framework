# Ideas, questions, help wanted: footprint data for AI search

## What this is

A brain dump of an idea I've been kicking around. I'm sending this round to a few people I trust to get a reality check before I spend any real time or money on it.

It's not a finished plan. It's the start of something. I don't know if it'll work, I don't know what shape it ends up being, I don't even know if anyone wants what I'm describing. But the underlying observation feels real to me, so I want to find out whether it stands up under proper scrutiny.

Honest "this won't work because..." feedback is what I'm after. Don't be polite, please.

## The thing I keep coming back to

AI search platforms (ChatGPT, Gemini, Claude, Perplexity, Copilot) are basically trust engines. When someone asks "best phone shop in Essex" or "where should I have lunch in Bristol," the AI is making a trust judgement about which businesses to surface.

Right now, it makes that judgement from purely digital signals. Web pages, online reviews, structured data, citations, social media mentions. That's it. That's the whole pool.

And the problem is that all of those signals can be faked. SEO, paid reviews, link buying, AI-generated content, bot networks. Anyone with budget can move the needle. The AI platforms know this and it's their biggest credibility risk: they recommend somewhere, the user goes there, the place is closed or rubbish, the platform looks stupid.

The signal they're missing is physical. Whether real people actually walk into a place, spend time there, come back. That's the strongest trust signal in existence and the hardest to fake. And right now, no AI platform can see it. They have access to half of trust (digital) and not the other half (physical).

That gap is what this idea is about.

## The idea, simply

Build something that captures real-world footprint data with consent, packages it into a format AI platforms can actually use, and licenses it to them as a grounding signal. The thing they can't currently see, sold to them as a feed.

Side benefit: the same data is exactly what retailers and venue landlords already pay for from companies like Placer.ai, except more granular and with cleaner consent.

## How would you actually capture this data

A few different shapes I've been thinking about. None of them is decided.

**Option 1: an indoor map for venues.** Think Lakeside, Westfield, big shopping centres, hospitals, airports, universities, stadiums. Visitor enters the building, scans a QR code on a sign, the map opens in their browser (no app install). Shows where they are and where everything in the venue is. Wayfinding is the user-visible value. Behind the scenes, with their permission, we capture their anonymous location data for that visit. Each pin on the map is also a structured entity record so the venue and its tenants become more discoverable to AI platforms.

**Option 2: aggregate data from sources that already exist.** Instead of building a consumer product to originate the data, license slices from places that have it already and stitch them together with a clever algorithm. Card transactions (Visa, Mastercard, Fable, Consumer Edge), venue WiFi networks (Cisco Meraki, Aruba, Purple), mobile phone carriers (Vodafone, O2, EE), social check-ins (Instagram, X, TikTok, OpenTable, Eventbrite), public transport tap data (TfL), parking apps (RingGo, JustPark). The value-add is the algorithm and the methodology that turns disparate signals into a single AI-grounding feed. Faster to ship, but no real moat per source.

Probably the right answer is some mix. Aggregate first to get into AI platform conversations early, originate via the map for the long-term moat.

**Option 3: kiosks.** There are companies already doing physical interactive kiosks at venues (22Miles, Visix, Acquire Digital, Mvix). They do wayfinding, advertising, ordering. None of them treats the kiosk as a footfall-data-generation device for AI grounding. Could be a partner channel, could be a hardware variant of the map. They've already proven venues will adopt physical placement at the entrance.

## The big-and-small thing

Important point I want to flag. This isn't just for shopping centres.

The trust problem is the same for a single independent café in Soho as it is for the H&M flagship in Lakeside. Both want to be recommended by ChatGPT. Both currently rely on the same gameable digital signals. Both would benefit from a footprint trust layer.

So the product needs to span the full size range:
- Big venues get the full indoor map experience.
- Mid venues (high streets, retail parks, mid-size hospitals) get a simpler version.
- Small businesses get a QR check-in by the door, free or cheap tier, no full map needed.

There are roughly 270,000 retail premises in the UK before you start counting hospitality, healthcare, culture. The big-venue path alone is too narrow. And small businesses are exactly who AI search currently fails worst, because they have weaker digital signals than the chains. A footprint trust signal helps the underdog disproportionately.

Pricing tiers, sales motion big-enterprise to self-serve like Stripe, network effect (big venues anchor, small ones fill the long tail). Same back-end data pipeline serving all of them.

Think of it less as an indoor-map company and more as a footprint trust layer for every business with a physical premises.

## Why I think AI platforms would actually buy this

Five reasons it might land:

1. It would cut hallucination on place questions. The biggest credibility risk for ChatGPT when someone asks "where should I go" is recommending somewhere that's closed, struggling, or fake. Footfall data prevents that class of error.

2. It's costly to fake. You can manufacture web content and reviews. You can't manufacture real human feet at scale.

3. It's fresh. Footfall is recent by definition. Stale web content can't tell you whether a place is still trading. A footfall feed can.

4. It complements their existing signals. A business with strong online signals and strong footfall is verifiably real. A business with only one is suspicious. The combined picture is much stronger than either alone.

5. OpenAI has shown they will pay real money for grounding data. AP, Le Monde, Reddit, Stack Overflow, FT, News Corp, all licensed in 2024 to 2025. Anywhere from $1M to $60M per year per deal depending on scale. Footfall fits the same shape, in a category they don't yet have a supplier for.

## A note on card data

Card data is the obvious adjacent thing and I want to be honest about why it's not enough on its own.

A family of four enters a venue, has lunch, browses three shops, buys clothes, leaves. Card data captures one cardholder, the parent who paid. Four humans, one signal. Loyalty schemes have the same flaw: one Clubcard, four people. And card data only registers the visit if a purchase happens. Browsers and non-payers are invisible.

Per-device location data inverts that. Four phones with the map open is four hits. Browsing visits count even with zero spend. You see arrival, dwell, route and departure, not just the till timestamp. Cross-tenant journeys are visible (the shops people didn't buy from).

But honestly per-device data has limits too. Children typically don't have phones. Not every family member will have the map open. People who don't scan are invisible to us. The honest answer is to blend sources, be transparent about coverage, and document the methodology so AI platforms can defend it in their own procurement.

## Going nicher might be the smart first move

The whole thing assumes shopping centres but I'm not sure that's actually the right starting point. Retail data is commercially sensitive, the venue ops teams are slow, and the existing footfall vendors are entrenched.

Categories where I think data acquisition is materially easier:
- Hospitals. Public funding, public-benefit angle. NHS partnership could open many sites in one signature. Wayfinding pain in hospitals is brutal.
- Universities. Open culture, student safety angle, seasonal footfall.
- Stadiums and event venues. Already heavily instrumented.
- Transport hubs. TfL already publishes some data.
- Museums, galleries, heritage sites. Open-data leaning, publicly funded.
- Single-operator chains (coffee, pharmacy, restaurants). One head office signature gets nationwide coverage rather than venue-by-venue sales.

Worth picking the niche where data is easiest to get and AI grounding queries are common, prove the model end-to-end, then expand.

## Why I think it's a window now

Several conditions only aligned in the last 12 to 18 months:
- AI search has legitimised. Real budgets being spent on grounding data.
- Mobile-SDK footfall (the legacy way to do this) is collapsing under Apple App Tracking Transparency and Google Privacy Sandbox. The FTC banned X-Mode/Outlogic in 2024. Gravy Analytics had a big breach in early 2025. The incumbents are weakened.
- Privacy regulation is now creating a moat for clean-consent operators rather than just being friction.
- Indoor mapping is mature enough that you can ship a competent product in months.
- The Rank4AI methodology already exists and gives the data product a thesis to sit inside.

Realistic first-mover window: maybe 18 to 24 months before Foursquare, Placer or one of the AI platforms themselves notices the category and pivots into it.

## What I think might be defensible

Not the data volume. The incumbents will always have more data than us early on.

What we could win on:
- Consent quality. Built from day one on visitor-initiated QR scans. The SDK-aggregator competitors carry years of murky consent and active regulator interest.
- Entity linkage. Every record tied to stable IDs that resolve to Wikidata, Companies House, brand parents, the Rank4AI graph. Most footfall vendors sell "device near coordinates" with no entity layer.
- Indoor specificity. Most outdoor footfall products are tile or postcode level. Inside Lakeside, "best phone shop" needs to know which actual unit, not which sector.
- Methodology bundle. Rank4AI is already published and scored, audit-anchored. The data sits inside a thesis, not as a standalone CSV.
- Speed. Big incumbents are slow to pivot strategy. Small operators can define a new category faster than they can react to it.

## What I genuinely don't know

Stuff I'd love sharper minds to push back on.

- Will AI platforms actually pay for this? Plausible but unproven. The cheapest way to find out is direct conversations with their data-partnership teams.
- What's the coverage threshold for the data to be interesting? Probably hundreds of venues, not tens. The road from venue 1 to venue 100 is real work.
- Will visitors actually scan the QR? Believable for venues that promote it well, unproven below maybe 30% scan rate.
- Could OpenAI or Google build this themselves rather than buy? They could. Defence is being smaller, faster, neutral and multi-platform.
- Is the indoor map plus venue SaaS market strong enough to fund the early years? Pointr and Mapwize numbers suggest yes but I'd need to validate venue economics ourselves.
- Have I missed someone who's already doing this? That's literally one of my questions to you.

## How I want to test this without spending much

Rough order, none committed yet:
1. Build a tiny prototype in a couple of weeks. Map of one venue, capture some intent events, show how the data would look. Free tools, near zero cost.
2. Quick competitive sweep. Search Crunchbase, LinkedIn, recent OpenAI/Anthropic hires from location-data backgrounds, footfall vendor acquisitions.
3. Five conversations with data-partnership people at OpenAI, Anthropic, Google, Perplexity, Microsoft. Use the prototype as the demo. Ask: would you license a feed shaped like this?
4. Pilot with one friendly venue. Real visitors, real scan rates, real data shape.
5. Side-by-side AI grounding eval. 50 prompts, baseline answers vs answers with our data injected as context. Score on factuality and recommendation quality.
6. Try to sell the indoor map alone (no AI angle) to three venues. If at least one signs, the SaaS layer of this is real.

Total cost for steps 1 to 6: maybe £30k to £80k including time. Six months ish. Won't raise serious capital until those steps are mostly green.

## What I'd love from you

If you're reading this to vet it, the most useful things you can tell me are:

1. Have you seen anyone else building this? Stealth startups, internal teams at AI platforms, recent moves from footfall vendors. If yes, who and how seriously.
2. Where would you push back hardest? Which assumption in here is the weakest?
3. Who should I be talking to? Specifically: data-partnerships people at the AI platforms, indoor-mapping operators, venue ops contacts, AI grounding researchers, anyone in the carrier-data world.
4. What kills it? What's the most likely reason this doesn't work that I've underweighted?

Honest critique massively appreciated. I'd much rather hear "this falls over because X" now than three months into building.

## One sentence version if you want to forward it

> AI search is a trust engine. Today its only trust signals are digital, and digital signals can be faked. The signal it's missing is physical: who actually goes where. I'm trying to figure out if there's a way to convert real-world footfall into LLM-readable trust data, for every business with a footprint, from a single café up to Lakeside-class venues. The map is the wedge. The data is the product. The window might be now. But it's early and I want pushback before I commit.

Thanks for reading.

Liam
