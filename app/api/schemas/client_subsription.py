from itertools import count
from dataclasses import dataclass, field

from litestar.dto import DataclassDTO, DTOConfig

from app.api.schemas.client import Client
from app.api.schemas.schedule import Schedule
from app.api.schemas.subscription import Subscription
from app.api.schemas.schedule_days import ScheduleDays
from app.api.schemas.сard_types import CardTypes
from app.api.enums.subscription_status import SubscriptionStatusType


@dataclass
class ClientSubsriptions:
    id: int = field(init=False, default_factory=count().__next__)
    client_id: Client = field(default=None)
    subscription_id: Subscription = field(default = None)
    schedule_id: Schedule = field(default = None)
    card_type_id: CardTypes = field(default=None)
    price: float = field(default=None)
    purchase_date: str = field(default=None)
    expiration_date: str = field(default=None)
    status_id: SubscriptionStatusType = field(default=None)


class WriteDTO(DataclassDTO[ClientSubsriptions]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[ClientSubsriptions]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[ClientSubsriptions]):
    config = DTOConfig(exclude={'id'}, partial=True)
