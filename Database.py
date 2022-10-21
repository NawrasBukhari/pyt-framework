from colorama import Back, Style
from mysql.connector import connect, Error
from Environment import get_env

"""
@Author: Nawras Bukhari
@Description: This script is used to get the environment variables
@Github: https://github.com/NawrasBukhari
@Date: 22/Oct/2022
@LastEditors: Nawras Bukhari
@LastEditTime: 22/Oct/2022
"""


"""
This Connect function will override the original connect function.
it will try to prepare connection to the database.
"""


def Connect(host, database, user, password, port):
    try:
        return connect(
            host=host,
            database=database,
            user=user,
            passwd=password,
            port=port
        )
    except Error as e:
        print(Back.RED + f"Can't connect to the database\n{e}")
        exit(100)


"""
This Connection function is the real function which gets all credentials
from Environment then is connects to the database.
    @:param host: database host
    @:param database: database name
    @:param user: database user
    @:param password: database password
    @:param port: database port
"""


def Connection():
    return Connect(
        get_env("DATABASE_HOST"),
        get_env("DATABASE_NAME"),
        get_env("DATABASE_USER"),
        get_env("DATABASE_PASSWORD"),
        get_env("DATABASE_PORT")
    )


"""
This function will fetch data from the database using the connector.
    @:param query: the query which will be executed.
"""


def Select(query):
    try:
        connection = Connection()
        cursor = connection.cursor()
        cursor.execute(query)
        for x in cursor.fetchall():
            print(x)

    except Error as e:
        print(Back.RED + f"Error while selecting data from database!\n{e}")
        exit(101)


"""
This function will handle any operation to the database except select fetch(select) method.
    @:param query: the query which will be executed.
"""


def Query(query):
    try:
        connection = Connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(Back.GREEN + "Query executed successfully", Style.RESET_ALL)
    except Error as e:
        print(Back.RED + f"Error while executing query\n{e}")
        exit(102)
