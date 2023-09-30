def solution():
    result = 0

    while True:
        cost = float(input())

        if cost == 0:
            print(result)
            break

        if cost >= 500:
            result += cost * 0.9
        else:
            result += cost


if __name__ == "__main__":
    solution()
