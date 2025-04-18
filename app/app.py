from uuid import UUID

from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.security.jwt import JWTAuth

# from .api.routes.auth_controller import auth_router
from app.utils.cli import cli_plugin
from .api.routes.auth_controller import auth_router
from .api.routes.bff_controller import bff_router
from .api.routes.client_subscription_controller import client_subscription_router
from .api.routes.subscription_controller import subscription_router
from .api.routes.ticket_controller import ticket_controller
from .api.services.client_service import ClientService
from .core.config import settings
from .core.db.db import plugin

from .api.routes.client_controller import client_router
from .api.routes.trainer_controller import trainer_router
from .scripts.seeds import seed_client_types, seed_statuses, seed_schedules, seed_card_types
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.spec import SecurityScheme, Components


async def on_startup() -> None:
    await seed_client_types()
    await seed_statuses()
    await seed_schedules()
    await seed_card_types()


openapi_config = OpenAPIConfig(
    title="Ponchik API",
    version="1.0.0",
    security=[{"BearerAuth": []}],
    components=Components(
        security_schemes={
            "BearerAuth": SecurityScheme(
                type="http",
                scheme="bearer",
                bearer_format="JWT",
                description="Enter your JWT token like: Bearer <token>"
            )
        }
    )
)
cors_config = CORSConfig(
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    # allow_headers=["Authorization", "Content-Type"],
    allow_headers=["*"],
    allow_credentials=True
)

client_service = ClientService()


async def retrieve_user(token, connection):
    # токен.sub — строковый UUID
    return await client_service.get_client(UUID(token.sub))


# jwt_auth = JWTAuth(
#     token_secret=settings.jwt_secret,  # секрет кодирования JWT
#     retrieve_user_handler=retrieve_user,  # как достать пользователя из токена
#     exclude=[
#         r"^/schema",
#         r"^/docs",
#         r"^/swagger",
#         r"^/auth"
#     ],
# )

app = Litestar(
    route_handlers=[
        bff_router,
        auth_router,
        client_router,
        trainer_router,
        ticket_controller,
        subscription_router,
        client_subscription_router,
    ],
    # middleware=[jwt_auth.middleware],
    plugins=[plugin, cli_plugin],
    cors_config=cors_config,
    openapi_config=openapi_config,
    on_startup=[on_startup]
)
