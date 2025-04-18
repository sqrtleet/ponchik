import { Button, Layout, message } from "antd";
import { NavMenu } from "./NavMenu";
import styles from "./Header.module.scss";
import { useAuth } from "../../../features/auth/model/useAuth";
import { useNavigate } from "react-router-dom";
import { routes } from "../../../processes/routing/routes";

const { Header: AntHeader } = Layout;

export const Header = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate(routes.login);
    message.success("Вы успешно вышли");
  };

  return (
    <AntHeader className={styles.header}>
      <NavMenu />
      <Button danger onClick={handleLogout}>
        Выйти
      </Button>
    </AntHeader>
  );
};
