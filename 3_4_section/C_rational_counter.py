import itertools


def solution():
    start, end, step = float(input()), float(input()), float(input())

    for i in itertools.count(start, step):
        if i > end:
            break
        print(f"{i:.2f}")


if __name__ == "__main__":
    solution()
