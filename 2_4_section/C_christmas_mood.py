def solution():
    arr = [str(i) for i in range(1, int(input()) + 1)]

    end = 1

    while len(arr) != 0:
        if len(arr) < end:
            print(" ".join(arr))
            break

        print(" ".join(arr[:end]))
        end += 1
        arr = arr[end - 1:]


if __name__ == "__main__":
    solution()
