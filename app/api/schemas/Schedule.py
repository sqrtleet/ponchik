from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig
from app.api.schemas.trainer import Trainer

from app.api.schemas.subscription import Subscription

@dataclass

class Schedule:
    id: int = field(init=False, default_factory=count().__next__)
    subsription_id: Subscription = field(default = None)
    time: str = field(default = None)



class WriteDTO(DataclassDTO[Schedule]):
    config = DTOConfig(exclude = {'id'})


class ReadDTO(DataclassDTO[Schedule]):
    config = DTOConfig(exclude = {''})


class PatchDTO(DataclassDTO[Schedule]):
    config = DTOConfig(exclude={'id'}, partial = True)