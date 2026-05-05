/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f7ff',
          100: '#e0eefe',
          200: '#bbdcfd',
          300: '#7dc0fb',
          400: '#37a0f7',
          500: '#0d85e8',
          600: '#0067c7',
          700: '#0153a1',
          800: '#054785',
          900: '#0a3c6e',
        },
        ink: {
          900: '#0c1014',
          800: '#1a2028',
          700: '#2a3038',
          600: '#454d57',
          500: '#6b7280',
          400: '#9ca3af',
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
