def solution():
    objects = {}

    while prompt := input():
        for object_name in prompt.split():
            if object_name in objects:
                objects[object_name] += 1
            else:
                objects[object_name] = 1

    print("\n".join([f"{thing} {thing_count}" for thing, thing_count in objects.items()]))


if __name__ == "__main__":
    solution()
