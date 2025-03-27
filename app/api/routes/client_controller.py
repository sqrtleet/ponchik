import json
import uuid
from http.client import HTTPException
from typing import Type, List
from loguru import logger

from litestar import post, get, Router
from litestar.params import Dependency
from litestar.status_codes import *
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.client import *
from app.core.db.models.sqlalchemy_models import ClientModel


class ClientController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post()
    async def create_client(self, data: DTOData[Client], db_session: AsyncSession) -> int:
        try:
            client_dto = data.create_instance()
            client = ClientModel(
                last_name=client_dto.last_name,
                first_name=client_dto.first_name,
                middle_name=client_dto.middle_name,
                phone_number=client_dto.phone_number,
                date_of_birth=datetime.combine(client_dto.date_of_birth,
                                               datetime.min.time()) if client_dto.date_of_birth else None,
                email=client_dto.email,
                client_type_id=client_dto.client_type.value,
                bonus=client_dto.bonus,
                is_active=client_dto.is_active,
                date_became_client=datetime.combine(client_dto.date_became_client,
                                                    datetime.min.time()) if client_dto.date_became_client else None,
            )
            async with db_session.begin():
                db_session.add(client)
        except Exception as e:
            logger.error(e)
            return HTTP_400_BAD_REQUEST
        return HTTP_201_CREATED

    @get('/{client_id:int}')
    async def get_client(self, client_id: int, db_session: AsyncSession) -> Client:
        result = await db_session.execute(
            select(ClientModel).where(ClientModel.id == client_id)
        )
        client_model = result.scalar_one_or_none()
        if not client_model:
            raise NotFoundException(f'Client with id \'{client_id}\' not found')
        return Client(
            id=client_model.id,
            last_name=client_model.last_name,
            first_name=client_model.first_name,
            middle_name=client_model.middle_name,
            phone_number=client_model.phone_number,
            date_of_birth=client_model.date_of_birth.date() if client_model.date_of_birth else None,
            email=client_model.email,
            client_type=client_model.client_type_id,
            bonus=client_model.bonus,
            is_active=client_model.is_active,
            date_became_client=client_model.date_became_client.date() if client_model.date_became_client else None,
        )

    @get('/')
    async def get_clients(self, db_session: AsyncSession) -> List[Client]:
        try:
            result = await db_session.execute(select(ClientModel))
            clients = result.scalars().all()
            return clients if isinstance(clients, list) else []
        except Exception as e:
            logger.error(e)
            return HTTP_400_BAD_REQUEST


client_router = Router(path='/clients', route_handlers=[ClientController])
