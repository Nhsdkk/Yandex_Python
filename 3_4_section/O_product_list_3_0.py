import itertools


def solution():
    products = []

    for _ in range(int(input())):
        products += input().split(", ")

    for item in itertools.permutations(sorted(products), r=3):
        print(" ".join(item))


if __name__ == "__main__":
    solution()
