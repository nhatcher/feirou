import { useTranslation } from "react-i18next";

export default function Notifications() {
  const [t] = useTranslation();
  return (
    <>
      <div>{t("common.not-implemented")}</div>
    </>
  );
}