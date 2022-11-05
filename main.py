from fastapi import FastAPI, responses
from .config.helpers import login, register

from app.User import User

app = FastAPI(debug=True)


@app.post("/api/users/register", status_code=201)
async def register_users(name: str, password: str):
    if register(User, name, password) is True:
        return responses.Response(content="User has been created successfully!", status_code=201)
    else:
        return responses.Response(content="Strong password needed or name is taken!", status_code=400)


@app.post("/api/users/login", status_code=200)
async def login_users(name: str, password: str):
    if login(model=User, user_name=name, user_password=password) is True:
        return responses.JSONResponse(content="Login successfully!", status_code=200)
    else:
        return responses.JSONResponse(content="These credentials do not match our records.", status_code=401)
