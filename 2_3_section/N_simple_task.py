def solution():
    n = int(input())

    if n == 1:
        print("NO")
        return

    is_simple = True

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_simple = False
            break

    if is_simple:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solution()
