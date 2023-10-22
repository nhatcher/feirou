import { Paper, Grid, TextField, Button } from "@mui/material";
import { useState, BaseSyntheticEvent } from "react";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const handleRecoverPassword = async (event: BaseSyntheticEvent) => {
    event.preventDefault();
    const response = await fetch("/api/recover-password/", {
      method: "POST",
      body: JSON.stringify({
        email,
      }),
      headers: {
        "Content-Type": "application/json",
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
    <Paper>
      <Grid container spacing={3} direction={"column"} alignItems={"center"}>
        <Grid item xs={12}>
          <TextField
            label="Email"
            onChange={(event) => setEmail(event.target.value)}
          ></TextField>
        </Grid>
        <Grid item xs={12}>
          <Button fullWidth onClick={handleRecoverPassword}>
            Recover Password
          </Button>
        </Grid>
      </Grid>
    </Paper>
  );
}

export default ForgotPassword;
