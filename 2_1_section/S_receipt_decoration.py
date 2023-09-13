def solution():
    name, cost, weight, money = input(), int(input()), int(input()), int(input())
    total_cost = cost * weight
    leftovers = money - total_cost
    print(f"""================Чек================
Товар:{" " * (35 - 6 - len(name))}{name}
Цена:{" " * (35 - 16 - len(str(weight)) - len(str(cost)))}{weight}кг * {cost}руб/кг
Итого:{" " * (35 - 9 - len(str(total_cost)))}{total_cost}руб
Внесено:{" " * (35 - 11 - len(str(money)))}{money}руб
Сдача:{" " * (35 - 9 - len(str(leftovers)))}{leftovers}руб
===================================""")


solution()
