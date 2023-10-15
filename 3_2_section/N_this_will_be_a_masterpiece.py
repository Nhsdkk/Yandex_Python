def solution():
    products = [input() for _ in range(int(input()))]
    m = int(input())

    can_be_cooked = []

    for _ in range(m):
        name = input()
        required_products_existence = [input() in products for _ in range(int(input()))]
        if False not in required_products_existence:
            can_be_cooked.append(name)

    if len(can_be_cooked) == 0:
        print("Готовить нечего")
    else:
        print("\n".join(sorted(can_be_cooked)))


if __name__ == "__main__":
    solution()
