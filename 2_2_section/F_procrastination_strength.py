def solution():
    year = int(input())

    if year % 4 != 0:
        print("NO")
        return

    if year % 100 != 0:
        print("YES")
        return

    if year % 400 == 0:
        print("YES")
        return

    print("NO")


if __name__ == "__main__":
    solution()
