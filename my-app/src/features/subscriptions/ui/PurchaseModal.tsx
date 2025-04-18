import { Modal, Form, Select, Button } from "antd";
import { PurchaseData } from "../model/types";
import { SUBSCRIPTION_TYPES, SCHEDULE_OPTIONS } from "../model/types";

export const PurchaseModal = ({
  visible,
  onCancel,
  onPurchase,
  cardTypeId,
}: {
  visible: boolean;
  onCancel: () => void;
  onPurchase: (data: PurchaseData) => void;
  cardTypeId: number | null;
}) => {
  const [form] = Form.useForm();

  const handleSubmit = () => {
    form
      .validateFields()
      .then((values) => {
        const purchaseData: PurchaseData = {
          client_id: "1",
          subscription_id: values.subscription_id,
          schedule_id: values.schedule_id,
          card_type_id: cardTypeId,
          purchase_date: "2025-04-18",
          expiration_date: "2025-04-18",
          status_id: 1,
        };
        onPurchase(purchaseData);
        form.resetFields();
      })
      .catch((info) => {
        console.log("Validate Failed:", info);
      });
  };

  return (
    <Modal
      title="Оформление абонемента"
      visible={visible}
      onCancel={onCancel}
      footer={[
        <Button key="back" onClick={onCancel}>
          Отмена
        </Button>,
        <Button key="submit" type="primary" onClick={handleSubmit}>
          Подтвердить покупку
        </Button>,
      ]}
    >
      <Form form={form} layout="vertical">
        <Form.Item
          name="subscription_id"
          label="Выберите направление"
          rules={[
            { required: true, message: "Пожалуйста, выберите направление" },
          ]}
        >
          <Select placeholder="Направление">
            {SUBSCRIPTION_TYPES.map((type) => (
              <Select.Option key={type.id} value={type.id.toString()}>
                {type.name}
              </Select.Option>
            ))}
          </Select>
        </Form.Item>

        <Form.Item
          name="schedule_id"
          label="Выберите расписание"
          rules={[
            { required: true, message: "Пожалуйста, выберите расписание" },
          ]}
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
