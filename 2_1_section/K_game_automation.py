def solution():
    number = input()
    print(number[:2][::-1] + number[2:][::-1])


if __name__ == "__main__":
    solution()
