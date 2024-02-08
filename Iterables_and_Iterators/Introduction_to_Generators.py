"""
                    GENERATORS
--> There are no tuple comprehensions because tuples are immutable
--> A generator is an iterator. It basically operates like the next() iterator
--> A generator calculates and hands out elements one at a time, as requested
        ---> e.g (i ** 2 for i in range(5)) unlike [i **0 for range(5)] which is a list comprehension that
        calculates all the elements and generates the list immediately.
--> A generator uses lazy iteration. A lazy proprerty is a property that is not calculated until it is requested.
--> Generators are more memory efficient however since generators are iterators, I would have to create it twice in
order to use it again.

            WHY USE GENERATORS?
--> Memory Efficiency: e.g it allows us to read from a file, write them out and transform them to another file, e.g
    --> take all rows from a file, and write them out, transformed to some other file
    --> We could use a for-loop or a comprehension for this method, which would require us to read the entire file in
    memory,
    iterate through it and save the rows in another sequence. There might not be enough memory for this!
    --> For-loops and Comprehensions are fine for small files, however, if the files are like 1GB or so,
    you would need
    another
    approach which would not require you to load the files into memory!
    --> Instead of committing them to memory, we can instead read the lines one at a time from a file, process it,
    save it, discard it, and request next row.
    --> Using generators would cause us to use only one line in memory at any point not the entire file
--> For performace reasons (possibly): if you only need to read the first few elements of the iterable,
we do not need to go through computations to calculate everything

            DOWNSIDE OF GENERATORS
--> Since generators are lazy iterators, they're only a one-time use. They're not desirable if you need to iterate
    through the same iterable many times or a few times or IO bound.
--> Testing containment in a generator uses up the generator

            CREATING GENERATORS
--> Use genrator comprehension
--> Use the "yield" keyword in functions instead of return keyword.
"""

squares = [i ** 2 for i in range(5)]
print(squares)

squares = (i ** 2 for i in range(5))

print(type(squares))

for i in squares:
    print(i)

for i in squares:
    print(i)  # This gives nothing because generators are iterators that can be used only once

squares = (i ** 2 for i in range(5))

print(type(squares))

for i in squares:
    print(i)

squares = (i ** 2 for i in range(5))

print(iter(squares))

print(iter(squares) is squares)

print(next(squares))
print(next(squares))

squares = (i ** 2 for i in range(5))

print(3 in squares)
print(3 in [1, 2, 4])

print(list(squares))

squares = (i ** 2 for i in range(5))
print(4 in squares)


print(list(squares))

from timeit import timeit

print(timeit('[i **2 for i in range(25_000_000)]', number=1))

print(timeit('(i **2 for i in range(250_000_000_000))', number=1))







