def solution():
    splitted_string = input().split()
    print("\n".join([f"{i}. {item}" for i, item in enumerate(splitted_string, start=1)]))


if __name__ == "__main__":
    solution()
