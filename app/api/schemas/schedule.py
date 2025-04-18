import uuid
from itertools import count
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID

from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.days_of_week import DaysOfWeek


@dataclass
class Schedule:
    id: Optional[int] = field(default_factory=count().__next__)
    day_name: Optional[str] = field(default=None)


class WriteDTO(DataclassDTO[Schedule]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[Schedule]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Schedule]):
    config = DTOConfig(exclude={'id'}, partial=True)
