import os
from pathlib import Path

"""
    @Author:        Nawras Bukhari
    @Description:   This script is used to get the environment variables
    @Github:        https://github.com/NawrasBukhari
    @Date:          22/Oct/2022
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  11/Nov/2022
"""

"""
    This env() function is used to get the value of the environment variable.
    when you call this function, you need to pass the key as a parameter.
    @:param key
    @:return value
"""


# add default parameter for the env() function
def env(key: str, ROOT_DIR=Path(__file__).parent.parent, env_file=".env"):
    try:
        env_file = os.path.join(ROOT_DIR, env_file)
        with open(env_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if key in line:
                    value = line.replace('"', "").replace(" ", "").replace("\n", "")
                    return value.split("=")[1]

            raise Exception(f"{key} environment variable is not set.")

    except Exception as e:
        return e


"""
    This set_env() function is used to set the value of the environment variable.
    when you call this function, you need to pass the key and value as a parameter.
    @:param key
    @:param value
    return True
"""


def set_env(key: str, value: str, ROOT_DIR=Path(__file__).parent.parent, env_file=".env"):
    try:
        env_file = os.path.join(ROOT_DIR, env_file)
        with open(env_file, "r") as file:
            lines = file.readlines()
            with open(env_file, "w") as file:
                for line in lines:
                    if key in line:
                        line = f'{key}="{value}"\n'
                    file.write(line)

    except Exception as e:
        return e


""" This is_debug() function is used to check if the application is in debug mode. """


def is_debug():
    return env("APP_DEBUG") == "True"
