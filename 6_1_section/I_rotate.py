import numpy as np


def rotate(array, angle):
    for i in range(angle // 90):
        array = np.rot90(array, axes=(1, 0))

    return array
