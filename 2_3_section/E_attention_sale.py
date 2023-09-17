def solution():
    res = 0

    while True:
        cost = float(input())

        if cost == 0:
            print(res)
            break

        if cost >= 500:
            res += cost * 0.9
        else:
            res += cost


if __name__ == "__main__":
    solution()
