import { Button, Form, Input, message, Typography } from "antd";
import { authApi } from "../api/authApi";
import { authStorage } from "../model/authStorage";
import { useAuth } from "../model/useAuth";
import { Link, useNavigate } from "react-router-dom";
import { routes } from "../../../processes/routing/routes";
import { useState } from "react";
import styles from "./AuthForms.module.scss";

const { Text } = Typography;

export const RegisterForm = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const onFinish = async (values: {
    last_name: string;
    first_name: string;
    middle_name: string;
    email: string;
    password: string;
  }) => {
    try {
      setLoading(true);
      const response = await authApi.register(values);
      authStorage.setToken(response.data.token);
      authStorage.setClientId(response.data.client_id);
      login(response.data.token, response.data.client_id);
      message.success("Регистрация прошла успешно");
      navigate(routes.main);
    } catch (error) {
      message.error("Ошибка регистрации");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.authContainer}>
      <Form name="register" onFinish={onFinish} layout="vertical">
        <Form.Item
          name="last_name"
          label="Фамилия"
          rules={[{ required: true, message: "Введите фамилию" }]}
        >
          <Input placeholder="Иванов" />
        </Form.Item>

        <Form.Item
          name="first_name"
          label="Имя"
          rules={[{ required: true, message: "Введите имя" }]}
        >
          <Input placeholder="Иван" />
        </Form.Item>

        <Form.Item name="middle_name" label="Отчество">
          <Input placeholder="Иванович" />
        </Form.Item>

        <Form.Item
          name="email"
          label="Email"
          rules={[
            { required: true, message: "Введите email" },
            { type: "email", message: "Неверный формат email" },
          ]}
        >
          <Input placeholder="example@mail.com" />
        </Form.Item>

        <Form.Item
          name="password"
          label="Пароль"
          rules={[
            { required: true, message: "Введите пароль" },
            { min: 6, message: "Минимум 6 символов" },
          ]}
        >
          <Input.Password placeholder="Пароль" />
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit" block loading={loading}>
            Зарегистрироваться
          </Button>
        </Form.Item>
      </Form>

      <div className={styles.footerLink}>
        <Text>
          Уже есть аккаунт?{" "}
          <Link to={routes.login} className={styles.link}>
            Войти
          </Link>
        </Text>
      </div>
    </div>
  );
};
