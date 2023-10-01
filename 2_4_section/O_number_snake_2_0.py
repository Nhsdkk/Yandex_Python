def solution():
    n, m = int(input()), int(input())

    for i in range(1, n + 1):
        center_value = len(str(m * n))
        numbers = []

        for j in range(m):
            number_even, number_odd = i + j * n, (j + 1) * n + 1 - i
            numbers.append(f"{number_even:>{center_value}}" if j % 2 == 0 else f"{number_odd:>{center_value}}")

        print(" ".join(numbers))


if __name__ == "__main__":
    solution()
