import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import LanguageDetector from 'i18next-browser-languagedetector';

import translationEN from './public/locale/en-us/translation.json';
import translationPT from './public/locale/pt-br/translation.json';

// the translations
// (tip move them in a JSON file and import them,
// or even better, manage them separated from your code: https://react.i18next.com/guides/multiple-translation-files)
const resources = {
  'en-US': {translation: translationEN},
  'pt-BR': {translation: translationPT}
};

console.log(resources);

i18n
  .use(initReactI18next)
  .use(LanguageDetector)
  .init({
    debug: true,
    resources,
    fallbackLng: 'en-US',
    detection: {
      order: ["cookie"],
      caches: ["cookie"],
      lookupCookie: 'locale',
    },
    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

  export default i18n;