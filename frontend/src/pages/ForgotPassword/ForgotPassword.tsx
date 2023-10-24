import { Paper, Grid, TextField, Button, Divider, Link } from "@mui/material";
import { useState, BaseSyntheticEvent } from "react";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";
import LanguageSelect from "../../components/LanguageSelect";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [cookies] = useCookies(["locale"]);
  const [t] = useTranslation();

  const handleRecoverPassword = async (event: BaseSyntheticEvent) => {
    event.preventDefault();
    const response = await fetch("/api/recover-password/", {
      method: "POST",
      body: JSON.stringify({
        email,
      }),
      headers: {
        "Content-Type": "application/json",
        "Accept-Language": cookies["locale"],
      },
    });
    let status_code = response.status;
    let message = "";
    try {
      const data = await response.json();
      message = `Email with instructions sent, please check your email. ${data.details}`;
    } catch (e) {
      status_code = status_code === 200 ? 500 : status_code;
      message = `Internal server error`;
    }
    console.log(message);
    // if (status_code === 200) {
    //     successMessage.style.display = 'block';
    //     errorMessage.style.display = 'none';
    //     successMessage.innerText = message;
    // } else {
    //     errorMessage.style.display = 'block';
    //     successMessage.style.display = 'none';
    //     errorMessage.innerText = message;
    // }
  };

  return (
    <div>
      <LanguageSelect />
      <Paper>
        <Grid container spacing={3} direction={"column"} alignItems={"center"}>
          <Grid item xs={12}>
            <TextField
              label={t("account.email")}
              onChange={(event) => setEmail(event.target.value)}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <Button fullWidth onClick={handleRecoverPassword}>
              {t("forgot_password.recover")}
            </Button>
            <Divider>{t("login.or")}</Divider>
            <Link href="/create-account/">{t("login.sign_in")}</Link>
          </Grid>
        </Grid>
      </Paper>
    </div>
  );
}

export default ForgotPassword;
