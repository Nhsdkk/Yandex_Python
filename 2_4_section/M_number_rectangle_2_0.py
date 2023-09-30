def solution():
    n, m = int(input()), int(input())

    for i in range(1, n + 1):
        print(" ".join([f"{i + j * n:>{len(str(m * n))}}" for j in range(m)]))


if __name__ == "__main__":
    solution()
