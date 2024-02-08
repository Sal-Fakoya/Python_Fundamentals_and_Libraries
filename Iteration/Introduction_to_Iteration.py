"""
--> Fundamental aspect of writing programs in repetition
--> A case where you know how many times you run the file: deterministic process
--> A case where you do not know how many times we run the file: non-deterministic process


        DETERMINISTIC ITERATION: for loop
--> we iterate over elements of some container such as sequences
--> More generally, we iterate over objects that are iterable (iterables are objects that can be iterated over)
--> Not all iterables are sequences, such as a bag of marble
--> For Loop is used for deterministic iterations

        NON-DETERMINISTIC ITERATION: while loop
--> Iterate while some condition is True
--> While Loop is used for non-deterministic iteration

              THE RANGE OBJECT
--> The range object is an iterable object
--> It serves up integers one by one as they are requested
--> The range object basically serves out integers one at a time, but they do not exist in memory
--> The full list of integers does not exist all at one in memory
--> It is memory efficient
--> It has a finite number of integers
--> We can iterate over a range object
--> Since it exists, it has a finite number of integers, therefore, it is a deterministic iteration
--> We can use the range() function to a range object
        e.g r = range(5)
--> To view contents of the range objects, convert it to a sequence: list or tuple
            r = range(5)
            r = tuple(r) or r = list(r)
--> The range object is iterable. We can use for-loop to iterate over the elements of this iterable hence
can be used to iterate in loops
--> Just like sequences, iterables have length. To chcck the length of range, simply use len(range(value))

                THE RANGE FUNCTION
--> Three types for range function depending on how many arguments are specified
--> It is extremely useful for repeating code a set number of times
--> It is convenient to use for deterministic operations: for loops

            range(end) [one argument]
--> generates integers from 0 (inclusive) to end (exclusive)

            range(start, end) [two arguments]
--> generates integers from start value (inclusive) to end value (exclusive)

            range(start, end, step) [three arguments]
--> generates integers from start (inclusive) to end (exclusive) in steps of step
--> Reminds me of slicing
-->



"""