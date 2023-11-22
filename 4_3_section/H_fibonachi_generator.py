def fibonacci(n):
    n_0 = 0
    n_1 = 1
    yield n_0
    if n == 1:
        return
    yield n_1
    if n == 2:
        return
    for _ in range(n - 2):
        n_1, n_0 = n_0 + n_1, n_1

        yield n_1
