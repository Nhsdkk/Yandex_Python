def solution():
    number = int(input())
    n1, n2 = number // 1000, number // 100 - (number // 1000 * 10),
    n3, n4 = number // 10 - (number // 100 * 10), number % 10
    print(n2, n1, n4, n3, sep="")


if __name__ == "__main__":
    solution()
