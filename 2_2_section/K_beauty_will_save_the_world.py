def solution():
    number = int(input())
    n1, n2, n3 = number // 100, number // 10 - (number // 100 * 10), number % 10

    min_n, max_n = min(n1, n2, n3), max(n1, n2, n3)
    n = n1 + n2 + n3 - max_n - min_n

    if max_n + min_n == n * 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solution()
