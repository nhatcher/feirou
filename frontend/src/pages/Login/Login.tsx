import { Button, Divider, Grid, Link, Paper, TextField } from "@mui/material";
import { BaseSyntheticEvent, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

function Login() {
    const { login } = useAuth();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const location = useLocation();
    const from = location.state?.from?.pathname || "/";
  
    const handleLogin = async (event: BaseSyntheticEvent) => {
      event.preventDefault();
      try {
        await login(username, password);
        // if OK, navigate to home
        navigate(from, { replace: true });
        // navigate("/");
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
              <Link href="/forgot-password/">Forgot password?</Link>
            </Grid>
            <Grid item xs={12}>
              <Button fullWidth onClick={handleLogin}>
                Sign In
              </Button>
              <Divider>or</Divider>
              <Button fullWidth onClick={() => navigate("/create-account/")}>
                Create an account
              </Button>
            </Grid>
          </Grid>
        </Paper>
      </div>
    );
  }
  
  export default Login;