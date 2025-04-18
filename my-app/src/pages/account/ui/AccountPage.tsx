import { Card, Descriptions, Typography, Spin, Alert, Tag } from "antd";
import { useAccount } from "../../../features/account/model/useAccount";
import styles from "./AccountPage.module.scss";

const { Title } = Typography;

export const AccountPage = () => {
  const { accountInfo, loading, error } = useAccount();

  if (loading) return <Spin size="large" className={styles.spin} />;
  if (error) return <Alert message={error} type="error" />;
  if (!accountInfo) return <Alert message="Данные не найдены" type="warning" />;

  const { client, subscription, schedule, card_type } = accountInfo;

  return (
    <div className={styles.container}>
      <Title level={2} className={styles.title}>
        Личный кабинет
      </Title>

      <Card title="Персональная информация" className={styles.card}>
        <Descriptions column={1}>
          <Descriptions.Item label="Фамилия">
            {client.last_name}
          </Descriptions.Item>
          <Descriptions.Item label="Имя">{client.first_name}</Descriptions.Item>
          <Descriptions.Item label="Отчество">
            {client.middle_name || "-"}
          </Descriptions.Item>
          <Descriptions.Item label="Email">{client.email}</Descriptions.Item>
        </Descriptions>
      </Card>

      <Card title="Абонемент" className={styles.card}>
        {subscription?.direction ? (
          <Descriptions column={1}>
            <Descriptions.Item label="Направление">
              {subscription.direction || "Не выбрано"}
            </Descriptions.Item>
            <Descriptions.Item label="Тип абонемента">
              {card_type.name ? (
                <Tag color="blue">{card_type.name}</Tag>
              ) : (
                "Не выбрано"
              )}
            </Descriptions.Item>
            <Descriptions.Item label="Стоимость">
              {card_type.price
                ? `${card_type.price.toLocaleString("ru-RU")} ₽`
                : "-"}
            </Descriptions.Item>
            <Descriptions.Item label="Дни посещения">
              {schedule.day_name || "Не выбрано"}
            </Descriptions.Item>
          </Descriptions>
        ) : (
          "Нет абонементов"
        )}
      </Card>
    </div>
  );
};
