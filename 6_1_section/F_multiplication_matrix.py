import numpy as np


def multiplication_matrix(n: int):
    return np.fromfunction(lambda i, j: (i + 1) * (j + 1), (n, n), dtype=int)