import itertools


def solution():
    people = []

    for _ in range(int(input())):
        people.append(input())

    for item in itertools.combinations(people, r=2):
        print(" - ".join(item))


if __name__ == "__main__":
    solution()
