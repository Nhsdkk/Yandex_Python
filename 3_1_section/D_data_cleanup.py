def solution():
    string = input()

    while string != "":
        if string[-3:] == "@@@":
            continue

        if string[:2] == "##":
            print(string[2:])
            continue

        print(string)

        string = input()


if __name__ == "__main__":
    solution()
