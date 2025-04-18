from typing import Any, Coroutine, Sequence

from sqlalchemy import Row, RowMapping, select
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.exceptions import HTTPException

from app.api.services.crud_base import CRUDService
from app.core.db.models.sqlalchemy_models import ClientSubscriptionModel
from app.api.schemas.client_subsription import ClientSubscription


class ClientSubscriptionService(CRUDService[ClientSubscriptionModel]):
    def __init__(self):
        super().__init__(ClientSubscriptionModel)

    async def create_from_dto(self, db: AsyncSession, dto: ClientSubscription) -> ClientSubscriptionModel:
        client_subscription = ClientSubscriptionModel(
            id=dto.id,
            client_id=dto.client_id,
            subscription_id=dto.subscription_id,
            schedule_id=dto.schedule_id,
            card_type_id=dto.card_type_id,
            purchase_date=dto.purchase_date,
            expiration_date=dto.expiration_date,
            status_id=dto.status_id,
        )
        return await self.create(db, client_subscription)

    async def get_client_subscription(self, db: AsyncSession, subscription_id) -> ClientSubscriptionModel:
        obj = await self.get_by_id(db, subscription_id)
        if not obj:
            raise HTTPException(status_code=404, detail="ClientSubscription not found")
        return obj

    async def get_client_subscription_by_client_id(self, db: AsyncSession, client_id) -> ClientSubscriptionModel:
        result = await db.execute(
            select(ClientSubscriptionModel).where(ClientSubscriptionModel.client_id == client_id)
        )
        obj = result.scalar_one_or_none()
        if not obj:
            raise HTTPException(status_code=404, detail="ClientSubscription not found")
        return obj

    async def get_all(self, db: AsyncSession) -> Sequence[Row[Any] | RowMapping | Any]:
        stmt = select(self.model)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def update_client_subscription(self, db: AsyncSession, subscription_id,
                                         data: dict) -> ClientSubscriptionModel:
        obj = await self.get_client_subscription(db, subscription_id)
        return await self.update(db, obj, data)

    async def delete_client_subscription(self, db: AsyncSession, subscription_id) -> None:
        obj = await self.get_client_subscription(db, subscription_id)
        await self.delete(db, obj)
