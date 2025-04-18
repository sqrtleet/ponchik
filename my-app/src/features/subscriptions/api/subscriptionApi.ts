import { api } from '../../../shared/api/instance';
import { PurchaseData } from '../model/types';

export const subscriptionApi = {
  purchaseSubscription: (data: PurchaseData) => {
    return api.post('/client-subscriptions', data);
  }
};