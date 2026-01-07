# 4. Write a decorator that logs the function name and its execution time

import functools, time

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print(f"[LOG] Calling {func.__name__}")
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[LOG] {func.__name__} finished in {elapsed:.6f}s")
        return result
    return wrapper

@log_time
def example(n):
    return sum(range(n))

print(example(1000000))