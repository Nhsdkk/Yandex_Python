def solution():
    objects = set()
    while prompt := input():
        splitted_prompt = prompt.split()

        if "зайка" not in splitted_prompt:
            continue

        for i in range(len(splitted_prompt)):
            if splitted_prompt[i] != "зайка":
                continue

            if i != 0:
                objects.add(splitted_prompt[i - 1])

            if i != len(splitted_prompt) - 1:
                objects.add(splitted_prompt[i + 1])

    print("\n".join(objects))


if __name__ == "__main__":
    solution()
