from loguru import logger

from litestar import Litestar, post, get, patch, put, delete
from litestar.exceptions import HTTPException

from core.db.db import plugin

from api.routes.client_controller import client_router

app = Litestar(route_handlers=[client_router], plugins=[plugin])
