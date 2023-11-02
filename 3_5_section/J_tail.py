def solution():
    input_file, n = input(), int(input())

    with open(input_file, "r", encoding="UTF-8") as file:
        data = [item.rstrip() for item in file.readlines()]

    print("\n".join(data[-n:]))
    

if __name__ == "__main__":
    solution()
