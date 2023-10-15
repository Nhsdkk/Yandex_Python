def solution():
    n = int(input())
    names_list = [input() for _ in range(n)]
    print(sum([names_list.count(name) for name in set(names_list) if names_list.count(name) != 1]))


if __name__ == "__main__":
    solution()
