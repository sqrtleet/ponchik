import { Layout } from "antd";
import { NavMenu } from "./NavMenu";
import styles from "./Header.module.scss";

const { Header: AntHeader } = Layout;

export const Header = () => {
  return (
    <AntHeader className={styles.header}>
      <NavMenu />
    </AntHeader>
  );
};
