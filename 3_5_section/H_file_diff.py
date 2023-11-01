def solution():
    first_file, second_file, output_file = input(), input(), input()

    with open(first_file, "r", encoding="UTF-8") as file:
        first_file_data = [item.rstrip() for item in file.readlines()]

    with open(second_file, "r", encoding="UTF-8") as file:
        second_file_data = [item.rstrip() for item in file.readlines()]

    with open(output_file, "w", encoding="UTF-8") as file:
        file.write("\n".join([item
                              for item in first_file_data
                              if item not in second_file_data] + [item
                                                                  for item in second_file_data
                                                                  if item not in first_file_data]))


if __name__ == "__main__":
    solution()
