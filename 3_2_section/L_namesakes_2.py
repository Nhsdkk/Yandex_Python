def solution():
    n = int(input())
    names_list = [input() for _ in range(n)]
    names_dict = {name: names_list.count(name) for name in names_list if names_list.count(name) != 1}
    if len(names_dict.keys()) == 0:
        print("Однофамильцев нет")
    else:
        print("\n".join([f"{name} - {names_dict[name]}" for name in sorted(names_dict.keys())]))


if __name__ == "__main__":
    solution()
