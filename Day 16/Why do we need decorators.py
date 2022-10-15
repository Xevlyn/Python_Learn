# Decorators
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        # This is done like this because
        t2 = time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()

# You can test how performant you code is
# Mind you it also depend on the hardware of you machine ie the CPU power to process.
