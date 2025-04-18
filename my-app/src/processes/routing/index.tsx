import { Routes, Route, Navigate } from "react-router-dom";
import { ProtectedRoute } from "./ProtectedRoute";
import { AuthLayout } from "./AuthLayout";
import { routes } from "./routes";
import { LoginPage } from "../../pages/auth/ui/LoginPage";
import { RegisterPage } from "../../pages/auth/ui/RegisterPage";
import { MainPage } from "../../pages/main";
import { ClassesPage } from "../../pages/classes";
import { SubscriptionsPage } from "../../pages/subscriptions";
import { AccountPage } from "../../pages/account/ui/AccountPage";

export const AppRouter = () => {
  return (
    <Routes>
      <Route element={<AuthLayout />}>
        <Route path={routes.login} element={<LoginPage />} />
        <Route path={routes.register} element={<RegisterPage />} />
      </Route>

      <Route element={<ProtectedRoute />}>
        <Route path={routes.main} element={<MainPage />} />
        <Route path={routes.classes} element={<ClassesPage />} />
        <Route path={routes.subscriptions} element={<SubscriptionsPage />} />
        <Route path={routes.account} element={<AccountPage />} />
      </Route>

      <Route path="*" element={<Navigate to={routes.login} replace />} />
    </Routes>
  );
};
