import json
import sys


def solution():
    input_values = [line.rstrip() for line in sys.stdin.readlines()]

    with open("scoring.json", "r") as file:
        data = json.load(file)

    i = 0
    score = 0

    for item in data:
        temp_successful_counter = 0
        for test in item["tests"]:
            if input_values[i] == test["pattern"]:
                temp_successful_counter += 1

            i += 1

        score += (temp_successful_counter * item["points"]) // len(item["tests"])

    print(score)


if __name__ == "__main__":
    solution()
