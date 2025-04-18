from typing import Any, Coroutine, Sequence

from litestar.status_codes import HTTP_404_NOT_FOUND
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.exceptions import HTTPException

from app.api.services.crud_base import CRUDService
from app.core.db.models.sqlalchemy_models import ClientModel, ClientTypeModel
from app.api.enums.client_type import ClientType
from app.api.schemas.client import Client


class ClientService(CRUDService[ClientModel]):
    def __init__(self):
        super().__init__(ClientModel)

    async def create_from_dto(self, db: AsyncSession, dto: Client) -> ClientModel:
        client_type_obj = await db.scalar(
            select(ClientTypeModel).where(ClientTypeModel.type == dto.client_type)
        )

        if not client_type_obj:
            raise HTTPException(detail="Invalid client_type", status_code=400)

        client = ClientModel(
            last_name=dto.last_name,
            first_name=dto.first_name,
            middle_name=dto.middle_name,
            phone_number=dto.phone_number,
            date_of_birth=dto.date_of_birth,
            email=dto.email,
            client_type=client_type_obj,
            bonus=dto.bonus,
            is_active=dto.is_active,
            date_became_client=dto.date_became_client
        )

        return await self.create(db, client)

    async def get_client(self, db: AsyncSession, client_id) -> ClientModel | None:
        client = await self.get_by_id(db, client_id)
        if not client:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="Not found"
            )
        return client

    async def get_clients(self, db: AsyncSession) -> Sequence[ClientModel]:
        stmt = select(self.model)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def delete_client(self, db: AsyncSession, client_id) -> None:
        client = await self.get_client(db, client_id)
        await self.delete(db, client)

    async def update_client(self, db: AsyncSession, client_id, data: dict) -> ClientModel:
        client = await self.get_client(db, client_id)
        return await self.update(db, client, data)