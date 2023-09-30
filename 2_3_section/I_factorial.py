def solution():
    number = int(input())

    result = 1
    for i in range(2, number + 1):
        result *= i

    print(result)


if __name__ == "__main__":
    solution()
