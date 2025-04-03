from litestar import Litestar
from litestar.plugins.sqlalchemy import (
    SQLAlchemyPlugin,
    SQLAlchemyAsyncConfig,
    AsyncSessionConfig
)
from .models.sqlalchemy_models import UUIDBase

session_config = AsyncSessionConfig(expire_on_commit=False)

config = SQLAlchemyAsyncConfig(
    connection_string="postgresql+asyncpg://test:test@localhost:5432/test",
    create_all=True,
    metadata=UUIDBase.metadata,
    session_config=session_config,
)

plugin = SQLAlchemyPlugin(config=config)
