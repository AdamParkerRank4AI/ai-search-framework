# 02 — Digital Presence Audit (Signals 03 and 04)

Snapshot of the current public surfaces that contribute to the entity graph. Each surface must either be migrated into the new brand, redirected, or formally decommissioned — anything left stale becomes a signal-drift source (Signal 05).

## Primary websites

### mymortgagebroker.co.uk (current, will be rebuilt)

Observed on crawl:

- Homepage copy mentions mortgages, remortgages, buy-to-let, critical illness, life insurance.
- Team page names **Oliver** (Founder/MD, "25+ years experience") and **Craig** (Mortgage Broker).
- Contact block: 01206 370 018 and two mobile numbers (07971 008896, 07770 668861).
- Regulatory line: *"Your home may be repossessed if you do not keep up repayments on your mortgage."* — present.
- FCA number: **not visible** on the pages we fetched. This is the single worst E-E-A-T gap for a YMYL site and the most likely reason AI platforms currently do not cite the firm.
- "Directly authorised by the FCA" string is present on the About page (see entity audit for the contradiction).
- No blog, no FAQ, no testimonials page, no privacy policy link, no cookie policy visible.
- No visible JSON-LD schema in the content extracted (needs DOM inspection to confirm).

### rb-financial.com (to be retired or redirected)

- Active at time of research. Lists Rishi and Josh Baker as advisers.
- 19a London Road, Colchester CO3 0NH, 01206 879559.
- FCA reference 764864 (AR of Sesame).
- Google 5.0 rating, 34 reviews.
- Testimonials page in place; no blog.
- British Property Awards banner referenced with no substantiation visible.

**Action:** 301 every URL on rb-financial.com to the equivalent (or most relevant) URL on the new mymortgagebroker.co.uk for 24 months minimum. Preserve `/about/testimonials/` content (with author attribution) by re-publishing under the new brand with a clear "historically received as RB Financial Advisers Ltd" attribution.

## Directories and aggregators

| Platform | Entity currently listed | Action |
|----------|-------------------------|--------|
| Companies House | Both MMB Ltd (09296120) and RBFA Ltd (10458087) | Update MMB registered office; confirm RBFA status (dormant / dissolved / continued as subsidiary). |
| FCA Register | FRN 795866 (MMB), FRN 764864 (RBFA) | Confirm which FRN survives; update principal/AR relationship on the one that closes. |
| Google Business Profile | Likely two profiles (CO3 0NH and CO4 5NE) | Merge into one profile at CO4 5NE; request Google to close the CO3 0NH listing once Sesame paperwork is complete; transfer reviews where possible. |
| Apple Business Connect | Unknown — audit needed | Create a single verified profile matching GBP. |
| Bing Places | Unknown — audit needed | Create and verify. |
| Unbiased.co.uk | RB Financial Advisers Ltd listed | Re-brand the profile; preserve reviews. |
| VouchedFor | Unknown — audit needed | Create profile for each adviser under MMB Ltd. |
| Trustpilot | mymortgagebroker.co.uk (22 reviews, 4.6–4.85) | Retain; embed live widget on new site; actively solicit reviews to grow past 50 where citation density increases. |
| LinkedIn (company) | "RB Financial Advisers" company page + a Rishi Bansropun personal profile describing RBFA | Re-brand the RBFA page or create a fresh MMB company page with a "formerly RB Financial Advisers Ltd" anchor line; update both directors' personal headlines on the same day. |
| financialadvisers.co.uk | My Mortgage Broker Limited listed under Colchester | Request update to reflect new team, corrected FCA status and address. |
| MyLocalMortgage | Rishi Bansropun / RB Financial profile | Update to new brand. |
| Companydirectorcheck | Rishi Bansropun record | Inspect; no editable surface but useful to verify the director graph for AI. |
| Wikidata | Likely absent | Consider submitting a Wikidata entry once Companies House and FCA are reconciled — a strong AI-era identity signal (Signal 04). |

## Review graph

Combined estate currently:

- Trustpilot: ~22 reviews, ~4.6–4.85 (mymortgagebroker.co.uk).
- Google: ~34 reviews, 5.0 (rb-financial.com / RBFA location).

Two review graphs for one business creates an AI reasoning split. After merger, reviewers should be directed to a single canonical Google Business Profile and a single Trustpilot page (we would keep the mymortgagebroker.co.uk Trustpilot account because it carries the name that will survive). Historical RB Financial Google reviews should be referenced by number and date on the About page for transparency, e.g. "Our predecessor brand RB Financial Advisers Ltd held a 5.0 rating across 34 Google reviews prior to merger".

## Socials

- LinkedIn: both directors active; company page exists for RBFA. Priority surface because ChatGPT and Copilot pull from LinkedIn via Bing.
- X / Twitter: no active handle identified — consider a dormant handle reservation rather than an active presence.
- YouTube: no channel identified — relevant for video bios (Signal 02 / E-E-A-T).
- Instagram / Facebook: not confirmed — audit needed.

## Content debt

Neither site currently publishes long-form educational content. This is the single largest opportunity for competitive displacement (Signal 02) because all of We Are Mortgages, Fitch & Fitch and YesCanDo Money are already publishing topic-cluster content.
