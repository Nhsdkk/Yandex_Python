import sys


def solution():
    input_string = [item.rstrip() for item in sys.stdin.readlines()]
    prompt = input_string[0].lower()

    result_files = []

    for input_file in input_string[1:]:
        with open(input_file, "r", encoding="UTF-8") as file:
            data = file.readlines()

        string = "".join(data)

        string = string.replace("\t", " ", -1)
        string = string.replace("\n", " ", -1)

        while "  " in string:
            string = string.replace("  ", " ")

        cleared_string = string.lower()

        if prompt in cleared_string:
            result_files.append(input_file)

    if len(result_files) == 0:
        print("404. Not Found")
    else:
        print("\n".join(result_files))


if __name__ == "__main__":
    solution()