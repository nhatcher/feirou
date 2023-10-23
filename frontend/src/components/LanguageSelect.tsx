import {
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  SelectChangeEvent,
  styled,
  Container,
} from "@mui/material";
import { useState, useEffect } from "react";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";

function LanguageSelect() {
  const [t, i18n] = useTranslation();

  const [cookies, setCookie] = useCookies(["locale"]);
  const [language, setLanguage] = useState(cookies["locale"] || "en");

  if (!cookies["locale"]) {
    setCookie("locale", "en");
  }

  useEffect(() => {
    i18n.changeLanguage(language);
  }, [language]);

  const handleLocaleChange = (event: SelectChangeEvent<any>) => {
    event.preventDefault();
    setCookie("locale", event.target.value);
    setLanguage(event.target.value);
  };

  return (
    <Wrapper>
      <FormControl fullWidth>
        <InputLabel id="language-select-label">
          {t("login.language")}
        </InputLabel>
        <Select
          labelId="language-select-label"
          value={language}
          label={t("login.language")}
          onChange={handleLocaleChange}
        >
          <MenuItem value="en">{t("common.english")}</MenuItem>
          <MenuItem value="pt">{t("common.portuguese")}</MenuItem>
        </Select>
      </FormControl>
    </Wrapper>
  );
}

const Wrapper = styled(Container)(() => ({
  position: "absolute",
  right: "0px",
  top: "10px;",
  width: "160px",
}));

export default LanguageSelect;
