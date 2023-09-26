def solution():
    petya, vasya, tolya = int(input()), int(input()), int(input())

    if petya >= vasya >= tolya:
        first, second, third = "Петя", "Вася", "Толя"
    elif petya >= tolya >= vasya:
        first, second, third = "Петя", "Толя", "Вася"
    elif vasya >= petya >= tolya:
        first, second, third = "Вася", "Петя", "Толя"
    elif vasya >= tolya >= petya:
        first, second, third = "Вася", "Толя", "Петя"
    elif tolya >= petya >= vasya:
        first, second, third = "Толя", "Петя", "Вася"
    else:
        first, second, third = "Толя", "Вася", "Петя"

    print(f"1. {first}")
    print(f"2. {second}")
    print(f"3. {third}")


if __name__ == "__main__":
    solution()
