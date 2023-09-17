def solution():
    results = {
        int(input()): "Петя",
        int(input()): "Вася",
        int(input()): "Толя",
    }

    keys = list(results.keys())
    keys.sort(reverse=True)

    print(f"""1. {results[keys[0]]}
2. {results[keys[1]]}
3. {results[keys[2]]}""")


if __name__ == "__main__":
    solution()
