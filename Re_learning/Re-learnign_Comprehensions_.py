"""

                LIST COMMPREHENSIONS
--> They allow us to append to the end of a list
They are used to generate a list object
--> Comprehension syntax supports an if-clause which acts as a filter.
    --> In general, [expression1 for item in items if expression2]

                        DICTIONARY COMPREHENSIONS:
--> Dictionary elements are pairs [key,value] pairs.
--> Dictionary comprehensoon: {key:value for item in items if expr}

                        SET COMPREHENSIONS:
--> Set comprehensions have elements, not key, value pairs
--> Uses the same curly brace:
    --> {expr for itemin items if expr2}
--> Used to create a set that contains unique values and so on

-->


                            GENERATORS:







"""
import math

lst = [(0, 0), (1, 1), (1, 2), (3, 5)]

vec = [mag1 ** 2 + mag2 ** 2 for mag1, mag2 in lst]
print(vec)

numbers = range(0, 11, 2)

evens = [number for number in numbers if number % 2 == 0]

print(evens)

vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]

mag = [math.sqrt(vec[0] ** 2 + vec[1] ** 2) for vec in vectors]
print(mag)

my_str = 'Python is an awesome language'.split(' ')

print(my_str)

filtered = [item for item in my_str if len(item) >= 5]

print(filtered)

sales = {
    'widget 1': 0,
    'widget 2': 5,
    'widget 3': 10,
    'widget 4': 2
}

high_sales = [
    key
    for key, value in sales.items() if value >= 5
]

print(high_sales)

m = [[0] * 3] * 3
print(m)

print(m[0] is m[1])
m[0][0] = 100
print(m)

m = [[0, 0, 0] for _ in range(3)]
print(m)

print(m[0] is m[1])

m = [[0] * 3 for _ in range(3)]

for row in range(3):
    for col in range(3):
        if row == col:
            m[row][col] = 1

print(m)

del m

m = [
    [1 if row == col else 0 for col in range(3)]
    for row in range(3)]
print(m)

widgets = ['widget 1', 'widget 2', 'widget 3', 'widget 4']
sales = [10, 5, 15, 0]

high_sales = {
    widget: sale
    for widget, sale in zip(widgets, sales)
    if sale > 0}

print(high_sales)

d = {}

for i in range(len(widgets)):
    if sales[i] > 0:
        d[widgets[i]] = sales[i]
print(d)

numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

numbers = {num ** 2 for num in numbers if num % 2 == 0}

print(numbers)

widget_sales = [
    {'name': 'widget 1', 'sales': 10},
    {'name': 'widget 2', 'sales': 5},
    {'name': 'widget 3', 'sales': 0}
]
# print(high_sales)

sales_by_widget = {}

for d in widget_sales:
    sales_by_widget[d['name']] = d['sales']

print(sales_by_widget)

widget_sales = [
    {'name': 'widget 1', 'sales': 10},
    {'name': 'widget 2', 'sales': 5},
    {'name': 'widget 3', 'sales': 0}
]

high_sales = {
    row['name']: row['sales']
    for row in widget_sales if row['sales'] > 0
}

print(high_sales)

data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd']

count = 0

for uniq in set(data):
    count = 0
    for val in data:
        if uniq == val:
            count += 1
    print(count)

freq = {}

for element in set(data):
    count = len([char for char in data if char == element])
    print(count)
    freq[element] = count

my_dict = {uniq: len([val for val in data if uniq == val]) for uniq in set(data)}
print(my_dict)



