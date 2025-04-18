import { Layout } from "antd";
import { AppRouter } from "./processes/routing";
import { Header } from "./widgets/header";
import { Footer } from "./widgets/footer";
import { useAuth } from "./features/auth/model/useAuth";
import { useEffect, useState } from "react";

import styles from "./App.module.scss";

const { Content } = Layout;

function App() {
  const { isAuthenticated } = useAuth();
  const [showLayout, setShowLayout] = useState(false);

  // Синхронизация состояния при изменении авторизации
  useEffect(() => {
    setShowLayout(isAuthenticated);
  }, [isAuthenticated]);

  return (
    <Layout className={styles.layout}>
      {showLayout && <Header />}
      <Content className={styles.content}>
        <AppRouter />
      </Content>
      {showLayout && <Footer />}
    </Layout>
  );
}

export default App;
