from datetime import datetime
from itertools import count
from dataclasses import dataclass, field

from litestar.dto import DataclassDTO, DTOConfig


@dataclass
class Trainer:
    id: int = field(init=False, default_factory=count().__next__)
    last_name: str = field(default=None)
    first_name: str = field(default=None)
    middle_name: str = field(default=None)
    phone_number: str = field(default=None)
    date_of_birth: str = field(default=None)
    email: str = field(default=None)
    is_active: bool = field(default=False)
    date_joined_trainer: str = field(default=None)
    date_left_trainer: str = field(default=None)


class WriteDTO(DataclassDTO[Trainer]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[Trainer]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Trainer]):
    config = DTOConfig(exclude={'id'}, partial=True)
