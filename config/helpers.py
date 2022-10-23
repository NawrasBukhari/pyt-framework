from config.security import verify_password, hash_password
from config.validator import validate_password, required


def login(model, user_name, user_password):
    try:
        model_class = model.where("name", user_name).first()
        name = model_class.name.replace(" ", "")
        password = model_class.password.replace(" ", "")
        if name == user_name and verify_password(password=user_password, hashed_password=password) is True:
            print("Welcome " + model_class.name)
        else:
            print("Wrong password")

    except AttributeError:
        print("These credentials do not match our records.")


def register(model, user_name, user_password):
    try:
        model_class = model.where("name", user_name).first()
        if model_class is None:
            if required(user_name) is True and required(user_password) is True:
                if validate_password(user_password) is True:
                    password = hash_password(user_password)
                    model.create({"name": user_name, "password": password})
                    print("User " + user_name + " created successfully!")

                else:
                    print(
                        "Error Password must be at least 8 characters long and contain at least one uppercase letter, "
                        "one lowercase letter, one digit and one symbol.")
            else:
                print("Error Username and password are required.")
        else:
            print("User already exists")

    except AttributeError:
        print("Error! Could not create user")


def update_credentials():
    pass
    # TODO: Update user credentials


def reset_password():
    pass
    # TODO: Reset user password


def logout():
    pass
    # TODO: Logout user
