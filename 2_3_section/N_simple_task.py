def solution():
    number = int(input())

    if number == 1:
        print("NO")
        return

    is_simple = True

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            is_simple = False
            break

    if is_simple:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solution()
