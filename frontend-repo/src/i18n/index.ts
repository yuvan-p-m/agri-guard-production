import i18n from 'i18next';
import { initReactI18next, useTranslation as useBaseTranslation } from 'react-i18next';

import en from './locales/en.json';
import ta from './locales/ta.json';
import te from './locales/te.json';
import ml from './locales/ml.json';
import kn from './locales/kn.json';
import hi from './locales/hi.json';
import bn from './locales/bn.json';
import mr from './locales/mr.json';
import gu from './locales/gu.json';
import pa from './locales/pa.json';
import ur from './locales/ur.json';
import or from './locales/or.json';
import as from './locales/as.json';
import ne from './locales/ne.json';
import si from './locales/si.json';
import ar from './locales/ar.json';
import fr from './locales/fr.json';
import es from './locales/es.json';
import pt from './locales/pt.json';
import de from './locales/de.json';
import it from './locales/it.json';
import ru from './locales/ru.json';
import ja from './locales/ja.json';
import ko from './locales/ko.json';
import zh from './locales/zh.json';

export interface LanguageOption {
  code: string;
  name: string;
  native: string;
  dir: 'ltr' | 'rtl';
}

export const SUPPORTED_LANGUAGES: LanguageOption[] = [
  { code: 'en', name: 'English', native: 'English', dir: 'ltr' },
  { code: 'ta', name: 'Tamil', native: 'தமிழ்', dir: 'ltr' },
  { code: 'te', name: 'Telugu', native: 'తెలుగు', dir: 'ltr' },
  { code: 'ml', name: 'Malayalam', native: 'മലയാളം', dir: 'ltr' },
  { code: 'kn', name: 'Kannada', native: 'ಕನ್ನಡ', dir: 'ltr' },
  { code: 'hi', name: 'Hindi', native: 'हिन्दी', dir: 'ltr' },
  { code: 'bn', name: 'Bengali', native: 'বাংলা', dir: 'ltr' },
  { code: 'mr', name: 'Marathi', native: 'मराठी', dir: 'ltr' },
  { code: 'gu', name: 'Gujarati', native: 'ગુજરાતી', dir: 'ltr' },
  { code: 'pa', name: 'Punjabi', native: 'ਪੰਜਾਬੀ', dir: 'ltr' },
  { code: 'ur', name: 'Urdu', native: 'اردو', dir: 'rtl' },
  { code: 'or', name: 'Odia', native: 'ଓଡ଼ିଆ', dir: 'ltr' },
  { code: 'as', name: 'Assamese', native: 'অসমীয়া', dir: 'ltr' },
  { code: 'ne', name: 'Nepali', native: 'नेपाली', dir: 'ltr' },
  { code: 'si', name: 'Sinhala', native: 'සිංහල', dir: 'ltr' },
  { code: 'ar', name: 'Arabic', native: 'العربية', dir: 'rtl' },
  { code: 'fr', name: 'French', native: 'Français', dir: 'ltr' },
  { code: 'es', name: 'Spanish', native: 'Español', dir: 'ltr' },
  { code: 'pt', name: 'Portuguese', native: 'Português', dir: 'ltr' },
  { code: 'de', name: 'German', native: 'Deutsch', dir: 'ltr' },
  { code: 'it', name: 'Italian', native: 'Italiano', dir: 'ltr' },
  { code: 'ru', name: 'Russian', native: 'Русский', dir: 'ltr' },
  { code: 'ja', name: 'Japanese', native: '日本語', dir: 'ltr' },
  { code: 'ko', name: 'Korean', native: '한국어', dir: 'ltr' },
  { code: 'zh', name: 'Chinese', native: '中文', dir: 'ltr' },
];

export const RTL_LANGUAGES = new Set(['ar', 'ur']);

export const resources = {
  en: { translation: en },
  ta: { translation: ta },
  te: { translation: te },
  ml: { translation: ml },
  kn: { translation: kn },
  hi: { translation: hi },
  bn: { translation: bn },
  mr: { translation: mr },
  gu: { translation: gu },
  pa: { translation: pa },
  ur: { translation: ur },
  or: { translation: or },
  as: { translation: as },
  ne: { translation: ne },
  si: { translation: si },
  ar: { translation: ar },
  fr: { translation: fr },
  es: { translation: es },
  pt: { translation: pt },
  de: { translation: de },
  it: { translation: it },
  ru: { translation: ru },
  ja: { translation: ja },
  ko: { translation: ko },
  zh: { translation: zh },
};

const savedLang = typeof window !== 'undefined' 
  ? (localStorage.getItem('agriguard_language') || localStorage.getItem('i18nextLng') || 'en')
  : 'en';

const initialLang = SUPPORTED_LANGUAGES.some((l) => l.code === savedLang) ? savedLang : 'en';

// Set HTML attributes on startup
if (typeof document !== 'undefined') {
  document.documentElement.lang = initialLang;
  document.documentElement.dir = RTL_LANGUAGES.has(initialLang) ? 'rtl' : 'ltr';
}

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: initialLang,
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false,
    },
    react: {
      useSuspense: false,
    },
  });

i18n.on('languageChanged', (lng: string) => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('agriguard_language', lng);
    localStorage.setItem('i18nextLng', lng);
    document.documentElement.lang = lng;
    document.documentElement.dir = RTL_LANGUAGES.has(lng) ? 'rtl' : 'ltr';
  }
});

export const changeAppLanguage = (lng: string) => {
  if (SUPPORTED_LANGUAGES.some((l) => l.code === lng)) {
    i18n.changeLanguage(lng);
  }
};

export const getCurrentLanguage = (): string => {
  return i18n.language || (typeof window !== 'undefined' ? localStorage.getItem('agriguard_language') : null) || 'en';
};

export const useAppTranslation = () => {
  const { t: baseT, i18n: i18nInst } = useBaseTranslation();

  const t = (key: string, fallbackOrOptions?: string | Record<string, any>, options?: Record<string, any>): string => {
    let fallback: string | undefined = undefined;
    let opts: Record<string, any> | undefined = undefined;

    if (typeof fallbackOrOptions === 'string') {
      fallback = fallbackOrOptions;
      opts = options;
    } else if (typeof fallbackOrOptions === 'object' && fallbackOrOptions !== null) {
      opts = fallbackOrOptions;
    }

    const val = baseT(key, opts as any);
    if (typeof val === 'string' && val && val !== key) {
      return val;
    }

    // 1. Resolve path on canonical en resource
    const parts = key.split('.');
    let cur: any = en;
    for (const p of parts) {
      if (cur && typeof cur === 'object' && p in cur) {
        cur = cur[p];
      } else {
        cur = undefined;
        break;
      }
    }
    let res = typeof cur === 'string' && cur.trim() ? cur : fallback;
    if (res && opts) {
      for (const [k, v] of Object.entries(opts)) {
        res = res.replace(new RegExp(`{{\\s*${k}\\s*}}`, 'g'), String(v));
      }
    }
    if (typeof res === 'string' && res.trim()) {
      return res;
    }

    // 2. Prevent raw dot-keys from displaying in UI
    const lastPart = parts[parts.length - 1];
    return lastPart ? lastPart.replace(/([A-Z])/g, ' $1').replace(/^./, (s) => s.toUpperCase()).trim() : key;
  };

  return { t, i18n: i18nInst, language: i18nInst.language || initialLang, changeLanguage: changeAppLanguage };
};

export default i18n;
