import { Button, Divider, FormControl, Grid, InputLabel, Link, MenuItem, Paper, Select, SelectChangeEvent, TextField } from "@mui/material";
import { BaseSyntheticEvent, useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { useCookies } from "react-cookie";
import { useTranslation } from 'react-i18next';

function Login() {
    const { t, i18n } = useTranslation();
    const { login } = useAuth();
    const [cookies, setCookie] = useCookies(["locale"]);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const location = useLocation();
    const [language, setLanguage] = useState(cookies["locale"] || "en");
    const from = location.state?.from?.pathname || "/";
    console.log('render');

    if (!cookies["locale"]) {
      setCookie("locale", "en");
    }

    useEffect(() => {
      i18n.changeLanguage(language);
    }, [language]);

    const handleLocaleChange = (event: SelectChangeEvent<any>) => {
      event.preventDefault();
      //i18n.changeLanguage(event.target.value);
      setCookie("locale", event.target.value);
      setLanguage(event.target.value);
    }
  
    const handleLogin = async (event: BaseSyntheticEvent) => {
      event.preventDefault();
      try {
        await login(username, password);
        // if OK, navigate to home
        navigate(from, { replace: true });
      } catch (error) {
        // TODO: improve error management according to server response codes & messages
        /*if (username === '') {
                  setEmailError(true);
              }
              if (password === '') {
                  setPassError(true);
              }*/
      }
    };
    return (
      <div style={{ padding: 30 }}>
        <Paper>
          <Grid container spacing={3} direction={"column"} alignItems={"center"}>
            <Grid item xs={12}>
              <TextField
                label={t("login.username")}
                onChange={(event) => setUsername(event.target.value)}
              ></TextField>
            </Grid>
            <Grid item xs={12}>
              <TextField
                label={t("login.password")}
                type={"password"}
                onChange={(event) => setPassword(event.target.value)}
              ></TextField>
            </Grid>
            <Grid item xs={12}>
            <FormControl fullWidth>
              <InputLabel id="language-select-label">{t("login.language")}</InputLabel>
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
          </Grid>
            <Grid item xs={12}>
              <Link href="/forgot-password/">{t('login.forgot_password')}</Link>
            </Grid>
            <Grid item xs={12}>
              <Button fullWidth onClick={handleLogin}>
                {t('login.sign_in')}
              </Button>
              <Divider>{t('login.or')}</Divider>
              <Button fullWidth onClick={() => navigate("/create-account/")}>
                {t('login.create_account')}
              </Button>
            </Grid>
          </Grid>
        </Paper>
      </div>
    );
  }
  
  export default Login;