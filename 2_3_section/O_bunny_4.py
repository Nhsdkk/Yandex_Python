def solution():
    n = int(input())
    cnt = 0

    for _ in range(n):
        string = input()

        if "зайка" in string:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    solution()
