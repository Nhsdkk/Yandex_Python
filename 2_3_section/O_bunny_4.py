def solution():
    n = int(input())
    counter = 0

    for _ in range(n):
        string = input()

        if "зайка" in string:
            counter += 1

    print(counter)


if __name__ == "__main__":
    solution()
