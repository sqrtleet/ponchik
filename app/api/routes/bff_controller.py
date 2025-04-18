from typing import Any, Annotated
from uuid import UUID
from litestar import get, Router, Controller, Request
from litestar.connection import ASGIConnection
from litestar.di import Provide
from litestar.exceptions import HTTPException
from litestar.params import Dependency
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.enums.client_type import ClientType
from app.api.enums.subscription_status import SubscriptionStatusType
from app.api.schemas.bff_model import BFFResponse
from app.api.schemas.client import Client
from app.api.schemas.client_subsription import ClientSubscription
from app.api.schemas.schedule import Schedule
from app.api.schemas.subscription import Subscription
from app.api.schemas.trainer import Trainer
from app.api.schemas.status import Status
from app.api.schemas.сard_types import CardTypes
from app.api.services.client_service import ClientService
from app.api.services.client_subscription_service import ClientSubscriptionService
from app.api.services.subscription_service import SubscriptionService
from app.api.services.trainer_service import TrainerService
from app.core.auth.guard import jwt_guard
from app.core.db.models.sqlalchemy_models import ScheduleModel, StatusModel, CardTypeModel

client_subscription_service = ClientSubscriptionService()
subscription_service = SubscriptionService()
client_service = ClientService()
trainer_service = TrainerService()


class BFFController(Controller):
    tags = ["BFFController"]

    @get("/info")
    async def get_client(
            self,
            db_session: AsyncSession,
            client_id: UUID
    ) -> BFFResponse:
        # user = request.user
        # if not user:
        #     raise HTTPException(status_code=401, detail="Unauthorized")
        #
        # client_id: UUID = user.id

        client_record = await client_service.get_client(db_session, client_id)
        client = Client(
            id=client_record.id,
            last_name=client_record.last_name,
            first_name=client_record.first_name,
            middle_name=client_record.middle_name,
            phone_number=client_record.phone_number,
            date_of_birth=client_record.date_of_birth,
            email=client_record.email,
            client_type=client_record.client_type.type if client_record.client_type else ClientType(
                client_record.client_type_id),
            bonus=client_record.bonus,
            is_active=client_record.is_active,
            date_became_client=client_record.date_became_client,
        )

        client_sub_record = await client_subscription_service.get_client_subscription_by_client_id(db_session,
                                                                                                   client.id)
        client_sub = ClientSubscription(
            id=client_sub_record.id,
            client_id=client_sub_record.client_id,
            subscription_id=client_sub_record.subscription_id,
            schedule_id=client_sub_record.schedule_id,
            card_type_id=client_sub_record.card_type_id,
            purchase_date=client_sub_record.purchase_date,
            expiration_date=client_sub_record.expiration_date,
            status_id=client_sub_record.status_id,
        )

        sub_record = await subscription_service.get_subscription(db_session, client_sub.subscription_id)
        sub = Subscription(
            id=sub_record.id,
            direction=sub_record.direction,
            periodicity=sub_record.periodicity,
            trainer=sub_record.trainer_id,
        )

        trainer_record = await trainer_service.get_trainer(db_session, sub.trainer)
        trainer = Trainer(
            id=trainer_record.id,
            last_name=trainer_record.last_name,
            first_name=trainer_record.first_name,
            middle_name=trainer_record.middle_name,
            phone_number=trainer_record.phone_number,
            date_of_birth=trainer_record.date_of_birth,
            email=trainer_record.email,
            is_active=trainer_record.is_active,
            date_joined_trainer=trainer_record.date_joined_trainer,
            date_left_trainer=trainer_record.date_left_trainer
        )

        schedule_record = await db_session.scalar(
            select(ScheduleModel).where(ScheduleModel.id == client_sub.schedule_id)
        )
        schedule = Schedule(
            id=schedule_record.id,
            day_name=schedule_record.day_name
        )

        status_record = await db_session.scalar(
            select(StatusModel).where(StatusModel.id == client_sub.status_id)
        )
        status = Status(
            id=status_record.id,
            type=SubscriptionStatusType(1)
        )

        card_type_record = await db_session.scalar(
            select(CardTypeModel).where(CardTypeModel.id == client_sub.card_type_id)
        )
        card_type = CardTypes(
            id=card_type_record.id,
            name=card_type_record.name,
            price=card_type_record.price,
        )

        result = BFFResponse(
            client=client,
            subscription=sub,
            trainer=trainer,
            client_subscription=client_sub,
            schedule=schedule,
            card_type=card_type,
            status=status
        )
        return result


bff_router = Router(path="/bff", route_handlers=[BFFController])
