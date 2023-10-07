def solution():
    string = input()
    current_char = string[0]
    counter = 0

    for char in string:
        if char != current_char:
            print(f"{current_char} {counter}")
            current_char = char
            counter = 0

        counter += 1

    print(f"{current_char} {counter}")


if __name__ == "__main__":
    solution()
