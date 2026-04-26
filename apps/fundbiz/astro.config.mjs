import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://fundbiz.co.uk',
  output: 'static',
  trailingSlash: 'always',
  build: { format: 'directory' },
  prefetch: { prefetchAll: true, defaultStrategy: 'viewport' },
});
