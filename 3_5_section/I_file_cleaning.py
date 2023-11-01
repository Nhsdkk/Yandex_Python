def solution():
    input_file, output_file = input(), input()

    with open(input_file, "r", encoding="UTF-8") as file:
        data = [item.rstrip().lstrip() for item in file.readlines()]

    cleared_lines = []

    for item in data:
        if item == "":
            continue

        string = item

        string = string.replace("\t", "", -1)

        while "  " in string:
            string = string.replace("  ", " ")

        cleared_lines.append(string)

    with open(output_file, "w", encoding="UTF-8") as file:
        file.writelines(cleared_lines)


if __name__ == "__main__":
    solution()
