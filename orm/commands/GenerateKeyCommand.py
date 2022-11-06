from secrets import token_hex
from orm.commands.Command import Command
from config.helpers import find_file


class GenerateKeyCommand(Command):

    """
    Generates a new application key.

    key:generate
    """
    def handle(self):
        old: str = "APP_KEY = "
        new: str = f'APP_KEY = "{token_hex(32)}"\n'
        file_path = find_file("environment.py")
        with open(file_path, "r") as file:
            data = file.readlines()
            for i, line in enumerate(data):
                if old in line:
                    data[i] = new
        with open(file_path, "w") as file:
            file.writelines(data)
        self.info("Application key generated successfully.")

