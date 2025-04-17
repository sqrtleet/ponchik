import React from "react";
import { ConfigProvider } from "antd";
import { StyleProvider } from "@ant-design/cssinjs";
import ruRU from "antd/locale/ru_RU";

export const withProviders = (component: () => React.ReactNode) => () => {
  return (
    <StyleProvider hashPriority="high">
      <ConfigProvider
        locale={ruRU}
        theme={{
          token: {
            colorPrimary: "#722ed1",
            borderRadius: 4,
          },
        }}
      >
        {component()}
      </ConfigProvider>
    </StyleProvider>
  );
};
