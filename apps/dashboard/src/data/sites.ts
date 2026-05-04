// Dashboard data — source of truth for what's planned, what's drafted,
// what monetises how. Updated as sites build out. Mobile-first reading.

export type SiteStatus = 'live' | 'building' | 'scaffolded' | 'planned' | 'tbd';
export type Surface = 'SEO' | 'AI Overviews' | 'AI Search' | 'Mixed';

export type Pillar = {
  name: string;
  slug: string;
  totalPages: number;
  draftedPages: number;
  topPages: { slug: string; title: string; status: 'planned' | 'drafted' | 'shipped' }[];
  note?: string;
};

export type Site = {
  slug: string;
  name: string;
  shortName: string;
  domain: string;
  port: number;
  status: SiteStatus;
  // The 1-line job description
  role: string;
  // 2–3 sentence "what is this site?"
  whatItIs: string;
  // 1–2 sentence "what makes this site different from sister sites?"
  whatsDifferent: string;
  // Where the money comes from
  monetisation: string;
  primarySurface: Surface;
  pillars: Pillar[];
  totalPlannedPages: number;
  draftedPages: number;
  revenueScenarioMid: number; // £/yr
  planFile?: string;
  liveDevPath?: string;
};

export const NETWORK = {
  thesis:
    'Six UK SMB lead-gen properties plus a Fleet of multilingual / hyper-local satellites. Optimised simultaneously for SEO, Google AI Overviews and AI search citation. Traffic is the meta-goal; every niche has a named monetisation path. Forms are deferred — current phase is structure, plan, pages, niches.',
  combinedRevenueMidGBP: 1_280_000, // synthesis figure
  combinedRevenueLowGBP: 760_000,
  combinedRevenueHighGBP: 2_070_000,
  totalPlannedPages: 575,
  splits: {
    bblVsFundbiz:
      'BBL is editorial / review only — no application forms. FundBiz is the broker / transactional site that runs the funnel. BBL writes the journalism that earns the AI-Overview citation; FundBiz converts the loan lead at £100–£300 direct CPL.',
    brandVsFleet:
      'Brand sites = English UK only, deep editorial, named authors, AI-citation engine. Fleet = separate satellite domains for multilingual content (Polish, Bengali, Urdu, Turkish, etc.), hyper-local geographies, and single-niche microsites. Multilingual NEVER goes into a /pl/ subfolder on a brand site — it dilutes the brand entity in the LLM graph.',
  },
  formsDeferred:
    'No lead-capture forms in this phase per user direction. CTAs across all sites are placeholder labels until phase 2. FCA permission is NOT required (limited companies / LLPs / partnerships of 4+ only on FundBiz when forms ship).',
} as const;

// ============================================================
// SITES
// ============================================================

