def solution():
    number = input()

    ns = [int(char) for char in number]
    min_n, max_n = min(ns), max(ns)
    n = sum(ns) - max_n - min_n

    if max_n + min_n == n * 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solution()
