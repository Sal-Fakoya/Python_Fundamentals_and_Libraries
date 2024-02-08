"""
                                            CLOSURES
--> We can reference/capture variables of an outer function in an inner function.
--> An inner function can capture variables in an outer function, both arguments and variables defined in the scope
of the argument can be accessed in the body of the inner function.
--> Variables in the scope of a closure can be of any type or class, it can be a custom class, an int, a float,
a function class, etc
"""
import math


#
# def outer(a):
#     def inner():
#         return a * 10
#     return inner

class Outer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_outer(self, c):
        def inner():
            return c * 10 * self.a

        return inner


new_ob = Outer(2, 4)

cat = new_ob.my_outer(c=9)
print(new_ob.my_outer(c=9))  # Prints the inner object type and ID
print(cat())  # Calling the inner function or closure


class Outer:
    def __init__(self, a, b):
        self.c = None
        self.a = a
        self.b = b

    def my_outer(self, c=20):
        self.c = c

        def inner():
            return self.c * 10

        return inner


new_ob = Outer(2, 4)

cat = new_ob.my_outer()
print(new_ob.my_outer())  # Prints the inner object type and ID
print(cat())  # Calling the inner function or closure


class Outer:
    def __init__(self, a, b):
        self.c = None
        self.a = a
        self.b = b

    def my_outer(self, c=20):
        self.c = c

        def inner():
            self.c = 15
            return self.c * 10

        return inner


new_ob = Outer(2, 4)

cat = new_ob.my_outer()
print(new_ob.my_outer())  # Prints the inner object type and ID
print(cat())  # Calling the inner function or closure


class Outer:
    def __init__(self, a, b):
        self.x = None
        self.c = None
        self.a = a
        self.b = b

    def my_outer(self, c=20):
        self.c = c

        def inner(x):
            self.x = x
            return self.x ** self.c

        return inner


new_ob = Outer(2, 4)

cat = new_ob.my_outer()
print(new_ob.my_outer())  # Prints the inner object type and ID
print(cat(x=1))  # Calling the inner function or closure... Here, 1 ** 20 is calculated = 1

new_ob1 = Outer(3, 5)

cat1 = new_ob.my_outer(c=2)
print(cat1(3))


def outer(a, b):
    sum_ = a + b

    def inner():
        prod = a * b
        print(a, b, sum_, prod)
        return f'You just called a closure'

    return inner


func = outer(2, 3)

print(func)

print(func.__closure__)

print(func())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def half_area(self):
        return self.area() * 0.5


def execute(func):
    def inner(a, b):
        result = func(a, b)
        return result

    return inner


def add_two(a, b):
    return a + b


add_executor = execute(add_two)

print(add_executor.__closure__)

print(add_executor(5, 6))


def execute_class(some_class_instance):
    def inner():
        return some_class_instance.area()

    return inner


c1 = Circle(radius=2)
print(c1)

some_func = execute_class(c1)

print(some_func())


def execute_class(some_class_instance):
    def inner():
        return some_class_instance.half_area()

    return inner


c1 = Circle(radius=2)
print(c1)

some_func = execute_class(c1)

print(some_func())


def execute_class(some_class_instance):
    def inner():
        return some_class_instance.radius

    return inner


c1 = Circle(radius=2)
print(c1)

some_func = execute_class(c1)

print(some_func())


def execute_class(some_class_instance):
    def inner():
        return (f'Perimeter of class Circle with area of {some_class_instance.area()} and radius of '
                f'{some_class_instance.radius} is {2 * math.pi * some_class_instance.radius}')

    return inner


c1 = Circle(radius=2)
print(c1)

some_func = execute_class(c1)

print(some_func())


def execute(my_func):
    def inner(*args, **kwargs):
        result = my_func(*args, **kwargs)
        return result

    return inner


def add(a, b, c):
    print('add...')
    return a + b + c


def say_hello(name, *, formal=True):
    print(f'say_hello')
    if formal:
        return f'Pleased to meet you, {name}'
    else:
        return f'Hi {name}'


exec_add = execute(add)

exec_greet = execute(say_hello)

print(exec_add(a=1, b=2, c=3))

print(exec_greet('Alex'))

print(exec_greet('Fred', formal=False))
