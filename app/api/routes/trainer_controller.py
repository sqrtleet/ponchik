import uuid
from typing import List
from uuid import UUID

from loguru import logger
from litestar import post, get, Router, Controller
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException, HTTPException
from litestar.status_codes import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.subscription import Subscription
from ..schemas.trainer import Trainer, WriteDTO, ReadDTO
from app.core.db.models.sqlalchemy_models import TrainerModel


class TrainerController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post()
    async def create_trainer(self, data: DTOData[Trainer], db_session: AsyncSession) -> int:
        try:
            trainer_dto = data.create_instance()
            trainer = TrainerModel(
                last_name=trainer_dto.last_name,
                first_name=trainer_dto.first_name,
                middle_name=trainer_dto.middle_name,
                phone_number=trainer_dto.phone_number,
                date_of_birth=trainer_dto.date_of_birth,
                email=trainer_dto.email,
                is_active=trainer_dto.is_active,
                date_joined_trainer=trainer_dto.date_joined_trainer,
                date_left_trainer=trainer_dto.date_left_trainer
            )
            async with db_session.begin():
                db_session.add(trainer)
            return trainer.id
        except Exception as e:
            logger.exception(e)
            raise HTTPException(detail="Error creating trainer", status_code=HTTP_400_BAD_REQUEST)

    @get('/{trainer_id:int}')
    async def get_trainer(self, trainer_id: int, db_session: AsyncSession) -> Trainer:
        result = await db_session.execute(
            select(TrainerModel).where(TrainerModel.id == trainer_id)
        )
        trainer_model = result.scalar_one_or_none()
        if not trainer_model:
            raise NotFoundException(f"Trainer with id '{trainer_id}' not found")
        return Trainer(
            id=trainer_model.id,
            last_name=trainer_model.last_name,
            first_name=trainer_model.first_name,
            middle_name=trainer_model.middle_name,
            phone_number=trainer_model.phone_number,
            date_of_birth=trainer_model.date_of_birth,
            email=trainer_model.email,
            is_active=trainer_model.is_active,
            date_joined_trainer=trainer_model.date_joined_trainer,
            date_left_trainer=trainer_model.date_left_trainer,
            abonements=[
                subscription.id
                for subscription in trainer_model.subscriptions
            ] if trainer_model.subscriptions else []
        )

    @get('/')
    async def get_trainers(self, db_session: AsyncSession) -> List[Trainer]:
        try:
            result = await db_session.execute(select(TrainerModel))
            models = result.scalars().all()
            return [
                Trainer(
                    id=model.id,
                    last_name=model.last_name,
                    first_name=model.first_name,
                    middle_name=model.middle_name,
                    phone_number=model.phone_number,
                    date_of_birth=model.date_of_birth,
                    email=model.email,
                    is_active=model.is_active,
                    date_joined_trainer=model.date_joined_trainer,
                    date_left_trainer=model.date_left_trainer,
                    abonements=[
                        subscription.id
                        for subscription in model.subscriptions
                    ] if model.subscriptions else []
                )
                for model in models
            ]
        except Exception as e:
            logger.exception(e)
            raise HTTPException(detail="Error fetching trainers", status_code=HTTP_400_BAD_REQUEST)


trainer_router = Router(path='/trainers', route_handlers=[TrainerController])
