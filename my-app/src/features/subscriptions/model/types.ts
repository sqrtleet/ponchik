export interface Subscription {
    id: number;
    title: string;
    description: string;
    price: number;
    card_type_id: number;
  }
  
  export interface PurchaseData {
    client_id: string | null;
    subscription_id: string | null;
    schedule_id: number | null;
    card_type_id: number | null;
    purchase_date: string | null;
    expiration_date: string | null;
    status_id: number | null;
  }
  
  export const SUBSCRIPTION_TYPES = [
    { id: 1, name: 'Йога' },
    { id: 2, name: 'Пилатес' },
    { id: 3, name: 'Стретчинг' }
  ];
  
  export const SCHEDULE_OPTIONS = [
    { id: 1, name: 'Понедельник, среда, пятница' },
    { id: 2, name: 'Вторник, четверг, суббота' },
    { id: 3, name: 'Вторник, пятница, воскресенье' }
  ];