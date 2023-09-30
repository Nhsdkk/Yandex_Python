def solution():
    x, y = 0, 0

    while True:
        direction = input()

        if direction == "СТОП":
            print(y)
            print(x)
            break

        diff = int(input())

        match direction:
            case "СЕВЕР":
                y += diff
            case "ЮГ":
                y -= diff
            case "ЗАПАД":
                x -= diff
            case "ВОСТОК":
                x += diff


if __name__ == "__main__":
    solution()
