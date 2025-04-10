from litestar import post, Controller, Router
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.exceptions import HTTPException

from app.api.services.auth_service import AuthService
from app.api.schemas.auth import RegisterDTO, LoginDTO

auth_service = AuthService()


class AuthController(Controller):
    @post("/register")
    async def register(self, data: RegisterDTO, db_session: AsyncSession) -> dict:
        try:
            token = await auth_service.register(db_session, data.email, data.password)
            return {"access_token": token, "token_type": "bearer"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @post("/login")
    async def login(self, data: LoginDTO, db_session: AsyncSession) -> dict:
        try:
            token = await auth_service.login(db_session, data.email, data.password)
            return {"access_token": token, "token_type": "bearer"}
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid credentials")


auth_router = Router(path="/auth", route_handlers=[AuthController])
