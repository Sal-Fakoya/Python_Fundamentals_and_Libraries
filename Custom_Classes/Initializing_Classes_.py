"""
                            INITIALIZING CLASSES
--> 1. Create a class instance
--> 2. Initialize the instance
--> 3. Return the initialized instance.

                        METHODS
--> A method is just a function that is bound to an object.
--> The __dict__ method is used to check the namescope of the class instance. An alternative is the vars(
_class_instance) function.


                        THE __init__ METHOD:
--> The __init__ function is a special function that is called by Python when we create a new instance of a class.
-->  It is a function defined inside the class, hence, we can define additional parameters.
--> self is not a special name, it's just convention.
--> By default, __init__ is bound to any class created, but defining the __init__ method helps you:
    --> create a custom class that does something once the class is called or an object is created
    --> initialize object instances inside the class
"""


class Circle:
    """
    Circle class
    """


def create_circle(radius):
    c = Circle()
    c.radius = radius
    return c


class Circle:
    def __init__(self):
        print('__init__ called')


class Person:
    """
    Class to represent a Person
    """


p1 = Person()

print(type(p1))

print(hex(id(p1)))


class Person:
    def __init__(self):
        print('custom init...', self)


p = Person()


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name  # initializing instance attribute
        self.last_name = last_name


p = Person(first_name='Eric', last_name='Idle')

p1 = Person('Eric', 'Idle')

print(p1.first_name)
print(p1.last_name)

p2 = Person('John', 'Cleese')

print(p2.__dict__)


class Point:
    def __init__(self, *coords):
        self.coordinates = coords
        print(f'Dimension is {len(coords)}')


p = Point(1, 2)

print(p.coordinates)

p2 = Point(1, 2, 3, 4, 5)
print(p2.coordinates)


class Circle:
    def __init__(self, *, radius=1):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self.radius = radius


c = Circle()
print(c.radius)

c = Circle(radius=10)
print(c.radius)

print(c.__dict__)

print(vars(c))

c1 = Circle(radius=10)
print(vars(c1))
