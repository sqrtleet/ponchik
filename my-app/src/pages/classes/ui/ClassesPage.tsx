import React from "react";
import { Typography } from "antd";
// import { Header } from "../../../widgets/header";
// import { Footer } from "../../../widgets/footer";
import styles from "./ClassesPage.module.scss";

const { Title, Paragraph } = Typography;

export const ClassesPage = () => {
  return (
    <div className={styles.classesPage}>
      {/* <Header /> */}

      <main className={styles.content}>
        <Title>Rora</Title>
        <Paragraph>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit...
        </Paragraph>

        <Title level={2}>Пилатес</Title>
        <Paragraph>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit...
        </Paragraph>

        <Title level={2}>Стретчинг</Title>
        <Paragraph>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit...
        </Paragraph>

        <Title level={2}>Барре</Title>
        <Paragraph>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit...
        </Paragraph>
      </main>

      {/* <Footer /> */}
    </div>
  );
};
