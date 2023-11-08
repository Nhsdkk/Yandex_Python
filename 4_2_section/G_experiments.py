numbers = []


def enter_results(*args):
    global numbers
    numbers += args


def get_sum():
    global numbers
    sum1 = sum([numbers[i] for i in range(len(numbers)) if i % 2 == 0])
    sum2 = sum([numbers[i] for i in range(len(numbers)) if i % 2 == 1])

    if type(sum1) is int:
        sum1 = int(sum1)
    else:
        sum1 = float(f"{sum1:.2f}")

    if type(sum2) is int:
        sum2 = int(sum2)
    else:
        sum2 = float(f"{sum2:.2f}")

    return sum1, sum2


def get_average():
    global numbers
    arr1 = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
    arr2 = [numbers[i] for i in range(len(numbers)) if i % 2 == 1]
    sr1 = float(f"{sum(arr1) // len(arr1):.2f}") \
        if sum(arr1) % len(arr1) == 0 else float(f"{sum(arr1) / len(arr1):.2f}")
    sr2 = float(f"{sum(arr2) // len(arr2):.2f}") \
        if sum(arr2) % len(arr2) == 0 else float(f"{sum(arr2) / len(arr2):.2f}")
    return sr1, sr2


enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())