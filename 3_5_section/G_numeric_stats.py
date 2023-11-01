def solution():
    with open("numbers.txt", "r") as file:
        data = [line.rstrip() for line in file.readlines()]

    numbers = []

    for line in data:
        numbers += [int(item) for item in line.split()]

    positive_amount = len([item for item in numbers if item > 0])

    print("\n".join([str(len(numbers)),
                     str(positive_amount),
                     str(min(numbers)),
                     str(max(numbers)),
                     str(sum(numbers)),
                     f"{sum(numbers)/len(numbers):.2f}"
                     ]))


if __name__ == "__main__":
    solution()
