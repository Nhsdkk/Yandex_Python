def solution():
    n, m = int(input()), int(input())
    names = [input() for _ in range(n + m)]
    one_lovers_amount = sum([1 for name in names if names.count(name) == 1])
    print("Таких нет" if one_lovers_amount == 0 else one_lovers_amount)


if __name__ == "__main__":
    solution()
