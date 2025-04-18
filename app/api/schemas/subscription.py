import uuid

from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.direction_type import DirectionType
from app.api.enums.periodicity_type import PeriodicityType
from app.api.schemas.trainer import Trainer


@dataclass
class Subscription:
    id: Optional[UUID] = field(default_factory=uuid.uuid4)
    direction: Optional[str| int] = field(default=None)
    trainer: Optional[UUID] = field(default=None)
    periodicity: Optional[str | int] = field(default=None)


class WriteDTO(DataclassDTO[Subscription]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[Subscription]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Subscription]):
    config = DTOConfig(exclude={'id'}, partial=True)
