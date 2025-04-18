from itertools import count
from dataclasses import dataclass, field
from typing import Optional

from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.periodicity_type import PeriodicityType


@dataclass
class CardTypes:
    id: Optional[int] = field(default_factory=count().__next__)
    name: Optional[str] = field(default=None)
    price: Optional[float] = field(default=None)


class WriteDTO(DataclassDTO[CardTypes]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[CardTypes]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[CardTypes]):
    config = DTOConfig(exclude={'id'}, partial=True)
