def solution():
    h = 0
    for i in range(int(input())):
        b = int(input())
        hn, r, m = b % 256, (b // 256) % 256, (b // 256 ** 2) % 256
        h_compare = (37 * (m + r + h)) % 256
        if h_compare != hn or hn > 99:
            print(i)
            return
        h = hn
    print(-1)


if __name__ == '__main__':
    solution()
