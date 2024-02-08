
"""
                    INDEXING SEQUENCES
---> First object is indexed as zero, Last element is indexed as -1

                    HOMOGENEOUS VS HETEROGENEOUS:
--> Homogeneous types can contain objects of all the same type
--> Heterogeneous types can contain objects that are of different types


                        EXAMPLES OF SEQUENCES:
--> Lists are mutable, heterogenous sequence types
--> Tuples are immutable heterogeneous sequence types
--> Strings are immutable homogenoeus sequence type

                LISTS:
--> It is a container type
--> It is a sequence type. Elements are ordered sequentially and can be indexed.
--> It can be heterogeneous
--> Lists are mutable, i.e, you can add, replace or remove elements.
--> Lists have unbounded growth, can add as many elements as we want, but lists are still finite
--> Lists are objects. They have state and functionality.
--> Lists can be nested.

            THE STR TYPE:
--> It is a container type
--> It is also a sequence type.
--> Strings are homogeneous, i.e they can only contain characters (unicode)
--> They are immutable.

                SLICING SEQUENCES:
--> Slicing is a way to extract ranges of elements from a sequence
--> Start index is inclusive of the element
--> Stop index is exclusive of the element
--> Slices are the same as the sequence being sliced.
--> You can create new sequences by slicing
--> Including last element in a slice: s[6:]
--> s[start:stop:step]


                    MANIPULATING MUTABLE ELEMENTS:
--> Replace elements:
    -->  We can replace elements at an index bu assigning a new element to that index
--> Replacing an entire slice:
    --> Just assign a new collection to the slice
    --> Slice will be replaced with elements in RHS
    --> Number of elements on RHS may not be equal to number of elements on LHS, excepts when it comes to step slicing.
    --> In step slicing, number of elements on both sides must be equal.
--> Delete elements or slice of elements:
    --> Simply use the del keyword
--> Add elements
    --> Often appended at the end by using .append() method.
    --> We can also add multiple elements by extending the sequence: use .extend() method
        --> .extend() takes only one argument, which can be any seequence
    --> We can also specify where in the sequence to insert
--> Inserting elements at some index:
    --> use .insert(where_to_insert, what_to_insert)


                    UNPACKING SEQUENCES
--> Using assignment operation
    --> Number of elements in sequence on LHS must be equal to number of symbols on RHS
    --> You can also unpack slices, as ling as the slice is part of an iterable on RHS


                COMMON STRING METHODS: never modify a string, rather they return new strings
--> Case mappings:
    --> string_name.capitalize()
    --> sting_name.upper() and string_name.lower()
    --> string_name.title()
    --> string_name.casefold() : used for caseless comparisons
--> .count()
--> Stripping start and end characters:
    --> string_name.lstrip()
    --> string_name.rstrip()
    --> string_name.strip() strips all white space on both ends of a strip
    --> string_name.strip(some_character): strips the character specified from both ends of the string

--> Splitting strings: are useful for parsing data from text file. It returns a list of strings
    --> string_name.split(some_character)

--> Joining Strings: concatenates ANY SEQUENCE of strings with some character specified, to create a new string.
    --> some_character.join(string_name)

--> Finding substrings:
    --> Use the "in" operator to check whether a sequence is contained inside another. This works for other
    sequences as well
    --> string_name.startswith(some_character) checks if the string starts with some character.
    --> string_name.endswith(some_character) checks if the string ends with some character.

--> Findig the index of a Substring: Used to know when the index of the start position of a substring.
    --> string_name.index(some_character): use this method in a try except. Moreover, index applies to all sequences
    --> string_name.find(some_character):  returns -1 if substring is not found. This method does not require to be
    used in try except. .find() applies to strings alone.

"""

l = [10,20,30,40,50]

print(len(l))


l = [] #Empty list
print(len(l))

# Replacing list elements
l = [10,20,30,40,50]
print(l[2])

l[2] = True

print(l[2])
print(l)

print(l[-1])
print(l[-5])

print(l[len(l) - 1])

print(l[-1])


l = []

print(type(l))

l = list()

print(type(l))


l = [10,20,30,40,50]

l[2] = 3.14
l[1] = 'Hello'

print(l)


# TUPLES:

t = 10,20,40, [True, True]

print(t[-1][0])
t[-1][0] = 'Left'

print(t)

l = (10,20,30)

l = list(l)
print(l)


# STRINGS
s = 'Python'

print(len(s))

print(s[0])


a = 'Hello'

print(a)

t = 1,2,3

print(str(t))

s = str(t)
print(s)
print(len(s))

print(s[0])


s = "Python"
t = tuple(s)

print(t)


l = list(s)
print(l)

l = ['a', 'b', 'c', 'd', 'e', 'f']

l = list('abcdef')

print(l)

s = '='*20

print(len(s))

t = (1,2,3)*3
print(t)
l = [1,2,3]*3
print(l)

l = [0]*10
print(l)

t = ([1,2], 30)

t2 = t*3

print(t2)

print(t2[2] is t2[0])

print(t2[4] is t2[0])


m = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

print(m[0][0], m[0][1], m[2][2])

l = [10,20,30,40]

print(l[0:2])

l[0:3] = [4,5,9]

print(l)

s = 'Isaac Newton'
print(s[0:4])

print(s[:])

print(s[0:])
print(s[2:10:2])


print(s[9:6:-1]) #Moving backwards
print(s[:6:-1])
print(s[3::-1])
print(s[::-1])
print(s[::-2])

my_list = [1,2,3,4,5]

my_list[0:3] = ['a', 'b']
print(my_list)

my_list[0:3] = 'a', 'b'
print(my_list)

my_list[0:3] = 'mkkan'
print(my_list)


del my_list[2]
print(my_list)

my_list.insert(0, 100)
print(my_list)


l = [10,20,30,20,420,15]

l[1:3] = 'python'

print(l)

l = list(range(1,9))

print(l)

l[1::2] = 20,40,60,80

print(l)

l[1::2] = 20,40,60,80
print(l)

l[1::2] = 5,8,9,4
print(l)

l.append('python')
print(l)

# Extend
l.extend('cat')
print(l)

l = [1,2,3,4]
l.extend([5,6,7,8])
print(l)
l.extend(range(5, 10))
print(l)

l.insert(2, 'cat')
print(l)

l.insert(4, ['dog', 98])
print(l)

a,b,c = (1,2,3)

print(a,b,c)

a,b = [10,20]

a,b,c = 'XYZ'
a,b = b,a

print(a,b)

t = a,b
print(t)

b,a = t
print(b,a)

data = ['10','20','30', 'cat']

data = ', '.join(data).strip()

print('='.join('python'))

print(data)

print('pyt' in 'Python'.casefold())

print(','.join('can you see?'))
print(','.join(['I', 'Mean It']))


data = 'Jones,Peter'


last_name, first_name = data.split(',')

data = ['item 1', 'item 2', 'item 3']

print(', '.join(data))

print(', '.join('abcd'))

print('rock' in 'python rocks')

print(1 in [1, 2, 3])

print('abc' in ('abc', 'def'))

print('Python rocks'.startswith('Python'))

print('Python rocks'.casefold().startswith('PYthon'.casefold()))

'Python rocks'.casefold().endswith('ROCKs'.casefold())


message = 'To every action there is always an equal and opposite reaction.'

print(message.casefold().index('every'.casefold()))
print([11213, 5].index(5))

print(message.casefold().find('eveery'.casefold()))

print(message.casefold().index('action'.casefold(), 9+len('action')))
