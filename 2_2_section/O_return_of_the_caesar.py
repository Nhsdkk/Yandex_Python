def solution():
    number1, number2 = int(input()), int(input())
    n11, n12, n21, n22 = number1 // 10, number1 % 10, number2 // 10, number2 % 10

    max_n, min_n = max(n11, n12, n21, n22), min(n11, n12, n21, n22)

    print(f"{max_n}{(n11 + n12 + n21 + n22 - max_n - min_n) % 10}{min_n}")


if __name__ == "__main__":
    solution()
