import time
from functools import wraps


def sleep(time_sec=5):
    def decorator(func):
        @wraps(func)
        def out(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(time_sec)
            return result
        return out
    return decorator
