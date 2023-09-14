def solution():
    name, cost, weight, money = input(), int(input()), int(input()), int(input())
    print(f"""Чек
{name} - {weight}кг - {cost}руб/кг
Итого: {cost * weight}руб
Внесено: {money}руб
Сдача: {money - cost * weight}руб""")


if __name__ == "__main__":
    solution()
