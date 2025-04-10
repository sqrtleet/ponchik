from litestar.plugins.sqlalchemy import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig,
    AsyncSessionConfig
)
from .models.sqlalchemy_models import UUIDBase
from ..config import settings

session_config = AsyncSessionConfig(expire_on_commit=False)

config = SQLAlchemyAsyncConfig(
    connection_string=settings.database_url,
    create_all=True,
    metadata=UUIDBase.metadata,
    session_config=session_config,
)

plugin = SQLAlchemyPlugin(config=config)
