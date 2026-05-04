import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://dashboard.local',
  output: 'static',
  trailingSlash: 'always',
  build: { format: 'directory' },
});
