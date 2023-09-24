def solution():
    number = input()

    n1, n2 = int(number[2]) + int(number[1]), int(number[1]) + int(number[0])
    print(f"{max(n1, n2)}{min(n1, n2)}")


if __name__ == "__main__":
    solution()
