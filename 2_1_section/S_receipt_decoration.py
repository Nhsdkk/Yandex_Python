def solution():
    name, cost, weight, money = input(), int(input()), int(input()), int(input())
    total_cost = cost * weight
    leftovers = money - total_cost
    string_length = 35
    template_string1 = "Товар:"
    template_string2 = "Цена:кг * руб/кг"
    template_string3 = "Итого:руб"
    template_string4 = "Внесено:руб"
    template_string5 = "Сдача:руб"

    print(f"""================Чек================
Товар:{" " * (string_length - len(template_string1) - len(name))}{name}
Цена:{" " * (string_length - len(template_string2) - len(str(weight)) - len(str(cost)))}{weight}кг * {cost}руб/кг
Итого:{" " * (string_length - len(template_string3) - len(str(total_cost)))}{total_cost}руб
Внесено:{" " * (string_length - len(template_string4) - len(str(money)))}{money}руб
Сдача:{" " * (string_length - len(template_string5) - len(str(leftovers)))}{leftovers}руб
===================================""")


if __name__ == "__main__":
    solution()
