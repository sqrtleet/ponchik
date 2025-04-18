import { api } from '../../../shared/api/instance';
import { authStorage } from '../../auth/model/authStorage';
import { AccountInfo } from '../model/types';

export const accountApi = {
  getAccountInfo: () => {
    const token = authStorage.getClientId();
    return api.get<AccountInfo>(`/bff/info?client_id=${token}`);
  },
};