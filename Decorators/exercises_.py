"""



"""
from functools import lru_cache
from time import perf_counter
from decimal import Decimal
from time import sleep


# 1
def my_decorator(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        running = func(*args, **kwargs)
        end = perf_counter()
        return f'Elapsed is {end - start} seconds'

    return inner


@my_decorator
def add(a, b, c):
    return a + b + c


print(add(1, 5, 9))

# 2
precision = 2


def normalize(func):
    def inner(*args, **kwargs):
        return round(float(func(*args, **kwargs)), precision)

    return inner


@normalize
def perc_diff(x, y):
    try:
        return (y - x) / x * 100
    except ZeroDivisionError:
        return 0


@normalize
def sum_squares(*args):
    return sum(x ** 2 for x in args)


@normalize
def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)


print(avg(1, 2, 9))


# 3
@lru_cache
def add(x, y):
    sleep(2)
    return x + y


start = perf_counter()
print(add(1, 9))
end = perf_counter()
print(f'{end-start}')

start = perf_counter()
print(add(1, 9))
end = perf_counter()
print(f'{end-start}')


#  4
def decorator_function(number):
    def normalize(func):
        def inner(*args, **kwargs):
            return round(float(func(*args, **kwargs)), precision)

        return inner
    return normalize



@decorator_function(2)
def perc_diff(x, y):
    try:
        return (y - x) / x * 100
    except ZeroDivisionError:
        return 0


@decorator_function(2)
def sum_squares(*args):
    return sum(x ** 2 for x in args)


@decorator_function(4)
def avg(*args):
    if len(args) == 0:
        return 0

    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)


print(avg(1, 2, 3.2564))