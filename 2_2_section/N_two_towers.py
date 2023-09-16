def solution():
    n = input()
    arr = [int(char) for char in n]

    arr.sort()

    if 0 in arr:
        print(f"{arr[1]}{arr[0]} {arr[2]}{arr[1]}")
    else:
        print(f"{arr[0]}{arr[1]} {arr[2]}{arr[1]}")


if __name__ == "__main__":
    solution()
