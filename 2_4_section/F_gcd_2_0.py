def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1

    return number1


def solution():
    n = int(input())
    result = int(input())

    for _ in range(n - 1):
        number = int(input())
        result = gcd(result, number)

    print(result)


if __name__ == "__main__":
    solution()
