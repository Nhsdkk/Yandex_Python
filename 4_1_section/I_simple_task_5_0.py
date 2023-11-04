def is_prime(number: int):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

