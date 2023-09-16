def solution():
    speed = {
        int(input()): "Петя",
        int(input()): "Вася",
        int(input()): "Толя"
    }

    keys = list(speed.keys())
    keys.sort(reverse=True)

    print(speed[keys[0]].center(8).center(24))
    print(speed[keys[1]].center(8).ljust(24))
    print(speed[keys[2]].center(8).rjust(24))
    print("II".center(8) + "I".center(8) + "III".center(8))


if __name__ == "__main__":
    solution()
