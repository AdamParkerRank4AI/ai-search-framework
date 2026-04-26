import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { lenderSchema, sectorSchema, author } from '@aisf/content-types';

export const collections = {
  lenders: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/lenders' }),
    schema: lenderSchema,
  }),
  sectors: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/sectors' }),
    schema: sectorSchema,
  }),
  authors: defineCollection({
    loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/authors' }),
    schema: author,
  }),
};
