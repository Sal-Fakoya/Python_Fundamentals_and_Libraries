"""
            ITERABLES: have .iter()
--> An iterable is something that can be looped over, e.g a list
--> How can we tell if something is iterable?
    --> If something is iterable, it needs to have a special method called __iter()__ or .iter() method
--> We can run the .iter() on the iterable e.g list to make it an iterator
--> Iterables do not have a state and therefore don't know how to get their next value, hence iterables are not
iterators
    e.g print(next(list_name)) gives a TypeError because iterable is not an iterable and doesn't have a .next() method.


                ITERATORS:
--> An iterator is an object with a state so that it remembers where it is during iteration
--> An Iterator has a state where it knows where it is during iteration, and it also knows how to get their next value.
--> Iterators get their next values using the __next()__ or .next() method
--> Iterators must also have the __iter()__ or .iter() method, and the __next()__or .next()
--> Iterators are also iterables. The difference is __iter()__ returns 'self'
--> Iterators can only be accessed forward, hence there is no going backwards or resetting or making a copy of it
--> Basically (or fundamentally) a for loop gets an iterator of an object and gets the next values until it hits a
stopIteration. It basically iterates an iterator of an iterable and uses the next method on the iterator
--> Unlike iterables, iterators do not need to end (i.e can continue on infinitely in a loop). Iterators are
fine as long as it has a
next value it
will yield

                            GENERATORS
--> Generators are iterators as well, but the __iter()__ and __next()__ are created automatically
-->

"""

nums = [1, 2, 3] #iterable

i_nums = iter(nums) #iterator of nums list
# for num in nums:
#     print(num)

print(i_nums) #prints list iterator
print(dir(i_nums))  # this returns the methods and attributes of nums list

# print(next(i_nums)) #prints next value of the list
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


for i in iter(nums):
    print(i)

i_nums = iter(nums)
for i in iter(nums):
    print(next(i_nums))


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1,10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

# nums = MyRange(1,10)
#
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

x = [1,2,1,3,4,1,4,2,1]

most = max(x, key=x.count)
print(most)

most = max(set(x), key=x.count)
print(most)







