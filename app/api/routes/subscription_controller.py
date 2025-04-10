import json
import uuid
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

from app.api.schemas.subscription import Subscription, WriteDTO, ReadDTO
from app.core.db.models.sqlalchemy_models import SubscriptionModel, TrainerModel
from app.api.schemas.trainer import Trainer

class SubscriptionController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @post()
    async def create_subscription(self, data: DTOData[Subscription], db_session: AsyncSession) -> int | Set[Exception]:
        try:
            subscription_dto = data.create_instance()
            trainer_id = subscription_dto.trainer.id
            trainer_result = await db_session.execute(select(TrainerModel).where(TrainerModel.id == trainer_id))
            trainer_model = trainer_result.scalar_one_or_none()

            if not trainer_model:
                raise NotFoundException(f"Trainer with id '{trainer_id}' not found")

            subscription = SubscriptionModel(
                direction=subscription_dto.direction,
                trainer=trainer_model,
                periodicity=subscription_dto.periodicity
            )

            async with db_session.begin():
                db_session.add(subscription)

        except Exception as e:
            logger.error(e)
            return {e}

        return subscription.id

    @get('/{subscription_id:int}')
    async def get_subscription(self, subscription_id: int, db_session: AsyncSession) -> Subscription:
        result = await db_session.execute(
            select(SubscriptionModel).where(SubscriptionModel.id == subscription_id)
        )
        subscription_model = result.scalar_one_or_none()
        if not subscription_model:
            raise NotFoundException(f'Subscription with id \'{subscription_id}\' not found')

        return Subscription(
            id=subscription_model.id,
            direction=subscription_model.direction,
            periodicity=subscription_model.periodicity,
            trainer=Trainer(
                id=subscription_model.trainer.id,
                last_name=subscription_model.trainer.last_name,
                first_name=subscription_model.trainer.first_name,
                middle_name=subscription_model.trainer.middle_name,
                phone_number=subscription_model.trainer.phone_number,
                date_of_birth=subscription_model.trainer.date_of_birth,
                email=subscription_model.trainer.email,
                is_active=subscription_model.trainer.is_active,
                date_joined_trainer=subscription_model.trainer.date_joined_trainer,
                date_left_trainer=subscription_model.trainer.date_left_trainer
            )
        )

    @get('/')
    async def get_subscriptions(self, db_session: AsyncSession) -> List[Subscription] | Set[Exception]:
        try:
            result = await db_session.execute(select(SubscriptionModel))
            subscriptions = result.scalars().all()

            return [
                Subscription(
                    id=sub.id,
                    direction=sub.direction,
                    periodicity=sub.periodicity,
                    trainer=Trainer(
                        id=sub.trainer.id,
                        last_name=sub.trainer.last_name,
                        first_name=sub.trainer.first_name,
                        middle_name=sub.trainer.middle_name,
                        phone_number=sub.trainer.phone_number,
                        date_of_birth=sub.trainer.date_of_birth,
                        email=sub.trainer.email,
                        is_active=sub.trainer.is_active,
                        date_joined_trainer=sub.trainer.date_joined_trainer,
                        date_left_trainer=sub.trainer.date_left_trainer
                    )
                )
                for sub in subscriptions
            ]

        except Exception as e:
            logger.error(e)
            return {e}


subscription_router = Router(path='/subscriptions', route_handlers=[SubscriptionController])
