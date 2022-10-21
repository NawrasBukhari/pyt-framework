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
# Database credentials
DATABASE_HOST       = "localhost"
DATABASE_NAME       = "python"
DATABASE_USER       = "root"
DATABASE_PASSWORD   = ""
DATABASE_PORT       = "3306"

# Mail credentials
MAIL_MAILER         = "smtp"
MAIL_HOST           = "mailhog"
MAIL_PORT           = "1025"
MAIL_USERNAME       = "null"
MAIL_PASSWORD       = "null"
MAIL_ENCRYPTION     = "null"
MAIL_FROM_ADDRESS   = "hello@example.com"
MAIL_FROM_NAME      = "APP_NAME"

# API credentials
API_ENDPOINT = "https://example.com/api"

"""
Here we are using the os.environ dictionary to get the value of the environment variable.
If the environment variable is not set, we raise an exception.
    @see https://docs.python.org/3/library/os.html#os.environ
    @see https://docs.python.org/3/library/os.html#os.environ.get
    @see https://docs.python.org/3/library/os.html#os.environ.setdefault
"""
os.environ["DATABASE_HOST"]     =   DATABASE_HOST
os.environ["DATABASE_NAME"]     =   DATABASE_NAME
os.environ["DATABASE_USER"]     =   DATABASE_USER
os.environ["DATABASE_PASSWORD"] =   DATABASE_PASSWORD
os.environ["DATABASE_PORT"]     =   DATABASE_PORT
os.environ["MAIL_MAILER"]       =   MAIL_MAILER
os.environ["MAIL_HOST"]         =   MAIL_HOST
os.environ["MAIL_PORT"]         =   MAIL_PORT
os.environ["MAIL_USERNAME"]     =   MAIL_USERNAME
os.environ["MAIL_PASSWORD"]     =   MAIL_PASSWORD
os.environ["MAIL_ENCRYPTION"]   =   MAIL_ENCRYPTION
os.environ["MAIL_FROM_ADDRESS"] =   MAIL_FROM_ADDRESS
os.environ["MAIL_FROM_NAME"]    =   MAIL_FROM_NAME
os.environ["API_ENDPOINT"]      =   API_ENDPOINT

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
