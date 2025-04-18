import { Layout } from "antd";
import { AppRouter } from "./processes/routing";
import { Header } from "./widgets/header";
import { Footer } from "./widgets/footer";

import styles from "./App.module.scss";
import { useAuth } from "./features/auth/model/useAuth";

const { Content } = Layout;

function App() {
  const { isAuthenticated } = useAuth();

  return (
    <Layout className={styles.layout}>
      {isAuthenticated && <Header />}
      <Content className={styles.content}>
        <AppRouter />
      </Content>
      {isAuthenticated && <Footer />}
    </Layout>
  );
}

export default App;
