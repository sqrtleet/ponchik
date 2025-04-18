from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

from litestar.dto import DTOConfig, DataclassDTO

from app.api.enums.client_type import ClientType


@dataclass
class Register:
    email: str
    password: str
    last_name: Optional[str] = field(default=None)
    first_name: Optional[str] = field(default=None)
    middle_name: Optional[str] = field(default=None)
    phone_number: Optional[str] = field(default=None)
    date_of_birth: Optional[date] = field(default=None)
    email: Optional[str] = field(default=None)
    client_type: ClientType = field(default=ClientType.REGULAR)
    bonus: Optional[float] = field(default=None)
    is_active: Optional[bool] = field(default=False)
    date_became_client: Optional[date] = field(default=datetime.now())


@dataclass
class Login:
    email: str
    password: str


@dataclass
class TokenResponse:
    access_token: str
    token_type: str
