from __future__ import annotations

import uuid
from abc import ABC
from datetime import date, datetime
from typing import List, Optional
from uuid import UUID

from sqlalchemy import ForeignKey, func, select, Integer, DateTime, String, Float, Boolean, Enum, UUID, Date
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from advanced_alchemy.base import UUIDAuditBase, UUIDBase

from app.api.enums.client_type import ClientType


class UserModel(UUIDBase):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)

    client: Mapped["ClientModel"] = relationship(back_populates="user", uselist=False)


class ClientModel(UUIDAuditBase):
    __tablename__ = "clients"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    last_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    middle_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    date_of_birth: Mapped[Optional[Date]] = mapped_column(DateTime, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    client_type_id: Mapped[int] = mapped_column(ForeignKey("client_types.id"), nullable=False)
    client_type: Mapped["ClientTypeModel"] = relationship(lazy="joined", innerjoin=True, back_populates="clients")
    bonus: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    date_became_client: Mapped[Optional[Date]] = mapped_column(DateTime, nullable=True)
    client_subscription: Mapped[Optional[ClientSubscriptionModel]] = relationship(
        "ClientSubscriptionModel", back_populates="client", uselist=False
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["UserModel"] = relationship(back_populates="client")


class ClientTypeModel(UUIDBase):
    __tablename__ = "client_types"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[ClientType] = mapped_column(Enum(ClientType), nullable=False)
    clients: Mapped[List[ClientModel]] = relationship(back_populates="client_type")


class ClientSubscriptionModel(UUIDAuditBase):
    __tablename__ = "client_subscriptions"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    client_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("clients.id"), nullable=False)
    subscription_id: Mapped[int] = mapped_column(Integer, ForeignKey("subscriptions.id"), nullable=False)
    subscription: Mapped["SubscriptionModel"] = relationship(
        lazy="joined", innerjoin=True, back_populates="clients_subscriptions"
    )
    client: Mapped[ClientModel] = relationship(
        "ClientModel", back_populates="client_subscription", uselist=False
    )


class SubscriptionModel(UUIDBase):
    __tablename__ = "subscriptions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    trainer_id: Mapped[int] = mapped_column(Integer, ForeignKey("trainers.id"), nullable=False)
    trainer: Mapped["TrainerModel"] = relationship(lazy="joined", innerjoin=True, back_populates="subscriptions")
    clients_subscriptions: Mapped[List[ClientSubscriptionModel]] = relationship(back_populates="subscription")


class TrainerModel(UUIDBase):
    __tablename__ = "trainers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    middle_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    date_of_birth: Mapped[Optional[Date]] = mapped_column(DateTime, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    date_joined_trainer: Mapped[Optional[Date]] = mapped_column(DateTime, nullable=True)
    date_left_trainer: Mapped[Optional[Date]] = mapped_column(DateTime, nullable=True)
    subscriptions: Mapped[List[SubscriptionModel]] = relationship(back_populates="trainer")
