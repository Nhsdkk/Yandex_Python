def solution():
    n, prompts = int(input()), []

    for _ in range(n):
        prompts.append(input())

    keyword = input().lower()

    for prompt in prompts:
        if keyword in prompt.lower():
            print(prompt)


if __name__ == "__main__":
    solution()
