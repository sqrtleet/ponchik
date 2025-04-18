import asyncio

from click import Group
from litestar.plugins import CLIPluginProtocol
from app.scripts.seeds import seed_client_types, seed_statuses, seed_schedules, seed_card_types


class CLIPlugin(CLIPluginProtocol):
    def on_cli_init(self, cli: Group) -> None:
        @cli.command()
        def seed_client_types_cmd():
            asyncio.run(seed_client_types())

        @cli.command()
        def seed_statuses_cmd():
            asyncio.run(seed_statuses())

        @cli.command()
        def seed_schedules_cmd():
            asyncio.run(seed_schedules())

        @cli.command()
        def seed_card_types_cmd():
            asyncio.run(seed_card_types())


cli_plugin = CLIPlugin()
