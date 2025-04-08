from itertools import count
from datetime import date
from dataclasses import dataclass, field
from typing import Optional, List
from uuid import UUID

from litestar.dto import DataclassDTO, DTOConfig


@dataclass
class Trainer:
    id: Optional[int] = field(default_factory=count().__next__)
    last_name: Optional[str] = field(default=None)
    first_name: Optional[str] = field(default=None)
    middle_name: Optional[str] = field(default=None)
    phone_number: Optional[str] = field(default=None)
    date_of_birth: Optional[date] = field(default=None)
    email: Optional[str] = field(default=None)
    is_active: Optional[bool] = field(default=None)
    date_joined_trainer: Optional[date] = field(default=None)
    date_left_trainer: Optional[date] = field(default=None)


class WriteDTO(DataclassDTO[Trainer]):
    config = DTOConfig(exclude={'id', 'abonements'})


class ReadDTO(DataclassDTO[Trainer]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Trainer]):
    config = DTOConfig(exclude={'id'}, partial=True)
