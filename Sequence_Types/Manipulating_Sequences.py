"""
MUTABLE SEQUENCES such as lists can be modified. Immutable sequences like tuples and strings are not.
You can:
--> replace elements
--> delete elements
--> add elements
        -- often appended to the end
        -- can also specify where in the sequence to insert

REPLACING ELEMENTS:
--> Replace an element at index i by assigning a new element tot that index.
l[validIndex] = newValue

REPLACING AN ENTIRE SLICE:
--> you can do this by assigning a new collection to the slice
--> slice will be replaced with elements in RHS
Python uses the elements of the sequence in RHS when assigning to a slice,
(but not when assigning using a single index)

DELETING AN ELEMENT:
--> delete an element by an index using 'del' keyword
        del sequenceName[index]
--> You can also delete an entire slice
        del sequenceName[1:3]

APPENDING ELEMENTS: ONE ELEMENT
--> We can add an element to the end of a list using append method
        listName.append(newElement)
        The element being added could be a sequence or integer.
APPENDING ELEMENTS: MULTIPLE ELEMENT
--> to append multiple elements, we extend the sequence
        listName.extend(['a','b','c','d']). This is the same as listName.append(('a','b','c')) and the same as
        listName.extend('abc')
        listName will become = [original List, 'a', 'b', 'c'];

        .extend() vs .append(): append treats the arguments like a single element to be added to the data type,
        while .extend() treats its arguments like multiple elements regardless if entered as a sequence data type.

INSERTING AN ELEMENT:
--> Instead of appending, we can insert at some index.
    --> This method is to be used sparingly hence it is much slower than appending or extending
    listName.insert(index, newElement)
    --> It inserts the element as a single entity
--> It takes in two arguments, one which tells it WHERE to insert. the second tells it WHAT to insert

WHEN REPLACING ELEMENTS USING SLICING WITH STEP SIZE:
--> The number of elements on the RHS must be equal to the number of elements on the LHS when a step size is involved

FINDING SEQUENCES: "in" and .index()
--> use the "in" operator to find a sequence in another sequence, e.g
        "x" in "xyz" --> returns True
        lsit1 in list2 --> returns True/False if list1 exists in list2
-> The "in" operator tests for containment, but it gives no indication
        of where the sequence is.
--> The "in" method doesn't tell whether the sequence is on the start of the bigger sequence or the end of the bigger sequence

"""

# -----------------------REPLACING ELEMENTS--------------------------------------------------------------------------
l = [10, 20, 30]
l[1] = "hello";
print(l)
myList = [1, 2, 3, 4, 5]
myList[0:3] = ['a', 'b']
print(myList)
myList[0] = [1, 2, 2]
print(myList)
myList[0][1] = 'a', ['b']
print(myList)
myList[0][2] = 'ab';
print(myList)
myList[0][1][1][0] = 1, 2, 3;
print(myList)

# -----------------------DELETING ELEMENTS--------------------------------------------------------------------------
myList = [1, 2, 3, 4, 5]
del myList[1];
print(myList)
myList = [1, 2, 3, 4, 5]
del myList[1:3];
print(myList)

# -----------------------APPENDING ELEMENTS--------------------------------------------------------------------------
myList.append(4);
print(myList)
myList.append((1, 2, 3));
print(myList)
myList.append([2, 4, 5]);
print(myList)
myList = [1, 2, 3]
k = 'abc'
myList.extend(list(k));
print(myList)
myList.extend('def');
print(myList)
myList.extend(('g', 'h', 'i'));
print(myList)

# -----------------------INSERTING ELEMENTS--------------------------------------------------------------------------
myList = [2, 3, 4, 5]
myList.insert(0, 100);
print(myList)
myList = [2, 3, 4, 5]
myList.insert(2, 100);
print(myList)

# ---------------------------------------------------------------------------------------------------------------------
myList = [10, 20, 3, 40, 50]
myList[2] = 30
print(myList)
myList = [1, 20, 30, 5, 6]
print(myList[1:3])
myList[1:3] = (2, 3, 4)
print(myList)
myList[1:3] = 'python'
print(myList)

myList = [1, 2, 3, 4, 5, 6, 7, 8]
myList[1::2] = 20, 40, 60, 80
print(myList)

myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(myList[:-3:-1])
myList[:-3:-1] = 100, 200
print(myList)

del myList[2]; print(myList)

myList = [1,2,3,4,5,6]
del myList[::2]; print(myList)

myList = [1,2,3,4,5,6]
myList.append(7); print(myList)
myList.append("python"); print(myList)
myList.extend("python"); print(myList)
myList.append([1,2,3]); print(myList)

myList = [1,2,3,4]
list2 = [5,6,7,8]
myList.extend(list2); print(myList)

myList.extend([10,20]); print(myList)
myList.extend('python'); print(myList)

myList.insert(2, 5); print(myList)
l = [1,2,3,4]; print(l[2])
l.insert(2, 'a'); print(l)

l.insert(0, 'abc'); print(l)

from timeit import timeit
l =[]
print(timeit('l.append(1)', globals=globals(), number=100_000))
print(len(l))
l = [];
print(timeit('l.insert(0,1)', globals=globals(), number=100_000))











