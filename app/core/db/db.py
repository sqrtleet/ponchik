from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin, SQLAlchemyAsyncConfig
from .models.sqlalchemy_models import Base

config = SQLAlchemyAsyncConfig(
    connection_string="postgresql+asyncpg://test:test@localhost:5432/test",
    create_all=True,
    metadata=Base.metadata
)

plugin = SQLAlchemyPlugin(config=config)
