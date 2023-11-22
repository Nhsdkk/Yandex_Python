def same_type(func):
    def wrapper(*args, **kwargs):
        if len(set([type(argument) for argument in args])) == 1:
            return func(*args, **kwargs)

        print("Обнаружены различные типы данных")
        return None

    return wrapper
