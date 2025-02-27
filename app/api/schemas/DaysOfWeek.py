from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig


@dataclass

class DaysOfWeek:
    id: int = field(init=False, default_factory=count().__next__)
    day_name: str = field(default = None)





class WriteDTO(DataclassDTO[DaysOfWeek]):
    config = DTOConfig(exclude = {'id'})


class ReadDTO(DataclassDTO[DaysOfWeek]):
    config = DTOConfig(exclude = {''})


class PatchDTO(DataclassDTO[DaysOfWeek]):
    config = DTOConfig(exclude={'id'}, partial = True)