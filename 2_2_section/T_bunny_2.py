def solution():
    strings = [input(), input(), input()]

    strings.sort()

    for item in strings:
        if "зайка" in item:
            print(item, len(item))
            break


if __name__ == "__main__":
    solution()
