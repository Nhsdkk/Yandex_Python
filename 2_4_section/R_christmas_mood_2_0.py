def solution():
    n = int(input())
    arr = [f"{i}" for i in range(1, n + 1)]
    
    strings = []
    i = 1
    
    while len(arr) != 0:
        string = " ".join(arr[:i])
        strings.append(string)
        arr = arr[i:]
        i += 1
    
    length = max([len(string) for string in strings])
    
    space = " "
    
    new_strings = []
    
    for string in strings:
        if (length - len(string)) % 2 != 0:
            pr_space, af_space = ((length - len(string)) // 2), (length - len(string) - ((length - len(string)) // 2))
        else:
            pr_space, af_space = (length - len(string)) // 2, (length - len(string)) // 2
    
        new_strings.append(f"{space * pr_space}{string}{space * af_space}")
    
    print("\n".join(new_strings))


if __name__ == "__main__":
    solution()
