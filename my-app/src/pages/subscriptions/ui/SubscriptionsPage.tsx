import { useState } from "react";
import { Typography, Row, Col, message } from "antd";
import { SubscriptionCard } from "../../../features/subscriptions/ui/SubscriptionCard";
import { PurchaseModal } from "../../../features/subscriptions/ui/PurchaseModal";
import styles from "./SubscriptionsPage.module.scss";

const { Title } = Typography;

export const SubscriptionsPage = () => {
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [selectedCardType, setSelectedCardType] = useState<number | null>(null);

  const subscriptions = [
    {
      id: 1,
      title: "1 месяц 12 занятий",
      description: "3 занятия в неделю в течение 1 месяца",
      price: 5000,
      card_type_id: 1,
    },
    {
      id: 2,
      title: "3 месяца 36 занятий",
      description: "3 занятия в неделю в течение 3 месяцев",
      price: 13000,
      card_type_id: 2,
    },
    {
      id: 3,
      title: "6 месяцев 72 занятий",
      description: "3 занятия в неделю в течение 6 месяцев",
      price: 24000,
      card_type_id: 3,
    },
  ];

  const handlePurchase = (cardTypeId: number) => {
    setSelectedCardType(cardTypeId);
    setIsModalVisible(true);
  };

  const handlePurchaseSuccess = () => {
    setIsModalVisible(false);
    // Можно добавить обновление данных после успешной покупки
  };

  return (
    <div className={styles.container}>
      <Title level={1} className={styles.title}>
        Абонементы
      </Title>

      <Row gutter={[24, 24]}>
        {subscriptions.map((subscription) => (
          <Col key={subscription.id} xs={24} sm={12} lg={8}>
            <SubscriptionCard
              subscription={subscription}
              onPurchase={handlePurchase}
            />
          </Col>
        ))}
      </Row>

      <PurchaseModal
        visible={isModalVisible}
        onCancel={() => setIsModalVisible(false)}
        onSuccess={handlePurchaseSuccess}
        cardTypeId={selectedCardType!}
      />
    </div>
  );
};
