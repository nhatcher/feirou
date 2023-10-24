import { Button, Grid, Paper } from "@mui/material";
import { useCookies } from "react-cookie";
import { useTranslation } from "react-i18next";
import { useNavigate } from "react-router-dom";

function Home() {
    const navigate = useNavigate();
    const [cookies] = useCookies(["csrftoken"]);
    const { t } = useTranslation();
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
          <div>{t('home.welcome')}</div>
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