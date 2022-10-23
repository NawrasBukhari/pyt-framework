from argon2 import PasswordHasher


def hash_password(password):
    password_hasher = PasswordHasher()
    return password_hasher.hash(password)


def verify_password(password, hashed_password):
    password_hasher = PasswordHasher()
    return password_hasher.verify(hashed_password, password)
