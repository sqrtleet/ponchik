from dataclasses import dataclass, field
from typing import Optional, Dict

from app.api.schemas.client import Client
from app.api.schemas.client_subsription import ClientSubscription
from app.api.schemas.schedule import Schedule
from app.api.schemas.subscription import Subscription
from app.api.schemas.trainer import Trainer
from app.api.schemas.сard_types import CardTypes
from app.api.schemas.status import Status


@dataclass
class BFFResponse:
    client: Optional[Client] = field(default=None)
    subscription: Optional[Subscription] = field(default=None)
    trainer: Optional[Trainer] = field(default=None)
    client_subscription: Optional[ClientSubscription] = field(default=None)
    schedule: Optional[Schedule] = field(default=None)
    card_type: Optional[CardTypes] = field(default=None)
    status: Optional[Status] = field(default=None)
