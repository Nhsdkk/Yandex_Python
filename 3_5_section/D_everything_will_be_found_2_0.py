from sys import stdin


def solution():
    input_lines = [line.rstrip("\n") for line in stdin.readlines()]
    search_item = input_lines[-1]

    print("\n".join([item for item in input_lines[:-1] if search_item.lower() in item.lower()]))


if __name__ == "__main__":
    solution()
