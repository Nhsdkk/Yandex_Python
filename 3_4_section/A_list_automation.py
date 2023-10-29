def solution():
    splitted_string = input().split()
    print("\n".join([f"{i + 1}. {splitted_string[i]}" for i in range(len(splitted_string))]))


if __name__ == "__main__":
    solution()
