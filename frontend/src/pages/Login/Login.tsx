import {
  Button,
  Container,
  Divider,
  Grid,
  Link,
  Paper,
  TextField,
  styled,
} from "@mui/material";
import { BaseSyntheticEvent, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { useTranslation } from "react-i18next";
import LanguageSelect from "../../components/LanguageSelect";

function Login() {
  const { t } = useTranslation();
  const { login } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const location = useLocation();
  const [errorMessage, setErrorMessage] = useState("");
  const from = location.state?.from?.pathname || "/";
  console.log("render");

  const handleLogin = async (event: BaseSyntheticEvent) => {
    event.preventDefault();
    const response = await login(username, password);
    let status_code = response.status;
    if (status_code === 200) {
      navigate(from, { replace: true });
    }
    let message = "";
    try {
      let data = await response.json();
      message = data.message;
    } catch (error) {
      message = t("internal-server-error");
    }
    setErrorMessage(message);
  };
  return (
    <div style={{ padding: 30 }}>
      <LanguageSelect />
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
            <Link href="/forgot-password/">{t("login.forgot_password")}</Link>
          </Grid>
          <Grid item xs={12}>
            <Button fullWidth onClick={handleLogin}>
              {t("login.sign_in")}
            </Button>
            <Divider>{t("login.or")}</Divider>
            <Link href="/create-account/">{t("login.create_account")}</Link>
          </Grid>
          <Grid item xs={12}>
            <ErrorMessage>{errorMessage}</ErrorMessage>
          </Grid>
        </Grid>
      </Paper>
    </div>
  );
}

const ErrorMessage = styled(Container)(() => ({
  color: "red",
}));

export default Login;
