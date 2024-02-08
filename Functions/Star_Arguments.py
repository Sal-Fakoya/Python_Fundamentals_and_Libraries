"""
                STAR ARGUMENTS
--> Star arguments allow s to specify an arbitrary number or parameters if we want to call the function with
different number of arguments.
--> We can use a * prefix on a parameter name
    --> def average(*parameter_name)
    Here average can be called with any number of arguments
    --> When the * is used to take the arguments as a single value, the parameter name is taken as a
    tuple containing all the argument values
--> Multiple star arguments cannot be used in a function. Only one *parameter is acceptable

            KEYWORD-ONLY ARGUMENTS
--> Are arguments that must be passed as a named argument.
--> They must be called by their keyword when passed after the *arguments

            UNPACKING ITERABLES INTO DIFFERENT ARGUMENTS
--> You can unpack iterables like sequences into different arguments by using the * when passing the argument in a
function,
e.g passing a list
l = [1,2,3,9]
average(*l) #decomposes l into different arguments to be passed into the function
"""


def average(*values):
    print(type(values))
    print(values)


average(1, 2, 3)


def average(*values):
    return sum(values) / len(values)


result = average(1, 2, 3)
print(result)


def my_func(*args):
    print(type(args))
    print(args)


my_func()
my_func(1)
my_func(1, 2, 3, 4, [1, 2], 'abc')


def my_func(a, b, *args):
    print(a)
    print(b)
    print(args)


my_func(1, 2)
my_func(1, 2, 3, 9)
my_func(1, 2, 3, 4, 5)


def my_func(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)


my_func(1, 2, 3, 9, c=3)
my_func(1, 2, 3, 4, c=5)


def my_func(a, b, *args):
    print(a)
    print(b)
    print(args)


my_func(1, 2, 35, 2)


def average(*values):
    return sum(values) / len(values)


result = average(1, 2, 3)
print(result)

def average(*values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0

result = average()
print(result)

result = average(1,2,3)
print(result)

def average(*values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)

result = average()
print(result)
result = average(9,8)
print(result)

def product(*values):
    prod = 1
    for value in values:
        prod *= value
    return prod


print(product(1, 2, 3))


def product(*values):
    try:
        if len(values) == 0:
            raise ValueError('Must provide at least one argument')
    except ValueError:
        return 0
    prod = 1
    for value in values:
        prod *= value
    return prod

result = product()
print(result)

result = product(1,2,3,4)
print(result)

l = [1,2,3,4]
result = product(*l)
print(result)