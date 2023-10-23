import { Paper, Grid, TextField, Button } from "@mui/material";
import { useState, BaseSyntheticEvent } from "react";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";
import LanguageSelect from "../../components/LanguageSelect";

function CreateAccount() {
  const { t } = useTranslation();
  const [cookies] = useCookies(["locale", "csrftoken"]);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

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
        language: cookies["locale"],
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
          </Grid>
        </Grid>
      </Paper>
    </div>
  );
}

export default CreateAccount;
