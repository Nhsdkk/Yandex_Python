def solution():
    separator = 500
    print(500)
    lowest = 0
    highest = 1001
    while True:
        inp = input()

        if inp == "Угадал!":
            break

        if inp == "Больше":
            separator, lowest = (highest - separator) // 2 + separator, separator

        if inp == "Меньше":
            separator, highest = separator - (separator - lowest) // 2, separator

        print(separator)


if __name__ == "__main__":
    solution()
