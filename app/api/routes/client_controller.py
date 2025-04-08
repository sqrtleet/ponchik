import uuid
from typing import List
from uuid import UUID

from loguru import logger
from litestar import post, get, delete, patch, Router, Controller
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.client import Client, WriteDTO, ReadDTO, PatchDTO
from app.api.services.client_service import ClientService
from app.api.enums.client_type import ClientType

client_service = ClientService()


class ClientController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post()
    async def create_client(self, data: DTOData[Client], db_session: AsyncSession) -> UUID:
        client_dto = data.create_instance()
        client = await client_service.create_from_dto(db_session, client_dto)
        return client.id

    @get("/")
    async def get_clients(self, db_session: AsyncSession) -> List[Client]:
        clients = await client_service.get_clients(db_session)
        return [
            Client(
                id=c.id,
                last_name=c.last_name,
                first_name=c.first_name,
                middle_name=c.middle_name,
                phone_number=c.phone_number,
                date_of_birth=c.date_of_birth,
                email=c.email,
                client_type=c.client_type.type if c.client_type else ClientType(c.client_type_id),
                bonus=c.bonus,
                is_active=c.is_active,
                date_became_client=c.date_became_client,
            )
            for c in clients
        ]

    @get("/{client_id:uuid}")
    async def get_client(self, client_id: UUID, db_session: AsyncSession) -> Client:
        c = await client_service.get_client(db_session, client_id)
        return Client(
            id=c.id,
            last_name=c.last_name,
            first_name=c.first_name,
            middle_name=c.middle_name,
            phone_number=c.phone_number,
            date_of_birth=c.date_of_birth,
            email=c.email,
            client_type=c.client_type.type if c.client_type else ClientType(c.client_type_id),
            bonus=c.bonus,
            is_active=c.is_active,
            date_became_client=c.date_became_client,
        )

    @patch("/{client_id:uuid}", dto=PatchDTO)
    async def update_client(self, client_id: UUID, data: DTOData[Client], db_session: AsyncSession) -> UUID:
        patch_data = data.as_builtins()
        updated = await client_service.update_client(db_session, client_id, patch_data)
        return updated.id

    @delete("/{client_id:uuid}")
    async def delete_client(self, client_id: UUID, db_session: AsyncSession) -> None:
        await client_service.delete_client(db_session, client_id)


client_router = Router(path="/clients", route_handlers=[ClientController])