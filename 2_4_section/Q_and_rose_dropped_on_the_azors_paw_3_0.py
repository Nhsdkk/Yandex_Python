def solution():
    counter = 0

    for _ in range(int(input())):
        string = input()

        if string == string[::-1]:
            counter += 1

    print(counter)


if __name__ == "__main__":
    solution()
