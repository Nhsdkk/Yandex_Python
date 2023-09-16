def solution():
    a, b, c = float(input()), float(input()), float(input())

    if a == b == c == 0:
        print("Infinite solutions")
        return

    d = b**2 - 4 * a * c
    a1 = (-b + (d**0.5)) / (2 * a)
    a2 = (-b - (d**0.5)) / (2 * a)

    if a1 == a2:
        print(round(a1, 2))
    else:
        res = [round(a1, 2), round(a2, 2)]
        res.sort()
        print(res[0], res[1])


if __name__ == "__main__":
    solution()
