from datetime import datetime
from itertools import count
from dataclasses import dataclass, field

from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.direction_type import DirectionType
from app.api.enums.periodicity_type import PeriodicityType
from app.api.schemas.trainer import Trainer


@dataclass
class Subscription:
    id: int = field(init=False, default_factory=count().__next__)
    direction: DirectionType = field(default=None)
    trainer: Trainer = field(default=None)
    periodicity: PeriodicityType = field(default=None)


class WriteDTO(DataclassDTO[Subscription]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[Subscription]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Subscription]):
    config = DTOConfig(exclude={'id'}, partial=True)
