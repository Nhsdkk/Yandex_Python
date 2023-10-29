def solution():
    max_i, max_j = int(input()), int(input())
    width = len(str(max_i * max_j))
    for i in range(1, max_i * max_j + 1):
        if (i - 1) % max_j == 0 and i != 1:
            print(f"\n{' ' * (width - len(str(i)))}{i}", end=" ")
        else:
            print(f"{' ' * (width - len(str(i)))}{i}", end=" ")


if __name__ == "__main__":
    solution()
