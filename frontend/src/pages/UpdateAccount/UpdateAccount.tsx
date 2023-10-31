import {
  Paper,
  Grid,
  TextField,
  Button,
  Container,
  styled,
  Checkbox,
  FormControlLabel,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
} from "@mui/material";
import { useState, BaseSyntheticEvent, useEffect } from "react";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";

function UpdateAccount() {
  const { t, i18n } = useTranslation();
  const [cookies] = useCookies(["locale", "csrftoken"]);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [locale, setLocale] = useState(i18n.language);
  const [changePassword, setChangePassword] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const getUserDetails = async () => {
      try {
        const response = await fetch("/api/get-user-details", {
          credentials: "same-origin",
        });
        const user = await response.json();
        console.log("User details:", user);
        setEmail(user.email);
        setUsername(user.username);
        setFirstName(user.first_name);
        setLastName(user.last_name);
        setLocale(user.locale);

        setIsLoading(false);
      } catch (err) {
        console.log("Got an error:", err);
      }
    };
    getUserDetails();
  }, [isLoading]);
  // TODO: MouseEventHandler<HTMLButtonElement> (?)
  const handleUpdateAccount = async (event: BaseSyntheticEvent) => {
    event.preventDefault();
    const response = await fetch("/api/update-user-settings", {
      method: "POST",
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        locale,
        change_password: changePassword,
        password,
        new_password: newPassword,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies["csrftoken"],
        "Accept-Language": locale,
      },
    });
    let status_code = response.status;
    let message = "";
    try {
      const data = await response.json();
      message = data.message;
    } catch (e) {
      status_code = status_code === 200 ? 500 : status_code;
      message = t("error.internal_server_error");
    }
    if (status_code === 200) {
      setSuccessMessage(t("account.updated-successfully"));
      setErrorMessage("");
    } else {
      setSuccessMessage("");
      setErrorMessage(message);
    }
  };

  if (isLoading) {
    return <div>Loading</div>;
  }

  return (
    <div>
      <Paper>
        <Grid container spacing={3} direction={"column"} alignItems={"center"}>
          <Grid item xs={12}>
            <TextField
              label={t("account.first_name")}
              onChange={(event) => setFirstName(event.target.value)}
              defaultValue={firstName}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <TextField
              label={t("account.last_name")}
              onChange={(event) => setLastName(event.target.value)}
              defaultValue={lastName}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <TextField
              label={t("account.email")}
              defaultValue={email}
              InputProps={{
                readOnly: true,
              }}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <TextField
              label={t("login.username")}
              value={username}
              InputProps={{
                readOnly: true,
              }}
            ></TextField>
          </Grid>
          <Grid item xs={12}>
            <FormControl fullWidth>
              <InputLabel id="language-select-label">
                {t("login.language")}
              </InputLabel>
              <Select
                labelId="language-select-label"
                value={locale}
                label={t("login.language")}
                onChange={(event) => setLocale(event.target.value)}
              >
                <MenuItem value="en-US">{t("common.english")}</MenuItem>
                <MenuItem value="pt-BR">{t("common.portuguese")}</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={12}>
            <FormControlLabel
              control={
                <Checkbox
                  checked={changePassword}
                  onChange={() => {
                    setChangePassword(!changePassword);
                  }}
                />
              }
              label={t("account.change_password")}
            />
            {changePassword && (
              <Grid
                container
                spacing={3}
                direction={"column"}
                alignItems={"center"}
              >
                <Grid item xs={12}>
                  <TextField
                    label={t("login.password")}
                    type={"password"}
                    onChange={(event) => setPassword(event.target.value)}
                  ></TextField>
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    label={t("account.new_password")}
                    type={"password"}
                    onChange={(event) => setNewPassword(event.target.value)}
                  ></TextField>
                </Grid>
              </Grid>
            )}
          </Grid>
          <Grid item xs={12}>
            <Button fullWidth onClick={handleUpdateAccount}>
              {t("account.update")}
            </Button>
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

export default UpdateAccount;
