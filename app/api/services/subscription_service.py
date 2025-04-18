from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.exceptions import HTTPException

from app.api.services.crud_base import CRUDService
from app.core.db.models.sqlalchemy_models import SubscriptionModel
from app.api.schemas.subscription import Subscription


class SubscriptionService(CRUDService[SubscriptionModel]):
    def __init__(self):
        super().__init__(SubscriptionModel)

    async def create_from_dto(self, db: AsyncSession, dto: Subscription) -> SubscriptionModel:
        subscription = SubscriptionModel(
            direction=dto.direction,
            trainer_id=dto.trainer,
            periodicity=dto.periodicity
        )
        return await self.create(db, subscription)

    async def get_subscription(self, db: AsyncSession, subscription_id) -> SubscriptionModel:
        subscription = await self.get_by_id(db, subscription_id)
        if not subscription:
            raise HTTPException(status_code=404, detail="Subscription not found")
        return subscription

    async def get_subscriptions(self, db: AsyncSession) -> Sequence[SubscriptionModel]:
        stmt = select(self.model)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def update_subscription(self, db: AsyncSession, subscription_id, data: dict) -> SubscriptionModel:
        subscription = await self.get_subscription(db, subscription_id)
        return await self.update(db, subscription, data)

    async def delete_subscription(self, db: AsyncSession, subscription_id) -> None:
        subscription = await self.get_subscription(db, subscription_id)
        await self.delete(db, subscription)
