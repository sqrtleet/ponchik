import { Typography, Image } from "antd";
import styles from "./MainPage.module.scss";
import { DirectionCards } from "../../../widgets/directionCards/ui/DirectionCards";

import tyotya from "../../../assets/images/main/main.png";
import missionImage from "../../../assets/images/main/mission.jpg";

const { Title, Paragraph } = Typography;

export const MainPage = () => {
  return (
    <div className={styles.mainPage}>
      <section className={styles.hero}>
        <Title level={2}>
          Позаботься о своем теле в нашей уютной фитнес-студии
        </Title>
        <Image alt="tyotya" src={tyotya} preview={false} />
      </section>

      <section className={styles.directions}>
        <div className={styles.classesPage}>
          <Title level={2}>Тренировки по разным направлениям</Title>
          <DirectionCards />
        </div>
      </section>

      <section className={styles.mission}>
        <div className={styles.container}>
          <div className={styles.section}>
            <Title level={2}>Наша миссия</Title>
            <Paragraph className={styles.text}>
              Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Cras
              rhoncus posuere ligula eu congue. Morbi facilisis porta aliquam.
              Donec magna odio, tempor ut vestibulum quis, gravida sit amet
              nibh. Nullam ultrices ligula quis nisi furibus, posuere sagittis
              nisl accumsan. Integer pulvinar venenatis tellus, vel condimentum
              metus tristique vitae.
            </Paragraph>
          </div>
          <div className={styles.section}>
            <Image
              src={missionImage}
              alt="Our Mission"
              preview={false}
              className={styles.image}
              height={400}
            />
          </div>
        </div>
      </section>
    </div>
  );
};
