def secret_replace(string: str, **kwargs):
    counter_dict = {char: 0 for char in kwargs.keys()}

    string_list = list(string)

    for i, char in enumerate(string_list):
        if char in kwargs:
            string_list[i] = kwargs[char][counter_dict[char]]
            if counter_dict[char] + 1 == len(kwargs[char]):
                counter_dict[char] = 0
            else:
                counter_dict[char] += 1

    return "".join(string_list)
