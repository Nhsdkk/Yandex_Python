import os, math


def solution():
    kbyte, mbyte, gbyte = 1024, 1024 * 1024, 1024 * 1024 * 1024
    filename = input()
    size = os.stat(filename).st_size

    if size < 1:
        print(f"{size * 8}б")
    elif size < kbyte:
        print(f"{size}Б")
    elif size < mbyte:
        print(f"{math.ceil(size / kbyte)}КБ")
    elif size < gbyte:
        print(f"{math.ceil(size / mbyte)}МБ")
    else:
        print(f"{math.ceil(size / gbyte)}ГБ")


if __name__ == "__main__":
    solution()
