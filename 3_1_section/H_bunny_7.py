def solution():
    n = int(input())

    for _ in range(n):
        string = input()
        index = string.find("зайка")

        if index == -1:
            print("Заек нет =(")
        else:
            print(string.find("зайка") + 1)


if __name__ == "__main__":
    solution()
