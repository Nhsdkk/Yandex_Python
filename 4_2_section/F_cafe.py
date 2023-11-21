def order(*args):
    global in_stock

    drinks = {
        'Эспрессо': {
            'coffee': 1,
            'milk': 0,
            'cream': 0
        },
        'Капучино': {
            'coffee': 1,
            'milk': 3,
            'cream': 0
        },
        'Макиато': {
            'coffee': 2,
            'milk': 1,
            'cream': 0
        },
        'Кофе по-венски': {
            'coffee': 1,
            'milk': 0,
            'cream': 2
        },
        'Латте Макиато': {
            'coffee': 1,
            'milk': 2,
            'cream': 1
        },
        'Кон Панна': {
            'coffee': 1,
            'milk': 0,
            'cream': 1
        }
    }

    for drink_name in args:
        drink_requirements = drinks[drink_name]

        if all([drink_requirements[key] <= in_stock[key] for key in drink_requirements.keys()]):
            in_stock["coffee"] -= drink_requirements["coffee"]
            in_stock["milk"] -= drink_requirements["milk"]
            in_stock["cream"] -= drink_requirements["cream"]
            return drink_name

    return "К сожалению, не можем предложить Вам напиток"
