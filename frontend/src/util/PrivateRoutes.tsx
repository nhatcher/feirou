import { Navigate, Outlet, useLocation } from "react-router-dom";
import { ContextProps } from "../context/AuthContext";

export default function PrivateRoutes({ user }: { user: ContextProps }) {
  let location = useLocation();

  if (user.isAuthenticated) {
    return <Outlet />;
  }
  return <Navigate to="/login" state={{ from: location }} replace />;
}
