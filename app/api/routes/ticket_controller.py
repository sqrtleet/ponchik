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
from ...core.auth.guard import jwt_guard


class TicketController(Controller):
    dto = WriteDTO
    return_dto = ReadDTO
    guards = [jwt_guard]
    tags = ["TicketController"]

    @get("/tickets")
    async def get_ticket_types(self) -> List:
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
    async def get_directions(self) -> List:
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


ticket_controller = Router(path="/", route_handlers=[TicketController])
