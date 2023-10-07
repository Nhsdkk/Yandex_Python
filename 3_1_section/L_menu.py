def solution():
    n = int(input())
    menu = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

    i = 0

    for _ in range(n):
        if i == len(menu):
            i = 0

        print(menu[i])
        i += 1


if __name__ == "__main__":
    solution()
