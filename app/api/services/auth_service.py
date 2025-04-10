from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.db.models.sqlalchemy_models import ClientModel
from app.core.db.models.sqlalchemy_models import UserModel
from app.core.auth.jwt_utils import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    async def register(session: AsyncSession, email: str, password: str) -> str:
        hashed = pwd_context.hash(password)
        user = UserModel(email=email, hashed_password=hashed)
        session.add(user)
        await session.flush()

        client = ClientModel(user_id=user.id)
        session.add(client)
        await session.commit()

        return create_access_token({"sub": str(user.id)})

    @staticmethod
    async def login(session: AsyncSession, email: str, password: str) -> str:
        result = await session.execute(select(UserModel).where(UserModel.email == email))
        user = result.scalar_one_or_none()
        if not user or not pwd_context.verify(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        return create_access_token({"sub": str(user.id)})
