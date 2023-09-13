def solution():
    x, y = input(), input()
    x, y = (3 - len(x)) * "0" + x, (3 - len(y)) * "0" + y
    print((int(x[0]) + int(y[0])) % 10, (int(x[1]) + int(y[1])) % 10, (int(x[2]) + int(y[2])) % 10, sep="")


solution()
