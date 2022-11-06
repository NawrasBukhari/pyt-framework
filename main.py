from fastapi import FastAPI, responses, Depends
from app.User import User
from config.helpers import Bearer, signJWT, login, register

app = FastAPI(debug=True)


@app.post("/api/users/register", status_code=201)
async def register_users(name: str, password: str):
    if register(User, name, password) is True:
        return signJWT(name)
    else:
        return responses.Response(content="Strong password needed or name is taken!", status_code=400)


@app.post("/api/users/login", dependencies=[Depends(Bearer())], status_code=200)
async def login_users(name: str, password: str):
    if login(model=User, user_name=name, user_password=password) is True:
        return signJWT(name)
    else:
        return responses.JSONResponse(content="These credentials do not match our records or no token was found!",
                                      status_code=401)
