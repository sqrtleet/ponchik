import React from "react";
import { Button, Card, Typography } from "antd";
// import { Header } from "../../../widgets/header";
// import { Footer } from "../../../widgets/footer";
import styles from "./SubscriptionsPage.module.scss";

const { Title, Text } = Typography;

export const SubscriptionsPage = () => {
  const subscriptions = [
    {
      title: "РАЗОВОЕ ЗАНЯТИЕ",
      description: "Включает в себя одно занятие на любом направлении",
      price: "800P",
    },
    // Другие абонементы...
  ];

  return (
    <div className={styles.subscriptionsPage}>
      {/* <Header /> */}

      <main className={styles.content}>
        <Title>ГЛАВНАЯ НАПРАВЛЕНИЯ</Title>

        <div className={styles.subscriptionList}>
          {subscriptions.map((sub, index) => (
            <Card key={index} className={styles.subscriptionCard}>
              <Title level={2}>{sub.title}</Title>
              <Text>{sub.description}</Text>
              <Title level={3}>{sub.price}</Title>
              <Button type="primary">Приобрести</Button>
            </Card>
          ))}
        </div>
      </main>

      {/* <Footer /> */}
    </div>
  );
};
