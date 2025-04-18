import { Layout, Space, Typography } from "antd";
import {
  EnvironmentOutlined,
  MailOutlined,
  PhoneOutlined,
} from "@ant-design/icons";
import { Link } from "react-router-dom";
import { routes } from "../../../processes/routing/routes";
import styles from "./Footer.module.scss";

const { Footer: AntFooter } = Layout;

export const Footer = () => {
  return (
    <AntFooter className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.section}>
          <Space direction="vertical" size="small">
            <Typography.Title level={4}>Информация</Typography.Title>
            <Typography.Text>
              <Link to={routes.main}>Главная</Link>
            </Typography.Text>
            <Typography.Text>
              <Link to={routes.classes}>Направления</Link>
            </Typography.Text>
            <Typography.Text>
              <Link to={routes.subscriptions}>Абонементы</Link>
            </Typography.Text>
            <Typography.Text>
              <Link to={routes.trainers}>Тренеры</Link>
            </Typography.Text>
            <Typography.Text>
              <Link to={routes.schedule}>Расписание</Link>
            </Typography.Text>
          </Space>
        </div>
        <div className={styles.section}>
          <Space direction="vertical" size="small">
            <Typography.Title level={4}>Контакты</Typography.Title>
            <Typography.Text>
              <EnvironmentOutlined className={styles.icon} />
              г. Якутск, ул. Кулаковского, 48
            </Typography.Text>
            <Typography.Text>677013</Typography.Text>
            <Typography.Text>
              <PhoneOutlined className={styles.icon} />
              111-222
            </Typography.Text>
            <Typography.Text>
              <MailOutlined className={styles.icon} /> email@gmail.com
            </Typography.Text>
          </Space>
        </div>
      </div>
    </AntFooter>
  );
};
