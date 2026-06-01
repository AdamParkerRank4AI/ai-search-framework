# High-Risk Checkout Risk Framework
## Detecting "Transfer-in-Disguise" Checkouts

A framework for identifying ecommerce checkout flows that present as ordinary
card purchases but actually move funds as irreversible transfers — "back to
bank" (account-to-account) and "pay to crypto" being the dominant patterns.

**Status:** Working framework (v0.1)

**Audience:** Payment service providers, acquirers, banks, fraud and risk teams,
and underwriting/onboarding analysts.

---

## 1. The Problem: When a Checkout Is Not a Purchase

A conventional ecommerce checkout collects card details and pulls funds through
the card rails. Those rails carry consumer protection: authorisation,
3-D Secure, chargeback rights and scheme dispute resolution. The buyer can
reverse the transaction if goods never arrive or the merchant is fraudulent.

A growing class of high-risk and outright fraudulent sites present the *visual
and interaction language* of a card checkout — a basket, an order summary, a
"Pay now" button, a padlock — while the underlying money movement is something
else entirely:

- An **account-to-account (A2A) bank transfer** ("back to bank"), pushed by the
  victim from their own bank app.
- A **crypto purchase or wallet transfer** ("pay to crypto"), converting fiat to
  an irreversible on-chain payment.
- A **manual / off-rails settlement** (e.g. "contact us to complete payment",
  wire instructions, gift cards, vouchers).

The defining characteristic is **deception about the rail, not just the goods.**
The user believes they are making a protected card purchase. They are in fact
authorising an irreversible push payment. When the goods or service fail to
materialise, there is no chargeback — the funds are gone.

This framework exists to **score how likely a given checkout is a
transfer-in-disguise**, so that it can be flagged before settlement, before
onboarding, or during monitoring.

---

## 2. Why This Matters

**The rail determines the recourse.** Card disputes are reversible; push
payments and crypto generally are not. A merchant or scam operator who can move
a buyer from card rails to a push rail removes the buyer's primary protection
and the acquirer's primary control.

**Disguise defeats consumer judgement.** Most buyers assess trust visually — a
professional checkout, a padlock, a recognisable layout. Disguised-transfer
flows weaponise that heuristic. The interface signals "safe card purchase" while
the mechanism is "irreversible transfer."

**It shifts liability and exposure.** Authorised Push Payment (APP) fraud,
crypto fraud and off-rails settlement sit in regulatory and reputational grey
zones. Detecting the disguise early protects the buyer, the legitimate payment
ecosystem, and the institution's risk position.

**It is a moving target.** Operators iterate: new redirect chains, new "open
banking" wrappers, new crypto on-ramps, new copy. A signal-based framework is
more durable than a blocklist because it targets the *structure of the
deception* rather than specific URLs.

---

## 3. Core Concept: The Disguise Gap

Every transfer-in-disguise checkout contains a **disguise gap** — a mismatch
between what the interface *implies* about the payment and what the mechanism
*actually does*.

| Dimension | What the checkout implies | What actually happens |
|-----------|---------------------------|------------------------|
| Rail | Card payment (Visa/Mastercard) | A2A bank transfer or crypto |
| Reversibility | Chargeable / disputable | Irreversible push payment |
| Counterparty | A merchant being *paid* | A beneficiary being *funded* |
| Action | "Buy a product" | "Send money" / "fund an account" |
| Protection | Scheme + acquirer protection | None |

The wider the disguise gap, the higher the risk. The framework below is a
systematic way to measure that gap from observable signals.

---

## 4. Taxonomy of Disguised-Transfer Mechanisms

### 4.1 Back-to-Bank (Account-to-Account / APP)
The checkout routes the user to a bank transfer rather than a card charge.
Variants:

- **Manual bank transfer.** Order summary, then "transfer to this sort
  code / IBAN / account number to complete your order." The user pushes the
  payment from their own banking app.
- **Open-banking wrapper.** A legitimate-looking "Pay by bank" redirect, but the
  beneficiary, reference, or amount is mismatched, or the brand is spoofed.
- **Faster Payments / SEPA / wire push.** Same pattern at higher value, often
  for "invoices," "deposits," or "verification payments."

**Hallmark:** the user initiates the payment *from their side*, so card-scheme
protection never applies.

### 4.2 Pay-to-Crypto
The checkout converts the purchase into a crypto payment.

- **On-ramp redirect.** "Pay" leads to a fiat-to-crypto on-ramp; the user buys
  crypto that is then sent to a wallet they don't control.
- **Direct wallet address / QR.** "Send X to this address to complete." May be
  framed as a discount ("save 10% paying in crypto").
- **"Crypto checkout processor" spoof.** Mimics a legitimate crypto PSP but the
  destination wallet is the operator's.

