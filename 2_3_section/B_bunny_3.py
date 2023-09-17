def solution():
    cnt = 0

    while True:
        string = input()

        if string == "Приехали!":
            print(cnt)
            break

        if "зайка" in string:
            cnt += 1


if __name__ == "__main__":
    solution()
