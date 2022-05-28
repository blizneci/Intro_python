import timeit
from operator import lt, gt


def min_max(*args, operator, key=None, default=None):
    if len(args) == 1:
        try:
            values = list(args[0]) # Also checks if the object is iterable
        except TypeError:
            raise TypeError(
                    f"{type(args[0]).__name__} object is not iterable"
                ) from None
    else:
        values = args
    
    if not values:
        if default is None:
            raise ValueError("args is an empty sequence")
        return default

    if key is None:
        keys = values
    else:
        if callable(key):
            keys = [key(value) for value in values]
        else:
            raise TypeError(f"{type(key).__name__} object is not callable")

    extreme_key, extreme_value = keys[0], values[0]
    for key, value in zip(keys[1:], values[1:]):
        if operator(key, extreme_key):
            extreme_key = key
            extreme_value = value
    return extreme_key


def custom_min(*args, key=None, default=None):
    return min_max(*args, operator=lt, key=key, default=default)

def custom_max(*args, key=None, default=None):
    return min_max(*args, operator=gt, key=key, default=default)


