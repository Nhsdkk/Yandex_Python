def solution():
    prompt = input()
    print(sum([int(string_number) for string_number in prompt.split(" ")]))


if __name__ == "__main__":
    solution()
