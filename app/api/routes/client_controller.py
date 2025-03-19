import json
from typing import Type

from litestar import post, get, Router

from litestar.status_codes import *

from litestar.dto import DTOData

from ..schemas.client import *

from app.core.db.models.sqlalchemy_models import ClientModel

from sqlalchemy.ext.asyncio import AsyncSession


class ClientController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post()
    async def create_client(self, data: DTOData[Client], db_session: AsyncSession) -> int:
        client = data.create_instance()
        db_session.add(ClientModel())
        await db_session.commit()
        return HTTP_201_CREATED

    @get('/{client_id:int}')
    async def get_client(self, client_id: int, db_session: AsyncSession) -> ClientModel:
        client_model = await db_session.get(ClientModel, client_id)
        if not client_model:
            from litestar.exceptions import NotFoundException
            raise NotFoundException(f'Client with id \'{client_id}\' not found')
        return client_model


client_router = Router(path='/clients', route_handlers=[ClientController])
