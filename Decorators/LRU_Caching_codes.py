"""
                Least Recently Used LRU CACHING: from functools import lru_cache; @lru_cache(maxsize= some_number)
--> It is an application of decorators
--> It solves the following problem:
    --> you have a function that gets called often.
    --> the function is deterministic
        --> i.e, calls with the sane arguments should produce the same result.
--> We could use a caching mechanism:
    --> The first time a set of arguments is encountered, results are calculated and stored in a cache.
    --> Subsequent calls with the same arguments, recovers result from cache.
--> Python has a decorator called the LRU-cache decorator
--> LRU cache should not grow indefinitely
    --> We store up to n-entries so flush oldest entry and keep the n-most recent entries
--> It works well when most recent calls are good predictors of incoming calls.
--> can specify the cache size we want.
    --> Maxsize is a postional argument to LRU decorator
    --> None which specifies unbounded cache
    --> Otherwise specify an int to set max cache size.
--> Can specify None, to mean unbounded


                HOW TO USE LRU CACHE
--> It uses a decorator
    -->The decorator can also take arguments
--> There is a restriction
    --> The arguments passed to the function must be hashable values
    --> That's because they are used as a key in the cache dictionary

"""
from functools import lru_cache


# Re_creating LRU_Cache

def my_cache(func):
    cache_dict = dict()

    def inner(*args):
        if args in cache_dict:
            print('cache hit')
            return cache_dict[args]
        else:
            print('cache miss')
            result = func(*args)
            cache_dict[args] = result
            return result

    return inner


@my_cache
def add(a, b):
    print('add running')
    return a + b


@my_cache
def mult(a, b):
    print('mult runninb')
    return a * b


print(add(1, 2))
print(mult(1, 2))

print(add(1, 2))
print(add(1, 2))
print(mult(3, 4))


@lru_cache(maxsize=2)
def add(a, b):
    print('add called...')
    return a + b


print(add(1, 2))
print(add(3, 4))

print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

print(add(1, 2))


@lru_cache(maxsize=3)
def fib(n):
    print(f'Fb {n} called...')
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


print(fib(5))
print(fib(8))
print(fib(20))
print(fib(10))
print(fib(40))
print(fib(300))

@lru_cache()
def my_func(l):
    print('calling my func')
    return l


print(my_func(10))







