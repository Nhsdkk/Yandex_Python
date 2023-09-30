def solution():
    max_number, width = int(input()), int(input())

    for i in range(1, max_number + 1):
        if i == 1:
            string = "|".join([f"{j:^{width}}" for j in range(1, max_number + 1)])
            print(string)
            if i != max_number:
                print("-" * len(string))
            continue

        string = "|".join([f"{i * j:^{width}}" for j in range(1, max_number + 1)])

        print(string)

        if i != max_number:
            print("-" * len(string))


if __name__ == "__main__":
    solution()
