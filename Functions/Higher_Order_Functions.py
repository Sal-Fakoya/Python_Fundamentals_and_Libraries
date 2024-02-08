"""
In Python, any object can:
    --> be passed to a function as an argument (or callable in general)
    --> be returned from a function (or callable)

                    HIGHER ORDER FUNCTIONS
--> Functions are Objects
--> Functions that can be passed to and/or returned from functions are called higher order functions
--> Python does not have first-order function. Python has higher-order functions
--> Function definition itself can contain another function definition, meaning functions can be nested
--> The variables in the outer function are available to the inner function

                    PASSING AND RETURNING FUNCTIONS AS ARGUMENTS
--> Function arguments can be functions
    --> The object is passed, not called.
        --> Don't use () to pass a function. The () will return the result of the function instead
--> A function can also return a function
--> Functions that are returned in a function are functions that have been created in the function





"""


# --------------------------------------NESTING FUNCTIONS
def say_hello(first_name, last_name):
    def assemble_name():
        return ' '.join([first_name, last_name])

    return ' '.join(['Hello,', assemble_name(), '!'])


print(say_hello('Eric', 'Idle'))


# ------------------------------PASSING FUNCTIONS AS ARGUMENTS AND RETURNING FUNCTIONS
def add(a, b):
    return (a + b)


def apply(func, *args):
    result = func(*args)
    return result


print(apply(add, 1, -5))


def greet(name):
    return f'Hello,{name}'


print(add(2, 3), greet('John'))

print(apply(add, 2, 3))

print(apply(greet, 'John'))

f = lambda a, b, c: a + b + c

print(apply(lambda a, b, c: a + b + c, 10, 20, 30))

print(apply(f, 10, 20, 30))


# def mult(a, b):
#     return a * b
#
#
# def power(a, n):
#     return a ** n


# def choose_operator(name):
#     if name == 'add':
#         return add
#     if name == 'mult':
#         return mult
#     if name == 'power':
#         return power
#
# op = choose_operator('add')

# print(op)
#
# print(op(2, 3))

def choose_operator(name):
    def adding(a, b):
        return a + b

    def mult(a, b):
        return a * b

    def power(a, n):
        return a ** n

    if name == 'add':
        return add
    if name == 'mult':
        return mult
    if name == 'power':
        return power


op = choose_operator('mult')
print(op(3, 4))

def choose_operator(name):
    if name == 'add':
        return lambda a,b: a+b
    if name == 'mult':
        return lambda a,b: a*b
    if name == 'power':
        return lambda a,b: a**b

op = choose_operator('power')
print(op)

def in_list(l, element):
    return element in l

def in_tuple(t, element):
    return element in t

def in_set(s, element):
    return element in s

from time import perf_counter

n = 10_000_000
l = list(range(n))
t = tuple(range(n))
s = set(range(n))

x = 5_000_000

start = perf_counter()
in_list(l,x)
end = perf_counter()
print(end-start)

start = perf_counter()
in_tuple(t,x)
end = perf_counter()
print(end-start)

start = perf_counter()
in_set(s,x)
end = perf_counter()
print(end-start)

def time_it(func, *args):
    start = perf_counter()
    result = func(*args)
    end = perf_counter()
    print(f'elapsed: {end-start}')
    return result

time_it(in_list, l, x)
time_it(in_set, s, x)