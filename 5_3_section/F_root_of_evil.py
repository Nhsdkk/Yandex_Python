class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if a == b == c == 0:
        raise InfiniteSolutionsError

    if a == b == 0 and c != 0:
        raise NoSolutionsError
    elif a == b == 0 and c == 0:
        raise InfiniteSolutionsError

    if a == 0:
        return -c / b

    d = b ** 2 - 4 * a * c

    if d < 0:
        raise NoSolutionsError

    a1 = (-b + (d ** 0.5)) / (2 * a)
    a2 = (-b - (d ** 0.5)) / (2 * a)

    if a1 == a2:
        return a1, a1
    else:
        res1, res2 = a1, a2
        return min(res1, res2), max(res1, res2)
