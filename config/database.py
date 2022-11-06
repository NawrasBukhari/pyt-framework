from orm.connections import ConnectionResolver as Connection
from .environment import env

"""
    @Author:        Nawras Bukhari
    @Description:   This script is used to get the environment variables
    @Github:        https://github.com/NawrasBukhari
    @Date:          22/Oct/2022
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  11/Nov/2022
"""

"""
    This Connect function will override the original connect function.
    it will try to prepare connection to the database.
"""

DATABASES = {
    "default": "mysql",
    "mysql": {
        "host": env("DATABASE_HOST"),
        "driver": env("DATABASE_DRIVER"),
        "database": env("DATABASE_NAME"),
        "user": env("DATABASE_USER"),
        "password": env("DATABASE_PASSWORD"),
        "port": env("DATABASE_PORT"),
        "log_queries": False,
        "strict": True,
        "engine": "InnoDB",
        "options": {

        }
    }
}

DB = Connection().set_connection_details(DATABASES)
