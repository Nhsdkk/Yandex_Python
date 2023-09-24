def solution():
    a, b, c = int(input()), int(input()), int(input())

    if a + b <= c or a + c <= b or b + c <= a:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    solution()
