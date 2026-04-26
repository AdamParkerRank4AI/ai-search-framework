import { z } from 'zod';

// ---------- Shared primitives ----------

export const moneyBand = z.object({
  min: z.number().nullable(),
  max: z.number().nullable(),
  currency: z.string().default('GBP'),
});

export const cplBand = z.object({
  min: z.number(),
  max: z.number(),
  unit: z.enum(['cpl', 'cpa', 'rev-share-percent']).default('cpl'),
});

export const surface = z.enum(['SEO', 'AI Overviews', 'AI Search']);
export const horizon = z.enum(['quick-win', 'mid-term', 'long-term']);

export const author = z.object({
  name: z.string(),
  slug: z.string(),
  bio: z.string(),
  role: z.string().optional(),
  linkedin: z.string().url().optional(),
  twitter: z.string().url().optional(),
  email: z.string().email().optional(),
  expertise: z.array(z.string()).default([]),
});

export const faq = z.object({
  question: z.string(),
  answer: z.string(),
});

// ---------- CardMachines ----------

export const terminalSchema = z.object({
  name: z.string(),
  manufacturer: z.string(),
  model: z.string(),
  slug: z.string(),
  type: z.enum(['mobile', 'countertop', 'portable', 'integrated', 'softpos']),
  priceGBP: z.number().nullable(),
  monthlyFeeGBP: z.number().nullable(),
  transactionFeePercent: z.number().nullable(),
  transactionFeeFixedPence: z.number().nullable(),
  contractMonths: z.number().nullable(),
  payoutSpeedDays: z.number().nullable(),
  bestFor: z.array(z.string()).default([]),
  pros: z.array(z.string()).default([]),
  cons: z.array(z.string()).default([]),
  verdict: z.string().optional(),
  rating: z.number().min(0).max(5).optional(),
  reviewedBy: z.string().optional(), // author slug
  reviewedDate: z.coerce.date().optional(),
  affiliate: z.object({
    url: z.string().url().optional(),
    network: z.string().optional(), // awin, direct, impact
    cpl: cplBand.optional(),
  }).optional(),
  faqs: z.array(faq).default([]),
});

export const acquirerSchema = z.object({
  name: z.string(),
  slug: z.string(),
  type: z.enum(['mainstream', 'high-risk', 'mobile-first', 'enterprise']),
  acceptsHighRiskMccs: z.array(z.string()).default([]),
  signaturePrice: z.string().optional(),
  contractTerms: z.string().optional(),
  pros: z.array(z.string()).default([]),
  cons: z.array(z.string()).default([]),
  rating: z.number().min(0).max(5).optional(),
  affiliate: z.object({
    url: z.string().url().optional(),
    network: z.string().optional(),
    cpl: cplBand.optional(),
  }).optional(),
  faqs: z.array(faq).default([]),
});

export const highRiskVerticalSchema = z.object({
  vertical: z.string(),
  slug: z.string(),
  mccCodes: z.array(z.string()).default([]),
  whyHighRisk: z.string(),
  ukAcquirers: z.array(z.string()).default([]),
  typicalReservePercent: z.number().nullable().optional(),
  searchVolume: z.number().nullable().optional(),
  cpl: cplBand.optional(),
  faqs: z.array(faq).default([]),
});

export const tradeSchema = z.object({
  trade: z.string(),
  slug: z.string(),
  ticketSizeBand: z.string().optional(),
  volumeBand: z.string().optional(),
  recommendedTerminal: z.string().optional(), // terminal slug
  alternativeTerminals: z.array(z.string()).default([]),
  faqs: z.array(faq).default([]),
});

export const switchingGuideSchema = z.object({
  acquirer: z.string(),
  slug: z.string(),
  contractTypicalLengthMonths: z.number().nullable(),
  earlyTerminationFeeBand: z.string().optional(),
  noticePeriodDays: z.number().nullable(),
  pciFeeMonthlyGBP: z.number().nullable(),
  alternativeAcquirers: z.array(z.string()).default([]),
  faqs: z.array(faq).default([]),
});

// ---------- BBL (lenders + reviews) ----------

export const lenderSchema = z.object({
  name: z.string(),
  slug: z.string(),
  type: z.enum(['bank', 'alt-lender', 'broker', 'specialist', 'mca', 'rbf', 'invoice', 'asset']),
  loanAmount: moneyBand.optional(),
  termMonths: z.object({ min: z.number(), max: z.number() }).optional(),
  indicativeApr: z.string().optional(),
  timeToFundingDays: z.string().optional(),
  bestFor: z.array(z.string()).default([]),
  pros: z.array(z.string()).default([]),
  cons: z.array(z.string()).default([]),
  verdict: z.string().optional(),
  rating: z.number().min(0).max(5).optional(),
  reviewedBy: z.string().optional(),
  reviewedDate: z.coerce.date().optional(),
  affiliate: z.object({
    url: z.string().url().optional(),
    network: z.string().optional(),
    cpl: cplBand.optional(),
  }).optional(),
  faqs: z.array(faq).default([]),
});

// ---------- FundBiz (sectors + decline reasons) ----------

export const sectorSchema = z.object({
  sector: z.string(),
  slug: z.string(),
  silo: z.enum(['hospitality', 'retail', 'trade', 'professional', 'healthcare', 'transport', 'manufacturing', 'agriculture', 'other']),
  pageType: z.enum(['lander', 'sub-vertical']),
  topLenders: z.array(z.string()).default([]),
  cpl: cplBand.optional(),
  searchVolume: z.number().nullable().optional(),
  faqs: z.array(faq).default([]),
});

export const declineReasonSchema = z.object({
  reason: z.string(),
  slug: z.string(),
  category: z.enum(['credit', 'trading-history', 'collateral', 'payment-history', 'bank-specific', 'other']),
  severity: z.enum(['common', 'specific', 'edge-case']).default('common'),
  alternativeProducts: z.array(z.string()).default([]),
  recommendedLenders: z.array(z.string()).default([]),
  faqs: z.array(faq).default([]),
});

export const productSchema = z.object({
  product: z.string(),
  slug: z.string(),
  productType: z.enum(['business-loan', 'mca', 'rbf', 'asset-finance', 'invoice-finance', 'vat-loan', 'r-and-d', 'commercial-mortgage', 'overdraft', 'card', 'bank-account']),
  isAdjacentFlex: z.boolean().default(false),
  faqs: z.array(faq).default([]),
});
