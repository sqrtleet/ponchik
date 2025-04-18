import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { withProviders } from "./app/providers/withProviders";
import App from "./App";
import "antd/dist/reset.css"; // Для Ant Design 5.x

import "./styles/globals.scss";
import "./styles/antd-overrides.scss";
import { MessageProvider } from "./features/common/MessageProvider";

const Root = withProviders(() => {
  return (
    <BrowserRouter>
      <MessageProvider>
        <App />
      </MessageProvider>
    </BrowserRouter>
  );
});

// Явная проверка элемента
const rootElement = document.getElementById("root");
if (!rootElement) throw new Error("Root element not found");

ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>
);
