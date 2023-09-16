def solution():
    arr = [int(input()), int(input()), int(input())]
    arr.sort(reverse=True)

    cos = (arr[1]**2 + arr[2]**2 - arr[0]**2) / (2 * arr[1] * arr[2])

    if cos == 0:
        print("100%")
    elif cos > 0:
        print("крайне мала")
    else:
        print("велика")


if __name__ == "__main__":
    solution()
