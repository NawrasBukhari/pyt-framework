# PY-Template (PYT)
A very simple Python general purpose template which is being in development stage right now

# Installation
```bash
python setup.py install
```

# Quick start
### Environment variables for PYT are placed in the file `config/environment.py` and I have made a sample file named ```config/environment.example``` for you to see how it works. You can copy the file and rename it to `environment.py` and then you can change the variables to your own.
```python
import os
from colorama import Back

# Application status
APP_DEBUG = "True"
APP_ENVIRONMENT = "development"

# Database credentials
DATABASE_DRIVER = "mysql"
DATABASE_PREFIX = ""
DATABASE_HOST = "localhost"
DATABASE_NAME = "python"
DATABASE_USER = "root"
DATABASE_PASSWORD = ""
DATABASE_PORT = "3306"

# Mail credentials
MAIL_MAILER = "smtp"
MAIL_HOST = "smtp.gmail.com"
MAIL_PORT = "587"
MAIL_USERNAME = "null"
MAIL_PASSWORD = "null"
MAIL_ENCRYPTION = "TLS"
MAIL_FROM_ADDRESS = "hello@example.com"
MAIL_FROM_NAME = "PY Template"

# API credentials
API_ENDPOINT = "https://example.com/api"

os.environ["DATABASE_DRIVER"]   =   str(DATABASE_DRIVER)
os.environ["DATABASE_PREFIX"]   =   str(DATABASE_PREFIX)
os.environ["DATABASE_HOST"]     =   str(DATABASE_HOST)
os.environ["DATABASE_NAME"]     =   str(DATABASE_NAME)
os.environ["DATABASE_USER"]     =   str(DATABASE_USER)
os.environ["DATABASE_PASSWORD"] =   str(DATABASE_PASSWORD)
os.environ["DATABASE_PORT"]     =   str(DATABASE_PORT)
os.environ["MAIL_MAILER"]       =   str(MAIL_MAILER)
os.environ["MAIL_HOST"]         =   str(MAIL_HOST)
os.environ["MAIL_PORT"]         =   str(MAIL_PORT)
os.environ["MAIL_USERNAME"]     =   str(MAIL_USERNAME)
os.environ["MAIL_PASSWORD"]     =   str(MAIL_PASSWORD)
os.environ["MAIL_ENCRYPTION"]   =   str(MAIL_ENCRYPTION)
os.environ["MAIL_FROM_ADDRESS"] =   str(MAIL_FROM_ADDRESS)
os.environ["MAIL_FROM_NAME"]    =   str(MAIL_FROM_NAME)
os.environ["API_ENDPOINT"]      =   str(API_ENDPOINT)
os.environ["APP_DEBUG"]         =   str(APP_DEBUG)
os.environ["APP_ENVIRONMENT"]   =   str(APP_ENVIRONMENT)

def get_env(name):
    try:
        return os.environ[name]
    except KeyError:
        message = Back.RED + "Expected environment variable '{}' not set.".format(name)
        if is_debug() is True:
            raise Exception(message)
        else:
            exit()


def is_debug():
    return get_env("APP_DEBUG") == "True"

```
# Login process
### Login process has been implemented in this template you can refer to ```config/helpers.py``` to customize your own login process
```python
from getpass import getpass
from app.User import User
from config.helpers import login

username = input("Enter your username: ")
password = getpass("Enter your password: ")
login(model=User, user_name=username, user_password=password)
```

# Register process
### Same thing was implemented for registration process
```python
from getpass import getpass
from app.User import User
from config.helpers import register

username = input("Enter your username: ")
password = getpass("Enter your password: ")
register(model=User, user_name=username, user_password=password)
```

## How does registration works?
The register function takes 3 arguments which are ```model```, ```user_name``` and ```user_password``` so if we want to signin we have to make query to the database, the orm takes care of this step by not using the boring sql syntax's, and it deals with the database in a very simple way

```python
from config.security import hash_password
from config.validator import validate_password, required


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
```

## How does login works?
The login function takes 3 arguments which are ```model```, ```user_name``` and ```user_password``` so if we want to signin we have to make query to the database, the orm takes care of this step by not using the boring sql syntax's, and it deals with the database in a very simple way same as register function
```python
from config.security import verify_password


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
```

