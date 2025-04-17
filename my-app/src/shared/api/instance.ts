import axios from 'axios';

const API_URL = 'http://213.218.238.79:7777';

export const apiInstance = axios.create({
  baseURL: API_URL,
  timeout: 10000, // Увеличил таймаут для надежности
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

// Request interceptor
apiInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
apiInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    // Унифицированная обработка ошибок
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // Перенаправление на страницу авторизации
          window.location.href = '/login';
          break;
        case 403:
          console.error('Forbidden:', error.config.url);
          break;
        case 500:
          console.error('Server Error:', error.config.url);
          break;
        default:
          console.error('Request Error:', error.message);
      }
    } else if (error.request) {
      console.error('No response received:', error.request);
    } else {
      console.error('Request setup error:', error.message);
    }
    
    return Promise.reject(error);
  }
);

// Экспорт часто используемых методов
export const api = {
  get: apiInstance.get,
  post: apiInstance.post,
  put: apiInstance.put,
  delete: apiInstance.delete,
  patch: apiInstance.patch,
};