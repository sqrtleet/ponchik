from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.daysOfWeek import DaysOfWeek
from app.api.schemas.schedule import Schedule


@dataclass

class ScheduleDays:
    schedule_id: Schedule = field(default = None)
    day_of_week_id: DaysOfWeek = field(default = None)