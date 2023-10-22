import React from "react";
import ReactDOM from "react-dom/client";
import { ThemeProvider } from "@mui/material";
import { theme } from "./Theme";
import App from "./App.tsx";
import "./index.css";
import { CookiesProvider } from "react-cookie";
import { AuthProvider } from "./context/AuthContext.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <AuthProvider>
        <CookiesProvider>
          <App />
        </CookiesProvider>
      </AuthProvider>
    </ThemeProvider>
  </React.StrictMode>
);
