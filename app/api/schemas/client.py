from datetime import datetime
from itertools import count
from dataclasses import dataclass, field

from litestar import Controller

from litestar.dto import DataclassDTO, DTOConfig


@dataclass
class Client:
    id: int = field(init=False, default_factory=count().__next__)
    last_name: str = field(default=None)
    first_name: str = field(default=None)
    middle_name: str = field(default=None)
    phone_number: str = field(default=None)
    date_of_birth: str = field(default=None)
    email: str = field(default=None)
    client_type_id: int = field(default=None)
    bonus: float = field(default=None)
    is_active: bool = field(default=False)
    date_became_client: str = field(default=None)


class WriteDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={'id'}, partial=True)


class ClientController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
