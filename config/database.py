from orm.connections import ConnectionResolver as Connection

from config.environment import get_env

"""
    @Author:        Nawras Bukhari
    @Description:   This script is used to get the environment variables
    @Github:        https://github.com/NawrasBukhari
    @Date:          22/Oct/2022
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  22/Oct/2022
"""

"""
    This Connect function will override the original connect function.
    it will try to prepare connection to the database.
"""

DATABASES = {
    "default": "mysql",
    "mysql": {
        "host":     get_env("DATABASE_HOST"),
        "driver":   get_env("DATABASE_DRIVER"),
        "database": get_env("DATABASE_NAME"),
        "user":     get_env("DATABASE_USER"),
        "password": get_env("DATABASE_PASSWORD"),
        "port":     get_env("DATABASE_PORT"),
        "log_queries": False,
        "strict": True,
        "engine": "InnoDB",
        "options": {

        }
    }
}

DB = Connection().set_connection_details(DATABASES)


