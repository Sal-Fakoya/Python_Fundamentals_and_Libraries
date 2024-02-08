"""
            MODULES
--> Modules are code files that cab group similar or related functionality together
--> Modules that can be created on other modules are called packages.

            BUILT-INS
--> Python has many built-in object types and functions
    such as bool, int, float, str, tuple, list, dict, print(), filter(), sorted(),zip(), len()

            STANDARD LIBRARY
--> Python has a lot of libraries (modules and packages that come standard with base Python installation
--> To use standard libraries, we have to "load" them using keyword: import
--> Python provides a huge selection of libraries (modules and packages) that cover things like:
        -> Numerical and math
            -> Math functions
            -> stats functions,
            -> random numbers
            -> Decimal objects (alternative to floats)
        -> Date and time
        -> CSV files
        -> Crytography
        -> Networking, internet

                        3RD Party Libraries: such as NumPy_Library_UDEMY, SciPy, QuantLib, Pandas_Library_UDEMY, Matplotlib_udemy_, scikit-learn
--> Many developers create libraries that leverage the standard library (or 3rd party library) but provide a high
level, easier to use interface to more specialized functionality.
--> Sometimes, 3rd party libraries have a narrow and specific focus performance or advanced functionality.
--> A list of 3rd party library source is on Pypi.org

                    BASIC IMPORTS
--> Modules are objects in python

--> e.g import math
    --> math is a module in the standard library for math-related functionality
    --> the math module has been loaded from file
    --> the variable (symbol) math is a reference to that module objects
    --> math contains many functions such as sqrt
    --> Like with any other object, we use dot notation to reach inside the object

--> e.g import some_module as sm
    --> loads some_module
    --> creates a variable some_symbol that references the some_module object

"""

import math

# math now exists as a symbol in the namespace and points to a module object

print(type(math))
print(math.sqrt(2))

help(math)

help(math.factorial)
print(math.factorial(3))
print(math.factorial(4))

# print(math.factorial(x=4)) This will not work because factorial take no keyword arguments

print(math.pi)
print(math.e)
print(math.gcd(15, 25))

import cmath

# --> cmath allows you to work with complex numbers

print(cmath.sqrt(-4))

import math as m

# m is just an alias for math object
print(m.pi)

import numpy as np

print(m is math)

import random as rnd

print(type(rnd))

print(rnd.randint(3, 10))

import os

print(os.path.curdir)

import os.path as os_path

print(os_path.curdir)

import os.path as path

print(path.abspath(path.curdir))

import fractions

f1 = fractions.Fraction(1, 2)
print(f1)

f2 = fractions.Fraction(1, 4)
print(f2)

print(f1 + f2)

print(f1 * f2)

f = fractions.Fraction(0.1)
print(f)

