import type en from './en.json';

export type Locale = 'ru' | 'en' | 'de' | 'uk' | 'es' | 'fr' | 'ar' | 'zh';

export type Messages = typeof en;

export const locales: Exclude<Locale, 'en'>[] = ['ru', 'de', 'uk', 'es', 'fr', 'ar', 'zh'];

export const localeHtmlLang: Record<Locale, string> = {
  ru: 'ru-RU',
  en: 'en',
  de: 'de',
  uk: 'uk',
  es: 'es',
  fr: 'fr',
  ar: 'ar',
  zh: 'zh-Hans',
};
