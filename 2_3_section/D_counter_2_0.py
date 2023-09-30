def solution():
    number1, number2 = int(input()), int(input())

    if number1 > number2:
        print(" ".join([str(i) for i in range(number2, number1 + 1)][::-1]))
    else:
        print(" ".join([str(i) for i in range(number1, number2 + 1)]))


if __name__ == "__main__":
    solution()
