import itertools


def solution():
    people = [input() for _ in range(int(input()))]
    for item in itertools.permutations(sorted(people), r=3):
        print(", ".join(item))


if __name__ == "__main__":
    solution()
