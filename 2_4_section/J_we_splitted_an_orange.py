def solution():
    parts_amount = int(input())
    print("А Б В")

    for a_amount in range(1, parts_amount):
        for b_amount in range(1, parts_amount):
            for c_amount in range(1, parts_amount):
                if a_amount + b_amount + c_amount == parts_amount:
                    print(f"{a_amount} {b_amount} {c_amount}")


if __name__ == "__main__":
    solution()
