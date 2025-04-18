from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.api.enums.client_type import ClientType
from app.api.enums.subscription_status import SubscriptionStatusType
from app.core.db.models.sqlalchemy_models import ClientTypeModel, ScheduleModel, StatusModel, CardTypeModel
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


async def seed_schedules():
    engine = create_async_engine(config.connection_string)
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    schedule_names = [
        "Понедельник, Среда, Пятница",
        "Вторник, Четверг, Суббота",
        "Вторник, Пятница, Воскресенье"
    ]

    async with async_session() as session:
        result = await session.execute(select(ScheduleModel.day_name))
        existing = {row[0] for row in result.all()}

        for name in schedule_names:
            if name not in existing:
                print(f"➕ Добавляем: {name}")
                session.add(ScheduleModel(day_name=name))

        await session.commit()
        print("✅ Расписания добавлены")

async def seed_statuses():
    engine = create_async_engine(config.connection_string)
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with async_session() as session:
        result = await session.execute(select(StatusModel.type))
        existing = {row[0] for row in result.all()}

        for status in SubscriptionStatusType:
            if status not in existing:
                print(f"➕ Добавляем статус: {status.name}")
                session.add(StatusModel(type=status))

        await session.commit()
        print("✅ Статусы подписок добавлены")

async def seed_card_types():
    engine = create_async_engine(config.connection_string)
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    card_types_data = [
        {"name": "1 месяц 12 занятий", "price": 5000},
        {"name": "3 месяца 36 занятий", "price": 13000},
        {"name": "6 месяцев 72 занятий", "price": 24000},
    ]

    async with async_session() as session:
        result = await session.execute(select(CardTypeModel.name))
        existing = {row[0] for row in result.all()}

        for card in card_types_data:
            if card["name"] not in existing:
                print(f"➕ Добавляем карту: {card['name']}")
                session.add(CardTypeModel(name=card["name"], price=card["price"]))

        await session.commit()
        print("✅ Карты подписок добавлены")