import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import PrivateRoutes from "./util/PrivateRoutes";
import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import CreateAccount from "./pages/CreateAccount/CreateAccount";
import ForgotPassword from "./pages/ForgotPassword/ForgotPassword";
import UpdatePassword from "./pages/UpdatePassword/UpdatePassword";
import NotFound from "./pages/NotFound/NotFound";
import UpdateAccount from "./pages/UpdateAccount/UpdateAccount";
import Notifications from "./pages/Notifications/Notifications";

function App() {
  const user = useAuth();
  return (
    <BrowserRouter>
      <Routes>
        {/* public routes */}
        <Route path="/create-account" element={<CreateAccount />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/update-password/:token" element={<UpdatePassword />} />
        {/* private routes */}
        <Route element={<PrivateRoutes user={user} />} >
          <Route path="/" element={<Home />} />
          <Route path="/update-account" element={<UpdateAccount />} />
          <Route path="/notifications" element={<Notifications />} />
        </Route>
        <Route path="/login" element={<Login />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
