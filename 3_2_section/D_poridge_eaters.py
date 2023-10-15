def solution():
    n, m = int(input()), int(input())
    names1, names2 = set([input() for _ in range(n)]), set([input() for _ in range(m)])
    both_lovers_amount = len(names1.intersection(names2))
    print("Таких нет" if both_lovers_amount == 0 else both_lovers_amount)


if __name__ == "__main__":
    solution()
