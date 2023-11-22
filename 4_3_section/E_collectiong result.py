def result_accumulator(func):
    results = []

    def wrapper(*args, method: str = "accumulate", **kwargs):
        result = func(*args, **kwargs)

        if method == "accumulate":
            results.append(result)
            return None
        else:
            results_copy = results.copy() + [result]
            results.clear()
            return results_copy

    return wrapper
