import { Navigate, Outlet } from "react-router-dom";
import { routes } from "./routes";
import { authStorage } from "../../features/auth/model/authStorage";

export const ProtectedRoute = () => {
  const token = authStorage.getToken();
  return token ? <Outlet /> : <Navigate to={routes.login} replace />;
};
