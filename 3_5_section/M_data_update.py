import json
import sys


def solution():
    input_data = sys.stdin.readlines()
    filename = input_data[0].rstrip("\n")

    with open(filename, "r", encoding="UTF-8") as file:
        data = json.load(file)

    for line in input_data[1:]:
        splitted_input = line.rstrip("\n").split(" == ")
        data[splitted_input[0]] = splitted_input[1]

    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    solution()
