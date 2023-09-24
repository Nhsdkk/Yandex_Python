def solution():
    a, b, c = float(input()), float(input()), float(input())

    if a == b == c == 0:
        print("Infinite solutions")
        return

    if a == b == 0 and c != 0:
        print("No solution")
        return
    elif a == b == 0 and c == 0:
        print("Infinite solutions")
        return

    if a == 0:
        print(-c / b)
        return

    d = b**2 - 4 * a * c

    if d < 0:
        print("No solution")
        return

    a1 = (-b + (d**0.5)) / (2 * a)
    a2 = (-b - (d**0.5)) / (2 * a)

    if a1 == a2:
        print(round(a1, 2))
    else:
        res1, res2 = round(a1, 2), round(a2, 2)
        print(min(res1, res2), max(res1, res2))


if __name__ == "__main__":
    solution()
