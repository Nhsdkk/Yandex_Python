def solution():
    n1, n2 = input(), input()
    numbers = [int(char) for char in n1] + [int(char) for char in n2]

    max_n, min_n = max(numbers), min(numbers)
    numbers.remove(max_n)
    numbers.remove(min_n)

    print(f"{max_n}{sum(numbers) % 10}{min_n}")


if __name__ == "__main__":
    solution()
