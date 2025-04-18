import { Card, Typography, Button } from "antd";
import styles from "./SubscriptionCard.module.scss";
import { Subscription } from "../model/types";

const { Title, Text } = Typography;

export const SubscriptionCard = ({
  subscription,
  onPurchase,
}: {
  subscription: Subscription;
  onPurchase: (cardTypeId: number) => void;
}) => {
  return (
    <Card className={styles.card} hoverable>
      <Title level={3} className={styles.title}>
        {subscription.title}
      </Title>
      <Text className={styles.description}>{subscription.description}</Text>
      <div className={styles.priceContainer}>
        <Title level={2} className={styles.price}>
          {subscription.price.toLocaleString("ru-RU")} ₽
        </Title>
        <Button
          type="primary"
          size="large"
          onClick={() => onPurchase(subscription.card_type_id)}
        >
          Приобрести
        </Button>
      </div>
    </Card>
  );
};
