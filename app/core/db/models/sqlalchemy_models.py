from __future__ import annotations

import uuid
from datetime import date
from typing import List
from uuid import UUID

from sqlalchemy import ForeignKey, func, select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Boolean

from app.api.enums.client_type import ClientType


class Base(DeclarativeBase):
    pass


class ClientModel(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column(String(100), nullable=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=True)
    middle_name: Mapped[str] = mapped_column(String(100), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    date_of_birth: Mapped[str] = mapped_column(String(10), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    client_type_id: Mapped[int] = mapped_column(ForeignKey("client_types.client_id"))
    client_type: Mapped["ClientTypeModel"] = relationship(back_populates="client")
    bonus: Mapped[float] = mapped_column(Float, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    date_became_client: Mapped[str] = mapped_column(String(10), nullable=True)


class ClientTypeModel(Base):
    __tablename__ = "client_types"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[ClientType]
    client: Mapped[List["ClientModel"]] = relationship(back_populates="client_type")

# class ClientSubscriptionsModel(Base):
#     __tablename__ = "client_subscriptions"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     client_id: Mapped[List[ClientModel]] = relationship(back_populates="id")
#     subscription_id: Mapped[SubscriptionsModel] = relationship(back_populates="id")
#
#
# class SubscriptionsModel(Base):
#     __tablename__ = "subscriptions"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
