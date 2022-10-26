from argon2 import PasswordHasher

"""
    @Author:        Nawras Bukhari
    @Description:   This script is used to get the environment variables
    @Github:        https://github.com/NawrasBukhari
    @Date:          24/Oct/2022
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  24/Oct/2022
"""

"""
    This function will be used to add security features to the application.
    hash_password() will be used to hash the password using argon2-cffi.
    for more information about argon2-cffi, visit https://argon2-cffi.readthedocs.io/en/stable/
    @:param password
    @:return hashed_password
"""


def hash_password(password):
    try:
        password_hasher = PasswordHasher()
        return password_hasher.hash(password)
    except Exception as e:
        print(e)


"""
    This function will verify the encrypted password and the password entered by the user.
    @:param password
    @:param hashed_password
    @:return True or False
"""


def verify_password(password, hashed_password):
    try:
        password_hasher = PasswordHasher()
        return password_hasher.verify(hashed_password, password)
    except Exception as e:
        print(e)
