def solution():
    n = int(input())
    simple_nums = []
    res = []

    for i in range(2, n + 1):
        is_simple = True
        for item in simple_nums:
            if i % item == 0:
                is_simple = False
                break

        if is_simple:
            simple_nums.append(i)

    if n in simple_nums:
        print(f"1 * {n}")

    while n not in simple_nums:
        for i in simple_nums:
            if n % i == 0:
                res.append(i)
                n //= i
                break

    res.append(n)

    print(' * '.join([str(item) for item in res]))


if __name__ == "__main__":
    solution()
