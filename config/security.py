from argon2 import PasswordHasher


def hash_password(password):
    try:
        password_hasher = PasswordHasher()
        return password_hasher.hash(password)
    except Exception as e:
        print(e)


def verify_password(password, hashed_password):
    try:
        password_hasher = PasswordHasher()
        return password_hasher.verify(hashed_password, password)
    except Exception as e:
        print(e)
