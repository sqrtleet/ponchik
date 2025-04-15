import asyncio
import sys
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.exc import OperationalError

from config import settings

db_url = settings.database_url


async def wait_for_db(max_retries: int = 10, delay: int = 2):
    print(f'⏳ Waiting for DB: {db_url}')
    engine = create_async_engine(db_url)
    for attempt in range(1, max_retries + 1):
        try:
            async with engine.begin():
                print('✅ Database is ready.')
                return
        except OperationalError as e:
            print(f'[{attempt}/{max_retries}] DB not ready: {e}')
            await asyncio.sleep(delay)
    print('❌ Database not available. Exiting.')
    sys.exit(1)


if __name__ == '__main__':
    asyncio.run(wait_for_db())