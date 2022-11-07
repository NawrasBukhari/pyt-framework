from fastapi import FastAPI, responses, Depends
from app.User import User
from config.helpers import Bearer, Lang, signJWT, login, register

app = FastAPI(debug=True)


@app.post("/api/users/register", status_code=201)
async def register_users(name: str, password: str):
    if register(User, name, password) is True:
        return signJWT(name)
    else:
        return responses.Response(content=f"{Lang('Wrong password')}", status_code=400)


@app.post("/api/users/login", dependencies=[Depends(Bearer())], status_code=200)
async def login_users(name: str, password: str):
    if login(model=User, user_name=name, user_password=password) is True:
        return signJWT(name)
    else:
        return responses.JSONResponse(content=f"{Lang('Login Not Found')}", status_code=401)


# create a new user
@app.post("/api/users", status_code=201)
async def create_user(name: str, password: str):
    if register(User, name, password) is True:
        return signJWT(name)
    else:
        return responses.Response(content=f"{Lang('Wrong password')}", status_code=400)
