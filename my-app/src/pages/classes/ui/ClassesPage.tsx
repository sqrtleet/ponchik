import { Typography } from "antd";
import { DirectionCards } from "../../../widgets/directionCards/ui/DirectionCards";
import styles from "./ClassesPage.module.scss";

const { Title } = Typography;

export const ClassesPage = () => {
  return (
    <div className={styles.classesPage}>
      <Title level={2}>Направления тренировок</Title>
      <DirectionCards />
    </div>
  );
};
