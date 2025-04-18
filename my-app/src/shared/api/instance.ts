import axios from 'axios';
import { message } from 'antd';
import { routes } from '../../processes/routing/routes';
import { authStorage } from '../../features/auth/model/authStorage';

export const api = axios.create({
  baseURL: 'http://213.218.238.79:7777',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

// Request interceptor - добавляем токен авторизации если есть
api.interceptors.request.use(
  (config) => {
    const token = authStorage.getToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor - обработка ошибок
api.interceptors.response.use(
  (response) => {
    // Можно обработать успешные ответы здесь
    if (response.data?.message) {
      message.success(response.data.message);
    }
    return response;
  },
  (error) => {
    // Обработка ошибок
    if (error.response) {
      switch (error.response.status) {
        case 400:
          message.error(error.response.data?.message || 'Неверный запрос');
          break;
        case 401:
          message.warning('Сессия истекла. Пожалуйста, войдите снова');
          authStorage.clear();
          window.location.href = routes.login;
          break;
        case 403:
          message.error('Доступ запрещен');
          break;
        case 404:
          message.error('Ресурс не найден');
          break;
        case 500:
          message.error('Ошибка сервера. Пожалуйста, попробуйте позже');
          break;
        default:
          message.error(error.response.data?.message || 'Произошла ошибка');
      }
    } else if (error.request) {
      message.error('Сервер не отвечает. Проверьте подключение к интернету');
    } else {
      message.error('Ошибка при настройке запроса');
    }

    return Promise.reject(error);
  }
);

// Вспомогательные методы для часто используемых запросов
export const apiService = {
  get: <T>(url: string, params?: object) => api.get<T>(url, { params }),
  post: <T>(url: string, data: object) => api.post<T>(url, data),
  put: <T>(url: string, data: object) => api.put<T>(url, data),
  delete: <T>(url: string) => api.delete<T>(url),
  patch: <T>(url: string, data: object) => api.patch<T>(url, data),
};

// import axios from 'axios';

// export const api = axios.create({
//   baseURL: 'http://213.218.238.79:7777',
//   timeout: 10000,
//   headers: {
//     'Content-Type': 'application/json',
//   },
// });

// // Добавьте интерцепторы при необходимости
// api.interceptors.response.use(
//   (response) => response,
//   (error) => {
//     if (error.response?.status === 401) {
//       // Обработка 401 ошибки
//     }
//     return Promise.reject(error);
//   }
// );

// import axios from 'axios';

// const API_URL = 'http://213.218.238.79:7777/';

// export const apiInstance = axios.create({
//   baseURL: API_URL,
//   timeout: 10000, // Увеличил таймаут для надежности
//   headers: {
//     'Content-Type': 'application/json',
//     'Accept': 'application/json',
//   },
// });

// // Request interceptor
// apiInstance.interceptors.request.use(
//   (config) => {
//     const token = localStorage.getItem('authToken');
//     if (token) {
//       config.headers.Authorization = `Bearer ${token}`;
//     }
//     return config;
//   },
//   (error) => {
//     return Promise.reject(error);
//   }
// );

// // Response interceptor
// apiInstance.interceptors.response.use(
//   (response) => response,
//   (error) => {
//     // Унифицированная обработка ошибок
//     if (error.response) {
//       switch (error.response.status) {
//         case 401:
//           // Перенаправление на страницу авторизации
//           window.location.href = '/login';
//           break;
//         case 403:
//           console.error('Forbidden:', error.config.url);
//           break;
//         case 500:
//           console.error('Server Error:', error.config.url);
//           break;
//         default:
//           console.error('Request Error:', error.message);
//       }
//     } else if (error.request) {
//       console.error('No response received:', error.request);
//     } else {
//       console.error('Request setup error:', error.message);
//     }
    
//     return Promise.reject(error);
//   }
// );

// // Экспорт часто используемых методов
// export const api = {
//   get: apiInstance.get,
//   post: apiInstance.post,
//   put: apiInstance.put,
//   delete: apiInstance.delete,
//   patch: apiInstance.patch,
// };