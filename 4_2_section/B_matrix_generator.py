def make_matrix(size, value: int = 0):
    if type(size) is int:
        return [[value] * size] * size
    else:
        return [[value] * size[0]] * size[1]

