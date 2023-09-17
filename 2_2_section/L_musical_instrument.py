def solution():
    a, b, c = int(input()), int(input()), int(input())

    if any([a + b <= c, a + c <= b, b + c <= a]):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    solution()
