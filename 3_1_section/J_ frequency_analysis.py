def solution():
    unique_chars = set()
    string_summ = ""

    string = input()

    if string == "ФИНИШ":
        return

    while string != "ФИНИШ":
        unique_chars.update(string.lower())
        string_summ += string.lower()
        string = input()

    max_char = ""
    max_char_amount = -1

    unique_chars.discard(" ")

    for unique_char in unique_chars:
        char_amount = string_summ.count(unique_char)
        if char_amount > max_char_amount:
            max_char_amount = char_amount
            max_char = unique_char

    print(max_char)


if __name__ == "__main__":
    solution()
