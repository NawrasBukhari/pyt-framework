from secrets import token_hex
from orm.commands.Command import Command
from config.environment import set_env


class GenerateKeyCommand(Command):
    """
    Generates a new application key.

    key:generate
    """

    def handle(self):
        key = token_hex(32)
        set_env("APP_KEY", key)
        self.info("Application key set successfully.")
