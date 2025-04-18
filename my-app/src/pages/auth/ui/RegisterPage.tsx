import { RegisterForm } from "../../../features/auth/ui/RegisterForm";
import styles from "./AuthPage.module.scss";

export const RegisterPage = () => {
  return (
    <div className={styles.authPage}>
      <RegisterForm />
    </div>
  );
};
