// src/features/common/MessageProvider.tsx
import { App } from "antd";
import { ReactNode, createContext, useContext } from "react";

const MessageContext = createContext<{
  success: (content: string) => void;
  error: (content: string) => void;
  warning: (content: string) => void;
} | null>(null);

export const MessageProvider = ({ children }: { children: ReactNode }) => {
  const { message } = App.useApp();

  const messageApi = {
    success: (content: string) => message.success(content),
    error: (content: string) => message.error(content),
    warning: (content: string) => message.warning(content),
  };

  return (
    <MessageContext.Provider value={messageApi}>
      <App>{children}</App>
    </MessageContext.Provider>
  );
};

export const useMessageApi = () => {
  const context = useContext(MessageContext);
  if (!context) {
    throw new Error("useMessageApi must be used within a MessageProvider");
  }
  return context;
};
