import { Container, Divider, Grid, Link, styled } from "@mui/material";
import { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { useTranslation } from "react-i18next";
import LanguageSelect from "../../components/LanguageSelect";
import Button from "../../components/Button";
import TextField from "../../components/TextField";

function Login() {
  const { t } = useTranslation();
  const { login } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const location = useLocation();
  const [errorMessage, setErrorMessage] = useState("");
  const from = location.state?.from?.pathname || "/";

  const handleLogin = async (event: React.MouseEvent<HTMLElement>) => {
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
    <Wrapper>
      <LanguageSelect />
      <Title>FEIROU</Title>
      <Grid container spacing={3} direction={"column"} alignItems={"center"}>
        <Grid item xs={12}>
          <LoginTitle>Login</LoginTitle>
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
    </Wrapper>
  );
}

const Wrapper = styled("div")`
  width: 100%;
  height: 100%;
  padding: 30px;
  background-color: #f1b707;
  text-align: center;
  position: relative;
  box-sizing: border-box;
`;

const ErrorMessage = styled(Container)(() => ({
  color: "red",
}));

const Title = styled("div")`
  margin: 60px 0px;
  color: #013a40;
  font-size: 30px;
`;

const LoginTitle = styled("div")`
  margin: 10px 0px;
`;

export default Login;
