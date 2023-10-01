def solution():
    max_digit_summ = None
    winner = None
    n = int(input())

    for _ in range(n):
        name = input()
        number = int(input())

        digit_summ = sum([int(char) for char in str(number)])

        if max_digit_summ is None or max_digit_summ <= digit_summ:
            max_digit_summ = digit_summ
            winner = name

    print(winner)


if __name__ == "__main__":
    solution()
