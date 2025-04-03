import json
import uuid
from http.client import HTTPException
from typing import Type, List, Set
from uuid import UUID

from loguru import logger

from litestar import post, get, Router, Controller
from litestar.params import Dependency
from litestar.status_codes import *
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException
from sqlalchemy import select, UUID

from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.client import *
from app.core.db.models.sqlalchemy_models import ClientModel
from ..schemas.client import Client


class ClientController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post()
    async def create_client(self, data: DTOData[Client], db_session: AsyncSession) -> set[Exception] | UUID:
        try:
            client_dto = data.create_instance()
            client = ClientModel(
                last_name=client_dto.last_name,
                first_name=client_dto.first_name,
                middle_name=client_dto.middle_name,
                phone_number=client_dto.phone_number,
                date_of_birth=client_dto.date_of_birth,
                email=client_dto.email,
                client_type_id=client_dto.client_type.value,
                bonus=client_dto.bonus,
                is_active=client_dto.is_active,
                date_became_client=client_dto.date_became_client
            )
            async with db_session.begin():
                db_session.add(client)
        except Exception as e:
            logger.error(e)
            return {e}
        return client.id

    @get('/{client_id:uuid}')
    async def get_client(self, client_id: uuid.UUID, db_session: AsyncSession) -> Client:
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
            client_type=client_model.client_type.type if client_model.client_type else ClientType(
                client_model.client_type_id),
            bonus=client_model.bonus,
            is_active=client_model.is_active,
            date_became_client=client_model.date_became_client.date()
        )

    @get('/')
    async def get_clients(self, db_session: AsyncSession) -> list[Client] | set[Exception]:
        try:
            result = await db_session.execute(select(ClientModel))
            models = result.scalars().all()
            return [
                Client(
                    id=model.id,
                    last_name=model.last_name,
                    first_name=model.first_name,
                    middle_name=model.middle_name,
                    phone_number=model.phone_number,
                    date_of_birth=model.date_of_birth,
                    email=model.email,
                    client_type=model.client_type.type if model.client_type else ClientType(model.client_type_id),
                    bonus=model.bonus,
                    is_active=model.is_active,
                    date_became_client=model.date_became_client,
                )
                for model in models
            ]
        except Exception as e:
            logger.error(e)
            return {e}


client_router = Router(path='/clients', route_handlers=[ClientController])
