import uuid
from itertools import count
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.days_of_week import DaysOfWeek
from app.api.enums.subscription_status import SubscriptionStatusType


@dataclass
class Status:
    id: Optional[int] = field(default_factory=count().__next__)
    type: Optional[SubscriptionStatusType] = field(default=SubscriptionStatusType(1))


class WriteDTO(DataclassDTO[Status]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[Status]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Status]):
    config = DTOConfig(exclude={'id'}, partial=True)
