def gcd(number1: int, number2: int) -> int:
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1

    return number1