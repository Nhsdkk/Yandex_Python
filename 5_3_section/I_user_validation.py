import re


class CapitalError(Exception):
    pass


class CyrillicError(Exception):
    pass


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


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    for letter in name:
        if not re.search("[а-яёА-ЯЁ]", letter):
            raise CyrillicError

    if not name[1:].islower() or not name[0].isupper():
        raise CapitalError

    return name


def user_validation(last_name=None, first_name=None, username=None, **kwargs):
    if len(kwargs) != 0 or last_name is None or first_name is None or username is None:
        raise KeyError
    if not isinstance(last_name, str) or not isinstance(first_name, str) or not isinstance(username, str):
        raise TypeError

    last_name = name_validation(last_name)
    first_name = name_validation(first_name)
    username = username_validation(username)
    return {
        "last_name": last_name,
        "first_name": first_name,
        "username": username,
    }
