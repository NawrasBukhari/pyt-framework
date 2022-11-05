import os
from colorama import Back

"""
    @Author:        Nawras Bukhari
    @Description:   This script is used to get the environment variables
    @Github:        https://github.com/NawrasBukhari
    @Date:          22/Oct/2022
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  27/Oct/2022
"""

"""
    Variables that are set in the environment are available to the program.
    Define what ever variables you need in the environment and then use them
    in the program.
"""
# Application status
APP_DEBUG = "True"
APP_ENVIRONMENT = "development"

# Database credentials
DATABASE_DRIVER = "mysql"
DATABASE_PREFIX = ""
DATABASE_HOST = "localhost"
DATABASE_NAME = "api"
DATABASE_USER = "root"
DATABASE_PASSWORD = ""
DATABASE_PORT = "3306"

# Mail credentials
MAIL_MAILER = "smtp"
MAIL_HOST = "smtp.gmail.com"
MAIL_PORT = "587"
MAIL_USERNAME = "null"
MAIL_PASSWORD = "null"
MAIL_ENCRYPTION = "TLS"
MAIL_FROM_ADDRESS = "hello@example.com"
MAIL_FROM_NAME = "PY Template"

# API credentials
API_ENDPOINT = "https://example.com/api"

"""
    Here we are using the os.environ dictionary to get the value of the environment variable.
    If the environment variable is not set, we raise an exception.
    @see https://docs.python.org/3/library/os.html#os.environ
    @see https://docs.python.org/3/library/os.html#os.environ.get
    @see https://docs.python.org/3/library/os.html#os.environ.setdefault
"""
os.environ["DATABASE_DRIVER"] = str(DATABASE_DRIVER)
os.environ["DATABASE_PREFIX"] = str(DATABASE_PREFIX)
os.environ["DATABASE_HOST"] = str(DATABASE_HOST)
os.environ["DATABASE_NAME"] = str(DATABASE_NAME)
os.environ["DATABASE_USER"] = str(DATABASE_USER)
os.environ["DATABASE_PASSWORD"] = str(DATABASE_PASSWORD)
os.environ["DATABASE_PORT"] = str(DATABASE_PORT)
os.environ["MAIL_MAILER"] = str(MAIL_MAILER)
os.environ["MAIL_HOST"] = str(MAIL_HOST)
os.environ["MAIL_PORT"] = str(MAIL_PORT)
os.environ["MAIL_USERNAME"] = str(MAIL_USERNAME)
os.environ["MAIL_PASSWORD"] = str(MAIL_PASSWORD)
os.environ["MAIL_ENCRYPTION"] = str(MAIL_ENCRYPTION)
os.environ["MAIL_FROM_ADDRESS"] = str(MAIL_FROM_ADDRESS)
os.environ["MAIL_FROM_NAME"] = str(MAIL_FROM_NAME)
os.environ["API_ENDPOINT"] = str(API_ENDPOINT)
os.environ["APP_DEBUG"] = str(APP_DEBUG)
os.environ["APP_ENVIRONMENT"] = str(APP_ENVIRONMENT)
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
        if is_debug() is True:
            raise Exception(message)
        else:
            exit()


def is_debug():
    return get_env("APP_DEBUG") == "True"
