def solution():
    tube1, tube2, tube3 = int(input()), int(input()), int(input())

    if tube1 + tube2 <= tube3 or tube1 + tube3 <= tube2 or tube2 + tube3 <= tube1:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    solution()
