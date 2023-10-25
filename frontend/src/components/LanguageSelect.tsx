import {
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  SelectChangeEvent,
  styled,
  Container,
} from "@mui/material";
// import { useState} from "react";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";

function LanguageSelect() {
  const [t, i18n] = useTranslation();

  const [cookies, setCookie] = useCookies(["locale"]);

  console.log("cookies", cookies["locale"]);

  const handleLocaleChange = (event: SelectChangeEvent<any>) => {
    event.preventDefault();
    const value = event.target.value;
    // set the cookie for later page refreshes
    setCookie("locale", value, { path: '/' });
    // change the i18n language to update the system
    i18n.changeLanguage(value);
  };

  return (
    <Wrapper>
      <FormControl fullWidth>
        <InputLabel id="language-select-label">
          {t("login.language")}
        </InputLabel>
        <Select
          labelId="language-select-label"
          value={i18n.language}
          label={t("login.language")}
          onChange={handleLocaleChange}
        >
          <MenuItem value="en-US">{t("common.english")}</MenuItem>
          <MenuItem value="pt-BR">{t("common.portuguese")}</MenuItem>
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
