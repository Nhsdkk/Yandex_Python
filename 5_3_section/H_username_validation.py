import re


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username: str):
    for letter in username:
        if not re.search("[a-zA-z1-9_]", letter):
            raise BadCharacterError

    if re.search("[1-9]", username[0]):
        raise StartsWithDigitError

    return username
