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

/** Base path: `` for English (default), `/ru`, `/de`, `/uk`, etc. for localized routes. */
export function pathPrefix(lang: Locale): string {
  return lang === 'en' ? '' : `/${lang}`;
}

/** In-page anchor targets for the current language route. */
export function anchorHref(lang: Locale, href: string): string {
  if (!href || href === '#') return '#';
  const id = href.startsWith('#') ? href.slice(1) : href;
  const path = lang === 'en' ? `/#${id}` : `/${lang}/#${id}`;
  return withBase(path);
}

export function homeHref(lang: Locale): string {
  const path = lang === 'en' ? '/' : `/${lang}/`;
  return withBase(path);
}

/** Language code used in `public/screens/{id}_{code}_{theme}.png` file names. */
export function screenLang(lang: Locale): string {
  return lang === 'uk' ? 'ua' : lang;
}

/** Light/dark screenshot URLs for one screen of the app in the page language. */
export function screenSrc(id: string, lang: Locale): { light: string; dark: string } {
  const base = `${import.meta.env.BASE_URL}screens/${id}_${screenLang(lang)}`;
  return { light: `${base}_light.png`, dark: `${base}_dark.png` };
}
