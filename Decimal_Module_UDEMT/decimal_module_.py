"""
                    DECIMAL MODULE:
--> Decimal objects can store decimal numbers exactly.
--> Literals are used to enclose numbers when using Decimal module
--> Many specialized math functions are defined in Decimal
--> They use more memory than floats.

                    DECIMAL OBJECTS:
--> Decimal is a data type (or class)
--> Decimal objects can be created using the Decimal() function
--> Integers are represented exactly the same way.
--> When it takes a float, we enclose the float in strings, and those floats will be stored exactly.
--> In terms of precison, 28 is the default precision
--> Leading zeros are ignored, and trailing zeros are taken into account when it comes to precision.


                PRECISION ON DECIMAL OBJECTS:
--> The round() function can be used to specify decimal figures to round.
--> The rounding is 5 significant figures.

                ARITHMETIC CONTEXTS:
--> When arithmetic operations are performed on Decimal numbers, precision can affect results.
--> Rounding mythology can affect results.
--> To view context, settings, call decimal.getcontext()
    --> precision default = 28
    --> rounding = 5 significant figures. Rounding occurs only when specified or during calculations.

                MATHEMTATICAL FUNCTIONS:
--> Arithmetic operators, round(), abs(), min(), max(), sum()
--> Be careful with math module because Decimals get converted to floats first.
--> Decimal objects implement math functions like:
    --> Decimal_item.exp()
    --> Decimal_item.log()
    --> Decimal_item.sqrt()
    --> Decimal_item.ln()
"""

import decimal
from decimal import Decimal

d = Decimal(100)
print(d)

print(Decimal(0.1))  # Float representation of float

print(Decimal('0.1'))  # Exact representation of float

my_d = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3')
# This returns True because this is an exact representation
print(my_d)

print(Decimal('0.1') * Decimal('0.3'))

print(Decimal(1) / Decimal(8))
print(Decimal(1) / Decimal(3))

print(Decimal('1') / Decimal('3'))

print(len('0.3333333333333333333333333333'))
# rounds to 28 significant figures during calculation if round precision is not specified.

print(decimal.getcontext())

print(round(0.1234, 3))

print(round(Decimal('1.135'), 2))

print(round(Decimal('1.145'), 2))

d1 = Decimal('1.20')
d2 = Decimal('2.00') * d1

print(d2)

d1 = Decimal('1.123456789032165564652649206457')
print(len('1.123456789032165564652649206457'))

print(+d1)

print(Decimal(10) // Decimal(3))

print(Decimal(10) % Decimal(3))

print(Decimal('0.1') ** Decimal(5))

k = min(Decimal('0.1'), Decimal('0.2'), 0.3)
print(k)

k = sum([Decimal('0.1'), Decimal('0.1'), Decimal('0.1')])
print(k)

del k
import math

d1 = Decimal('2.0')

result = math.sqrt(d1)

print(result, type(result))

print(d1.sqrt())

f_name = 'DEXUSEU.csv'

with open(f_name) as f:
    for _ in range(5):
        print(next(f).strip())

import csv

with open(f_name) as f:
    reader = csv.reader(f)
    for _ in range(5):
        print(next(reader))

from datetime import datetime


def load_data(f_name, dt_format, use_decimal=False):
    with open(f_name) as f:
        reader = csv.reader(f)
        next(reader)

        data = [
            (
                datetime.strptime(row[0], dt_format),
                Decimal(row[1]) if use_decimal else float(row[1])
            )
            for row in reader
            if row[1] != '.'
        ]
    return data


dt_format = '%Y-%m-%d'

print(datetime.strptime('2010-01-31', dt_format))

data_float = load_data(f_name, dt_format)
data_dec = load_data(f_name, dt_format, use_decimal=True)

print(data_float)

print(data_dec)

from time import perf_counter

start = perf_counter()
for _ in range(10_000):
    result = sum(row[1] for row in data_float)
end = perf_counter()
print(end-start, result)


start = perf_counter()
for _ in range(10_000):
    result = sum(row[1] for row in data_dec)
end = perf_counter()
print(end-start, result)

from sys import getsizeof

print(getsizeof(0.1))

print(getsizeof(Decimal('0.1')))

print(sum(getsizeof(el[1]) for el in data_float))
print(sum(getsizeof(el[1]) for el in data_dec))