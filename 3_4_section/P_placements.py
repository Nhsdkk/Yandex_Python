import itertools


def solution():
    dictionary = {
        "буби": "бубен",
        "пики": "пик",
        "трефы": "треф",
        "черви": "червей",
    }

    suits = ["бубен", "пик", "треф", "червей"]
    nominals = sorted([str(i) for i in range(2, 11)]) + ["валет", "дама", "король", "туз"]
    include_suit, exclude_number = input(), input()

    nominals.remove(exclude_number)

    possible_cards = [f"{item[0]} {item[1]}" for item in itertools.product(nominals, suits)]

    lowest1, lowest2 = possible_cards.pop(0), possible_cards.pop(0)

    if dictionary[include_suit] in lowest1 or dictionary[include_suit] in lowest2:
        i = 0
        for item in possible_cards:
            if i == 10:
                break
            print(", ".join([lowest1, lowest2, item]))
            i += 1
    else:
        i = 0
        for item in [item1 for item1 in possible_cards if dictionary[include_suit] in item1]:
            if i == 10:
                break
            print(", ".join([lowest1, lowest2, item]))
            i += 1


if __name__ == "__main__":
    solution()
