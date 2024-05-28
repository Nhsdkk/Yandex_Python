import numpy as np


def snake(m, n, direction="H"):
    arr = np.fromfunction(lambda i, j: j + 1, (1, n * m), dtype=np.int16)
    arr = np.reshape(arr, (m, n) if direction == "V" else (n, m))
    for i in range(1, n if direction == "H" else m):
        if i % 2 == 1:
            arr[i] = np.flip(arr[i])
    if direction == "V":
        arr = arr.transpose()
    return arr