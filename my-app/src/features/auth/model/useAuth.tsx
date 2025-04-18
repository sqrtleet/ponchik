import { useState, useEffect } from "react";
import { authStorage } from "./authStorage";

export const useAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(
    !!authStorage.getToken()
  );

  useEffect(() => {
    // Синхронизация состояния при изменении в других вкладках
    const handleStorageChange = () => {
      setIsAuthenticated(!!authStorage.getToken());
    };

    window.addEventListener("storage", handleStorageChange);
    return () => window.removeEventListener("storage", handleStorageChange);
  }, []);

  const login = (token: string, clientId: string) => {
    authStorage.setToken(token);
    authStorage.setClientId(clientId);
    setIsAuthenticated(true);
  };

  const logout = () => {
    authStorage.clear();
    setIsAuthenticated(false);
  };

  return { isAuthenticated, login, logout };
};
