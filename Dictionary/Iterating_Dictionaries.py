"""
-> Dictionaries are iterable
--> We can choose to iterate over keys, values and key:value pairs
--> The default iteration is over the dictionary keys
        e.g data = {'a':1, 'b':2, 'c':3}
        for k in data:
            print(k) #prints the keys in every iteration


            ITERATING OVER KEYS: keys()
--> Dictionaries have .keys() method
--> The .keys() method behaves like .values() or .items(), except that .keys() returns an iterable
        containing the keys of the dictionary
--> It is not used as much because the default iteration is over the keys anyway
        for k in data.keys():
                    print(k) #prints the values in every iteration

            ITERATING OVER DICTIONARY VALUES: using .values()
--> Dictionaries have a method called .values(), which are often used in loops
--> The values method returns an iterable containing just the values of the dictionary
        such as data = {'a':1, 'b':2, 'c':3}
                for k in data.values():
                    print(k) #prints the values in every iteration

            ITERATING OVER KEY:VALUE PAIRS: using .items()
--> Dictionaries have a method called items(), often used in loops
--> .items() returns an iterable containing keys and values in a tuple
        data = {'a':1, 'b':2, 'c':3}
        for t in data.items():
            print(t) #This prints the (key, value) in every iteration
--> We can unpack the key and value in dictionaryName.items() when iterating
        for k, v in data.items():
            print(f"{k} = {v}") #prints the key = value in every iteration

                INSERTION ORDER
--> Python dictionaries have key:value pairs that could be looked up by key
--> The iteration order is maintained in python
--> The iteration order reflects the insertion order
--> The insertion order for a literal is the order in which the key:value pairs are listed out
--> If we order over a dictionary, the order in which the items or keys or values will be returned will be the order
in which they were inserted.
--> Adding a new element. d['x'] = 98
--> If a new element is added to the list, the new element will be the 'last' element
--> Although, dictionaries have ordering, we cannot retrieve elements in dictionary by index


"""
data = {'a':1, 'b':2, 'c':3}
for k in data:
    print(k)

for k in data.keys():
    print(k)

for k in data.values():
    print(k)

for key, value in data.items():
    print(f'{key} : {value}')

d = {
    'key 1': 1,
    'key 2': 2,
    3.14: 'pi'
}

for k in d:
    print(k)

for k in d:
    print(f"d[{k}] = {d[k]}")

for v in d.values():
    print(v)

for t in d.items():
    key, value = t
    print(key, value)

for key, value in d.items():
    print(key, value)
    print(f"d[{key}] = {value}")

d['x'] = 100
print(d)

d['key 1'] = 100

for k in d:
    print(k)

del d['key 1']
print(d)

d['key 1'] = 100
for k in d:
    print(k)































































