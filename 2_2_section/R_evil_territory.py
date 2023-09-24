def solution():
    n1, n2, n3 = int(input()), int(input()), int(input())
    max_n = max(n1, n2, n3)

    if max_n == n1:
        cos = (n2**2 + n3**2 - max_n**2) / (2 * n2 * n3)
    elif max_n == n2:
        cos = (n1 ** 2 + n3 ** 2 - max_n ** 2) / (2 * n1 * n3)
    else:
        cos = (n2 ** 2 + n1 ** 2 - max_n ** 2) / (2 * n1 * n2)

    if cos == 0:
        print("100%")
    elif cos > 0:
        print("крайне мала")
    else:
        print("велика")


if __name__ == "__main__":
    solution()
