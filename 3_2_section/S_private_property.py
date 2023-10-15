def solution():
    objects = []
    for _ in range(int(input())):
        objects += set(input().split(": ")[1].split(", "))

    print("\n".join(sorted([object_private for object_private in objects if objects.count(object_private) == 1])))


if __name__ == "__main__":
    solution()
