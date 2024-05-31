import "./App.css";
import {
  BrowserRouter,
  Route,
  Routes,
} from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import PrivateRoutes from "./util/PrivateRoutes";
import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import CreateAccount from "./pages/CreateAccount/CreateAccount";
import ForgotPassword from "./pages/ForgotPassword/ForgotPassword";
import UpdatePassword from "./pages/UpdatePassword/UpdatePassword";
import NotFound from "./pages/NotFound/NotFound";
import Presentation from "./pages/Presentation/Presentation";


function App() {
  const user = useAuth();
  return (
    <BrowserRouter>
      <Routes>
        {/* public routes */}
        <Route path="/create-account" element={<CreateAccount />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/update-password/:token" element={<UpdatePassword />} />
        <Route path="/" element={<Presentation />} />
        {/* private routes */}
        <Route
          path="/home"
          element={
            <PrivateRoutes user={user}>
              <Home />
            </PrivateRoutes>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
