def solution():
    n, m = int(input()), int(input())

    taken_from_petya, given_to_petya = 3, 2
    taken_from_vasya, given_to_vasya = 2, 5

    if n + given_to_petya - taken_from_petya > m + given_to_vasya - taken_from_vasya:
        print("Петя")
    else:
        print("Вася")


if __name__ == "__main__":
    solution()
