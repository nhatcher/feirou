import { Navigate, useLocation } from "react-router-dom";
import { ContextProps } from "../context/AuthContext";

export default function PrivateRoutes({ children, user }: { children: JSX.Element, user: ContextProps }) {
  let location = useLocation();

  if (user.isAuthenticated) {
    return children;
  }
  return <Navigate to="/login" state={{ from: location }} replace />;
}
