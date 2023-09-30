def solution():
    number = int(input())
    int1, int2 = number // 1000, number // 100 - (number // 1000 * 10),
    int3, int4 = number // 10 - (number // 100 * 10), number % 10
    print(int2, int1, int4, int3, sep="")


if __name__ == "__main__":
    solution()
