def solution():
    petya, vasya, tolya = int(input()), int(input()), int(input())
    if petya >= vasya >= tolya or petya >= tolya >= vasya:
        print("Петя")
    elif vasya >= petya >= tolya or vasya >= tolya >= petya:
        print("Вася")
    elif tolya >= petya >= vasya or tolya >= vasya >= petya:
        print("Толя")


if __name__ == "__main__":
    solution()
