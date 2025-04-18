import uuid
from typing import List, Any, Coroutine
from uuid import UUID

from litestar import post, get, delete, patch, Router, Controller
from litestar.dto import DTOData
from litestar.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.trainer import Trainer, WriteDTO, ReadDTO, PatchDTO
from app.api.services.trainer_service import TrainerService
from ...core.auth.guard import jwt_guard

trainer_service = TrainerService()


class TrainerController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
    tags = ["TrainerController"]
    guards = [jwt_guard]

    @post()
    async def create_trainer(self, data: DTOData[Trainer], db_session: AsyncSession) -> UUID:
        trainer_dto = data.create_instance()
        trainer = await trainer_service.create_from_dto(db_session, trainer_dto)
        return trainer.id

    @get("/")
    async def get_trainers(self, db_session: AsyncSession) -> List[Trainer]:
        trainers = await trainer_service.get_trainers(db_session)
        return [
            Trainer(
                id=t.id,
                last_name=t.last_name,
                first_name=t.first_name,
                middle_name=t.middle_name,
                phone_number=t.phone_number,
                date_of_birth=t.date_of_birth,
                email=t.email,
                is_active=t.is_active,
                date_joined_trainer=t.date_joined_trainer,
                date_left_trainer=t.date_left_trainer
            )
            for t in trainers
        ]

    @get("/{trainer_id:uuid}")
    async def get_trainer(self, trainer_id: UUID, db_session: AsyncSession) -> Trainer:
        t = await trainer_service.get_trainer(db_session, trainer_id)
        if not t:
            raise HTTPException(status_code=404)
        return Trainer(
            id=t.id,
            last_name=t.last_name,
            first_name=t.first_name,
            middle_name=t.middle_name,
            phone_number=t.phone_number,
            date_of_birth=t.date_of_birth,
            email=t.email,
            is_active=t.is_active,
            date_joined_trainer=t.date_joined_trainer,
            date_left_trainer=t.date_left_trainer
        )

    @patch("/{trainer_id:uuid}", dto=PatchDTO)
    async def update_trainer(self, trainer_id: UUID, data: DTOData[Trainer], db_session: AsyncSession) -> UUID:
        patch_data = data.as_builtins()
        trainer = await trainer_service.update_trainer(db_session, trainer_id, patch_data)
        return trainer.id

    @delete("/{trainer_id:uuid}")
    async def delete_trainer(self, trainer_id: UUID, db_session: AsyncSession) -> None:
        await trainer_service.delete_trainer(db_session, trainer_id)


trainer_router = Router(path="/trainers", route_handlers=[TrainerController])
