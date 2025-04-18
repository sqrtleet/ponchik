import uuid
from datetime import date
from itertools import count
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from litestar.dto import DataclassDTO, DTOConfig

from app.api.schemas.client import Client
from app.api.schemas.schedule import Schedule
from app.api.schemas.subscription import Subscription
from app.api.schemas.schedule_days import ScheduleDays
from app.api.schemas.сard_types import CardTypes
from app.api.enums.subscription_status import SubscriptionStatusType


@dataclass
class ClientSubscription:
    id: Optional[UUID] = field(default_factory=uuid.uuid4)
    client_id: Optional[UUID] = field(default=None)
    subscription_id: Optional[UUID] = field(default = None)
    schedule_id: Optional[int] = field(default = None)
    card_type_id: Optional[int] = field(default=None)
    purchase_date: Optional[date] = field(default=None)
    expiration_date: Optional[date] = field(default=None)
    status_id: Optional[int] = field(default=None)


class WriteDTO(DataclassDTO[ClientSubscription]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[ClientSubscription]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[ClientSubscription]):
    config = DTOConfig(exclude={'id'}, partial=True)
