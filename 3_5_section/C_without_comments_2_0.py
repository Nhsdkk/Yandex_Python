from sys import stdin


def solution():
    input_lines = [line.rstrip("\n") for line in stdin.readlines()]
    for line in input_lines:
        if "#" not in line:
            print(line)
            continue

        splitted_line = line.split("#")

        if splitted_line[0] != "":
            print(splitted_line[0].rstrip())


if __name__ == "__main__":
    solution()
