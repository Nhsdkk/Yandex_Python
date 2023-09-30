def is_simple(number):
    if number == 1:
        return False

    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False

    return True


def solution():
    n = int(input())
    counter = 0

    for _ in range(n):
        number = int(input())
        if is_simple(number):
            counter += 1

    print(counter)


if __name__ == "__main__":
    solution()
