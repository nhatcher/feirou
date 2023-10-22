import { Button, Grid, Paper } from "@mui/material";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";

function Home() {
    const navigate = useNavigate();
    const [cookies] = useCookies(["csrftoken"]);
    console.log(cookies);
    const handleLogout = async () => {
      const response = await fetch("/api/logout/", {
        credentials: "same-origin",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": cookies["csrftoken"],
        },
      });
      const data = await response.json();
      if (response.status === 200) {
        console.log("Logged out!");
        navigate("/login");
      } else {
        throw new Error(data.detail);
      }
    };
    return (
      <Paper>
        <Grid item xs={12}>
          <div>Welcome home!</div>
        </Grid>
        <Grid item xs={12}>
          <Button fullWidth onClick={handleLogout}>
            Logout
          </Button>
        </Grid>
      </Paper>
    );
  }

  export default Home;