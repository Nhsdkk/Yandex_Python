def solution():
    objects = set()

    for _ in range(int(input())):
        objects.update(input().split())

    print("\n".join(objects))


if __name__ == "__main__":
    solution()
