from datetime import datetime
from http import HTTPStatus
from itertools import count
from dataclasses import dataclass, field

from litestar import Controller, Litestar, patch, post, put, get, patch

from litestar.status_codes import *

from litestar.dto import DataclassDTO, DTOConfig, DTOData

from ..schemas.client import *


class ClientController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post('')
    def create_client(self, data: DTOData[Client]):
        data.create_instance()
        return HTTP_201_CREATED

    @get('/clients/{client_id:int}')
    def get_client(self, client_id: int) -> Client:

