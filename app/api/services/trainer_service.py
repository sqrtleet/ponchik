from typing import Any, Coroutine, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.exceptions import HTTPException

from app.api.services.crud_base import CRUDService
from app.core.db.models.sqlalchemy_models import TrainerModel
from app.api.schemas.trainer import Trainer


class TrainerService(CRUDService[TrainerModel]):
    def __init__(self):
        super().__init__(TrainerModel)

    async def create_from_dto(self, db: AsyncSession, dto: Trainer) -> TrainerModel:
        trainer = TrainerModel(
            last_name=dto.last_name,
            first_name=dto.first_name,
            middle_name=dto.middle_name,
            phone_number=dto.phone_number,
            date_of_birth=dto.date_of_birth,
            email=dto.email,
            is_active=dto.is_active,
            date_joined_trainer=dto.date_joined_trainer,
            date_left_trainer=dto.date_left_trainer
        )
        return await self.create(db, trainer)

    async def get_trainer(self, db: AsyncSession, trainer_id) -> TrainerModel | None:
        trainer = await self.get_by_id(db, trainer_id)
        if not trainer:
            return None
        return trainer

    async def get_trainers(self, db: AsyncSession) -> Sequence[TrainerModel]:
        stmt = select(self.model)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def update_trainer(self, db: AsyncSession, trainer_id, data: dict) -> TrainerModel:
        trainer = await self.get_trainer(db, trainer_id)
        return await self.update(db, trainer, data)

    async def delete_trainer(self, db: AsyncSession, trainer_id) -> None:
        trainer = await self.get_trainer(db, trainer_id)
        await self.delete(db, trainer)