export const SITES: Site[] = [
  {
    slug: 'cardmachines',
    name: 'CardMachines',
    shortName: 'CM',
    domain: 'cardmachines.co.uk',
    port: 4321,
    status: 'building',
    role: 'UK card terminals + merchant accounts + payment processing',
    whatItIs:
      'The dedicated UK payments site. Editorial + transactional combined: terminal reviews, switching content, vertical pages by trade, high-risk merchant content, booking and accounting integrations.',
    whatsDifferent:
      'Single biggest commercial vertical in the network — high-risk merchant UK alone is ~£450k/yr at modest market share, the largest single revenue line. Worldpay/Barclaycard switching is the second-largest. UK SERPs for high-risk and Tap-to-Pay are near-vacuums.',
    monetisation:
      'Awin (Tide, SumUp, Zettle, Square) + direct (SumUp, Square, Zettle, Stripe, Dojo) + direct CPL (Take Payments, Paymentsense, MerchantSavvy) + high-risk direct (Trust Payments, Universe, Acquired.com — £200–500 CPL).',
    primarySurface: 'AI Search',
    revenueScenarioMid: 780_000,
    totalPlannedPages: 155,
    draftedPages: 6,
    planFile: 'docs/sites/cardmachines-plan.md',
    liveDevPath: 'pnpm dev:cm',
    pillars: [
      {
        name: 'High-risk merchant accounts',
        slug: 'high-risk',
        totalPages: 19,
        draftedPages: 3,
        topPages: [
          { slug: '/high-risk/', title: 'High-risk hub', status: 'drafted' },
          { slug: '/high-risk/cbd/', title: 'CBD merchant account UK', status: 'drafted' },
          { slug: '/high-risk/vape/', title: 'Vape shop card machine UK', status: 'drafted' },
          { slug: '/high-risk/adult/', title: 'Adult merchant account UK', status: 'planned' },
          { slug: '/high-risk/firearms/', title: 'Firearms merchant UK', status: 'planned' },
          { slug: '/high-risk/gambling/', title: 'Gambling-adjacent merchant UK', status: 'planned' },
        ],
        note: 'Single biggest revenue line — ~£450k/yr potential. UK SERP dominated by US-coded pages.',
      },
      {
        name: 'Switching from Worldpay / Barclaycard',
        slug: 'switching',
        totalPages: 16,
        draftedPages: 1,
        topPages: [
          { slug: '/switch/cancel-worldpay/', title: 'Cancel Worldpay', status: 'drafted' },
          { slug: '/switch/cancel-barclaycard-merchant-services/', title: 'Cancel Barclaycard', status: 'planned' },
          { slug: '/switch/cancel-elavon/', title: 'Cancel Elavon', status: 'planned' },
          { slug: '/switch/exit-cost-calculator/', title: 'Exit cost calculator', status: 'planned' },
          { slug: '/switch/worldpay-alternatives/', title: 'Worldpay alternatives', status: 'planned' },
        ],
        note: 'Hot transactional intent. £75–200k/yr opportunity.',
      },
      {
        name: 'Terminal reviews',
        slug: 'reviews',
        totalPages: 22,
        draftedPages: 1,
        topPages: [
          { slug: '/reviews/dojo-go/', title: 'Dojo Go review', status: 'drafted' },
          { slug: '/reviews/sumup-solo/', title: 'SumUp Solo review', status: 'planned' },
          { slug: '/reviews/zettle-reader-2/', title: 'Zettle Reader 2 review', status: 'planned' },
          { slug: '/reviews/stripe-reader-s700/', title: 'Stripe Reader S700 review', status: 'planned' },
          { slug: '/reviews/bbpos-wisepos-e/', title: 'BBPOS WisePOS E review', status: 'planned' },
        ],
        note: 'Biggest AI Overview citation driver in the network.',
      },
      {
        name: 'Tap to Pay on iPhone',
        slug: 'tap-to-pay',
        totalPages: 13,
        draftedPages: 0,
        topPages: [
          { slug: '/tap-to-pay-iphone/', title: 'Tap to Pay UK hub', status: 'planned' },
          { slug: '/tap-to-pay-iphone/sumup/', title: 'SumUp Tap to Pay', status: 'planned' },
          { slug: '/tap-to-pay-iphone/square/', title: 'Square Tap to Pay', status: 'planned' },
        ],
        note: '3 years post-launch — UK content vacuum.',
      },
      {
        name: 'Comparisons (X vs Y)',
        slug: 'vs',
        totalPages: 9,
        draftedPages: 0,
        topPages: [
          { slug: '/vs/sumup-vs-zettle/', title: 'SumUp vs Zettle', status: 'planned' },
          { slug: '/vs/dojo-vs-worldpay/', title: 'Dojo vs Worldpay', status: 'planned' },
          { slug: '/vs/square-vs-stripe/', title: 'Square vs Stripe Terminal', status: 'planned' },
        ],
      },
      {
        name: 'By trade (mobile readers)',
        slug: 'trade',
        totalPages: 17,
        draftedPages: 0,
        topPages: [
          { slug: '/trade/plumber/', title: 'Card machine for plumbers', status: 'planned' },
          { slug: '/trade/electrician/', title: 'Card reader for electricians', status: 'planned' },
          { slug: '/trade/mobile-mechanic/', title: 'Mobile mechanic card reader', status: 'planned' },
        ],
        note: 'MTD April 2026 trigger.',
      },
      {
        name: 'Hospitality verticals',
        slug: 'hospitality',
        totalPages: 15,
        draftedPages: 0,
        topPages: [
          { slug: '/hospitality/restaurant/', title: 'Card machine for restaurants', status: 'planned' },
          { slug: '/hospitality/pub/', title: 'Card machine for pubs', status: 'planned' },
          { slug: '/hospitality/takeaway/', title: 'Card machine for takeaways', status: 'planned' },
        ],
      },
      { name: 'Retail verticals', slug: 'retail', totalPages: 9, draftedPages: 0, topPages: [] },
      { name: 'Salon / beauty / health', slug: 'salon', totalPages: 11, draftedPages: 0, topPages: [] },
      { name: 'Integrations (EPOS, accounting, booking)', slug: 'integrations', totalPages: 14, draftedPages: 0, topPages: [] },
      { name: 'Guides & glossary', slug: 'guides', totalPages: 16, draftedPages: 0, topPages: [] },
      { name: 'Trust pages', slug: 'trust', totalPages: 5, draftedPages: 1, topPages: [{ slug: '/', title: 'Homepage', status: 'drafted' }] },
    ],
  },
  {
    slug: 'bbl',
    name: 'BestBusinessLoans',
    shortName: 'BBL',
    domain: 'bestbusinessloans.co.uk',
    port: 4322,
    status: 'building',
    role: 'UK business loans editorial / review',
    whatItIs:
      'Independent editorial site for UK business loans. "Best X for Y" listicles, head-to-head comparisons, lender reviews, "what is" definition pages. Trust + AI-citation play.',
    whatsDifferent:
      'Pure editorial — NO application forms. Trust layer that earns AI-Overview citations and feeds FundBiz the loan funnel via internal links. The lender review programme is the biggest AI-citation engine; persona axis (women, halal, no-PG, post-decline) is a vacuum.',
    monetisation:
      'Awin (Funding Circle, iwoca, Capital on Tap, Tide, Capify, Liberis) + cross-link contribution to FundBiz application funnel (£100–300 direct CPL).',
    primarySurface: 'AI Search',
    revenueScenarioMid: 75_000, // direct + £100k+ cross-link contribution
    totalPlannedPages: 100,
    draftedPages: 3,
    planFile: 'docs/sites/bbl-plan.md',
    liveDevPath: 'pnpm dev:bbl',
    pillars: [
      {
        name: 'Halal / Sharia finance',
        slug: 'halal',
        totalPages: 12,
        draftedPages: 2,
        topPages: [
          { slug: '/halal/', title: 'Halal business finance hub', status: 'drafted' },
          { slug: '/halal/best-sharia-business-loans-uk-2026/', title: 'Best Sharia loans 2026', status: 'drafted' },
          { slug: '/halal/qardus-review/', title: 'Qardus review', status: 'planned' },
          { slug: '/halal/gatehouse-bank-review/', title: 'Gatehouse Bank review', status: 'planned' },
          { slug: '/halal/what-is-murabaha/', title: 'What is Murabaha?', status: 'planned' },
        ],
        note: 'Single biggest content vacuum in the BBL plan. Zero editorial competitors.',
      },
      {
        name: 'Women-led / underrepresented',
        slug: 'women',
        totalPages: 8,
        draftedPages: 0,
        topPages: [
          { slug: '/women/', title: 'Women founders hub', status: 'planned' },
          { slug: '/women/best-business-loans-women-2026/', title: 'Best loans for women 2026', status: 'planned' },
        ],
        note: 'Persona axis is a vacuum — only product pages exist on competitor sites.',
      },
      {
        name: 'Post-decline editorial',
        slug: 'declined',
        totalPages: 10,
        draftedPages: 0,
        topPages: [
          { slug: '/declined/best-lenders-after-decline-2026/', title: 'Best lenders after decline', status: 'planned' },
          { slug: '/declined/business-loan-after-bank-said-no/', title: 'After the bank said no', status: 'planned' },
        ],
        note: 'Editorial layer above FundBiz matcher — feeds £100–300 CPL funnel.',
      },
      {
        name: 'Lender reviews',
        slug: 'reviews',
        totalPages: 18,
        draftedPages: 0,
        topPages: [
          { slug: '/reviews/funding-circle/', title: 'Funding Circle review', status: 'planned' },
          { slug: '/reviews/iwoca/', title: 'iwoca review', status: 'planned' },
          { slug: '/reviews/liberis/', title: 'Liberis review', status: 'planned' },
          { slug: '/reviews/youlend/', title: 'YouLend review', status: 'planned' },
          { slug: '/reviews/capify/', title: 'Capify review', status: 'planned' },
        ],
        note: '5 priority lenders pay direct £100–300 CPL. Single biggest AI-citation magnet.',
      },
      {
        name: 'Best-of listicles by sector',
        slug: 'best-by-sector',
        totalPages: 14,
        draftedPages: 0,
        topPages: [
          { slug: '/best/business-loans-uk-2026/', title: 'Best business loans UK 2026', status: 'planned' },
          { slug: '/best/business-loans-for-restaurants/', title: 'Best loans for restaurants', status: 'planned' },
          { slug: '/best/business-loans-for-salons/', title: 'Best loans for salons', status: 'planned' },
        ],
      },
      { name: 'X vs Y comparisons', slug: 'vs', totalPages: 8, draftedPages: 0, topPages: [] },
      { name: 'Definition guides', slug: 'guides', totalPages: 14, draftedPages: 0, topPages: [] },
      { name: 'By persona (sole trader, ltd, etc.)', slug: 'persona', totalPages: 9, draftedPages: 0, topPages: [] },
      { name: 'Glossary', slug: 'glossary', totalPages: 4, draftedPages: 0, topPages: [] },
      { name: 'Trust pages (about, methodology, authors)', slug: 'trust', totalPages: 3, draftedPages: 1, topPages: [{ slug: '/', title: 'Homepage', status: 'drafted' }] },
    ],
  },
  {
    slug: 'fundbiz',
    name: 'FundBiz',
    shortName: 'FB',
    domain: 'fundbiz.co.uk',
    port: 4323,
    status: 'building',
    role: 'UK business loans broker / transactional (Ltd / LLP / partnerships of 4+)',
    whatItIs:
      'The funnel site. Sector landing pages, eligibility checkers, calculators, application forms (forms come later). Captures qualified loan leads. Allowed to flex into adjacent SMB finance (cards, accounts, insurance, MCA, asset finance).',
    whatsDifferent:
      'B2B only — limited companies, LLPs, partnerships of 4+ (sole traders deflected to BBB Start Up Loans). Outside the FCA perimeter. The post-decline funnel is the single biggest revenue line — £225–360k/yr TAM at modest market share, with no competitor running an interactive matcher.',
    monetisation:
      'Direct CPL with lenders (Liberis, YouLend, Capify, 365, iwoca, Funding Circle — £100–300 CPL) + Awin for ancillaries (Tide, Capital on Tap, Superscript).',
    primarySurface: 'SEO',
    revenueScenarioMid: 430_000,
    totalPlannedPages: 120,
    draftedPages: 3,
    planFile: 'docs/sites/fundbiz-plan.md',
    liveDevPath: 'pnpm dev:fb',
    pillars: [
      {
        name: 'Post-decline funnel',
        slug: 'declined',
        totalPages: 22,
        draftedPages: 2,
        topPages: [
          { slug: '/declined/', title: 'Post-decline hub', status: 'drafted' },
          { slug: '/declined/by-bank/lloyds/', title: 'Lloyds declined business loan', status: 'drafted' },
          { slug: '/declined/by-bank/natwest/', title: 'NatWest declined business loan', status: 'planned' },
          { slug: '/declined/by-bank/hsbc/', title: 'HSBC declined business loan', status: 'planned' },
          { slug: '/declined/bad-credit/', title: 'Business loan with bad credit', status: 'planned' },
          { slug: '/declined/with-ccj/', title: 'Business loan with CCJ', status: 'planned' },
          { slug: '/declined/first-year-trading/', title: 'Business loan first year trading', status: 'planned' },
        ],
        note: '£225–360k/yr TAM. No competitor runs a diagnose-the-decline matcher.',
      },
      {
        name: 'Sector landers',
        slug: 'sectors',
        totalPages: 32,
        draftedPages: 0,
        topPages: [
          { slug: '/sectors/hospitality/', title: 'Hospitality business loans', status: 'planned' },
          { slug: '/sectors/restaurants/', title: 'Restaurant business loans', status: 'planned' },
          { slug: '/sectors/e-commerce/', title: 'E-commerce business loans', status: 'planned' },
          { slug: '/sectors/construction/', title: 'Construction business loans', status: 'planned' },
          { slug: '/sectors/dental-practices/', title: 'Dental practice loans', status: 'planned' },
        ],
        note: 'Rangewell only competitor with proper sector landers — UX is dated.',
      },
      {
        name: 'Products',
        slug: 'products',
        totalPages: 21,
        draftedPages: 0,
        topPages: [
          { slug: '/products/business-loan/', title: 'Business loan UK', status: 'planned' },
          { slug: '/products/merchant-cash-advance/', title: 'Merchant cash advance UK', status: 'planned' },
          { slug: '/products/asset-finance/', title: 'Asset finance UK', status: 'planned' },
        ],
      },
      { name: 'By amount', slug: 'by-amount', totalPages: 7, draftedPages: 0, topPages: [] },
      { name: 'Calculators (placeholders for now)', slug: 'calculators', totalPages: 7, draftedPages: 0, topPages: [] },
      {
        name: 'Adjacent flex (cards, accounts, insurance)',
        slug: 'adjacent',
        totalPages: 12,
        draftedPages: 0,
        topPages: [
          { slug: '/adjacent/business-credit-cards/', title: 'Business credit cards UK', status: 'planned' },
          { slug: '/adjacent/business-bank-accounts/', title: 'Business bank accounts UK', status: 'planned' },
        ],
        note: 'The 80/20 flex — adjacent SMB finance topics that ride the same funnel.',
      },
      { name: 'Guides', slug: 'guides', totalPages: 11, draftedPages: 0, topPages: [] },
      { name: 'Trust pages', slug: 'trust', totalPages: 4, draftedPages: 1, topPages: [{ slug: '/', title: 'Homepage', status: 'drafted' }] },
      { name: 'Lender redirect (→ BBL)', slug: 'lenders-redirect', totalPages: 1, draftedPages: 0, topPages: [], note: 'Routes /lenders/ requests to BBL editorial — no duplication.' },
    ],
  },
  {
    slug: 'marketinvoice',
    name: 'MarketInvoice',
    shortName: 'MI',
    domain: 'marketinvoice.co.uk',
    port: 4326,
    status: 'planned',
    role: 'UK invoice finance — pure receivables play',
    whatItIs:
      'Dedicated UK invoice finance site. Factoring, invoice discounting, selective invoice finance, recourse vs non-recourse, confidential factoring, spot factoring.',
    whatsDifferent:
      'Pure invoice finance — does not stretch into other trade finance products unless they\'re a direct receivables play. Sector cash-flow plays (construction, recruitment, manufacturing, wholesale, hauliers) over-index here.',
    monetisation:
      'Direct (MarketFinance, Bibby, Aldermore, Sonovate for recruitment, Optimum, Skipton) + brokers (Touch Financial, Wise Factoring).',
    primarySurface: 'SEO',
    revenueScenarioMid: 0, // not yet sized
    totalPlannedPages: 0,
    draftedPages: 0,
    pillars: [],
  },
  {
    slug: 'seocompare',
    name: 'SEOCompare',
    shortName: 'SC',
    domain: 'seocompare.co.uk',
    port: 4327,
    status: 'planned',
    role: 'UK SEO services / agencies / tools comparison',
    whatItIs:
      '80/20 site: 80% pure SEO comparison content (agencies, tools, freelancers), up to 20% adjacent (AI-search-optimisation services where they overlap with SEO buyers).',
    whatsDifferent:
      'The only site in the network where SEO is the topic itself. Cross-link target for the other sites whenever an audience is shopping for SEO support.',
    monetisation:
      'SEMrush + Ahrefs (rev share), Surfer SEO, agency referral fees (negotiate direct, 10–20% of first contract), AI-search audit tools (Profound, Otterly, Peec AI).',
    primarySurface: 'Mixed',
    revenueScenarioMid: 0, // not yet sized
    totalPlannedPages: 0,
    draftedPages: 0,
    pillars: [],
  },
  {
    slug: 'webbuilder',
    name: 'WebBuilder',
    shortName: 'WB',
    domain: 'webbuilder.uk',
    port: 4324,
    status: 'scaffolded',
    role: 'AI-search-optimised website builds + audits — service-led',
    whatItIs:
      'The service site. AI-search audits, AI-ready website builds, managed AI-search-optimisation programmes. Built on the Rank4AI methodology.',
    whatsDifferent:
      'The ONLY site in the network where we deliver the service ourselves rather than refer to an affiliate. Lead capture funnels to our internal delivery team. Different unit economics — service revenue, not commission.',
    monetisation:
      'Direct service revenue: free AI search audit → one-off site build → monthly managed programme. No affiliates.',
    primarySurface: 'AI Search',
    revenueScenarioMid: 0, // not yet sized
    totalPlannedPages: 0,
    draftedPages: 1,
    pillars: [
      { name: 'Homepage + service tiers', slug: 'home', totalPages: 1, draftedPages: 1, topPages: [{ slug: '/', title: 'Homepage', status: 'drafted' }] },
    ],
    liveDevPath: 'pnpm dev:wb',
  },
  {
    slug: 'ainews',
    name: 'AI Search News',
    shortName: 'AIN',
    domain: 'aisearchnews.uk',
    port: 4325,
    status: 'tbd',
    role: 'AI search publication — scope TBD',
    whatItIs:
      'Slot reserved for an AI-search news / publication property. Editorial vs directory, B2B vs B2C, paid newsletter vs ad-supported — all open questions.',
    whatsDifferent:
      'Different product type from the rest of the network — publication / news, not lead-gen. Could feed traffic to the lead-gen sites or run as a standalone monetised publication.',
    monetisation:
      'TBD — newsletter sponsorship, display ads, paid subscriptions, lead-gen for the network.',
    primarySurface: 'AI Search',
    revenueScenarioMid: 0,
    totalPlannedPages: 0,
    draftedPages: 1,
    pillars: [],
    liveDevPath: 'pnpm dev:ai',
  },
];

