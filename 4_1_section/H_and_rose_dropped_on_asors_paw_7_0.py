def is_palindrome(item: str):
    if type(item) is int:
        return str(item)[::-1] == str(item)

    return item[::-1] == item