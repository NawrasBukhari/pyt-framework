from config.helpers import login, register
from app.User import User


def login_form():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login(User, username, password)


def register_form():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    register(model=User, user_name=username, user_password=password)


if __name__ == "__main__":
    print("Welcome to the app")
    print("1. Login")
    print("2. Register")
    option = input("Enter your option: ")
    if option == "1":
        login_form()
    elif option == "2":
        register_form()
