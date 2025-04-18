import { api } from '../../../shared/api/instance';
import { ClassType } from '../model/types';

export const classApi = {
  getClasses: async (): Promise<ClassType[]> => {
    const response = await api.get('/directions');
    return response.data;
  },
};