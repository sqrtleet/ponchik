from itertools import count
from dataclasses import dataclass, field


from litestar.dto import DataclassDTO, DTOConfig


from app.api.schemas.client_subsription import ClientSubsriptions

@dataclass

class RemainingSessions:
    id: int = field(init=False, default_factory=count().__next__)
    client_subsription_id: ClientSubsriptions = field(default = None)
    sessions_remaining: int = field(default = None)
    lust_update: str = field(default = None)


class WriteDTO(DataclassDTO[RemainingSessions]):
    config = DTOConfig(exclude = {'id'})


class ReadDTO(DataclassDTO[RemainingSessions]):
    config = DTOConfig(exclude = {''})


class PatchDTO(DataclassDTO[RemainingSessions]):
    config = DTOConfig(exclude={'id'}, partial = True)
