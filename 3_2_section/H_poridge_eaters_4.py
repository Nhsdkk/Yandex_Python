def solution():
    poridges = {}

    for _ in range(int(input())):
        splitted_input = input().split()

        for poridge in splitted_input[1:]:
            if poridge in poridges:
                poridges[poridge].append(splitted_input[0])
            else:
                poridges[poridge] = [splitted_input[0]]

    prompt = input()

    if prompt in poridges:
        print("\n".join(sorted(poridges[prompt])))
    else:
        print("Таких нет")


if __name__ == "__main__":
    solution()
