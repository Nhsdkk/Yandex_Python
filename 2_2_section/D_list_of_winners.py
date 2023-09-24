def solution():
    pet, vas, tol = int(input()), int(input()), int(input())

    if pet >= vas >= tol:
        first, second, third = "Петя", "Вася", "Толя"
    elif pet >= tol >= vas:
        first, second, third = "Петя", "Толя", "Вася"
    elif vas >= pet >= tol:
        first, second, third = "Вася", "Петя", "Толя"
    elif vas >= tol >= pet:
        first, second, third = "Вася", "Толя", "Петя"
    elif tol >= pet >= vas:
        first, second, third = "Толя", "Петя", "Вася"
    else:
        first, second, third = "Толя", "Вася", "Петя"

    print(f"1. {first}")
    print(f"2. {second}")
    print(f"3. {third}")


if __name__ == "__main__":
    solution()
