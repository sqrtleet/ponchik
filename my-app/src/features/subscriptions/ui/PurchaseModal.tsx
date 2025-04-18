import { Modal, Form, Select, Button, App } from "antd";
import { subscriptionApi } from "../api/subscriptionApi";
import { SUBSCRIPTION_TYPES, SCHEDULE_OPTIONS } from "../model/types";
import { authStorage } from "../../auth/model/authStorage";
import { useState } from "react";

export const PurchaseModal = ({
  visible,
  onCancel,
  onSuccess,
  cardTypeId,
}: {
  visible: boolean;
  onCancel: () => void;
  onSuccess: () => void;
  cardTypeId: number;
}) => {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);
  const { message } = App.useApp(); // Используем useApp для доступа к message

  const handleSubmit = async () => {
    try {
      setLoading(true);
      const values = await form.validateFields().catch((err) => {
        message.error("Пожалуйста, заполните все обязательные поля");
        throw err;
      });

      const clientId = authStorage.getClientId();
      if (!clientId) {
        message.error("Ошибка: клиент не авторизован");
        return;
      }

      const purchaseData = {
        schedule_id: values.schedule_id,
        card_type_id: cardTypeId,
        direction: values.direction,
        client_id: clientId,
      };

      await subscriptionApi.purchaseSubscription(purchaseData);
      message.success("Абонемент успешно приобретен!");
      onSuccess();
      form.resetFields();
    } catch (error: any) {
      console.error("Purchase error:", {
        message: error.message,
        response: error.response,
        status: error.response?.status,
        data: error.response?.data,
      });
      if (error.response?.status === 400) {
        message.error("У вас уже есть действительная подписка");
      } else if (!error.message.includes("validateFields")) {
        message.error(
          error.response?.data?.message || "Ошибка при оформлении абонемента"
        );
      }
      onCancel();
    } finally {
      setLoading(false);
    }
  };

  return (
    <Modal
      title="Оформление абонемента"
      open={visible}
      onCancel={onCancel}
      footer={[
        <Button key="back" onClick={onCancel}>
          Отмена
        </Button>,
        <Button
          key="submit"
          type="primary"
          onClick={handleSubmit}
          loading={loading}
        >
          Подтвердить покупку
        </Button>,
      ]}
    >
      <Form form={form} layout="vertical">
        <Form.Item
          name="direction"
          label="Выберите направление"
          rules={[{ required: true, message: "Выберите направление" }]}
        >
          <Select placeholder="Направление">
            {SUBSCRIPTION_TYPES.map((type) => (
              <Select.Option key={type.id} value={type.name}>
                {type.name}
              </Select.Option>
            ))}
          </Select>
        </Form.Item>

        <Form.Item
          name="schedule_id"
          label="Выберите расписание"
          rules={[{ required: true, message: "Выберите расписание" }]}
        >
          <Select placeholder="Расписание">
            {SCHEDULE_OPTIONS.map((schedule) => (
              <Select.Option key={schedule.id} value={schedule.id}>
                {schedule.name}
              </Select.Option>
            ))}
          </Select>
        </Form.Item>
      </Form>
    </Modal>
  );
};
