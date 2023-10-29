def solution():
    prompt1, prompt2, prompt3 = input().split(", "), input().split(", "), input().split(", ")
    product_list = sorted(prompt1 + prompt2 + prompt3)
    index_list = [i + 1 for i in range(len(product_list))]
    for item in zip(index_list, product_list):
        print(f"{item[0]}. {item[1]}")


if __name__ == "__main__":
    solution()
