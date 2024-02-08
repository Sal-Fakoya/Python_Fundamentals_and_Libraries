"""
                                PROPERTIES:
--> We have seen how to define classes and how to:
    --> define instance methods
    --> get/set attributes directly on the instance
    --> We can control things in the __init__ when instances are created, but we cannot control
        how the values can be set subsequently. To control how the values can be set, we use properties.
--> A property is like an attribute, but:
    --> the value is set via a method (setter)
    --> the value is retrieved via a method (getter)
    --> e.g if name is a property in the Person class, and p is an instance,
        p.name = 'Alex' calls the setter method for name, passing 'Alex' and the setter method handles saving the
        data 'Alex' into the state of the class instance.
    --> print(p.name) calls the getter method for name, returning a value

                    READ-ONLY PROPERTIES VS WRITE-ONLY PROPERTIES
--> We can create read-only properties by creating a getter method but don't define a setter
--> We can create write-only properties by defining a setter but without the getter method. It's doable but
    harder to achieve.

                        CREATING READ-ONLY PROPERTIES
--> STEP 1: We define a method, with the name of the property
--> STEP 2: We decorate the method with a @property
--> The user can call the method without parentheses (as an attribute)
--> The method being called can be an internal attribute, meaning, the internal attribute should be initialized with a
single underscore in front of it. It is convention to name internal attributes this way, when we're using setters
and getters in python. Otherwise, we will create an infinite loop and cause maximum recursion error.

FOR EXAMPLE:

class Sale:
    def __init__(self, quantity):
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

                    READ-WRITE PROPERTY
--> First define a getter: @property
--> Then define a setter: variable_name.setter. Setters never return any value
--> NOTE that the property names must match.

                    CALCULATED PROPERTIES
--> Properties are very general:
    --> They are methods.
    --> They do not have to be used just to return an attribute.
    --> They can just calculate and return some value.

"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        print('radius getter called...')
        return self._radius

    @radius.setter
    def radius(self, value):
        print('radius setter called...')
        if not (isinstance(value, float) or isinstance(value, int)):
            raise ValueError('radius is either a float or an int')
        if value < 0:
            raise ValueError('radius cannot be negative')

        self._radius = value

    @property
    def area(self):
        print('area property called...')
        return math.pi * self._radius ** 2


c = Circle(1)

print(c.radius)


