def gcd(n1, n2):
    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1

    return n1


def solution():
    n1, n2 = int(input()), int(input())
    lcm = (n1 * n2) // gcd(n1, n2)

    print(lcm)


if __name__ == "__main__":
    solution()
