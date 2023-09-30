def solution():
    number = int(input())
    n1, n2, n3 = number // 100, number // 10 - (number // 100 * 10), number % 10

    min_n, max_n = min(n1, n2, n3), max(n1, n2, n3)

    sr = 0

    if (min_n == n1 and max_n == n2) or (min_n == n2 and max_n == n1):
        sr = n3
    elif (min_n == n2 and max_n == n3) or (min_n == n3 and max_n == n2):
        sr = n1
    elif (min_n == n1 and max_n == n3) or (min_n == n3 and max_n == n1):
        sr = n2

    if n1 == 0 or n2 == 0 or n3 == 0:
        print(f"{sr}{min_n} {max_n}{sr}")
    else:
        print(f"{min_n}{sr} {max_n}{sr}")


if __name__ == "__main__":
    solution()
