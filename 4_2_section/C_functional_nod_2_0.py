def gcd_two_values(number1: int, number2: int) -> int:
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1

    if number1 == 0:
        return number2
    else:
        return number1


def gcd(*args):
    if len(args) == 1:
        return args[0]
    else:
        res = args[0]
        for i in range(len(args) - 1):
            res = gcd_two_values(res, args[i + 1])
        return res
