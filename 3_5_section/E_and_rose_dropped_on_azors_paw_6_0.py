from sys import stdin


def solution():
    input_lines = [line.rstrip("\n") for line in stdin.readlines()]
    words = []
    for line in input_lines:
        words += line.split()

    print("\n".join(sorted(set([word for word in words if word.lower() == word.lower()[::-1]]))))


if __name__ == "__main__":
    solution()
