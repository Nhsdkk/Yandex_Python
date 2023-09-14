def solution():
    name = input("Как Вас зовут?")

    print(f"Здравствуйте, {name}!")

    mood = input("Как дела?")

    if mood == "хорошо":
        print("Я за вас рада!")
    else:
        print("Всё наладится!")


if __name__ == "__main__":
    solution()
