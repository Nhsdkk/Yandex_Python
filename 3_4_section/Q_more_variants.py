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
    prompt = input()

    nominals.remove(exclude_number)

    possible_cards = [f"{item[0]} {item[1]}" for item in itertools.product(nominals, suits)]
    variants = [f"{item[0]}, {item[1]}, {item[2]}" for item in itertools.combinations(possible_cards, r=3)]

    start_index = variants.index(prompt)

    for item in variants[start_index + 1:]:
        if dictionary[include_suit] in item:
            print(item)
            break


if __name__ == "__main__":
    solution()
