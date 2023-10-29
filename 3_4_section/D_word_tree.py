import itertools


def solution():
    prompt = input().split()

    for i in range(len(prompt)):
        print(" ".join(prompt[:i + 1]))


if __name__ == "__main__":
    solution()
