import { Button, Form, Input, message, Typography } from "antd";
import { authApi } from "../api/authApi";
import { authStorage } from "../model/authStorage";
import { useAuth } from "../model/useAuth";
import { Link, useNavigate } from "react-router-dom";
import { routes } from "../../../processes/routing/routes";
import { useState } from "react";
import styles from "./AuthForms.module.scss";

const { Text } = Typography;

export const LoginForm = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const onFinish = async (values: { email: string; password: string }) => {
    try {
      setLoading(true);
      const response = await authApi.login(values);
      authStorage.setToken(response.data.token);
      authStorage.setClientId(response.data.client_id);
      login(response.data.token, response.data.client_id);
      message.success("Вход выполнен успешно");
      navigate(routes.main);
    } catch (error) {
      message.error("Ошибка входа. Проверьте данные");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.authContainer}>
      <Form name="login" onFinish={onFinish} layout="vertical">
        <Form.Item
          name="email"
          label="Email"
          rules={[
            { required: true, message: "Введите email" },
            // { type: "email", message: "Неверный формат email" },
          ]}
        >
          <Input placeholder="example@mail.com" />
        </Form.Item>

        <Form.Item
          name="password"
          label="Пароль"
          rules={[{ required: true, message: "Введите пароль" }]}
        >
          <Input.Password placeholder="Пароль" />
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit" block loading={loading}>
            Войти
          </Button>
        </Form.Item>
      </Form>

      <div className={styles.footerLink}>
        <Text>
          Нет аккаунта?{" "}
          <Link to={routes.register} className={styles.link}>
            Зарегистрироваться
          </Link>
        </Text>
      </div>
    </div>
  );
};
