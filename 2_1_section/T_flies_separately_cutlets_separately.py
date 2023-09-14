def solution():
    n, m = int(input()), int(input())
    k1, k2 = int(input()), int(input())

    w1 = (n * (m - k2)) // (k1 - k2)
    w2 = n - w1

    print(w1, w2)


if __name__ == "__main__":
    solution()
