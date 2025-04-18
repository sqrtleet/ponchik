export interface PurchaseData {
    schedule_id: number;
    card_type_id: number;
    direction: string;
    client_id: string; // UUID
  }
  
  export interface Subscription {
    id: number;
    title: string;
    description: string;
    price: number;
    card_type_id: number;
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