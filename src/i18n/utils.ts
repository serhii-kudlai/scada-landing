import type { Locale } from './types';

/** Base path: `` for Russian (default), `/en`, `/de`, `/uk` for localized routes. */
export function pathPrefix(lang: Locale): string {
  return lang === 'ru' ? '' : `/${lang}`;
}

/** In-page anchor targets for the current language route. */
export function anchorHref(lang: Locale, href: string): string {
  if (!href || href === '#') return '#';
  const id = href.startsWith('#') ? href.slice(1) : href;
  if (lang === 'ru') return `/#${id}`;
  return `/${lang}/#${id}`;
}

export function homeHref(lang: Locale): string {
  return lang === 'ru' ? '/' : `/${lang}/`;
}
