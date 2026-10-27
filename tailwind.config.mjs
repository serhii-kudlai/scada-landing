/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      /**
       * Tokens mirror the OBJECTSCADA app (login screen + gray theme).
       * Values live in CSS variables (src/styles/global.css) so light/dark swap in one place.
       */
      colors: {
        bg: 'var(--c-bg)',
        paper: 'var(--c-paper)',
        sunken: 'var(--c-sunken)',
        ink: 'var(--c-ink)',
        muted: 'var(--c-muted)',
        line: 'var(--c-line)',
        'line-strong': 'var(--c-line-strong)',
        accent: 'var(--c-accent)',
        'accent-ink': 'var(--c-accent-ink)',
        ok: 'var(--c-ok)',
        warn: 'var(--c-warn)',
        alarm: 'var(--c-alarm)',
      },
      fontFamily: {
        sans: ['Manrope', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'SFMono-Regular', 'monospace'],
      },
      borderRadius: {
        DEFAULT: '4px',
      },
    },
  },
  plugins: [],
};
