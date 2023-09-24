def solution():
    number = int(input())

    n1, n2 = number // 1000, number // 100 - (number // 1000 * 10),
    n3, n4 = number // 10 - (number // 100 * 10), number % 10

    if n1 == n4 and n2 == n3:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solution()
