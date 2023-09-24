def solution():
    name1, name2, name3 = input(), input(), input()

    min_name = min(name1, name2, name3)

    if min_name == name1:
        print(name1)
    elif min_name == name2:
        print(name2)
    else:
        print(name3)


if __name__ == "__main__":
    solution()
