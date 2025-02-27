from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig


@dataclass

class ClientSubsriptions:
    id: int = field(init=False, default_factory=count().__next__)
    client_id: int = field(default = None)
    subscription_id: int = field(default = None)
    schedule_id: int = field(default = None)
    card_type_id: int = field(default = None)
    price: float = field(default = None)
    purchase_date: str = field(default = None)
    expiration_date: str = field(default = None)
    status_id: int = field(default = None)



class WriteDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude = {'id'})


class ReadDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude = {''})


class PatchDTO(DataclassDTO[Client]):
    config = DTOConfig(exclude={'id'}, partial = True)