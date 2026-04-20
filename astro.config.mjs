import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';

export default defineConfig({
  server: {
    host: true,
    port: 4321,
    strictPort: true,
  },
  vite: {
    plugins: [tailwindcss()],
    server: {
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
