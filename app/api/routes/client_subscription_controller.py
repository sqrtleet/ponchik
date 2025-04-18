from typing import List, Any, Coroutine
from uuid import UUID

from litestar import post, get, delete, patch, Router, Controller
from litestar.dto import DTOData
from litestar.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services.client_subscription_service import ClientSubscriptionService
from app.api.schemas.client_subsription import ClientSubscription, WriteDTO, ReadDTO, PatchDTO
from app.core.auth.guard import jwt_guard

client_subscription_service = ClientSubscriptionService()


class ClientSubscriptionController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
    guards = [jwt_guard]
    tags = ["ClientSubscriptionController"]

    @post()
    async def create(self, data: DTOData[ClientSubscription], db_session: AsyncSession) -> UUID:
        dto_obj = data.create_instance()
        result = await client_subscription_service.create_from_dto(db_session, dto_obj)
        return result.id

    @get("/")
    async def get_subscriptions(self, db_session: AsyncSession) -> List[ClientSubscription]:
        records = await client_subscription_service.get_all(db_session)
        return [
            ClientSubscription(
                id=record.id,
                client_id=record.client_id,
                subscription_id=record.subscription_id,
                schedule_id=record.schedule_id,
                card_type_id=record.card_type_id,
                purchase_date=record.purchase_date,
                expiration_date=record.expiration_date,
                status_id=record.status_id,
            )
            for record in records

        ]

    @get("/{record_id:uuid}")
    async def get_subscription(self, record_id: UUID, db_session: AsyncSession) -> ClientSubscription | None:
        record = await client_subscription_service.get_client_subscription(db_session, record_id)
        if not record:
            raise HTTPException(status_code=404)
        return ClientSubscription(
            id=record.id,
            client_id=record.client_id,
            subscription_id=record.subscription_id,
            schedule_id=record.schedule_id,
            card_type_id=record.card_type_id,
            purchase_date=record.purchase_date,
            expiration_date=record.expiration_date,
            status_id=record.status_id,
        )

    @get("/{client_id:uuid}")
    async def get_subscription_by_client_id(self, client_id: UUID, db_session: AsyncSession) -> ClientSubscription:
        record = await client_subscription_service.get_client_subscription_by_client_id(db_session, client_id)
        return ClientSubscription(
            id=record.id,
            client_id=record.client_id,
            subscription_id=record.subscription_id,
            schedule_id=record.schedule_id,
            card_type_id=record.card_type_id,
            purchase_date=record.purchase_date,
            expiration_date=record.expiration_date,
            status_id=record.status_id,
        )

    @patch("/{record_id:uuid}", dto=PatchDTO)
    async def update_client_subscription(self, record_id: UUID, data: DTOData[ClientSubscription], db_session: AsyncSession) -> UUID:
        patch_data = data.as_builtins()
        obj = await client_subscription_service.update_client_subscription(db_session, record_id, patch_data)
        return obj.id

    @delete("/{record_id:uuid}")
    async def delete_client_subscription(self, record_id: UUID, db_session: AsyncSession) -> None:
        await client_subscription_service.delete_client_subscription(db_session, record_id)


client_subscription_router = Router(path="/client-subscriptions", route_handlers=[ClientSubscriptionController])
