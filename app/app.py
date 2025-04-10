from loguru import logger

from litestar import Litestar, post, get, patch, put, delete
from litestar.exceptions import HTTPException
from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin

from .api.routes.auth_controller import auth_router
from .cli import cli_plugin
from .core.db.db import plugin

from .api.routes.client_controller import client_router
from .api.routes.trainer_controller import trainer_router
from .scripts.seed_client_types import seed_client_types


async def on_startup() -> None:
    await seed_client_types()


app = Litestar(route_handlers=[client_router, trainer_router, auth_router], plugins=[plugin, cli_plugin],
               on_startup=[on_startup])
