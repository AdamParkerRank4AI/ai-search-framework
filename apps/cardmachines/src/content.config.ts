import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import {
  terminalSchema,
  acquirerSchema,
  highRiskVerticalSchema,
  tradeSchema,
  switchingGuideSchema,
  author,
} from '@aisf/content-types';

export const collections = {
  terminals: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/terminals' }),
    schema: terminalSchema,
  }),
  acquirers: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/acquirers' }),
    schema: acquirerSchema,
  }),
  highRisk: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/high-risk' }),
    schema: highRiskVerticalSchema,
  }),
  trades: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/trades' }),
    schema: tradeSchema,
  }),
  switching: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/switching' }),
    schema: switchingGuideSchema,
  }),
  authors: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/authors' }),
    schema: author,
  }),
};
