def solution():
    n, m = int(input()), int(input())

    for i in range(n):
        if i % 2 == 0:
            print(" ".join([f"{i * m + j:>{len(str(m * n))}}" for j in range(1, m + 1)]))
        else:
            print(" ".join([f"{i * m + j:>{len(str(m * n))}}" for j in range(1, m + 1)][::-1]))


if __name__ == "__main__":
    solution()
