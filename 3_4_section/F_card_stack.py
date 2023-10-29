def solution():
    suits = ["пик", "треф", "бубен", "червей"]
    nominals = [str(i) for i in range(2, 11)] + ["валет", "дама", "король", "туз"]

    excluded_suit = input()
    suits.remove(excluded_suit)

    for nominal in nominals:
        for suit in suits:
            print(f"{nominal} {suit}")


if __name__ == "__main__":
    solution()
