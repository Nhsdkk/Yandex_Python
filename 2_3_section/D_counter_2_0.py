def solution():
    arr = [int(input()), int(input())]

    if arr[0] > arr[1]:
        print(" ".join([str(i) for i in range(min(arr), max(arr) + 1)][::-1]))
    else:
        print(" ".join([str(i) for i in range(min(arr), max(arr) + 1)]))


if __name__ == "__main__":
    solution()
