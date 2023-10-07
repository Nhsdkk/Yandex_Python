def solution():
    string = input()

    while string != "":
        if string[0] != "#":
            print(string.split("#")[0])

        string = input()


if __name__ == "__main__":
    solution()
