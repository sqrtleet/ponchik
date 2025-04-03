from itertools import count
from dataclasses import dataclass, field

from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.periodicity_type import PeriodicityType


@dataclass
class CardTypes:
    id: int = field(init=False, default_factory=count().__next__)
    name: str = field(default=None)
    number_of_sessions: int = field(default=None)
    periodicity: PeriodicityType = field(default=None)
    price: float = field(default=None)
    description: str = field(default=None)


class WriteDTO(DataclassDTO[CardTypes]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[CardTypes]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[CardTypes]):
    config = DTOConfig(exclude={'id'}, partial=True)
