def solution():
    sep = 500
    print(500)
    lowest = 0
    highest = 1001
    while True:
        inp = input()

        if inp == "Угадал!":
            break

        if inp == "Больше":
            sep, lowest = (highest - sep) // 2 + sep, sep

        if inp == "Меньше":
            sep, highest = sep - (sep - lowest) // 2, sep

        print(sep)


if __name__ == "__main__":
    solution()
