def solution():
    meals = sorted([input() for _ in range(int(input()))])
    m = int(input())
    prepared_meals = []
    for _ in range(m):
        for _ in range(int(input())):
            prepared_meals.append(input())

    not_prepared_meals = [item for item in meals if item not in prepared_meals]

    if len(not_prepared_meals) == 0:
        print("Готовить нечего")
    else:
        print("\n".join(not_prepared_meals))


if __name__ == "__main__":
    solution()
