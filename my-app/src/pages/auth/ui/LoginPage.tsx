import { LoginForm } from "../../../features/auth/ui/LoginForm";
import styles from "./AuthPage.module.scss";

export const LoginPage = () => {
  return (
    <div className={styles.authPage}>
      <LoginForm />
    </div>
  );
};
