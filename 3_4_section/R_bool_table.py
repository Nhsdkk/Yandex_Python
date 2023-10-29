import itertools


def solution():
    prompt = " " + input() + " "
    print("a b c f")
    for item in itertools.product(range(2), repeat=3):
        new_prompt = prompt.replace(" a ", f" {item[0]} ").replace(" b ", f" {item[1]} ").replace(" c ", f" {item[2]} ")
        print(f"{item[0]} {item[1]} {item[2]} {int(eval(new_prompt))}")


if __name__ == "__main__":
    solution()
