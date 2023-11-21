def to_string(*args, **kwargs):
    sep, end = " ", "\n"
    kwargs_sep, kwargs_end = kwargs.get("sep"), kwargs.get("end")
    if kwargs_sep is not None:
        sep = kwargs_sep
    if kwargs_end is not None:
        end = kwargs_end

    result = sep.join([str(item) for item in args]) + end
    return result.__repr__()
