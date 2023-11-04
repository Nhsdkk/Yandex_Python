def merge(numbers_1: tuple[int], numbers_2: tuple[int]):
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
