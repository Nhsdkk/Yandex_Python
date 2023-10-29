import itertools


def solution():
    n = int(input())

    product_result = itertools.product(range(1, n + 1), range(1, n + 1))
    table_items = []

    for item in product_result:
        table_items.append(f"{item[0] * item[1]}")

    for i in range(n):
        print(" ".join(table_items[i * n: i * n + n]))


if __name__ == "__main__":
    solution()
