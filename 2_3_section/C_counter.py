def solution():
    number1, number2 = int(input()), int(input())

    print(" ".join([str(i) for i in range(number1, number2 + 1)]))


if __name__ == "__main__":
    solution()
