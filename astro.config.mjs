import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';

/** GitHub Pages project sites live under /<repo>/; user/org pages use /. */
const owner = process.env.GITHUB_REPOSITORY_OWNER ?? '';
const repo = process.env.GITHUB_REPOSITORY?.split('/')[1] ?? '';
const isUserOrOrgRootSite =
  !repo || repo.toLowerCase() === `${owner.toLowerCase()}.github.io`;
const base = isUserOrOrgRootSite ? '/' : `/${repo}/`;
const site = owner ? `https://${owner}.github.io` : undefined;

export default defineConfig({
  site,
  base,
  server: {
    host: true,
    port: 4321,
    strictPort: true,
  },
  vite: {
    plugins: [tailwindcss()],
    server: {
      // Windows: JSON/i18n updates are sometimes not reflected until restart; polling helps file watching
      watch: {
        usePolling: process.platform === 'win32',
      },
      proxy: {
        '/api/contact': {
          target: 'http://localhost:5000',
          changeOrigin: true,
        },
      },
    },
    preview: {
      host: true,
    },
  },
  output: 'static',
});
