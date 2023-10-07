def solution():
    n = int(input())
    cnt = 0

    for _ in range(n):
        cnt += input().count("зайка")

    print(cnt)


if __name__ == "__main__":
    solution()
