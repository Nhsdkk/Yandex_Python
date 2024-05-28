import numpy as np


def stairs(n):
    size = n.size
    n = np.reshape(n, (-1, size))
    new = np.reshape(np.arange(size), (-1, size))
    new[0] = n.copy()
    for i in range(1, size):
        new = np.concatenate((new, np.roll(n, i)), axis=0)

    return new
