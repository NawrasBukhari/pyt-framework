from password_validator import PasswordValidator

"""
    @Author:        Nawras Bukhari
    @Description:   This file is used to validate the user input
    @Github:        https://github.com/NawrasBukhari
    @Date:          24/Oct/2022
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  24/Oct/2022
"""

"""
    This function is used to enforce the user for filling any input field
    @:param data
    @:return boolean
"""


def required(data):
    return data != ""


"""
    This function is used to validate any password process
    @:param password
    @:return boolean
"""


def validate_password(password):
    try:
        validator = PasswordValidator()
        validator.min(8).max(100).has().uppercase().has().lowercase().has().digits().has().symbols() and required(
            password)
        return validator.validate(password)
    except AttributeError:
        return False
