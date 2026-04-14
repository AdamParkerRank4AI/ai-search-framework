# 01 — Entity Audit (Signal 01: Identity Clarity)

The merger creates a single surviving entity with a fragmented public identity graph. This file records what the external sources currently say, where they disagree, and what must be reconciled before new content is published.

## My Mortgage Broker Limited — known facts

| Field | Value | Source |
|-------|-------|--------|
| Registered company number | 09296120 | Companies House search |
| Incorporation date | 5 November 2014 | Companies House |
| Registered office | Unit 4, 99 London Road, Stanway, Colchester, Essex, CO3 0NY | Companies House |
| Trading office (per client letter) | Lodge Park Business Centre, Lodge Lane, Langham, Colchester, CO4 5NE | Client correspondence, current site |
| Main phone | 01206 370 018 | Client letter, current site |
| Directors (post-merger) | Rishi Bansropun, Oliver Gwinnell | Client letter |
| Existing adviser named on site | Craig Gilbert ("Craig") | mymortgagebroker.co.uk/about-us, Trustpilot reviews |
| Trustpilot TrustScore | 4.6 — 4.85 (22 reviews, 100% 5-star as of crawl) | Trustpilot |
| Directory FCA reference | FRN 795866, Appointed Representative of Sesame Ltd | financialadvisers.co.uk listing, Trustpilot summary |
| Current site FCA statement | "Directly authorised by the FCA" | mymortgagebroker.co.uk/about-us |

## RB Financial Advisers Ltd — known facts

| Field | Value | Source |
|-------|-------|--------|
| Registered company number | 10458087 | Companies House |
| Trading office | 19a London Road, Colchester, CO3 0NH | rb-financial.com, Unbiased |
| FCA reference | FRN 764864 (Appointed Representative of Sesame Ltd) | rb-financial.com, Unbiased |
| Director | Rishi Bansropun (from 2 November 2016) | Companies House, LinkedIn |
| Lenders panel | "Over 65 lenders" | rb-financial.com |
| Google rating | 5.0, 34 reviews | rb-financial.com |
| Other advisers named | Josh Baker | rb-financial.com |

## Contradictions to resolve before launch

1. **FCA authorisation status of My Mortgage Broker Ltd.**
   The current About page reads "Directly authorised by the FCA". The financialadvisers.co.uk directory and the summary metadata on the Trustpilot page both state it is an *Appointed Representative of Sesame* under FRN 795866. These two statements cannot both be true. An AI system cross-referencing the FCA register will pick whichever matches — and the other instance becomes a misclassification signal.
   **Action before build:** Pull a fresh screenshot of the live FCA Register entry for FRN 795866, confirm current status, and write the regulatory footer exactly once, then propagate.

2. **Registered address vs. trading address.**
   Companies House shows CO3 0NY (Stanway); the letter, website and Google Business Profile reference CO4 5NE (Langham). AI Overviews, Google's Local Pack and Apple Business Connect each sanity-check against the Companies House record. This is the number-one NAP inconsistency in the estate.
   **Action before build:** Update the Companies House registered office to Langham (or, if Stanway is retained for mail purposes, publish both and label them clearly as "Registered office" vs "Client office"). Schema.org `Organization.address` and `PostalAddress` must match the registered entity.

3. **"Over 15 years of experience" claim.**
   The limited company has been incorporated for ~11.5 years. The claim in the client letter is plausible if it refers to Oliver Gwinnell's personal practitioner track record, but in standalone form on a website it will fail entity verification on any AI system that cross-references Companies House.
   **Action before build:** Replace with precise, attributable phrasing — e.g. "Oliver Gwinnell has 25+ years' mortgage advice experience; My Mortgage Broker Ltd has been trading since 2014; combined team experience exceeds 60 years."

4. **Team composition.**
   - Client letter: Rishi + Oliver (Directors).
   - Current site: Oliver + Craig.
   - RB site: Rishi + Josh Baker.
   Post-merger the visible team must be stated once, with dated bios. If Craig Gilbert and Josh Baker remain, they belong on the new site; if they have left, their historical client reviews still need to be honoured but their bios removed.

5. **Two FCA numbers in the live ecosystem.**
   FRN 764864 (RB Financial) and FRN 795866 (My Mortgage Broker) are both currently active public references. Post-merger only one should be cited as the operating entity. The other must either be surrendered, redirected (AR transfer) or explicitly noted as historical. AI systems treat two live FCA numbers for one claimed business as a misclassification signal.

## Disambiguation protocol (per Signal 01)

Before any new content is written, produce a single-page **"Entity Fact Sheet"** that the site, the Google Business Profile, LinkedIn, Unbiased, VouchedFor, Trustpilot, Companies House and the FCA register all agree on. Every page on the new site must cite *exactly* this text, verbatim, in its Organization schema and in its visible footer.

Suggested entity fact block (draft — subject to FCA verification):

```
My Mortgage Broker Ltd
Registered in England and Wales, company number 09296120
FCA reference [TO BE CONFIRMED]
Registered office: [TO BE CONFIRMED after Companies House update]
Client office: Lodge Park Business Centre, Lodge Lane, Langham, Colchester CO4 5NE
Directors: Rishi Bansropun, Oliver Gwinnell
Trading since 2014; successor business to RB Financial Advisers Ltd (merged 1 April 2026)
Your home may be repossessed if you do not keep up repayments on your mortgage.
```

## Exclusion statements (Signal 01 requirement)

A mortgage broker in a YMYL sector needs explicit "we are not" statements to prevent misclassification. Suggested boundaries for My Mortgage Broker Ltd:

- We are **not** a lender. We do not issue mortgages ourselves.
- We are **not** a comparison website. We advise.
- We are **not** an IFA practice offering investment or pension advice (unless/until that permission is held).
- We are **not** debt management or debt advice.
- We are **not** affiliated with the unrelated Australian firm "mymortgagebrokers.co.uk" or with estate agents operating under similar names.

These lines, placed in an About page and mirrored in FAQ schema, collapse the ambiguity that AI systems otherwise resolve in favour of whichever entity they saw first.
