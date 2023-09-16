def solution():
    number = input()

    n = [int(number[2]) + int(number[1]), int(number[1]) + int(number[0])]
    n.sort(reverse=True)
    print("".join([str(item) for item in n]))


if __name__ == "__main__":
    solution()
