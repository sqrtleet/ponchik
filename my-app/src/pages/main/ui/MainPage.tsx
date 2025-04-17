import React from "react";
import { Button, Card, Row, Col, Typography } from "antd";
// import { Header } from "../../../widgets/header";
// import { Footer } from "../../../widgets/footer";
import styles from "./MainPage.module.scss";

const { Title, Paragraph } = Typography;

export const MainPage = () => {
  return (
    <div className={styles.mainPage}>
      {/* <Header /> */}

      <section className={styles.hero}>
        <Title level={1}>
          Позаботься о своем теле в нашей уютной фитнес-студии
        </Title>
        <Title level={3}>
          Запишись на первое пробное занятие всего за 800 рублей
        </Title>
        <Button type="primary" size="large">
          Записаться
        </Button>
      </section>

      <section className={styles.directions}>
        <Title level={2}>Тренировки по разным направлениям</Title>
        <Row gutter={16}>
          <Col span={6}>
            <Card cover={<img alt="Фото" src="/photo.jpg" />}>Фото</Card>
          </Col>
          <Col span={6}>
            <Card cover={<img alt="Пилатес" src="/pilates.jpg" />}>
              Пилатес
            </Card>
          </Col>
          <Col span={6}>
            <Card cover={<img alt="Стретчинг" src="/stretching.jpg" />}>
              Стретчинг
            </Card>
          </Col>
          <Col span={6}>
            <Card cover={<img alt="Барре" src="/barre.jpg" />}>Барре</Card>
          </Col>
        </Row>
      </section>

      <section className={styles.mission}>
        <Title level={2}>Наша миссия</Title>
        <Paragraph>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit...
        </Paragraph>
      </section>

      {/* <Footer /> */}
    </div>
  );
};
