import { Paper, Grid, TextField, Button } from "@mui/material";
import { useState, BaseSyntheticEvent } from "react";
import { useCookies } from "react-cookie";

function CreateAccount() {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [cookies] = useCookies(["csrftoken"]);
  
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
          nickname: username,
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
                label="First Name"
                onChange={(event) => setFirstName(event.target.value)}
              ></TextField>
            </Grid>
            <Grid item xs={12}>
              <TextField
                label="Last Name"
                onChange={(event) => setLastName(event.target.value)}
              ></TextField>
            </Grid>
            <Grid item xs={12}>
              <TextField
                label="Email"
                onChange={(event) => setEmail(event.target.value)}
              ></TextField>
            </Grid>
            <Grid item xs={12}>
              <TextField
                label="Username"
                onChange={(event) => setUsername(event.target.value)}
              ></TextField>
            </Grid>
            <Grid item xs={12}>
              <TextField
                label="Password"
                type={"password"}
                onChange={(event) => setPassword(event.target.value)}
              ></TextField>
            </Grid>
            <Grid item xs={12}>
              <Button fullWidth onClick={handleCreateAccount}>
                Create Account
              </Button>
            </Grid>
          </Grid>
        </Paper>
      </div>
    );
  }

  export default CreateAccount;