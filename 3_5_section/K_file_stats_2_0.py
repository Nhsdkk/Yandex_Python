import json


def solution():
    input_file, output_file = input(), input()
    with open(input_file, "r") as file:
        data = [line.rstrip() for line in file.readlines()]

    numbers = []

    for line in data:
        numbers += [int(item) for item in line.split()]

    positive_amount = len([item for item in numbers if item > 0])

    stats = {
        "count": len(numbers),
        "positive_count": positive_amount,
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2)
    }

    with open(output_file, "w", encoding="UTF-8") as file:
        json.dump(stats, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    solution()
