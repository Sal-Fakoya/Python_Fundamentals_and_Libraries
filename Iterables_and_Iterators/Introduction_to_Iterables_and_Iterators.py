"""
            ITERABLES AND ITERATORS
--> An iterable is something that can be iterated over, i.e we can take one element, then the next, until all
elements have been covered.
--> No specific iteration order is mandated
--> A sequence type is iterable (has positional ordering)
--> Dictionaries can be iterated over (insert order)
--> We are also sets: iterable, but no guaranteed order of any kind.
--> The general idea behind iteration is that we start somewhere in the collection, for instance at the beginning,
    --> keep requesting the next element until there's nothing left

--> We have a collection of objects we can iterate over (iterable)
--> An iterator is something that is able to give us the next element when we request it

                SPECIAL ITERABLE METHODS: __iter()__ or iter() method, __next()__ or next() method
--> Iterables implement a special method __iter()__ that returns a new iterator. It can also be called by using the
iter() function
--> __next()__ or next() is a special method that can be called to get the next element.
--> Iterators keep track of what is already handed out (so they are kind of a one-time use)
--> The iterator raises a StopIteration exception when next() us called if there's nothing left

            INTERNAL MECHANICS OF A FOR-LOOP
--> When you do a for-loop, python is first getting the iterator for the iterable that you're iterating over and
using the next() of the iterator until it gets to StopIteration exception

                FEATURES OF ITERATORS:
--> Iterators has some state, i.e, there is no going back or starting from the beginning again
--> If we want to go back, we have to request a new iterator like in for-loop
--> Objects such as lists, tuples, string, dictionaries, set and range objects are all iterables
--> Sine objects like iter() are iterators (not iterables)
--> Iterators only allow us to iterate over them once
"""

l = [1, 2, 3]
iterator = iter(l)
print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) returs a StopIteration exception

print(id(iterator))
iterator = iter(l)
print(id(iterator))

l = [1, 2, 3, 4, 5]

for elements in l:
    print(elements)

iterator = iter(l)
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    print('done Iterating')
    pass

r = range(10)

r_iter = iter(r)
print(next(r_iter))
print(next(r_iter))
print(next(r_iter))

print(list(r_iter))

r = range(100_000_000)
for i in range(100_000_000):
    print(i)
    if i > 4:
        break

from time import perf_counter

start = perf_counter()
l = range(100_000_000)
end = perf_counter()
print(f"elapsed: {end - start}")

start = perf_counter()
l = list(range(100_000_000))
end = perf_counter()
print(f"elapsed: {end - start}")

del l

r = range(10)
print(list(r))

enum_me = enumerate('abc')
print(list(enum_me))

print(list(enum_me))  # will give nothing because iterators can only be used once

flag = 0
while flag:
    print('okay')