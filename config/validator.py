from password_validator import PasswordValidator


def required(data):
    return data != ""


def validate_password(password):
    try:
        validator = PasswordValidator()
        validator.min(8).max(100).has().uppercase().has().lowercase().has().digits().has().symbols() and required(password)
        return validator.validate(password)
    except AttributeError:
        return False