// ============================================================
// FLEET — separate from brand sites
// ============================================================

export const FLEET = {
  rule: 'Fleet sites live on separate domains, never as subfolders on a brand site. They route leads back into the same monetisation paths but protect the brand sites\' English entity descriptions in the LLM graph.',
  triggers: [
    'All multilingual content (Polish, Bengali, Urdu, Punjabi, Hindi, Gujarati, Turkish, Arabic, Romanian, Mandarin, Albanian, Portuguese, Tagalog, Ukrainian)',
    'Hyper-local geographies (postcode-level, single-town pages)',
    'Single-niche microsites that would dilute a brand site\'s positioning',
  ],
  examples: [
    { name: 'Polish card machines', domain: 'terminalkartowy.uk', community: 'Polish builders / trades' },
    { name: 'Polish business loans', domain: 'biznesdotacje.uk', community: 'Polish SMB owners' },
    { name: 'Bengali curry-house finance', domain: 'curryhousefunding.uk', community: 'Bangladeshi/Indian restaurants' },
    { name: 'Turkish barber loans', domain: 'kuaforfinansman.uk', community: 'Turkish barber shop owners' },
    { name: 'Romanian construction finance', domain: 'finantareconstructii.uk', community: 'Romanian contractors' },
    { name: 'High-risk vape merchant', domain: 'vapemerchant.uk', community: 'Single-niche vape retailers' },
    { name: 'CBD payments', domain: 'cbdpayments.uk', community: 'Single-niche CBD retailers' },
    { name: 'Card machines London', domain: 'cardmachines-london.co.uk', community: 'Hyper-local geo' },
  ],
  status: 'planned — first 3 sites ship after brand sites are live',
};
