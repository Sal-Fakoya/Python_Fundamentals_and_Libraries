"""
            DICTIONARY AND SET COMPREHENSIONS
--> Identical to list comprehensions, except curly braces are used
--> Dictionary elements are pairs in keys and values and set elements are single values

            DICTIONARY COMPREHENSIONS
--> {key:value for item in items if expr}
    where: key can be any valid expression that calculates a valid key
            value can be any valid expression that calculates some value

            SET COMPREHENSIONS
--> Similar to dictionary comprehensions, but not key: value pairs. Just the "key" portion
--> newSet = {expr1 for item in items if expr2}
    where expr1 can be any valid python expression that calculates some value
"""

# Create a dictionary whose keys are the widget names and values are the number of sales, but only include objects
# that had sale
widgets = ['widget 1', 'widget 2', 'widget 3', 'widget 4']
sales = [10, 5, 15, 0]

d = {}
for i in range(len(widgets)):
    if sales[i] > 0:
        d[widgets[i]] = sales[i]
print(d)

del d
d = {
    widgets[i]: sales[i]
    for i in range(0, len(widgets))
    if sales[i] > 0
}
print(d)

# Given a list of integers, create a set that contains a unique collection of the squares of the even integers
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
s = {number ** 2
     for number in numbers
     if number % 2 == 0
     }

print(s)

# -------------------------------DICTIONARY AND SET COMPREHENSIONS ------------------------------------------------
widget_sales = [
    {'name': 'widget 1', 'sales': 10},
    {'name': 'widget 2', 'sales': 5},
    {'name': 'widget 3', 'sales': 0},
]

# Create a system that creates a list of widget and the quantity that was sold. Name as Key, Sales_Value as Value

sales_by_widget = {}

for d in widget_sales:
    widget_name = d['name']
    sales = d['sales']
    sales_by_widget[widget_name] = sales
print(sales_by_widget)

sales_by_widget = {}

for d in widget_sales:
    sales_by_widget[d['name']] = d['sales']
print(sales_by_widget)

sales_by_widget = {d['name']: d['sales'] for d in widget_sales}
print(sales_by_widget)

sales_by_widget = {}

for d in widget_sales:
    if d['sales'] > 0:
        sales_by_widget[d['name']] = d['sales']
print(sales_by_widget)

sales_by_widget = {d['name']: d['sales'] for d in widget_sales if d['sales'] > 0}
print(sales_by_widget)

# Given a paragraph of text, we want to identify all the words of length 5 or more.
paragraph = """
To be or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them, To die, to sleep--
No more--and by a sleep we say we end
The heartache, and the thousand natural shocks
That flesh is heir to.
"""

punctuation = ",.!:-\n"
print(punctuation)

for char in punctuation:
    paragraph = paragraph.replace(char, ' ')
print(paragraph)

all_words = paragraph.split()
print(all_words)

word = {word.lower() for word in all_words if len(word) > 4}
print(word)

data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']

freq = {}

for element in set(data):
    count = len([char for char in data if char == element])
    freq[element] = count
print(freq)

freq = {
    element: len([char for char in data if char == element])
    for element in set(data)
}
print(freq)

from collections import Counter

freq = Counter(data)
print(freq)
print(type(freq))

print(dict(freq))
paragraph = 'lorem ipsum' * 50
freq = Counter(paragraph)
print(dict(freq))

ignored = ' ,.\n'
freq = Counter(paragraph.casefold())
freq = {key: value for key, value in freq.items() if key not in ignored}

print(freq)

freq = {
    key: value
    for key, value in Counter(paragraph.casefold()).items()
    if key not in ignored
}

