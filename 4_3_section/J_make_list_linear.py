def make_linear(array):
    result = []
    for item in array:
        if type(item) is list:
            result += make_linear(item)
        else:
            result.append(item)

    return result
