def solution():
    n = int(input())
    result = 0

    for _ in range(n):
        number = int(input())
        for i in range(0, len(str(number))):
            digit = (number // 10**i) - (number // 10**(i + 1)) * 10
            result += digit

    print(result)


if __name__ == "__main__":
    solution()
