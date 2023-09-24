def solution():
    pet, vas, tol = int(input()), int(input()), int(input())

    max_v, min_v = max(pet, tol, vas), min(pet, tol, vas)

    if max_v == pet and min_v == vas:
        first, second, third = "Петя", "Толя", "Вася"
    elif max_v == pet and min_v == tol:
        first, second, third = "Петя", "Вася", "Толя"
    elif max_v == tol and min_v == vas:
        first, second, third = "Толя", "Петя", "Вася"
    elif max_v == tol and min_v == pet:
        first, second, third = "Толя", "Вася", "Петя"
    elif max_v == vas and min_v == pet:
        first, second, third = "Вася", "Толя", "Петя"
    else:
        first, second, third = "Вася", "Петя", "Толя"

    centered_first, centered_second = f"{first:^8}", f"{second:^8}"
    centered_third = f"{third:^8}"

    print(f"{centered_first:^24}")
    print(f"{centered_second:<24}")
    print(f"{centered_third:>24}")

    str1, str2, str3 = "I", "II", "III"

    print(f"{str2:^8}" + f"{str1:^8}" + f"{str3:^8}")


if __name__ == "__main__":
    solution()
