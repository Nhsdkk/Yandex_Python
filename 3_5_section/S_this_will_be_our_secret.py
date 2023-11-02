def solution():
    start_alph, end_alph = ord("a"), ord("z")
    diff = int(input())

    with open("public.txt", "r") as file:
        data = file.read()

    new_chars = []

    for char in data:
        if not char.isalpha():
            new_chars.append(char)
            continue

        int_char = ord(char.lower())
        int_char += diff % (end_alph - start_alph + 1)

        if int_char < start_alph:
            int_char = end_alph - (start_alph - int_char - 1)

        if int_char > end_alph:
            int_char = start_alph + (int_char - end_alph - 1)

        print(int_char)

        if char.isupper():
            new_chars.append(chr(int_char).upper())
        else:
            new_chars.append(chr(int_char))

    with open("private.txt", "w") as file:
        file.write("".join(new_chars))


if __name__ == "__main__":
    solution()
