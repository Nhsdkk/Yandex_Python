def solution():
    line1, line2 = input().split(", "), input().split(", ")
    i = 0

    while i < len(line1) and i < len(line2):
        print(f"{line1[i]} - {line2[i]}")
        i += 1


if __name__ == "__main__":
    solution()
