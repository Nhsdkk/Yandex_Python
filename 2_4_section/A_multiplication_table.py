def solution():
    max_number = int(input())

    for i in range(1, max_number + 1):
        if i == 1:
            print(" ".join([str(j) for j in range(1, max_number + 1)]))
            continue

        print(" ".join([str(i * j) for j in range(1, max_number + 1)]))


if __name__ == "__main__":
    solution()
