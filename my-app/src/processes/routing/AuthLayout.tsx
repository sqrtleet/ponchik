import styles from "./AuthLayout.module.scss";
import { Outlet } from "react-router-dom";

export const AuthLayout = () => {
  return (
    <div className={styles.authLayout}>
      <Outlet /> {/* Это заменит children */}
    </div>
  );
};
