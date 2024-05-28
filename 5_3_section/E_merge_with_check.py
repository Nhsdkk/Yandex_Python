from typing import Iterable


def merge(numbers_1, numbers_2):
    if not isinstance(numbers_1, Iterable) or not isinstance(numbers_2, Iterable):
        raise StopIteration

    for i in range(len(numbers_1)):
        if not isinstance(numbers_1[i], type(numbers_1[0])):
            raise TypeError

        if i > 0 and numbers_1[i] < numbers_1[i - 1]:
            raise ValueError

    for i in range(len(numbers_2)):
        if not isinstance(numbers_2[i], type(numbers_1[0])):
            raise TypeError

        if i > 0 and numbers_2[i] < numbers_2[i - 1]:
            raise ValueError

    numbers_1, numbers_2 = list(numbers_1), list(numbers_2)
    result = []

    while len(numbers_1) != 0 or len(numbers_2) != 0:
        if len(numbers_1) == 0:
            result.append(numbers_2.pop(0))
            continue

        if len(numbers_2) == 0:
            result.append(numbers_1.pop(0))
            continue

        if numbers_1[0] < numbers_2[0]:
            result.append(numbers_1.pop(0))
        else:
            result.append(numbers_2.pop(0))

    return tuple(result)