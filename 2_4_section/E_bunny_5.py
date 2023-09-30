def solution():
    n = int(input())
    bunny_counter = 0

    for _ in range(n):
        string = input()
        has_bunny = False
        while string != "ВСЁ":
            if string == "зайка":
                has_bunny = True

            string = input()

        if has_bunny:
            bunny_counter += 1

    print(bunny_counter)


if __name__ == "__main__":
    solution()
