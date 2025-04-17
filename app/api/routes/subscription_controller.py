import uuid
from typing import List
from uuid import UUID

from loguru import logger
from litestar import post, get, delete, patch, Router, Controller
from litestar.dto import DTOData
from litestar.exceptions import NotFoundException, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.client import Client, WriteDTO, ReadDTO, PatchDTO
from app.api.services.client_service import ClientService
from app.api.enums.client_type import ClientType


class SubscriptionController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO

    @get("/subs")
    async def get_subs(self) -> List:
        return [
            {
                "direction": "Йога",
                "trainer": "Федоров Дьулуур",
                "period": "2 раза в неделю",
                "price": 5000
            },
            {
                "direction": "Пилатес",
                "trainer": "Захаров Вячеслав",
                "period": "3 раза в неделю",
                "price": 7000
            },
            {
                "direction": "Стретчинг",
                "trainer": "Осипов Денис",
                "period": "3 раза в неделю",
                "price": 7000
            },
        ]

    @get("/directions")
    async def get_direction(self) -> List:
        return [
            {
                "direction": "Йога"
            },
            {
                "direction": "Пилатес"
            },
            {
                "direction": "Стретчинг"
            },
        ]


sub_router = Router(path="/subs", route_handlers=[SubscriptionController])
