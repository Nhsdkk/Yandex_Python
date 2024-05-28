import re
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, possible_chars=None, min_length=8, at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    if possible_chars is None:
        if any([not re.match("[a-zA-Z0-9]", char) for char in password]):
            raise PossibleCharError
    else:
        if any([char not in possible_chars for char in password]):
            raise PossibleCharError

    if not any([at_least_one(char) for char in password]):
        raise NeedCharError

    return sha256(password.encode('utf-8')).hexdigest()
