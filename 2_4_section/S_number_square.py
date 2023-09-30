import math


def rectangle(matrix, k, n, number):
    for j in [n - 1 - k, k]:
        for i in range(k, n - k):
            matrix[i][j] = f"{number}"

    for i in [n - 1 - k, k]:
        for j in range(k, n - k):
            matrix[i][j] = f"{number}"


def solution():
    matrix = []
    n = int(input())

    if n == 1:
        print(1)
        return

    for i in range(n):
        matrix_row = []
        for j in range(n):
            matrix_row.append("0")
        matrix.append(matrix_row)

    for i in range(n):
        rectangle(matrix, i, n, i + 1)

    number_align_value = len(str(math.ceil(n / 2)))

    for row in matrix:
        string = " ".join([f"{number:>{number_align_value}}" for number in row])
        print(string)


if __name__ == "__main__":
    solution()
