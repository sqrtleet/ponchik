import { Card, List, Typography, Alert, Spin } from "antd";
import styles from "./DirectionCards.module.scss";
import { useClasses } from "../../../features/classes/model/useClasses";

import yoga from "../../../assets/images/classes/yoga.jpg";
import pilates from "../../../assets/images/classes/pilates.jpg";
import stretching from "../../../assets/images/classes/stretching.jpg";
import barre from "../../../assets/images/classes/barre.jpg";

const { Paragraph } = Typography;

export const DirectionCards = () => {
  const { classes, loading, error } = useClasses();

  if (error) {
    return <Alert message={error} type="error" />;
  }

  return (
    <div className={styles.classesPage}>
      {loading ? (
        <Spin size="large" />
      ) : (
        <List
          grid={{ gutter: 16, column: 4 }}
          dataSource={classes}
          renderItem={(item) => (
            <List.Item>
              <Card
                hoverable
                cover={
                  item.direction === "Йога" ? (
                    <img alt={item.direction} src={yoga} />
                  ) : item.direction === "Пилатес" ? (
                    <img alt={item.direction} src={pilates} />
                  ) : item.direction === "Стретчинг" ? (
                    <img alt={item.direction} src={stretching} />
                  ) : (
                    <img alt={item.direction} src={barre} />
                  )
                }
              >
                <Card.Meta
                  title={item.direction}
                  description={
                    <>
                      <Paragraph ellipsis={{ rows: 2 }}>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                      </Paragraph>
                    </>
                  }
                />
              </Card>
            </List.Item>
          )}
        />
      )}
    </div>
  );
};
