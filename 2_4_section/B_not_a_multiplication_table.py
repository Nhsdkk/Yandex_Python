def solution():
    max_number = int(input())

    for i in range(1, max_number + 1):
        for j in range(1, max_number + 1):
            print(f"{j} * {i} = {j * i}")


if __name__ == "__main__":
    solution()
