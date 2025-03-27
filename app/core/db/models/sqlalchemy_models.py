from __future__ import annotations

import uuid
from abc import ABC
from datetime import date, datetime
from typing import List, Optional
from uuid import UUID

from sqlalchemy import ForeignKey, func, select, Integer, DateTime, String, Float, Boolean, Enum, UUID
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from advanced_alchemy.base import UUIDAuditBase, UUIDBase

from app.api.enums.client_type import ClientType


class ClientModel(UUIDBase):
    __tablename__ = "clients"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    last_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    middle_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    date_of_birth: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    client_type_id: Mapped[int] = mapped_column(ForeignKey("client_types.id"), nullable=False)
    client_type: Mapped["ClientTypeModel"] = relationship(lazy="joined", innerjoin=True, viewonly=True)
    bonus: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    date_became_client: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class ClientTypeModel(UUIDAuditBase):
    __tablename__ = "client_types"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[ClientType] = mapped_column(Enum(ClientType), nullable=False)
    clients: Mapped[List[ClientModel]] = relationship(back_populates="client_type")
