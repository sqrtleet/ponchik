from itertools import count
from dataclasses import dataclass, field

from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.days_of_week import DaysOfWeek


@dataclass
class Schedule:
    id: int = field(init=False)
