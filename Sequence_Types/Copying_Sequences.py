"""
SHALLOW VS DEEP COPIES
    A sequence is a collection of references to objects.
SHALLOW COPIES:
--> a new sequence is created, ie not same sequence object as original
--> Elements in the new sequence reference the same elements as the original
--> To make a shallow copy is to make a copy of the original sequence. Since the elements in the orginal copy and
shallow copy have the same objects, they reference the same objects but not the containers are not the same
--> original is shallowCopy will return False.
--> Adding or removing/replacing elements in one copy does not affect the other
--> Mutating the elements will affect both since they share the same reference
--> Shallow copy is a recursive approach
--> Modifications such as insertion, deletion, and replacements can affect the original and vice versa

CREATING SHALLOW COPIES:
--> Use slicing to slice the entire sequence
--> use the .copy() method i.e sequenceName.copy()

DEEP COPIES:
--> a new sequence is created (not the same sequence object as original)
--> each element in new sequence is a deep copy of the original
    -->The elements are totally new and independent objects.
--> To use deep copy, uses the deepcopy function in the copy module
        from copy import deepcopy


NOTE: Shallow Copies applies to mutable sequences only, but deep copy applies to either.
"""
# -----------------------------------------SHALLOW COPY--------------------------------------------------------------
myList = [1, 2, 3]
# USING SLICE
myCopy = myList[:];
print(myCopy)

# USING .copy() method
myCopy = myList.copy();
print(myCopy)
print(myList is myCopy)
print(myList[2] is myCopy[2])

# ADDING OR REMOVING OR REPLACING ELEMENTS DO NOT AFFECT THE OTHER
myCopy[2] = 4;
print(myCopy);
print(myList)
del myCopy[0];
print(myCopy);
print(myList)

# MUTATING ELEMENTS AFFECT THE OTHER SINCE THEY SHARE A REFERENCE
# Adding or removing or appending elements to one object does not affect the other, but mutating the elements inside
# either of them's sequence affect the other; since lists are mutable, mutating the list will affect the other list.
# NOTE, integers and strings are immutable hence they can only be added or removed to the original and copied lists
myList = [['a', 'b'], 2, 3]
myCopy = myList.copy();
print(myList);
print(myCopy)

print(myList[0] is myCopy[0])
print(myList[1] is myCopy[1])
print(myList[2] is myCopy[2])

print(myList is myCopy);
print(id(myList) == id(myCopy));
print(id(myList[0]) == id(myCopy[0]))

myCopy[0].append('c');
print(myCopy);
print(myList)
del myList[0];
print(myList);
print(myCopy)

myCopy[0].append(2);
print(myCopy);
print(myList)

# -----------------------------------------DEEP COPY--------------------------------------------------------------
myList = [1, 2, 3]
from copy import deepcopy

myList = [['a', 'b'], 2, 3]
myCopy = deepcopy(myList);
print(myList);
print(myCopy)
# With deep copy, the original and deepcopy will not reference the same element, instead a new reference is created
# for each object and container, hence mutating or adding or deleting or appending one element will not affect the
# either containers.
print(myList[0] is myCopy[0])
myCopy[0].append('c');
print(myCopy);
print(myList)

# -------------------------------------------------------------------------------------------------------------------
l1 = [1, 2, 3]
l2 = l1[:];
print(l1);
print(l2)

print(l1 is l2)
l2.append(10);
print(l1);
print(l2)
l3 = l1.copy();
print(l3)
print(l1 is l3)

l3.append(10);
print(l3);
print(l1)

m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
print(m1)
m2 = m1.copy()

print(m1 is m2)
m2.append([10, 20, 30]);
print(m1);
print(m2)
print(m1[0] is m2[0])

print(m1[0])
print(m2[0])
m2[0].append(-1);
print(m2);
print(m1)

m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
print(m1)
m2 = deepcopy(m1);
print(m1);
print(m2)
print(m1[0])
print(m2[0])

print(m1[0] is m2[0])

m2[0].append(10);
print(m2);
print(m1)
