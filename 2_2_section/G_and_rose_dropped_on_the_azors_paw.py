def solution():
    number = input()

    if number == number[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solution()
