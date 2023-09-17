def solution():
    arr = [int(input()), int(input())]
    print(" ".join([str(i) for i in range(min(arr), max(arr) + 1)]))


if __name__ == "__main__":
    solution()
