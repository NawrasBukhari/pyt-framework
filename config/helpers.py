import os.path

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from typing import Any
import time
import jwt
from .security import verify_password, hash_password, validate_password, required
from .environment import env
from .language import TRANSLATIONS

"""
    @Author:        Nawras Bukhari
    @Description:   This script is used to provide a quick access to another scripts
    @Github:        https://github.com/NawrasBukhari
    @Date:          24/Oct/2022
    @LastEditors:   Nawras Bukhari
    @LastEditTime:  07/Nov/2022
"""

"""
    This File() function is used to find the file path of the file.
    when you call this function, you need to pass the file name as a parameter.
    @:param file_name
    @:return file_path
"""


def File(file_name: str) -> str | Exception:
    try:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        return file_path
    except Exception as e:
        return e


"""
    This Lang() is used to get the language of the user
    @:param key
    @:param language
    @:return TRANSLATIONS[language][key]
"""


def Lang(key: str, language: str = env("APP_LANGUAGE")) -> str | None | Exception:
    try:
        if key in TRANSLATIONS[language]:
            return print(TRANSLATIONS[language][key])
    except Exception as e:
        return e


"""
    This token_response() is used to return the token to the user
    @:param token
"""


def token_response(token: str) -> dict[str, str] | Exception:
    return {
        "access_token": token
    }


"""
    This signJWT() is used to sign the JWT token
    which means creating it
    @:param user_id
    @:return token_response
    Dictionary of the user_id and the expiration time
    token_response() is called to return the token to the user
"""


def signJWT(user_id: str) -> dict[str, str] | Exception:
    try:
        payload = {
            "user_id": user_id,
            "expires": time.time() + 600
        }
        token = jwt.encode(payload=payload, key=env("APP_KEY"), algorithm=env("HS256"))

        return token_response(token)
    except Exception as e:
        return e


"""
    This decodeJWT() is used to decode the JWT token
    which means reading it
    @:param token
    @:return decoded_token
    Dictionary of the user_id and the expiration time
"""


def decodeJWT(token: str) -> Exception | None | Any:
    try:
        decoded_token = jwt.decode(jwt=token, key=env("APP_KEY"), algorithms=["HS256"])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        return e


"""
    This verify_jwt() is used to verify the JWT token
    which means checking if it is valid
    @:param token
    @:return isTokenValid
    Boolean value of the token validity
"""


def verify_jwt(token: str) -> bool:
    isTokenValid: bool = False

    try:
        payload = decodeJWT(token)
    except:
        payload = None
    if payload:
        isTokenValid = True
    return isTokenValid


"""
    This Bearer() is extending the HTTPBearer class
    which means it is inheriting from it
    @:param credentials
    @:return credentials
    @:raise HTTPException
    HTTPException is raised if the token is not valid
"""


class Bearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(Bearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        try:
            credentials: HTTPAuthorizationCredentials = await super(Bearer, self).__call__(request)
            if credentials:
                if not credentials.scheme == "Bearer":
                    raise HTTPException(status_code=403, detail=f"{Lang('Invalid scheme')}")
                if not verify_jwt(credentials.credentials):
                    raise HTTPException(status_code=403, detail=f"{Lang('Invalid token')}")
                return credentials.credentials
            else:
                raise HTTPException(status_code=403, detail=f"{Lang('Invalid auth')}")
        except HTTPException as e:
            raise e


"""
    Password must be at least 8 characters long and contain at least one number, one uppercase and one lowercase letter
    This function is used to add a new user to the database
    by calling the register function from the helpers.py file
    validation is done in the validator.py file
    @:param model
    @:param user_name
    @:param user_password
    for example:
    register(User, "John Doe", "Password123!")
"""


def register(model, user_name: str, user_password: str) -> bool | Exception:
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


def login(model, user_name: str, user_password: str) -> bool | Exception:
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


"""TODO: Add more functions"""


def update_credentials(model, user_name, user_password):
    # TODO: Update user credentials
    pass


def reset_password():
    # TODO: Reset user password
    pass


def logout():
    # TODO: Logout user
    pass
