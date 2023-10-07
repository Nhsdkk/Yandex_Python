def fac(number):
    result = 1

    for i in range(2, number + 1):
        result *= i

    return result


def solution():
    array = []
    string = input()
    binary_operations = ["*", "/", "-", "+"]
    unary_operations = ["~", "!", "#"]
    ternary_operation = "@"

    for item in string.split(" "):
        if item in binary_operations:
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
                case "/":
                    array.append(a // b)

            continue

        if item in unary_operations:
            a = array[-1]

            array.pop(len(array) - 1)

            match item:
                case "~":
                    array.append(-a)
                case "!":
                    array.append(fac(a))
                case "#":
                    array += [a, a]

            continue

        if item == ternary_operation:
            a, b, c = array[-3], array[-2], array[-1]

            array.pop(len(array) - 1)
            array.pop(len(array) - 1)
            array.pop(len(array) - 1)

            array += [b, c, a]

            continue

        array.append(int(item))

    print(array[0])


if __name__ == "__main__":
    solution()
