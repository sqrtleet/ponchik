const AUTH_TOKEN_KEY = "auth_token";
const CLIENT_ID_KEY = "client_id";

export const authStorage = {
  getToken: (): string | null => {
    return localStorage.getItem(AUTH_TOKEN_KEY);
  },

  setToken: (token: string): void => {
    localStorage.setItem(AUTH_TOKEN_KEY, token);
  },

  getClientId: (): string | null => {
    return localStorage.getItem(CLIENT_ID_KEY);
  },

  setClientId: (clientId: string): void => {
    localStorage.setItem(CLIENT_ID_KEY, clientId);
  },

  clear: (): void => {
    localStorage.removeItem(AUTH_TOKEN_KEY);
    localStorage.removeItem(CLIENT_ID_KEY);
  },
};
