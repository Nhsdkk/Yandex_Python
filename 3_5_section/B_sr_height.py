from sys import stdin


def solution():
    input_lines = [line.rstrip("\n") for line in stdin.readlines()]
    deltas = [int(line.split()[2]) - int(line.split()[1]) for line in input_lines]
    print(round(sum(deltas) / len(deltas)))


if __name__ == "__main__":
    solution()
