def make_matrix(size, value: int = 0):
    if type(size) is int:
        return [[value for _ in range(size)] for _ in range(size)]
    else:
        return [[value for _ in range(size[0])] for _ in range(size[1])]
