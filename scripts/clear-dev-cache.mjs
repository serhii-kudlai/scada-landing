/**
 * Removes Astro/Vite dev caches so locale and other JSON changes apply on next `npm run dev`.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

for (const rel of ['.astro', path.join('node_modules', '.vite')]) {
  const p = path.join(root, rel);
  try {
    fs.rmSync(p, { recursive: true, force: true });
    console.log('[clear-dev-cache] removed', rel);
  } catch (e) {
    console.warn('[clear-dev-cache]', e?.message ?? e);
  }
}
