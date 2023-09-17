def solution():
    n1, n2 = int(input()), int(input())

    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1

    print(n1)


if __name__ == "__main__":
    solution()
