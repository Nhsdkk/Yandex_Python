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

    substring_aligning_length = 8
    string_aligning_length = substring_aligning_length * 3

    centered_first, centered_second = f"{first:^{substring_aligning_length}}", f"{second:^{substring_aligning_length}}"
    centered_third = f"{third:^{substring_aligning_length}}"

    print(f"{centered_first:^{string_aligning_length}}")
    print(f"{centered_second:<{string_aligning_length}}")
    print(f"{centered_third:>{string_aligning_length}}")

    str1, str2, str3 = "I", "II", "III"

    place_string = f"{str2:^{substring_aligning_length}}" + f"{str1:^{substring_aligning_length}}"
    place_string += f"{str3:^{substring_aligning_length}}"
    print(place_string)


if __name__ == "__main__":
    solution()
