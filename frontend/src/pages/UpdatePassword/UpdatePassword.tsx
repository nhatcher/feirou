import { Paper, Grid, TextField, Button } from "@mui/material";
import { useState, BaseSyntheticEvent } from "react";
import { useParams } from "react-router-dom";

function UpdatePassword() {
  const [password, setPassword] = useState("");
  const { token } = useParams();
  const handleUpdatePassword = async (event: BaseSyntheticEvent) => {
    event.preventDefault();
    // const emailToken = window.location.href.split("=")[1];
    const response = await fetch("/api/update-password/", {
      method: "POST",
      body: JSON.stringify({
        password,
        "email-token": token,
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
  };
  return (
    <Paper>
      <Grid container spacing={3} direction={"column"} alignItems={"center"}>
        <Grid item xs={12}>
          <TextField
            label="New Password"
            onChange={(event) => setPassword(event.target.value)}
          ></TextField>
        </Grid>
        <Grid item xs={12}>
          <Button fullWidth onClick={handleUpdatePassword}>
            Set Password
          </Button>
        </Grid>
      </Grid>
    </Paper>
  );
}

export default UpdatePassword;
