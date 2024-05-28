def only_positive_even_sum(item1, item2):
    if not isinstance(item1, int) or not isinstance(item2, int):
        raise TypeError
    if item1 < 0 or item2 < 0 or item1 % 2 != 0 or item2 % 2 != 0:
        raise ValueError
    return item1 + item2
