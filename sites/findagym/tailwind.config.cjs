/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#fdf4f3',
          100: '#fbe8e6',
          200: '#f7d3d0',
          300: '#f0adaa',
          400: '#e57e7a',
          500: '#d65450',
          600: '#c33936',
          700: '#a32d2c',
          800: '#82282a',
          900: '#6c2627',
        },
        ink: {
          900: '#0c1014',
          800: '#1a2028',
          700: '#2a3038',
          600: '#454d57',
          500: '#6b7280',
          400: '#9ca3af',
        },
        accent: {
          500: '#16a34a',
          700: '#15803d',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'],
        display: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
