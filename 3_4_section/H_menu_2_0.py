import itertools


def solution():
    products = [input() for _ in range(int(input()))]
    end = int(input())
    for item in itertools.islice(itertools.cycle(products), end):
        print(item)


if __name__ == "__main__":
    solution()
