import sys


def solution():
    numbers = []
    for line in sys.stdin:
        numbers += [int(item) for item in line.split()]

    print(sum(numbers))


if __name__ == "__main__":
    solution()