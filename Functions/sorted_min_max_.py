"""
                SORTED, MIN AND MAX FUNCTIONS IN PYTHON
SORTING NUMBERS: sorted()
--> Numbers have a natural sort order.  They can be sorted ascending or descending by that order
--> sorted() is a built-in function that can be used as a collection of numbers
    --> takes a single positional argument: an iterable containing the numbers
    --> By default, it sorts in ascending order
        --> There is a keyword-only argument to 'reverse' the sort order
            --> The default is false, which sorts ascending
            --> if I specify reverse = True, it sorts descending
    --> It always returns a new list
    --> The original iterable is not mutated

SORTING STRINGS
--> Strings have a natural sort order known as lexicographic order
    --> Note that a and A are not the same
--> Python will use alphabetical sorting, but upper case letters are sorted before their equivalent lowercase versions
--> Natural sort order of string is case-sensitive
--> We can "visually" sort other types of objects
        For instance, a list of personc can be sorted by name, age, profession, etc
--> We can always sort by some property of the objects we are sorting

MIN AND MAX
--> used to find the minimum of a collection
--> min and max cannot find the minimum and maximum of empty sequence. It will return a ValueError exception if the
iterable is empty
--> We can specify a default value to return if the iterable is empty, using a keyword-only argument called default
    e.g min([], default=0) #sets the default value of 0 if the sequence is empty
--> We can also use an arbitrary number of positional arguments instead of necessarily passing a sequence in, such as:
    min(1, 10, 2, 9, 3, 8) #which returns 1
    max(1, 10, 2, 9, 3, 8) #which returns 10

"""
t = (1, 10, 2, 9, 3, 8)
sorted_t = sorted(t)
print(sorted_t)
print(sorted(t, reverse=True))  # sorts in descending order
print(sorted(t, reverse=False))  # sorts in ascending order

print(sorted(['Baby', 'baby']))

from copy import deepcopy

l = [1, 10, 2, 9, 3, 8]
t = deepcopy(tuple(l))
s = deepcopy(set(l))

print(sorted(l))
print(l)

print(sorted(t))
print(t)

print(sorted(s))
print(s)

print(sorted(l, reverse=True))
help(sorted)

print(ord('a'))
print(ord('A'))

print('A' < 'a')
print(sorted(('a', 'b', 'c')))
print(sorted('azbycz'))

print(sorted('aAbBxX'))
print(ord('x'))
print(ord('X'))

print(sorted(['Zebra', 'apple'])) # Z is smaller than a
print(sorted(['Zebra', 'apple', 'atom']))

print(sorted([]))

# ---------------------------------------------MIN AND MAX-------------------------------------------------------
l = [1, 10, 2, 9, 3, 8]
sorted_ascending = sorted(l, reverse=False)
print(sorted_ascending)

print(min(l))
print(max(l))

print(min([], default=0))