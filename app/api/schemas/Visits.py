from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig


@dataclass

class Visits:
    id: int = field(init=False, default_factory=count().__next__)
    client_subsription_id: int = field(default = None)
    date_time: str = field(default = None)
    visit: bool = field(default = False)


class WriteDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude = {'id'})


class ReadDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude = {''})


class PatchDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={'id'}, partial = True)