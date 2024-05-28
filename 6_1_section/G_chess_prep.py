import numpy as np


def make_board(n: int):
    return np.fromfunction(lambda i, j: (i + j + 1) % 2, (n, n), dtype=np.int8)
