from uuid import uuid4
from datetime import timedelta

from litestar import Router, post
from litestar.dto import DTOData, DataclassDTO
from litestar.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from passlib.hash import bcrypt

from app.api.schemas.client import Login, TokenResponse, Client
from app.api.services.client_service import ClientService
from app.core.db.models.sqlalchemy_models import ClientModel, ClientTypeModel
from app.core.auth.jwt import create_access_token

client_service = ClientService()


@post("/register", dto=DataclassDTO[Client])
async def register(data: DTOData[Client], db_session: AsyncSession) -> dict:
    dto = data.create_instance()

    existing = await db_session.scalar(
        select(ClientModel).where(ClientModel.email == dto.email)
    )
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    client_type_obj = await db_session.scalar(
        select(ClientTypeModel).where(ClientTypeModel.type == dto.client_type)
    )
    client = ClientModel(
        last_name=dto.last_name,
        first_name=dto.first_name,
        middle_name=dto.middle_name,
        phone_number=dto.phone_number,
        date_of_birth=dto.date_of_birth,
        email=dto.email,
        hashed_password=bcrypt.hash(dto.password),
        client_type=client_type_obj,
        bonus=dto.bonus,
        is_active=dto.is_active,
        date_became_client=dto.date_became_client
    )

    db_session.add(client)
    await db_session.commit()
    token = create_access_token({"sub": str(client.id)}, expires_delta=timedelta(hours=1))
    return {"message": "User registered", "token": token}


@post("/login", dto=DataclassDTO[Login])
async def login(data: DTOData[Login], db_session: AsyncSession) -> TokenResponse:
    dto = data.create_instance()
    user = await db_session.scalar(select(ClientModel).where(ClientModel.email == dto.email))

    if not user or not bcrypt.verify(dto.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)}, expires_delta=timedelta(hours=1))
    return TokenResponse(access_token=token, token_type="bearer")


auth_router = Router(path="/auth", route_handlers=[register, login])
