import type { Locale } from './types';

/**
 * Prefix BASE_URL so links work both on dev (base = '/')
 * and on GitHub Pages project sites (base = '/repo-name/').
 * import.meta.env.BASE_URL always has a trailing slash.
 */
function withBase(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}${path}`;
}

/** Base path: `` for Russian (default), `/en`, `/de`, `/uk` for localized routes. */
export function pathPrefix(lang: Locale): string {
  return lang === 'ru' ? '' : `/${lang}`;
}

/** In-page anchor targets for the current language route. */
export function anchorHref(lang: Locale, href: string): string {
  if (!href || href === '#') return '#';
  const id = href.startsWith('#') ? href.slice(1) : href;
  const path = lang === 'ru' ? `/#${id}` : `/${lang}/#${id}`;
  return withBase(path);
}

export function homeHref(lang: Locale): string {
  const path = lang === 'ru' ? '/' : `/${lang}/`;
  return withBase(path);
}
