def solution():
    n, m = int(input()), int(input())
    names = [input() for _ in range(n + m)]
    one_lovers = [name for name in names if names.count(name) == 1]
    print("Таких нет" if len(one_lovers) == 0 else "\n".join(sorted(one_lovers)))


if __name__ == "__main__":
    solution()