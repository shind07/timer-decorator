"""
Demonstration of decorators using a function timer.
"""
from functimer import timeit, timeit_unwrapped


def fibonacci(n):
    if n < 0: return
    if n in (0, 1): return n
    return (fibonacci(n - 2)  + fibonacci(n - 1))


@timeit
def fibonacci_decorated(n):
    if n < 0: return
    if n in (0, 1): return n
    return (fibonacci(n - 2)  + fibonacci(n - 1))


@timeit_unwrapped
def fibonacci_decorated_unwrapped(n):
    if n < 0: return
    if n in (0, 1): return n
    return (fibonacci(n - 2)  + fibonacci(n - 1))


def decorator_example(n=10):
    """Example of the @timeit decorator in use."""

    print("Calling fibonacci() (no timer)...")
    print(fibonacci(n))    

    print("Calling timed fibonacci() (no decorator)...")
    fibonacci_timed = timeit(fibonacci)
    print(fibonacci_timed(n))

    print("Calling timed fibonacci() with decorator...")
    print(fibonacci_decorated(n))


def wraps_example(n=10):
    """Example of using @wraps in a decorator"""

    print("Printing value of fibonacci() (no decorator)")
    print(fibonacci, "\n")

    print("Printing value of decoratored func with no @wraps...")
    fibonacci_unwrapped = timeit_unwrapped(fibonacci)
    print(fibonacci_unwrapped,)

    print("Printing value of decoratored func with @wraps...")
    fibonacci_wrapped = timeit(fibonacci)
    print(fibonacci_wrapped)


if __name__ == "__main__":

    wraps_example()

   
