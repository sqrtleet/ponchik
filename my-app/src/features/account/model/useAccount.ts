import { useState, useEffect } from 'react';
import { accountApi } from '../api/accountApi';
import { AccountInfo } from './types';

export const useAccount = () => {
  const [accountInfo, setAccountInfo] = useState<AccountInfo | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchAccountInfo = async () => {
      try {
        const response = await accountApi.getAccountInfo();
        setAccountInfo(response.data);
      } catch (err) {
        setError('Ошибка при загрузке данных');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchAccountInfo();
  }, []);

  return { accountInfo, loading, error };
};