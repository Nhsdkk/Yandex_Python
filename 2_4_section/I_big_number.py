def solution():
    n = int(input())

    result = ""

    for _ in range(n):
        string_number = input()
        max_digit = max(string_number)
        result += max_digit

    print(result)


if __name__ == "__main__":
    solution()
