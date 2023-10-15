def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1

    return number1


def solution():
    numbers = [int(item) for item in input().split("; ")]
    numbers_dict = {}

    for number1 in numbers:
        for number2 in numbers:
            if number1 != number2 and gcd(number1, number2) == 1:
                if number1 in numbers_dict:
                    numbers_dict[number1].append(number2)
                else:
                    numbers_dict[number1] = [number2]

                if number2 in numbers_dict:
                    numbers_dict[number2].append(number1)
                else:
                    numbers_dict[number2] = [number1]

    strings = [f"{number} - {', '.join([str(item) for item in sorted(set(numbers_dict[number]))])}"
               for number in sorted(numbers_dict.keys())]

    print("\n".join(strings))


if __name__ == "__main__":
    solution()
