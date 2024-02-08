"""
                            SPECIAL METHODS
--> There are many methods that provide special behavior to our custom classes.
--> These methods/functions are special functions:
    --> start and end with double underscores.
    --> They are often referred to as dunder methods.
    --> NOTE: DO NOT USE THIS CONVENTION FOR YOUR METHOD NAMES!

                        TWO SPECIAL METHODS: __str__ and __repr__
--> str(c) will call c.__str__()
--> repr(c) will call c.__repr()
--> __str__ is used for string representation for users. To display string to user.
--> __repr__ is used for string representation for developers (because it gives more details on the string
representation of the object)
--> print(c) uses __str__ if the method is present for the class
    --> Otherwise it users __repr__ if the method is present for the class,
    --> Otherwise it uses the default class name and object ID, just like for printing the class object on its own.

                                        OBJECT EQUALITY
--> If there are two different lists with the same elements,
    --> they are equal objects i.e list1 == list2 returns True
    --> but they are not the same objects list1 is list2 returns False
--> However, for classes, if there are two custom objects of a class, the objects are not the same and are not equal
    --> i.e p1 == p2 returns False, and p1 is p2 returns False
--> We can override the equality definition for our custom objects using the __eq__ method.


"""

l = [1, 2, 3]
print(l)


class Circle:
    def __init__(self, radius):
        self.radius = radius


c = Circle(10)

print(c)  # prints class name and object ID


class Person:
    def __init__(self, name):
        self.name = name  # Initializing the instance methods

    def __eq__(self, other):  # Overriding __eq__
        return self.name == other.name


p1 = Person('Alex')
p2 = Person('Alex')

print(p1 == p2)

print(p1.__eq__(p2))


class Circle:
    def __init__(self, radius):
        self.radius = radius


c = Circle(radius=1)
print(str(c))  # prints class name and custom ID
l = [1, 2, 3]

print(str(l))

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return 'this is our custom string representation for this class Circle'


c = Circle(1)

print(c)
print(str(c))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f'this is a Circle({self.radius})'


c = Circle(radius=3)
print(str(c))
print(c)

from decimal import Decimal

d = Decimal('10.56')

print(str(d))

print(repr(d))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f'this is a Circle({self.radius})'

    def __repr__(self):
        return f'Circle(radius={self.radius})'


c = Circle(10)
print(c)
print(str(c))
print(repr(c))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f'Circle(radius={self.radius})'


c = Circle(10)
print(str(c))
print(repr(c))

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 == l2)

c1 = Circle(1)
c2 = Circle(1)

print(c1 is c2)
print(c1 == c2)

print(c1 == c1)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f'Circle(radius={self.radius})'

    def __eq__(self, other):
        print(f'__eq__ called: {self}, {other}')
        return True


c1 = Circle(1)
c2 = Circle(10)
print(type(c1) is Circle)
print(isinstance(c1, Circle))

print(c1 == c2)

print(c1 == 'a string')


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f'Circle(radius={self.radius})'

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False


c1 = Circle(1)
c2 = Circle(1)
c3 = Circle(10)

print(c1 is c2)
print(c2 is c3)

print(c1 == c2)
print(c1 == c3)

print(c1 == 'a string')


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __repr__(self):
        return f'Circle(radius={self.radius})'

    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius
        # return True if isinstance(other, Circle) and self.radius == other.radius else False


c1 = Circle(1)
c2 = Circle(1)
c3 = Circle(10)

print(c1 is c2)
print(c2 is c3)

print(c1 == c2)
print(c1 == c3)

print(c1 == 'a string')

print(c2 == 10)

c1 = Circle(10)
c2 = Circle(100)

# print(c1 < c2) To do this, you have to define a less than method in the class using def __lt__(self, other)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f'Circle(radius={self.radius})'

    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius
        # return True if isinstance(other, Circle) and self.radius == other.radius else False

    def __lt__(self, other):
        return isinstance(other, Circle) and self.radius < other.radius


c1 = Circle(1)
c2 = Circle(1)
c3 = Circle(10)

print(c1 is c2)
print(c2 is c3)

print(c1 == c2)
print(c1 == c3)

print(c1 == 'a string')

print(c2 == 10)

c1 = Circle(10)
c2 = Circle(100)

print(c1 < c3)
print(c1 < 10)
