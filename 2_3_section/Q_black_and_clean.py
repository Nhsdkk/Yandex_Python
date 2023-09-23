def solution():
    string = input()
    print(''.join([char for char in string if int(char) % 2 != 0]))


if __name__ == "__main__":
    solution()