# Security and validation
## Password hashing
I have used argon2 since it is considered now one of the strongest password hashing algorithms libraries, it is very simple, and it generates random salt for each password which we can avoid human predictable passwords.
```python
from argon2 import PasswordHasher

def hash_password(password):
    try:
        password_hasher = PasswordHasher()
        return password_hasher.hash(password)
    except Exception as e:
        print(e)
```

## Password verification
```python
from argon2 import PasswordHasher

def verify_password(password, hashed_password):
    try:
        password_hasher = PasswordHasher()
        return password_hasher.verify(hashed_password, password)
    except Exception as e:
        print(e)
```

## Password validation
### I have made sure to use the most secure password validation rules which can be found in OWASP, you can add your custom rules in ```config/validator.py``` file
```python
from password_validator import PasswordValidator

def required(data):
    return data != ""


def validate_password(password):
    try:
        validator = PasswordValidator()
        validator.min(8).max(100).has().uppercase().has().lowercase().has().digits().has().symbols() and required(
            password)
        return validator.validate(password)
    except AttributeError:
        return False
```

# Database
### Database configuration can be found in ```config/database.py``` and it can not be changed to another directory
```python
from orm.connections import ConnectionResolver as Connection
from config.environment import get_env

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
```

# Models
### Models can be found in ```app``` directory, and they can not be changed to another directory, you can create your own models by extending the ```Model``` class, and you can use the ```Model``` class to make queries to the database for example:
```python
""" User Model """
from orm.models import Model


class User(Model):
    """User Model"""
    __table__ = 'users'
    __primary_key__ = 'id'
    __fillable__ = ['name', 'email', 'password', 'role']
    __timestamps__ = True
    __hidden__ = ['password', 'role', 'created_at', 'updated_at', 'remember_token']
```
where: </br>
```__table__``` is the name of the table in the database </br>
```__primary_key__``` is the primary key of the table the default is ```id```</br> 
```__fillable__``` is the columns that can be filled by the user </br> 
```__timestamps__``` is the columns that will be filled automatically by the orm </br> 
```__hidden__``` is the columns that will not be shown to the user </br>

# API
### You can easy implement api requests using the database by the following example
```python
from fastapi import FastAPI, responses
from config.helpers import login, register

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

```

# Generate classes
### You can setup the project by running the following commands
```
USAGE
  ORM Version: [-h] [-q] [-v [<...>]] [-V] [--ansi] [--no-ansi] [-n] <command> [<arg1>] ... [<argN>]

ARGUMENTS
  <command>              The command to execute
  <arg>                  The arguments of the command

GLOBAL OPTIONS
  -h (--help)            Display this help message
  -q (--quiet)           Do not output any message
  -v (--verbose)         Increase the verbosity of messages: "-v" for normal output, "-vv" for more verbose output and "-vvv" for debug
  -V (--version)         Display this application version
  --ansi                 Force ANSI output
  --no-ansi              Disable ANSI output
  -n (--no-interaction)  Do not ask any interactive question

AVAILABLE COMMANDS
  help                   Display the manual of a command
  migrate                Run migrations.
  migrate:refresh        Rolls back migrations and migrates them again.
  migrate:reset          Reset migrations.
  migrate:rollback       Rolls back the last batch of migrations.
  migrate:status         Display migrations status.
  migration              Creates a new migration file.
  model                  Creates a new model file.
  model:docstring        Generate model docstring and type hints (for auto-completion).
  observer               Creates a new observer file.
  seed                   Creates a new seed file.
  seed:run               Run seeds.
  shell                  Connect to your database interactive terminal.

```

# TODO
- [x] Add more database drivers
- [x] Add more database features
- [x] Add more database relations
- [x] Add more database migrations
- [ ] Add more features
- [ ] Add more tests
- [ ] Add more documentation
- [ ] Add more examples
- [ ] Add more security
- [ ] Add more validation

# License
```
MIT License
Copyright (c) 2022 Nawras Bukhari
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
```
