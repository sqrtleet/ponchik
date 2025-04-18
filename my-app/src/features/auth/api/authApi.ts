import { api } from "../../../shared/api/instance";

interface RegisterData {
  last_name: string;
  first_name: string;
  middle_name: string;
  email: string;
  password: string;
}

interface LoginData {
  email: string;
  password: string;
}

interface AuthResponse {
  token: string;
  client_id: string;
}

export const authApi = {
  register: (data: RegisterData) => {
    return api.post<AuthResponse>('/auth/register', data);
  },
  login: (data: LoginData) => {
    return api.post<AuthResponse>('/auth/login', data);
  },
};