
"""
Slicing is a way to extract ranges of elements from a sequence.
Slicing is used to reverse the order in a sequence.
The start and stop position are index number.

elementSequence [start:stop]
--> the start index is inclusive of the element
--> the stop index is exclusive of the element.
--> slices are the same type as the sequence being sliced.

For instance l = [10, 20, 30, 40]
l[0:2] = [10, 20]
l[1:3] =  [20, 30]

t = (10,20,30,40)
t[0:2] = (10,20)

s ='Isaac Newton'
s[0:4] = 'Isaa'

SLICING TO THE LAST ELEMENT
--> It is okay to specify indexes outside the Bounds when slicing!
--> n = len(element)
--> s[0:n+1] will slice the element to the end
---> s[0:1000] also works for this however, a more meaningful method is
--> s[0:] slices all the elements

TO START AT THE BEGINNING OF A SEQUENCE:
--> This is done by leaving the first index blank.
--> This is valid for start to last index sequenceName[:]

SLICING WITH STEPS: POSITIVE STEPS
--> A step is a way to specify an interval when slicing a sequence.
--> sequenceName[start:stop:step]
[2:10:2]-- start aind include index 2, move in step of 2 elements and exclude index 10
--> are used for moving forwards

NEGATIVE STEPS:
--> This is done by using negative step values.
--> start at index start(inclusive)
--> stops at index end (exclusive)
--> moves backwards so start should be greater than end.

NOTE: Leaving the colons empty as a start or stop value includes
the last index.
--> Slicing creates new objects, but the elements are the same objects as the original ones.

SHALLOW COPY VS DEEP COPY:

"""
l = 10,20,30,40,50,60,70,80,90,100
print(l[9:6:-1])

print(l[:6:-1])
print(l[3::-1])
print(l[::-1])

s = 'Isaac Newton'
print(s[:5:-1])
print(s[::-1])
print(s[::-2])

s = 'Python Rocks!'
print(s[5])

print(s[0:5])
print(s[0:5 + 1])

t = 1, 2, 3, 4, 5
print(type(t[1:4]))

l = list(t)
print(l[1:4])
print(type(l[1:4]))

l2 = l[0:3]
print(l is l2)

l2[0] = 100
print(l2)

l = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]

sub = l[0:2]; print(sub)
print((sub is l))

sub[1] = 'Python'
print(sub)

print((sub[0] is l[0]))

sub[0][0] = 100
print(sub); print(l)

s = 'Python rocks!'
print(s[7:])

print(s[0:6])
print(s[:6])

l = [1,2,3,4,5]
l2 = l[:]

print((l is l2))

l2[0] = 100
print(l2)
print(l)

s = [1,2,3,4,5,6,7,8,9,10]
print(s[1:8])
print(s[1:8:2])
print(s[1::2])

print(s[0::2])
print(s[::2])

s = 'abcdef'
s = list(s)
print(s)

print(s[-4])
print(s[-1])
print(s[-4:-1])
print(s[-1:-4:-1])
print(s[:-4:-1])
print(s[2::-1])
print(s[2:0:-1])
print(s[::-1])
m = [1,2,30, 100]

print(m[::-1])
a = 'racecar'
print(a == a[::-1])












