import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { sectorSchema, declineReasonSchema, productSchema, author } from '@aisf/content-types';

export const collections = {
  sectors: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/sectors' }),
    schema: sectorSchema,
  }),
  declineReasons: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/decline-reasons' }),
    schema: declineReasonSchema,
  }),
  products: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/products' }),
    schema: productSchema,
  }),
  authors: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/authors' }),
    schema: author,
  }),
};
