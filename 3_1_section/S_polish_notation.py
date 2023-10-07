def solution():
    array = []
    string = input()

    for item in string.split(" "):
        if item == "*" or item == "-" or item == "+":
            a, b = array[-2], array[-1]

            array.pop(len(array) - 1)
            array.pop(len(array) - 1)

            match item:
                case "*":
                    array.append(a * b)
                case "+":
                    array.append(a + b)
                case "-":
                    array.append(a - b)

            continue

        array.append(int(item))

    print(array[0])


if __name__ == "__main__":
    solution()
