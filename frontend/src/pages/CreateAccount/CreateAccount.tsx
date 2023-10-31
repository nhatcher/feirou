import {
  Paper,
  Grid,
  TextField,
  Button,
  Container,
  styled,
  Divider,
  Link,
} from "@mui/material";
import { useState, BaseSyntheticEvent } from "react";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";
import LanguageSelect from "../../components/LanguageSelect";

function CreateAccount() {
  const { t, i18n } = useTranslation();
  const [cookies] = useCookies(["locale", "csrftoken"]);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  // TODO: MouseEventHandler<HTMLButtonElement> (?)
  const handleCreateAccount = async (event: BaseSyntheticEvent) => {
    event.preventDefault();
    const locale = i18n.language;
    const response = await fetch("/api/create-account/", {
      method: "POST",
      body: JSON.stringify({
        username,
        "first_name": firstName,
        "last_name": lastName,
        email,
        locale,
        password,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies["csrftoken"],
        "Accept-Language": locale
      },
    });
    let status_code = response.status;
    let message = "";
    try {
      const data = await response.json();
      message = data.message;
    } catch (e) {
      status_code = status_code === 200 ? 500 : status_code;
      message = "Internal server error";
    }
    if (status_code === 200) {
      setSuccessMessage("Account created, please check your email.");
      setErrorMessage("");
    } else {
      setSuccessMessage("");
      setErrorMessage(message);
    }
  };

  return (
    <div>
      <LanguageSelect />
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
            <TextField
              label={t("login.password")}
              type={"password"}
              onChange={(event) => setPassword(event.target.value)}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <Button fullWidth onClick={handleCreateAccount}>
              {t("login.create_account")}
            </Button>
            <Divider>{t("login.or")}</Divider>
            <Link href="/">{t("login.sign_in")}</Link>
          </Grid>
          <Grid item xs={12}>
            <ErrorMessage>{errorMessage}</ErrorMessage>
            <SuccessMessage>{successMessage}</SuccessMessage>
          </Grid>
        </Grid>
      </Paper>
    </div>
  );
}

const ErrorMessage = styled(Container)(() => ({
  color: "red",
}));

const SuccessMessage = styled(Container)(() => ({
  color: "green",
}));

export default CreateAccount;
