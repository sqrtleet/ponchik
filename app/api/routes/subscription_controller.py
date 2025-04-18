from typing import List
from uuid import UUID

from litestar import post, get, delete, patch, Router, Controller
from litestar.dto import DTOData
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services.subscription_service import SubscriptionService
from app.api.schemas.subscription import Subscription, WriteDTO, ReadDTO, PatchDTO
from app.core.db.models.sqlalchemy_models import TrainerModel

subscription_service = SubscriptionService()


class SubscriptionController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
    tags = ["SubscriptionController"]

    @post()
    async def create_subscription(self, data: DTOData[Subscription], db_session: AsyncSession) -> UUID:
        dto_obj = data.create_instance()
        sub = await subscription_service.create_from_dto(db_session, dto_obj)
        return sub.id

    @get("/")
    async def get_subscriptions(self, db_session: AsyncSession) -> List[Subscription]:
        subscriptions = await subscription_service.get_subscriptions(db_session)
        return [
            Subscription(
                id=sub.id,
                direction=sub.direction,
                periodicity=sub.periodicity,
                trainer=sub.trainer_id,
            )
            for sub in subscriptions
        ]

    @get("/{subscription_id:uuid}")
    async def get_subscription(self, subscription_id: UUID, db_session: AsyncSession) -> Subscription:
        sub = await subscription_service.get_subscription(db_session, subscription_id)
        return Subscription(
            id=sub.id,
            direction=sub.direction,
            periodicity=sub.periodicity,
            trainer=sub.trainer_id,
        )

    @patch("/{subscription_id:uuid}", dto=PatchDTO)
    async def update_subscription(self, subscription_id: UUID, data: DTOData[Subscription], db_session: AsyncSession) -> UUID:
        patch_data = data.as_builtins()
        sub = await subscription_service.update_subscription(db_session, subscription_id, patch_data)
        return sub.id

    @delete("/{subscription_id:uuid}")
    async def delete_subscription(self, subscription_id: UUID, db_session: AsyncSession) -> None:
        await subscription_service.delete_subscription(db_session, subscription_id)


subscription_router = Router(path="/subscriptions", route_handlers=[SubscriptionController])
