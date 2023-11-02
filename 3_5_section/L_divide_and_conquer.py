def solution():
    numbers_filename, even_filename, odd_filename, same_filename = input(), input(), input(), input()

    with open(numbers_filename, "r") as file:
        data = []
        for item in file.readlines():
            data.append(item.strip().split())

    odd, even, same = [], [], []
    for row in data:
        to_append_odd, to_append_even, to_append_same = [], [], []
        for item in row:
            odd_count, even_count = sum([1
                                         for char in item
                                         if int(char) % 2 == 1]), sum([1
                                                                       for char in item
                                                                       if int(char) % 2 == 0])

            if odd_count > even_count:
                to_append_odd.append(item)
            elif odd_count < even_count:
                to_append_even.append(item)
            else:
                to_append_same.append(item)

        odd.append(to_append_odd)
        even.append(to_append_even)
        same.append(to_append_same)

    with open(odd_filename, "a") as file:
        file.writelines(["\n".join([" ".join([item for item in row]) for row in odd])] + ["\n"])

    with open(even_filename, "a") as file:
        file.writelines(["\n".join([" ".join([item for item in row]) for row in even])] + ["\n"])

    with open(same_filename, "a") as file:
        file.writelines(["\n".join([" ".join([item for item in row]) for row in same])] + ["\n"])


if __name__ == "__main__":
    solution()
