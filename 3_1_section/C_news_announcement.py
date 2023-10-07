def solution():
    l, n = int(input()), int(input())

    for _ in range(n):
        announcement = input()
        print(f"{announcement[:l - len('...')]}..." if len(announcement) > l else announcement)


if __name__ == "__main__":
    solution()
