import { Layout } from "antd";
import { AppRouter } from "./processes/routing";
import { Header } from "./widgets/header";
// import { Footer } from "./widgets/footer";

import styles from "./App.module.scss";

const { Content } = Layout;

function App() {
  return (
    <Layout className={styles.layout}>
      <Header />
      <Content className={styles.content}>
        <AppRouter />
      </Content>
      {/* <Footer /> */}
    </Layout>
  );
}

export default App;

// import React from 'react';
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.tsx</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
