def solution():
    word = input()
    print("YES" if word == word[::-1] else "NO")


if __name__ == "__main__":
    solution()
