import { Avatar, Menu } from "antd";
import { Link } from "react-router-dom";
import { UserOutlined } from "@ant-design/icons";
import { routes } from "../../../processes/routing/routes";

export const NavMenu = () => {
  const items = [
    {
      key: "main",
      label: <Link to={routes.main}>Главная</Link>,
    },
    {
      key: "classes",
      label: <Link to={routes.classes}>Направления</Link>,
    },
    {
      key: "subscriptions",
      label: <Link to={routes.subscriptions}>Абонементы</Link>,
    },
    {
      key: "account",
      label: (
        <Link to={routes.account}>
          <Avatar icon={<UserOutlined />} />
        </Link>
      ),
    },
    // {
    //   key: "trainers",
    //   label: <Link to={routes.trainers}>Тренеры</Link>,
    // },
    // {
    //   key: "schedule",
    //   label: <Link to={routes.schedule}>Расписание</Link>,
    // },
  ];

  return (
    <Menu
      theme="light"
      mode="horizontal"
      items={items}
      style={{
        flex: 1,
        justifyContent: "flex-end",
        borderBottom: "none",
        background: "none",
      }}
    />
  );
};
