def solution():
    with open("secret.txt", "r", encoding="UTF-8") as file:
        data = file.read()

    print("".join([chr(ord(item) % 128) for item in data]))


if __name__ == "__main__":
    solution()
