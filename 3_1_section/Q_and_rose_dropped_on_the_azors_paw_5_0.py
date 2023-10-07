def solution():
    string = "".join(input().lower().split(" "))
    print("YES" if string == string[::-1] else "NO")


if __name__ == "__main__":
    solution()