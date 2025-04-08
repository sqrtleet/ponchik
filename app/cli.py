import asyncio

from click import Group
from litestar.plugins import CLIPluginProtocol
from app.scripts.seed_client_types import seed_client_types


class CLIPlugin(CLIPluginProtocol):
    def on_cli_init(self, cli: Group) -> None:
        @cli.command()
        def seed_client_types_cmd():
            asyncio.run(seed_client_types())


cli_plugin = CLIPlugin()
