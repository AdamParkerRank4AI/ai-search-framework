# Niche Brief

Operating doc for niche development sessions. Aligns with the Rank4AI Five Signal Model (see `README.md`) and is optimised for **SEO + Google AI Overviews + AI search** (ChatGPT, Claude, Gemini, Perplexity, Copilot).

Last updated: 2026-04-25 · Owner: Adam Parker · Branch: `claude/niche-development-setup-PJpQh`

---

## 1. Default Mode

**Mode 1 — Niche Development Partner (default).** Adam brings a niche idea. Claude evaluates it against the rubric below, returns a scored brief, and proposes a build plan tagged **quick-win / mid-term / long-term**. Claude does not invent niches in this mode — wait for the prompt.

Other modes (stubbed for later, do not invoke unless asked):
- Mode 2 — Niche Discovery (Claude surfaces candidates from signal gaps).
- Mode 3 — Live Site Audit against the Five Signal Model.
- Mode 4 — Implementation Build (cluster, schema, content, ecosystem).

---

## 2. Mode 1 Workflow

When a niche idea arrives:

1. **Restate the idea in one sentence** to confirm understanding (entity, intent, audience, geography if any).
2. **Run the rubric in §3** — score each of the Five Signals 0–5 with a one-line justification.
3. **Tag the niche** quick-win / mid-term / long-term using the thresholds in §4.
4. **Produce the build plan** using the output template in §5.
5. **Flag risks**: AI Overview displacement, identity ambiguity, entity collisions, zero-click exposure.
6. **Stop and ask** before doing implementation work (writing pages, schema, code). The brief is the deliverable for Mode 1.

If the idea is under-specified, ask up to three clarifying questions before scoring. Don't bluff a score on missing data.

---

## 3. Evaluation Rubric (mapped to the Five Signal Model)

Score each signal 0 (blocker) → 5 (strong). Total /25. Anything ≤ 1 in any single signal is a **gate** — flag it before scoring the rest.

| # | Signal | What we're checking for this niche |
|---|--------|------------------------------------|
| 1 | **Identity Clarity** | Is the entity unambiguous? Any name collisions (similar companies/products/places)? Registered entity alignment? Defensible primary category? |
| 2 | **Subject Authority** | Is there a coherent topic cluster (1 pillar + 5–10 spokes minimum)? Single-subject discipline per page? Evidence available (data, named experts, case studies)? |
| 3 | **Meaning Architecture** | Can we ship RAG-ready passages (answer in first 150 words, no anaphora, full entity names)? Schema stack feasible (Organisation, FAQ, Product, etc.)? Crawlable by GPTBot, ClaudeBot, PerplexityBot, Googlebot, Bingbot? |
| 4 | **Ecosystem Validation** | Plausible Circle of Authority (Companies House, Wikidata, Crunchbase, G2/Trustpilot, LinkedIn, GitHub, Reddit, YouTube, press)? What already exists vs. what we'd build? |
| 5 | **Signal Consistency** | Can we keep messaging stable for 12+ months? Any legacy content to reconcile? Multimodal feasible (YouTube/images/data)? |

In addition to the five-signal score, capture these niche-level inputs:

- **Primary intent mode**: Exploratory / Diagnostic / Transactional / Navigational.
- **Query shape**: short head, mid-tail, long-tail (7+ words), question form.
- **Geography**: global / national / local (city-level changes the playbook).
- **Competitor SERP read** (manual): are positions 3–7 occupied by forums, thin sites, outdated content, or established E-E-A-T players?
- **AI Overview presence**: does an AIO already trigger? Who's cited? Is YouTube cited?
- **Platform fit**: which of the six platforms (ChatGPT, Claude, Gemini, AI Overviews, Perplexity, Copilot) is this niche most exposed to?

---

## 4. Tagging: Quick-Win / Mid-Term / Long-Term

Every niche must carry one tag. If the rubric puts it on a boundary, default to the slower tag and explain why.

### Quick-win (first measurable result ≤ 90 days)
- KD ≤ 20 **or** weak SERP (forums, thin pages, outdated content in top 10).
- Scope = 1 pillar + 5–10 supporting pages (single tight cluster).
- Identity Clarity ≥ 4 with no disambiguation work needed.
- Long-tail/question queries (7+ words) where either no AIO triggers yet **or** AIO citation slot is grabable (≥ 1 cited source from outside top 50).
- ≥ 1 multimodal asset feasible inside 30 days (YouTube, image set, data table).
- Ecosystem already partly built (≥ 2 of: Companies House, LinkedIn, GitHub, Trustpilot, active Reddit/X presence) **or** trivial to add.
- Total rubric score ≥ 17/25 with no signal < 3.

### Mid-term (3–9 months to consolidated visibility)
- KD 20–40 **or** mixed SERP (some thin, some authoritative).
- Scope = 25–50 pages across 2–4 clusters; programmatic templates may apply.
- One signal at 2 (typically Identity Clarity disambiguation, or Ecosystem Validation gap).
- Requires net-new external validation: Wikidata entry, G2/Capterra/Trustpilot, podcast guesting, organic Reddit presence, original data study.
- AIO already triggers and cites incumbents; we need consensus signal across ≥ 3 independent sources before AI platforms reweight.
- Total rubric score 12–17/25.

### Long-term (9–24 months, brand-level build)
- KD 40+ **or** SERP dominated by strong E-E-A-T incumbents.
- Scope = 100+ pages, multi-cluster, full ecosystem build.
- Two or more signals at 2, **or** Identity Clarity ≤ 2 (entity construction required).
- Requires sustained multimodal output (full YouTube channel, recurring original research, press programme) to build temporal signal.
- Wikidata / Crunchbase / industry-recognised awards needed.
- Total rubric score < 12/25, **or** any signal at 1.

