def solution():
    length, n = int(input()), int(input())

    length -= len("...")

    for _ in range(n):
        string = input()

        if length <= 0:
            continue

        length -= len(string)

        if length < 0:
            print(f"{string[:length]}...")
        elif length > 0:
            print(string)
        else:
            print(f"{string}...")


if __name__ == "__main__":
    solution()
