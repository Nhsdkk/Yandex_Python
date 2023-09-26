def solution():
    elfs, gnomes, humans = input(), input(), input()

    if elfs[0] == gnomes[0] == humans[0]:
        print(elfs[0])
    elif elfs[1] == gnomes[1] == humans[1]:
        print(elfs[1])


if __name__ == "__main__":
    solution()