**Hallmark:** irreversibility plus pseudonymous beneficiary.

### 4.3 Off-Rails / Manual Settlement
The checkout cannot actually complete on-platform.

- "Order received — an agent will contact you to arrange payment."
- Gift cards, vouchers, prepaid codes presented as a payment method.
- WhatsApp/Telegram/email handoff to "finalise."

**Hallmark:** the payment leaves any auditable, reversible rail entirely.

### 4.4 Rail-Switch / Bait-and-Switch
A genuine card field is shown, then fails ("card declined — please use bank
transfer / crypto instead"), funnelling the user to an irreversible rail. This
is the most deceptive variant because it actively *defeats* the protected path.

---

## 5. The Signal Model

Risk is assessed across five signal layers. Weakness (i.e. red flags) in any
layer raises suspicion; concentration across layers is near-conclusive.

### Signal 01 — Rail Integrity
*Does the stated payment method match the actual money movement?*

Red flags:
- "Card" is offered but consistently fails, then a transfer/crypto path is
  offered.
- The only functional method is bank transfer, crypto, gift card or "manual."
- Final-step beneficiary name does not match the merchant/brand.
- Amount or reference field is free-text / editable in a way card checkouts are
  not.
- No card processor, 3-D Secure step, or scheme branding ever appears.

### Signal 02 — Interface Honesty
*Does the UI accurately represent the transaction it is creating?*

Red flags:
- "Pay now / Buy / Checkout" language attached to an action that is actually
  "send / transfer / fund."
- Trust marks (padlock, "Secure checkout," card-scheme logos) with no
  corresponding card-rail behaviour.
- A cart/order-summary aesthetic wrapped around what is functionally a transfer
  form.
- Countdown timers, "complete within X minutes or lose your order" pressure on a
  payment step.

### Signal 03 — Reversibility & Recourse
*Can the buyer get their money back if the deal is bad?*

Red flags:
- Payment method has no chargeback path (push transfer, crypto, gift card).
- No refund mechanism that uses the same rail as payment.
- Terms disclaim all refunds, or refunds are "manual" / "in store credit only."
- "Crypto/bank discount" used to steer away from card rails.

### Signal 04 — Counterparty & Beneficiary Clarity
*Who actually receives the money, and does it match the seller?*

Red flags:
- Beneficiary is a personal account, a money-transfer agent, or an unrelated
  company.
- Wallet address / bank details differ from the trading entity or change between
  sessions.
- No verifiable legal entity, registration, or consistent identity behind the
  checkout.
- Multiple unrelated "stores" resolve to the same beneficiary details.

### Signal 05 — Behavioural & Contextual Signals
*Does the surrounding context behave like a real merchant?*

Red flags:
- Pressure, scarcity, or "act now" framing concentrated on the payment step.
- Handoff to chat apps / email to "complete payment."
- Prices, inventory, or branding cloned from a legitimate retailer.
- Newly registered domain, mismatched contact details, or recycled template.
- Reviews, badges, and "verified" seals that do not link to real third parties.

---

## 6. The Detection Model (Gated, Not Summed)

A naïve model scores all five signals and sums them. That fails in two
directions: it **flags honest** pay-by-bank/crypto merchants (who score high on
"uses irreversible rail") and it **misses clean disguises** that trip only one
decisive signal. The working model is therefore **gated**: a small number of
dispositive facts decide the outcome, and the soft signals only move cases that
sit on the boundary.

### Step 1 — Establish the two facts that decide most cases

The model turns on two observable facts, captured at the *final* payment step
(and after any deliberate card failure):

- **Fact A — Actual rail.** What truly moves the money: `CARD` (with
  authorisation / 3-DS), `A2A` (push bank transfer), `CRYPTO`, or `OFF_RAILS`
  (gift card, manual, chat handoff).
- **Fact B — Claimed protection.** What the interface *implies*: does it present
  itself as a protected card purchase (card logos, "secure card checkout",
  card-style fields, padlock-as-card-trust)?

### Step 2 — Apply the primary gate (Rail Honesty)

| Actual rail (A) | Interface claims card protection? (B) | Outcome |
|-----------------|----------------------------------------|---------|
| CARD | — | **PASS** — protected purchase, exit model |
| A2A / CRYPTO / OFF_RAILS | **No** (rail honestly disclosed) | **WATCH** — legitimate alt-payment until proven otherwise → go to Step 4 |
| A2A / CRYPTO / OFF_RAILS | **Yes** (presented as card purchase) | **DISGUISE CONFIRMED** — irreversible rail dressed as protected card → go to Step 3 |

This single gate does most of the work. The disguise *is* the mismatch in this
table; everything else is corroboration or false-positive control.

### Step 3 — Apply the override triggers (any one ⇒ Critical)

Independent of any score, treat as **Critical** if any of these is observed,
because each is the deception in action:

- **Rail-switch.** A card field that fails ("card declined — use bank
  transfer/crypto") and funnels to an irreversible rail.
- **Beneficiary mismatch.** Receiving account/wallet/entity differs from the
  advertised merchant, is a personal account, or changes between sessions.
- **Beneficiary reuse.** The same account/wallet sits behind multiple unrelated
  "stores."

### Step 4 — Corroborating score (only for WATCH / boundary cases)

For cases that cleared the gate as plausibly legitimate, or sit on the boundary,
score the soft signals (Interface Honesty, Reversibility disclosure,
Counterparty clarity, Behavioural context) **0–4 each** for how strongly
disguise red-flags are present. These only *promote* a case; they never clear a
gate failure.

| Soft score (0–16) | Effect |
|--------------------|--------|
| 0–3 | Stays **Clear/Watch** — honest alt-payment merchant |
| 4–8 | **Elevated** — review the rail-honesty disclosure |
| 9+ | **Elevated → escalate** — disguise likely despite passing the gate |

### Outcome bands

| Band | How reached | Suggested action |
|------|-------------|------------------|
| Clear | Actual rail = CARD, or honest disclosure + low soft score | Monitor only |
| Watch | Irreversible rail, honestly disclosed | Enhanced monitoring |
| Elevated | Gate ambiguity or soft score 4–8 | Hold / manual review / restrict |
| Critical | Gate = DISGUISE, or any override trigger | Block / offboard / escalate |

**Why this model works:** the decision is driven by the *disguise gap itself*
(rail vs. claimed protection, beneficiary vs. merchant), which is precisely what
separates a fraudulent flow from an honest one — rather than by the rail choice,
which does not. This keeps false positives on legitimate pay-by-bank/crypto
merchants low while making a single decisive signal (rail-switch, beneficiary
mismatch) sufficient to catch the disguise.

---

## 7. Detection Workflow

1. **Capture the checkout.** Record the full payment journey, including any
   "card declined → alternative method" branches. The disguise often only
   reveals itself at the final step or after a deliberate card failure.
2. **Establish Fact A (actual rail).** Determine what really moves the money:
   `CARD`, `A2A`, `CRYPTO`, or `OFF_RAILS`.
3. **Establish Fact B (claimed protection).** Does the interface present itself
   as a protected card purchase?
4. **Apply the primary gate** (Step 2 table). Most cases resolve here.
5. **Check the override triggers** — rail-switch, beneficiary mismatch,
   beneficiary reuse. Any one ⇒ Critical.
6. **Score soft signals only for boundary/Watch cases** and apply the band.
7. **Decide and document.** Record the disguise-gap evidence (rail vs. claimed
   protection, beneficiary vs. merchant) so the decision is auditable.
8. **Re-test periodically.** Operators rotate domains, beneficiaries and copy;
   re-run the gate on a schedule and on any reported incident.

---

## 8. Response & Mitigation

- **Pre-settlement holds** on transactions where rail integrity scores high.
- **Onboarding rejection / EDD** where a merchant's checkout exhibits disguise
  signals at underwriting.
- **Buyer-facing warnings** when a protected rail is being abandoned for an
  irreversible one ("You are about to send a bank transfer / crypto payment.
  This is not a card purchase and cannot be reversed").
- **Beneficiary intelligence sharing** — recycled accounts and wallets across
  "stores" are a powerful network signal.
- **Rail-switch interdiction** — treat "card declined, use transfer/crypto
  instead" as a high-severity event, not a routine fallback.

---

## 9. Measurement

Track the framework's effectiveness with:

- **Detection rate** — share of confirmed disguised-transfer checkouts caught
  before settlement.
- **Disguise gap precision** — how reliably high scores correspond to true
  transfer-in-disguise cases (vs. legitimate alternative-payment merchants).
- **False-positive rate** — legitimate "Pay by bank" / crypto merchants
  incorrectly flagged. (Legitimacy hinges on *honest representation of the
  rail*, not on the rail itself.)
- **Time-to-detection** — onboarding vs. monitoring vs. post-incident.

---

## 10. Important Boundary: Disguise, Not Rail

A2A and crypto payments are **legitimate rails** used by many honest merchants.
This framework does **not** flag a checkout simply for using them. It flags the
**disguise** — presenting an irreversible push payment as if it were a protected
card purchase, switching rails to defeat protection, or hiding the true
beneficiary.

The test is honesty of representation. A merchant that clearly says "Pay by bank
transfer — this is not a card payment" scores low. A site that dresses a
transfer up as a card checkout scores high. The framework measures the **gap
between what is shown and what is done.**
