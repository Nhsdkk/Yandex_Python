def solution():
    a, b, c = int(input()), int(input()), int(input())
    distance = b - a
    print(round(distance / c, 2))


if __name__ == "__main__":
    solution()
