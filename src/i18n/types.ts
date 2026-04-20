import type ru from './ru.json';

export type Locale = 'ru' | 'en' | 'de' | 'uk' | 'es' | 'fr';

export type Messages = typeof ru;

export const locales: Exclude<Locale, 'ru'>[] = ['en', 'de', 'uk', 'es', 'fr'];

export const localeHtmlLang: Record<Locale, string> = {
  ru: 'ru-RU',
  en: 'en',
  de: 'de',
  uk: 'uk',
  es: 'es',
  fr: 'fr',
};
