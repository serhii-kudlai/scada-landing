import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';

/** Custom domain — assets always served from root. */
const base = '/';
const site = 'https://objectscada.site';

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
