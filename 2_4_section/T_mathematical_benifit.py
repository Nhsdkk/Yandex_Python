def translate(number, base):
    result = ""
    
    while number // base != 0:
        result = f"{number % base}" + result
        number //= base
        
    return f"{number % base}" + result


def solution():
    number = int(input())
    max_digit_sum = None
    most_valuable_base = None

    for base in range(2, 11):
        if base == 10:
            digit_sum = sum([int(char) for char in str(number)])
        else:
            digit_sum = sum([int(char) for char in translate(number, base)])

        if max_digit_sum is None or max_digit_sum < digit_sum:
            max_digit_sum = digit_sum
            most_valuable_base = base

    print(most_valuable_base)


if __name__ == "__main__":
    solution()
