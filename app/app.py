from loguru import logger

from litestar import Litestar, post, get, patch, put, delete
from litestar.exceptions import HTTPException

from .core.db.db import plugin

from .api.routes.client_controller import client_router
from .api.routes.trainer_controller import trainer_router

app = Litestar(route_handlers=[client_router, trainer_router], plugins=[plugin])
