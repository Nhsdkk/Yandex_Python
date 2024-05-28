import re


class CapitalError(Exception):
    pass


class CyrillicError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    for letter in name:
        if not re.search("[а-яёА-ЯЁ]", letter):
            raise CyrillicError

    if not name[1:].islower() or not name[0].isupper():
        raise CapitalError

    return name
