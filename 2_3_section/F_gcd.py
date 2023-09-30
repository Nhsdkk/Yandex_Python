def solution():
    number1, number2 = int(input()), int(input())

    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1

    print(number1)


if __name__ == "__main__":
    solution()
