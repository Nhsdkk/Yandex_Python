def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1

    return number1


def solution():
    numbers = [int(number) for number in input().split(" ")]
    result = None

    for number in numbers:

        if result is None:
            result = number
            continue

        result = gcd(result, number)

    print(result)


if __name__ == "__main__":
    solution()
