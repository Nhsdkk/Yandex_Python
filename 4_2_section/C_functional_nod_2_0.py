def gcd(*args):
    if len(args) == 1:
        return args[0]
    else:
        res = args[0]
        for i in range(len(args) - 1):
            number1, number2 = res, args[i + 1]

            while number1 != 0 and number2 != 0:
                if number1 > number2:
                    number1 %= number2
                else:
                    number2 %= number1

            if number1 == 0:
                res = number2
            else:
                res = number1
        return res
