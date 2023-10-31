import { Container, Grid, Paper, styled } from "@mui/material";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";
import { Bell, User, LogOut } from "lucide-react";
import { useEffect, useState } from "react";

function Home() {
  const navigate = useNavigate();
  const [cookies] = useCookies(["csrftoken"]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const init = async () => {
      const response = await fetch("/api/get-user-groups");
      const data = await response.json();
      const consumerGroups = data.consumer_groups;
      const producer_groups = data.producer_groups;
      console.log(data);
    }
    init();
  }, [isLoading])
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
        <Bell onClick={() => navigate("/notifications")} />
        <User onClick={() => navigate("/update-account")} />
        <LogOut onClick={handleLogout} />
      </Grid>
      {isLoading && <Loading/>}
      {!isLoading && (<div>Hola!</div>)}
    </Paper>
  );
}

const Loading = styled(Container)(() => ({
}));

export default Home;
