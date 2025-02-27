from loguru import logger

from litestar import Litestar, post, get, patch, put, delete
from litestar.exceptions import HTTPException


app = Litestar(route_handlers=[])