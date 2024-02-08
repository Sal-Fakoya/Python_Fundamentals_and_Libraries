"""
x = 5
color = 'red' if x < 5 else 'blue'
print(color)

variable = TrueValue if expression else FalseValue

Ternary operators make code easy to read.
They also work inside f-strings or when creating lists, functions and methods, list comprehensions, etc.

TERNARY OPERATORS are operators that take 3 operands
and used on a single assignment conditional

The conditions for a ternary operator:
--> The conditional expression
-> The value to return if the expression is True
-> The value to return if the expression is False

So instead of:

if <condition exp>: var = value1
else: var = value2

You can write in a single ternary operator:
var = value1 if <conditional exp> else value2
-->Python returns value1 if true else value2



"""

x = 5
color = 'red' if x < 5 else 'blue'
print(color)
print(f"{color}")

print(f"The color is {'red' if x < 5 else 'blue'}")

a = 'red' if x < 5 else 'blue', 'yellow', 'green'
print(a)

price = 500

if price < 100:
    volume = 10
else:
    volume = 1

volume = 10 if price < 100 else 1
print(volume)
print(10 if price < 100 else 1)

a =5
b = 2
var = 3

var = (a-b) if (a > b) else (b-a)
print(var)

result = (a/b) if b != 0 else 'NaN'
print(result)
print((a/b) if b != 0 else 'NaN')

a = 10
b = 0

print((a/b) if b != 0 else 'NaN')

ask_price = 100

if ask_price > 50: volume = 50
else: volume = 80

print(volume)

volume = 50 if ask_price>50 else 80
print(volume)

a = 10
b = 20
distance = (a - b) if a >= b else (b-a)
print(distance)

"""
Suppose we are looping (iterating) through some data file and for every row we process we have the following data
--> current value -> the value of some column in our current row. A value of -999 indicates the value is missig
--> running_total -> running total of that column's values so far, possibly zero
--> running_count -> running count of number of rows not including the current one
"""

currentValue = 100
runningTotal = 15000
runningCount = 125
# if currentValue == -999: cleanValue = 0
# else: cleanValue = currentValue
#
# runningTotal = runningTotal + cleanValue
# print(runningTotal)


runningTotal = (runningTotal + 0) if runningTotal == -999 else (runningTotal+currentValue)
print(runningTotal)

runningTotal = runningTotal + (0 if runningTotal == -999 else currentValue)
print(runningTotal)

# Exercise1
a = 5
if a == None: print("N/A")
else: print(a)

# Exercise2
a = ("N/A") if (a == None) else a

# Exercise 3
score = 580
rating = 670

match [score, rating]:
    case [0,580]: print("poor")
    case [580, 670]: print("Fair")
    case [670, 740]: print("Very Good")
    case [800, 850]: print("Excellent")
    case _: print("No grade")

elapsed = 5
minutes = elapsed / 60;

if elapsed < 1: magnitude = 'seconds'
elif (elapsed > 1) & (elapsed < 60): magnitude = 'minutes'
elif elapsed < (24*60): magnitude = "hours"
elif elapsed < (24*60*7): magnitude = "days"
else: magnitude = "weeks"

print(magnitude)