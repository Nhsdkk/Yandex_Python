def solution():
    first_file, second_file, output_file = input(), input(), input()

    first_words = []
    second_words = []

    with open(first_file, "r", encoding="UTF-8") as file:
        for line in file.readlines():
            first_words += line.rstrip().split()

    with open(second_file, "r", encoding="UTF-8") as file:
        for line in file.readlines():
            second_words += line.rstrip().split()

    first_diff = [item for item in first_words if item not in second_words]
    second_diff = [item for item in second_words if item not in first_words]

    with open(output_file, "w", encoding="UTF-8") as file:
        file.write("\n".join(sorted(set(first_diff + second_diff))))


if __name__ == "__main__":
    solution()
