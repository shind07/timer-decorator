"""[summary]

:return: [description]
:rtype: [type]
"""
from functools import wraps
import time 

def timeit(func):
    """Prints the execution time of func"""
    
    @wraps(func)
    def timed_func(*args, **kwargs):

        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time

        print(f"Time to run {func.__name__}: {elapsed_time:.7f}")
        return result

    return timed_func


def timeit_unwrapped(func):
    """Same as above, with the @wraps decorator (for demo purposes)"""
    
    def timed_func(*args, **kwargs):

        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time

        print(f"Time to run {func.__name__}: {elapsed_time:.7f}")
        return result

    return timed_func
