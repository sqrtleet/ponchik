import uuid
from datetime import date
from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID


from litestar.dto import DataclassDTO, DTOConfig

from app.api.enums.client_type import ClientType


@dataclass
class Client:
    id: Optional[UUID] = field(default_factory=uuid.uuid4)
    last_name: Optional[str] = field(default=None)
    first_name: Optional[str] = field(default=None)
    middle_name: Optional[str] = field(default=None)
    phone_number: Optional[str] = field(default=None)
    date_of_birth: Optional[date] = field(default=None)
    email: Optional[str] = field(default=None)
    client_type: ClientType = field(default=ClientType.REGULAR)
    bonus: Optional[float] = field(default=None)
    is_active: Optional[bool] = field(default=False)
    date_became_client: Optional[date] = field(default=None)


class WriteDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={'id'})


class ReadDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={''})


class PatchDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={'id'}, partial=True)
