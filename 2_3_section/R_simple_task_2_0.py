def solution():
    number = int(input())
    simple_nums = []
    result = []

    for i in range(2, number + 1):
        is_simple = True
        for item in simple_nums:
            if i % item == 0:
                is_simple = False
                break

        if is_simple:
            simple_nums.append(i)

    if number in simple_nums:
        print(f"1 * {number}")

    while number not in simple_nums:
        for i in simple_nums:
            if number % i == 0:
                result.append(i)
                number //= i
                break

    result.append(number)

    print(' * '.join([str(item) for item in result]))


if __name__ == "__main__":
    solution()
