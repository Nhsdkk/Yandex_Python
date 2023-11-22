def cycle(items: list[int]):
    i = 0
    while True:
        if i == len(items):
            i = 0

        yield items[i]
        i += 1
