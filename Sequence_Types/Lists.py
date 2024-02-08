"""LISTS SEQUENCE DATA TYPE

--> It is a heterogeneous, mutable container type (can contain many data types and allows us to add or remove
elements inside it)
--> It is a sequence type, meaning the order of numbers are indexed from 0 upwards.
--> Last number is indexed n-1 where n is the number of objects in the sequence.
--> Lists have unbounded growth, since we can add as many elements as we want
--> Lists are objects: They have state (the elements contained in a list)
                        They have functionality (to retrieve elements, remove, add elements and so on)
--> Lists can be nested
--> Elements can be referenced by its index.
--> Use len() function to find the length of a list

        LIST LITERALS
Python Lists can be created using literals, which enclosing them in square brackets

    REPLACING ELEMENTS
--> The indexes must be valid when replacing elements! You cannot replace elements out of the bounds of the indexes
l = [10, 20, 30, 40, 50]
l[INDEX] = replacementValue

    CREATING EMPTY LIST
L = [] OR
L = list()
"""

myList = [10, 3.14, True]
print(myList)

nestedList = [10, 20, 30, myList]
print(nestedList)

nestedList = [10, 20, 30, [10, 3.14, True]]
print(nestedList)

print(myList[0], myList[1], nestedList[3])

len(myList)
print(len(nestedList))
print(myList.__len__())

myList[1] = True
print(myList)

l = [10, 20, 30, 40, 50]
type(l)
print(l[0])

print(len(l))

"""
Negative Indexes...
"""
print(l[-1])
print(l[-5])

# LAST ELEMENT
print(l[-1])

# Creating Empty Lists
l = list()

myList[2] = 3.14
myList[-1] = 'Hello'

print(myList)
