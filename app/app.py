from litestar import Litestar
from litestar.config.cors import CORSConfig

# from .api.routes.auth_controller import auth_router
from app.utils.cli import cli_plugin
from .api.routes.bff_controller import bff_router
from .api.routes.client_subscription_controller import client_subscription_router
from .api.routes.subscription_controller import subscription_router
from .api.routes.ticket_controller import ticket_controller
from .core.db.db import plugin

from .api.routes.client_controller import client_router
from .api.routes.trainer_controller import trainer_router
from .scripts.seeds import seed_client_types, seed_statuses, seed_schedules, seed_card_types


async def on_startup() -> None:
    await seed_client_types()
    await seed_statuses()
    await seed_schedules()
    await seed_card_types()


cors_config = CORSConfig(
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    # allow_headers=["Authorization", "Content-Type"],
    allow_headers=["*"],
    allow_credentials=True
)

app = Litestar(
    route_handlers=[
        bff_router,
        client_router,
        trainer_router,
        ticket_controller,
        subscription_router,
        client_subscription_router,
    ],
    plugins=[plugin, cli_plugin],
    cors_config=cors_config,
    on_startup=[on_startup]
)
