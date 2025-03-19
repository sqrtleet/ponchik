from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin, SQLAlchemySyncConfig
from models.sqlalchemy_models import Base

config = SQLAlchemySyncConfig(
    connection_string="sqlite:///clients.db",
    create_all=True,
    metadata=Base.metadata,
)

plugin = SQLAlchemyPlugin(config=config)
