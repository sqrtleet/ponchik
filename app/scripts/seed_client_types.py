from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.api.enums.client_type import ClientType
from app.core.db.models.sqlalchemy_models import ClientTypeModel
from app.core.db.db import config


async def seed_client_types():
    engine = create_async_engine(config.connection_string)
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with async_session() as session:
        result = await session.execute(select(ClientTypeModel.type))
        existing_types = {row[0] for row in result.all()}

        for ct in ClientType:
            if ct not in existing_types:
                print(f"Добавляем: {ct}")
                session.add(ClientTypeModel(type=ct))

        await session.commit()
        print("✅ Типы клиентов добавлены")
