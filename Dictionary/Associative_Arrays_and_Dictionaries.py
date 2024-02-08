"""
                A DICTIONARY
--> A dictionary is a data structure that associates a value to a key
    --> where both value and key are python objects
    --> Key must be a hashable type, such as immutable sequences like sting, ints, bool, float, etc, but not lists
    --> Keys must be unique, meaning a dictionary cannot contain the same key twice
    --> The value can be any type including dictionary. A value can be a list, tuple, string, etc
    --> Dictionaries are not hashable objects, hence a dictionary cannot be used a key in another dictionary
    --> The type for a dictionary is dict
    --> A dictionary is a collection og key:value pairs
    --> A dictionary is a container object hence it is iterable
    --> A dictionary is not a sequence type
    --> Values are looked up by key (not by index)
    --> Technically, there is no ordering in a dictionary
--> A dictionary is a mutable collection hence it is not itself a hashable object

                DICTIONARY LITERALS
--> Dictionaries can be created using literals (use of curly braces)

                LOOKING UP VALUES IN A DICTIONARY:
--> Use [] just like for sequence types
    --> but instead of an index value, we specify the key.
        dictName[key]

                REPLACING ASSOCIATED VALUES IN A DICTIONARY:
--> Change a value by re-assigning a dictionary key to something else
        dictName[key] = newValue

                ADDING A NEW KEY:VALUE PAIR TO A DICTIONARY:
--> Simply assign a value to a new key
    --> If the key exists, the value will be updated else a new key:value is created

                    DELETING A KEY:VALUE PAIR: del keyword
--> We can remove key:value pairs from a dictionary using del keyword
--> use the del keyword on the key

                    COMMON EXCEPTIONS:
--> KeyError exceptions include:
    --> Trying to read a non-existent key
    --> Trying to delete a non-existent key
--> TypeError exceptions include:
    --> Trying to use a non-hashable object as a key

"""

d = {
    'a': 97,
    'b': 98,
    'A': 65,
    'B': 166
}

print(d['a'])

d = {'symbol': 'AAPL', 'date': '2020-30-10', 'close': 285.34}
print(d['close'])

d['open'] = 277.14
print(d)

del d['open']
print(d)

d = {
    'a': 1,
    'b': 2,
    'c': 3
}

person = {
    'first_name': 'Eric',
    'last_name': 'Idle',
    'year_born': 2016,
}
print(person['first_name'])
print(person['year_born'])

person['year_born'] = 1943
print(person)

person['month_born'] = 'March'
print(person)

d = {
    3.14:'pi',
    2:'even',
    'prime':7,
}
print(d[3.14])
print(d[2])

# l = [1, 2, 3]
# d = {l: 100}

print(hash(100))
print(hash(3.14))

# print(hash([1, 2, 3]))

t = (1,2,3,4)
print(hash(t))

# t1 = ([1,2] ,3,4)
# print(hash(t1)) ... t1 contains a list hence not hashable

d1 = {
    (0,0): 'origin',
    (1,0): 'unit-x',
    (0,1): 'unit-y'
}
print(d1[(0, 0)])

dNew = {
    'a':1,
    'b':2,
    'c':3
}

print(id(dNew))
del dNew['a']

print(dNew)
print(id(dNew))

# print(globals())

print(type(globals()))

print(globals()['person'])
p = globals()['person']
print(p)
print(p is person)


