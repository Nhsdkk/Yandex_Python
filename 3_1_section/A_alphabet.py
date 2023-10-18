def solution():
    n = int(input())
    are_correct = True

    for _ in range(n):
        word = input()
        if word[0] in ["а", "б", "в"]:
            are_correct = False

    print("YES" if are_correct else "NO")


if __name__ == "__main__":
    solution()
