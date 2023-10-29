import itertools


def solution():
    n = int(input())
    print("А Б В")
    for product_item in itertools.product(range(1, n - 2 + 1), repeat=3):
        if sum(product_item) == n:
            print(" ".join([str(item) for item in product_item]))


if __name__ == "__main__":
    solution()
