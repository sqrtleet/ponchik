import { useState, useEffect } from 'react';
import { classApi } from '../api/classApi';
import { ClassType } from './types';

export const useClasses = () => {
  const [classes, setClasses] = useState<ClassType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchClasses = async () => {
      try {
        const data = await classApi.getClasses();
        setClasses(data);
      } catch (err) {
        setError('Ошибка при загрузке направлений');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchClasses();
  }, []);

  return { classes, loading, error };
};