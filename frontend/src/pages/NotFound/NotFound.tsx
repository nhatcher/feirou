import { useTranslation } from "react-i18next";
import LanguageSelect from "../../components/LanguageSelect";

export default function NotFound() {
  const [t] = useTranslation();
  return (
    <>
      <LanguageSelect />
      <div>{t("common.page_not_found")}</div>
    </>
  );
}
