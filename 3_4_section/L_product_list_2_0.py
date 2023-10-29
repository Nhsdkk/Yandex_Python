def solution():
    products = []
    for _ in range(int(input())):
        products += input().split(", ")

    for item in zip(range(1, len(products) + 1), sorted(products)):
        print(f"{item[0]}. {item[1]}")


if __name__ == "__main__":
    solution()
