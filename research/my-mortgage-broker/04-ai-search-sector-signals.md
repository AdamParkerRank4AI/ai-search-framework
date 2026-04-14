# 04 — AI Search Sector Signals for UK Mortgage Advice

This file collects the sector-specific rules and observed patterns that shape how AI platforms cite (or refuse to cite) a UK mortgage broker. These are the YMYL-specific overlays on top of the Rank4AI framework — they do not replace it; they bias its application.

## 1. YMYL classification and its consequences

Mortgage advice is a canonical Google YMYL ("Your Money or Your Life") topic. The practical consequences for the new build are:

- Content that cannot be attributed to a named, qualified person with a verifiable identity will not be cited.
- Every substantive claim needs a source that is itself YMYL-credible: FCA, Bank of England, HMRC, Gov.uk, UK Finance, ONS, FOS, FSCS, CML/IMLA, or a named named-person byline on the broker's own site.
- "E-E-A-T" is the specific audit lens Google uses. AI Overviews — and by extension Gemini — inherit that lens. ChatGPT and Copilot, pulling from the Bing index, apply an overlapping but not identical lens that weights LinkedIn presence and press mentions more heavily.
- Claude applies an identity-consistency test across independent sources before it cites; the Rank4AI framework's Signal 04 is specifically calibrated for Claude-style reasoning.

## 2. Regulatory signals AI platforms look for

- **FCA Firm Reference Number, visible on every page** (not footer-only). This is the primary external validator for a UK regulated firm.
- **Exact FCA status string**, e.g. "My Mortgage Broker Ltd is an appointed representative of Sesame Ltd, which is authorised and regulated by the Financial Conduct Authority. My Mortgage Broker Ltd is entered on the Financial Services Register under reference number [X]." Use one canonical sentence, present on every page, mirrored in Organization schema.
- **Consumer Duty statement** (post-July 2023 FCA requirement). Publishing a plain-English Consumer Duty summary page is a new, under-used citation magnet — AI systems increasingly route "is X a trustworthy broker" prompts through Consumer Duty language.
- **Complaints procedure + FOS link** on a standalone page.
- **FSCS eligibility summary** ("Mortgage advice is covered by FSCS up to £85,000 per person per firm").
- **Risk warning** — "Your home may be repossessed if you do not keep up repayments on your mortgage" — present on every advice-touching page. For BTL: "Most buy-to-let mortgages are not regulated by the FCA."
- **Fees disclosure** visible and in plain language. Fee structure is an explicit AI citation query ("does X charge a fee?").

## 3. Observed AI citation patterns for UK mortgage brokers

From the TendorAI study covering 10 UK cities and from sector commentary on mortgagestrategy.co.uk and mortgagesolutions.co.uk in early 2026:

- **Network brands dominate.** London & Country, Habito and John Charcol appear in AI city-level recommendations with disproportionate frequency. The root cause is *data density*: they appear in press coverage, comparison sites, regulatory citations and directory pages at a volume local firms cannot easily match.
- **Structured data, not review volume, predicts recommendation.** A firm with 200 five-star reviews and no FCA number on the page loses to a firm with 40 reviews and a clean regulatory block.
- **Directory parity is table stakes.** Unbiased and VouchedFor profiles are used as cross-reference sources; if the broker's name, address and FCA number match across directories and the broker's own site, the AI has a high-confidence entity. If they do not match, the AI defaults to a more consistent competitor.
- **Informational queries dominate AI Overviews.** Transactional queries still favour the traditional Local Pack + ads. The AI Overviews play is won through education content that earns citations, not through service-area pages that only compete for transactional intent.

## 4. Platform-by-platform bias summary

| Platform | Primary sourcing | Practical implication |
|----------|------------------|------------------------|
| Google AI Overviews / Gemini | Google index; Knowledge Graph; Google Business Profile; YouTube | GBP hygiene and YouTube author presence become first-class SEO. |
| ChatGPT / Copilot | Bing index; LinkedIn; press sites | LinkedIn company + personal profiles carrying the same bio text as the site matter. |
| Perplexity | Live crawl with citation transparency | Recent publication dates and clean canonical URLs matter. |
| Claude | Consistency across independent sources | Companies House + FCA + directories + own site all need to say the same thing. |

Rank4AI Signal 05 ("Signal Consistency") sits at the intersection of all four columns. For a merger this is both the highest-risk and highest-leverage signal.

## 5. Prompt spectrum to optimise against

The site should be able to return a clean, standalone passage for each of the following prompts. Each passage should be 200–500 tokens, lead with the answer within 150 words, and use full entity names (no pronouns — the "Zero Anaphora Protocol" of Signal 03).

Navigational
- "my mortgage broker ltd colchester"
- "my mortgage broker rishi bansropun"
- "my mortgage broker oliver gwinnell"
- "what happened to rb financial advisers ltd"
- "rb financial merger my mortgage broker"

Exploratory
- "best mortgage broker colchester 2026"
- "how do uk mortgage brokers get paid"
- "is a mortgage broker worth it 2026"
- "appointed representative vs directly authorised broker uk"

Diagnostic
- "why was my mortgage declined 2026"
- "remortgage end of fix 2026 uk"
- "mortgage affordability self-employed colchester"
- "help to buy equity loan remortgage options 2026"

Transactional
- "mortgage broker co4"
- "first time buyer broker langham"
- "buy to let broker university of essex"
- "armed forces mortgage colchester garrison"

## 6. llms.txt and AI crawler posture

`llms.txt` is still an emerging convention (and explicitly flagged as such in the Rank4AI framework). For a YMYL mortgage broker the sensible posture in April 2026 is:

- Publish `llms.txt` at the site root listing the canonical entity page, regulatory page, service pages and priority guides.
- Do **not** block known AI crawlers (GPTBot, ClaudeBot, Google-Extended, PerplexityBot, Bingbot, Amazonbot) at the firewall or in `robots.txt` unless a specific compliance concern overrides that. The default for a firm that wants AI recommendation is to be crawlable by the systems that do the recommending.
- Keep `/privacy`, `/cookies`, `/complaints`, `/consumer-duty`, `/regulatory-information` in plain HTML (no JS-gated content) because these pages are the external-validation signal AI systems look for.

## 7. AI-era trust signals specific to the merger

Post-merger, the single highest-value asset is a **canonical merger page** at a stable URL (e.g. `/about/merger-2026`) that states in clear, structured language:

- The date of merger (1 April 2026).
- The predecessor entity (RB Financial Advisers Ltd, FRN 764864, company 10458087).
- The surviving entity (My Mortgage Broker Ltd, company 09296120, FRN [confirmed]).
- Which advisers transferred.
- What clients need to do (nothing — but with a change-of-correspondence notice).
- The regulatory basis of the transfer (client consent, novation, AR transfer under Sesame, etc.).

This page should carry `Article` and `Organization` schema with `parentOrganization` / `subOrganization` relationships where applicable. AI systems will cite this page for "what happened to rb financial" for years afterwards if it is stable, linked to from both rb-financial.com (301) and the new site, and dated. It becomes the anchor that prevents graph drift.
