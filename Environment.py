import os
from colorama import Back

"""
@Author: Nawras Bukhari
@Description: This script is used to get the environment variables
@Github: https://github.com/NawrasBukhari
@Date: 22/Oct/2022
@LastEditors: Nawras Bukhari
@LastEditTime: 22/Oct/2022
"""


"""
Variables that are set in the environment are available to the program.
Define what ever variables you need in the environment and then use them
in the program.
"""
DATABASE_HOST = "localhost"
DATABASE_NAME = "python"
DATABASE_USER = "root"
DATABASE_PASSWORD = ""
DATABASE_PORT = "3306"
API_ENDPOINT = "https://example.com/api"

"""
Here we are using the os.environ dictionary to get the value of the environment variable.
If the environment variable is not set, we raise an exception.
    @see https://docs.python.org/3/library/os.html#os.environ
    @see https://docs.python.org/3/library/os.html#os.environ.get
    @see https://docs.python.org/3/library/os.html#os.environ.setdefault
"""
os.environ["DATABASE_HOST"] = DATABASE_HOST
os.environ["DATABASE_NAME"] = DATABASE_NAME
os.environ["DATABASE_USER"] = DATABASE_USER
os.environ["DATABASE_PASSWORD"] = DATABASE_PASSWORD
os.environ["DATABASE_PORT"] = DATABASE_PORT
os.environ["API_ENDPOINT"] = API_ENDPOINT

"""
Here we are using the os.environ dictionary to get the value of the environment variable.
If the environment variable is not set, we raise an exception.
    @see https://docs.python.org/3/library/os.html#os.environ
    @:param name The name of the environment variable
"""


def get_env(name):
    try:
        return os.environ[name]
    except KeyError:
        message = Back.RED + "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