If a niche has **any signal at 0**, it's a **no-go** — say so explicitly and propose a precursor niche or a fix.

---

## 5. Output Template (what Claude returns in Mode 1)

```
NICHE: <one-line restatement>

INTENT MODE: <Exploratory|Diagnostic|Transactional|Navigational>
QUERY SHAPE: <short|mid|long-tail|question>
GEOGRAPHY: <global|UK national|UK local: city>
PRIMARY PLATFORM EXPOSURE: <AIO|ChatGPT|Perplexity|Gemini|Claude|Copilot>

FIVE SIGNAL SCORE  (/25)
  1. Identity Clarity        x/5  — <one line>
  2. Subject Authority       x/5  — <one line>
  3. Meaning Architecture    x/5  — <one line>
  4. Ecosystem Validation    x/5  — <one line>
  5. Signal Consistency      x/5  — <one line>

SERP / AIO READ
  - Top-10 competitors: <list>
  - AIO triggers: <yes/no, who cited, multimodal cited?>
  - Citation slot opportunity: <which source could we displace>

TAG: <quick-win | mid-term | long-term>
RATIONALE: <2–3 lines>

BUILD PLAN
  Pillar:  <topic>
  Spokes:  <list of 5–10 (quick-win) or cluster map (mid/long)>
  Schema:  <Organisation, FAQ, Product, HowTo, etc.>
  Multimodal: <YouTube? data viz? images?>
  Ecosystem moves: <Wikidata? G2? Reddit? press?>
  First 30 days: <concrete actions>
  Next 90 days: <if mid/long>

RISKS
  - <AIO displacement / zero-click exposure>
  - <identity collisions>
  - <ecosystem gaps>

KPIs (per Rank4AI)
  - Inclusion Rate (target %, baseline)
  - Citation Frequency (target)
  - Misclassification Rate (must be < x%)
  - Sentiment Alignment
```

Keep it tight. No filler. If a section is N/A, write `n/a — <reason>`, don't pad.

---

## 6. Platform-Specific Optimisation Cheat Sheet

The Five Signal Model is platform-agnostic, but execution differs. When proposing a build plan, weight tactics to where the niche actually surfaces.

| Platform | What it trusts most | Niche moves that win |
|----------|---------------------|----------------------|
| **Google AI Overviews / Gemini** | Google's own index, structured data, freshness, YouTube | Schema stack, FAQ blocks, YouTube companion content, original data, recency stamps |
| **ChatGPT** | Wikipedia, internet consensus, professional platforms | Wikidata + Wikipedia-grade sources, LinkedIn presence, consistent entity language across web |
| **Perplexity** | Real-time crawl, expert sources, customer reviews | Recency, named-expert quotes, G2/Trustpilot, citation-friendly passage structure |
| **Claude** | Consistent entity descriptions across multiple independent environments | Identity language identical across site, schema, directories, profiles; reconcile legacy content |
| **Copilot** | Bing index, LinkedIn, professional platforms | Bing Webmaster, LinkedIn company + author pages, professional directories |

Default targets in any plan: **be cited by ≥ 3 platforms** (consensus signal triggers AIO citations more reliably than any single optimisation), and ensure at least one **multimodal** asset (multimodal content shows materially higher selection rates per current research).

---

## 7. Reference Data (April 2026)

Use these when justifying scores, tags, or build choices. Refresh quarterly.

- **AI Overview citation behaviour**: 88% of AIOs cite 3+ sources; 46.5% of cited URLs rank outside top 50 organic; YouTube is the single most-cited domain (≈18% of citations from outside top 100).
- **Selection probability**: pages with 15+ recognised entities ≈ 4.8× more likely to be cited; high semantic completeness ≈ 4.2× more likely; multimodal ≈ 1.5× higher selection rate vs. text-only.
- **Long-tail / question dominance**: ≈ 46% of AIO appearances on 7+ word queries; ≈ 58% are question queries.
- **Zero-click reality**: ≈ 83% zero-click rate on AIO-triggered searches; AIOs reduce CTR by ≈ 58% on affected queries. **Implication**: cited-but-not-clicked is now a primary KPI; plan for inclusion, not just traffic.
- **Cited-page upside**: cited pages earn ≈ 35% more organic clicks and ≈ 91% more paid clicks vs. uncited competitors.
- **Source preferences**: Wikipedia ≈ 7.8% of all ChatGPT citations; Reddit ≈ 6.6% of Perplexity citations and ≈ 2.2% of AIO citations.
- **Niche keyword baseline**: 100–1,000 monthly volume, KD 0–30, high-intent — still the standard quick-win envelope.
- **Topical authority threshold**: ≥ 25 authoritative articles in a tightly connected cluster is the working minimum to register as authoritative.

These figures are directional, not contractual. When a number changes the recommendation materially, re-verify before scoring.

---

## 8. Working Conventions

- **British English** in all output (Rank4AI is a UK entity).
- **No filler, no hype.** Score honestly; if a niche is weak, say so.
- **Cite the rubric, not opinion.** Every tag and recommendation must trace back to §3 or §4.
- **Stop at the brief.** Mode 1 ends at the build plan. Don't start writing pages, schema, or code until explicitly asked (that's Mode 4).
- **Respect Adam's framework.** Don't invent new signals or rename existing ones. The model is fixed at five.
