def solution():
    n = int(input())
    are_correct = True

    for _ in range(n):
        word = input()
        if word[0] != "а" and word[0] != "б" and word[0] != "в":
            are_correct = False

    print("YES" if are_correct else "NO")


if __name__ == "__main__":
    solution()
