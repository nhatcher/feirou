import {
  Paper,
  Grid,
  TextField,
  Button,
  Select,
  InputLabel,
  MenuItem,
  FormControl,
} from "@mui/material";
import { useState, BaseSyntheticEvent, useEffect } from "react";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";

function CreateAccount() {
  const { t, i18n } = useTranslation();
  const [cookies, setCookie] = useCookies(["locale", "csrftoken"]);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [language, setLanguage] = useState("en");

  if (!cookies["locale"]) {
    setCookie("locale", "en");
  }

  useEffect(() => {
    i18n.changeLanguage(language);
  }, [language]);

  // TODO: MouseEventHandler<HTMLButtonElement> (?)
  const handleCreateAccount = async (event: BaseSyntheticEvent) => {
    event.preventDefault();
    const response = await fetch("/api/create-account/", {
      method: "POST",
      body: JSON.stringify({
        username,
        "first-name": firstName,
        "last-name": lastName,
        email,
        language,
        password,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies["csrftoken"],
      },
    });
    let status_code = response.status;
    let message = "";
    try {
      const data = await response.json();
      message = `Account created, please check your email. ${data.details}`;
    } catch (e) {
      status_code = status_code === 200 ? 500 : status_code;
      message = `Internal server error`;
    }
    console.log(message);
  };

  return (
    <div style={{ padding: 30 }}>
      <Paper>
        <Grid container spacing={3} direction={"column"} alignItems={"center"}>
          <Grid item xs={12}>
            <TextField
              label={t("account.first_name")}
              onChange={(event) => setFirstName(event.target.value)}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <TextField
              label={t("account.last_name")}
              onChange={(event) => setLastName(event.target.value)}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <TextField
              label={t("account.email")}
              onChange={(event) => setEmail(event.target.value)}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <TextField
              label={t("login.username")}
              onChange={(event) => setUsername(event.target.value)}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <FormControl fullWidth>
              <InputLabel id="language-select-label">Language</InputLabel>
              <Select
                labelId="language-select-label"
                value={language}
                label={t("login.language")}
                onChange={(event) => setLanguage(event.target.value)}
              >
                <MenuItem value={"en"}>{t('common.english')}</MenuItem>
                <MenuItem value={"pt"}>{t('common.portuguese')}</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <TextField
              label={t("login.password")}
              type={"password"}
              onChange={(event) => setPassword(event.target.value)}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <Button fullWidth onClick={handleCreateAccount}>
              {t('login.create_account')}
            </Button>
          </Grid>
        </Grid>
      </Paper>
    </div>
  );
}

export default CreateAccount;
