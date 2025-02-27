from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.daysOfWeek import DaysOfWeek


@dataclass

class ScheduleDays:
    id: int = field(init=False, default_factory=count().__next__)
    day_of_week_id: DaysOfWeek = field(default = None)