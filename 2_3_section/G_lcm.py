def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1

    return number1


def solution():
    number1, number2 = int(input()), int(input())
    lcm = (number1 * number2) // gcd(number1, number2)

    print(lcm)


if __name__ == "__main__":
    solution()
