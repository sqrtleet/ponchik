from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig


@dataclass

class Schedule:
    id: int = field(init=False, default_factory=count().__next__)
    subsription_id: int = field(default = None)
    time: str = field(default = None)



class WriteDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude = {'id'})


class ReadDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude = {''})


class PatchDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={'id'}, partial = True)