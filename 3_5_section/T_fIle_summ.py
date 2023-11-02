import struct


def solution():
    with open("numbers.num", "rb") as file:
        data = file.read()

    append_to_format = 'h' * (len(data) // 2)
    print(sum(struct.unpack(f">0h{append_to_format}", data)) % 2 ** 16)


if __name__ == "__main__":
    solution()
