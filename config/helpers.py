from .security import verify_password, hash_password
from .validator import validate_password, required

"""
    @Author:        Nawras Bukhari
    @Description:   This script is used to get the environment variables
    @Github:        https://github.com/NawrasBukhari
    @Date:          24/Oct/2024
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  06/Nov/2022
"""

"""
    ** Password must be at least 8 characters long and contain at least one number, one uppercase and one lowercase letter **
    This function is used to add a new user to the database
    by calling the register function from the helpers.py file
    validation is done in the validator.py file
    @:param model
    @:param user_name
    @:param user_password
    for example:
    register(User, "John Doe", "Password123!")
"""


def register(model, user_name, user_password):
    try:
        model_class = model.where("name", user_name).first()
        if model_class is None:

            if required(user_name) is True and required(user_password) is True:

                if validate_password(user_password) is True:
                    password = hash_password(user_password)
                    model.create({"name": user_name, "password": password})
                    return True

                else:
                    return False
            else:
                return False
        else:
            return False

    except AttributeError:
        return False


"""
    This function is used to login user to the application
    by calling the login function from the helpers.py file
    validation is done in the validator.py file
    @:param model
    @:param user_name
    @:param user_password
    for example:
    login(User, "John Doe", "Password123!")
"""


def login(model, user_name, user_password):
    try:
        model_class = model.where("name", user_name).first()
        name = model_class.name.replace(" ", "")
        password = model_class.password.replace(" ", "")

        if name == user_name and verify_password(password=user_password, hashed_password=password) is True:
            return True
        else:
            return False

    except AttributeError:
        return False



def update_credentials(model, user_name, user_password):
    # TODO: Update user credentials
    pass



def reset_password():
    # TODO: Reset user password
    pass


def logout():
    # TODO: Logout user
    pass
