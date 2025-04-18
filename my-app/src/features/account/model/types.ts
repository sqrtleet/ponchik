export interface AccountInfo {
    client: {
      last_name: string;
      first_name: string;
      middle_name: string;
      email: string;
    };
    subscription: {
      direction: string | null;
    } | null;
    schedule: {
      day_name: string | null;
    };
    card_type: {
      name: string | null;
      price: number | null;
    };
  }