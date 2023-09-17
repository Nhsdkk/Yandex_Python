def solution():
    n = int(input())

    res = 1
    for i in range(2, n + 1):
        res *= i

    print(res)


if __name__ == "__main__":
    solution()
