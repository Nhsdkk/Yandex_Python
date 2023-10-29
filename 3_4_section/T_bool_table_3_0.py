import itertools
from typing import Optional

OPS_PRIORITY = {
    "not": 1,
    "and": 2,
    "or": 3,
    "^": 3,
    "->": 4,
    "~": 5,
}


def create_variants(chars: list[str]) -> list[dict[str, int]]:
    variants_tuple = itertools.product(range(2), repeat=len(chars))
    return [{chars[j]: variant[j] for j in range(len(variant))} for variant in variants_tuple]


def output(variants: list[dict[str, int]], chars: list[str], polish_dict: dict[str, str]):
    print(" ".join(chars + ["F"]))
    for variant in variants:
        result = solve_multi_polish(polish_dict, variant)
        print(" ".join([str(item) for item in variant.values()]) + f" {int(result)}")


def get_chars(prompt: str) -> set[str]:
    return set([item.replace("(", "").replace(")", "").replace(" ", "") for item in prompt.split()
                if item.replace("(", "").replace(")", "").replace(" ", "") not in OPS_PRIORITY.keys()])


def split_prompt_to_braces(prompt: str) -> dict[str, str]:
    splitted_prompt = {}
    max_index = 0

    temp_string = ""

    for char in prompt:
        if char == ")":
            max_index += 1
            open_brace_index = len(temp_string) - 1 - temp_string[::-1].index("(")
            splitted_prompt[f"X{max_index}"] = temp_string[open_brace_index + 1:]
            temp_string = temp_string[:open_brace_index] + f"X{max_index}"
        else:
            temp_string += char

    splitted_prompt["X0"] = temp_string
    return splitted_prompt


def to_polish(splitted_prompt: dict[str, str]):
    for key, value in splitted_prompt.items():
        stack = []
        polish_list = []

        for item in value.split():
            if item not in OPS_PRIORITY.keys():
                polish_list.append(item)
                continue

            if len(stack) == 0:
                stack.append(item)
                continue

            if OPS_PRIORITY[item] < OPS_PRIORITY[stack[-1]]:
                stack.append(item)
                continue

            while len(stack) != 0:
                if OPS_PRIORITY[item] < OPS_PRIORITY[stack[-1]]:
                    break
                polish_list.append(stack.pop())

            stack.append(item)

        splitted_prompt[key] = " ".join(polish_list + stack[::-1])


def solve_single_polish(polish_prompt: str, variant: dict[str, int], solved_prompts: dict[str, int]) -> Optional[int]:
    stack = []
    for item in polish_prompt.split(" "):
        if OPS_PRIORITY.get(item) is not None:
            match item:
                case "->":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b <= a)
                case "not":
                    a = stack.pop()
                    stack.append(not a)
                case "~":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b == a)
                case "or":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b or a)
                case "and":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b and a)
                case "^":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b != a)
                case _:
                    return None
            continue

        if variant.get(item) is not None:
            stack.append(variant.get(item))
            continue

        if solved_prompts.get(item) is not None:
            stack.append(solved_prompts.get(item))
            continue

        return None

    # print(f"Result for polish prompt - {polish_prompt} is {stack[0]}")

    return stack[0]


def solve_multi_polish(polish_dict: dict[str, str], variant: dict[str, int]) -> int:
    solved_prompts = {}

    while solved_prompts.get("X0") is None:
        for key, value in polish_dict.items():
            result = solve_single_polish(value, variant, solved_prompts)
            if result is not None:
                solved_prompts[key] = result

    return solved_prompts["X0"]


def solution():
    prompt = input()
    chars = sorted(get_chars(prompt))
    # print("CHARS: ", chars)
    variants = create_variants(chars)
    splitted_prompt = split_prompt_to_braces(prompt)
    # print("BEFORE TRANSLATION: ", splitted_prompt)
    to_polish(splitted_prompt)
    output(variants, chars, splitted_prompt)
    # print("AFTER TRANSLATION: ", splitted_prompt)
    # print("VARIANTS: ", variants)


if __name__ == "__main__":
    solution()
