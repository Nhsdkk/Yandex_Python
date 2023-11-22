def recursive_sum(*args) -> int:
    if len(args) == 0:
        return 0
    return args[0] + recursive_sum(*args[1:])
