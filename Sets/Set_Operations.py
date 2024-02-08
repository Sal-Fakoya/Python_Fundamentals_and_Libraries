"""
                DISJOINTEDNESS: setName.isdisjoint(setName2)
--> Two sets are disjoint if they have no intersections in common
    --> Returns True if the set are disjoint
    --> Returns False if one or more common elements exist
--> Two Elements are the same if set1 == set2

            ADDING AND REMOVING ELEMENTS: .add(), .remove(), .discard()
--> .add() method adds elements to the set
--> .remove() and .discard() removes element in a list The only difference is
    --> .remove() raises exceptions if the element that is to be removed does not exist
    --> .discard() does not raise any exceptions if the element we're trying to remove exits

                    SET OPERATIONS: SUBSETS(strict subset and subset) AND (strict superset and superset)
--> s1 < s2 returns True if s2 is a strict subset of s2
--> s1 <= s2 returns True if s1 is a subset of s2
--> s1 > s2 returns True if s1 is a strict superset of s2
--> s1 >= s2 returns True if s1 is a superset of s2

                    UNIONS AND INTERSECTIONS
--> s1 | s2 returns the union of s1 and s2, The | symbol is sometimes referred to mean "or"
--> s1 & s2 returns the intersection of s1 and s2

                    SET DIFFERENCE: s1 - s2
--> The difference s1 - s2 of two sets is all the elements of one set minus all the elements of the other set
--> Set difference is not commutative, meaning s1-s2 is not the same as s2 - s1
--> It is basically used to collect the elements in set that are not in another set

____NOTES: Membership testing in sets is much faster than lists or tuples
            --> It is easy to eliminate duplicate values by converting the type to set
            --> It is easy to find common values between two collections by finding their intersection
            --> It is easy to find values that are in one collection but not in another, by finding the set difference


"""

s = set('abc')
print(s)

s.add(5)
print(s)

s.remove('b')
print(s)

s.discard(4)
print(s)

print({1, 2} < {1, 2, 3})
print({1, 2} <= {1, 2, 3})

print({1,2} < {1,2})
print({1,2} <= {1,2})

print({1, 2, 3} > {1, 2})
print({1, 2, 3} >= {1, 2})

print({1, 2} > {1, 2})
print({1, 2} >= {1, 2})

s1 = {1,2,3}
s2 = {3,4,5}

print(s1 | s2)
print(s1 & s2)

print(s1 - s2)
print(s2 - s1)


# ----------------------------------CODING-----------------------------------------------------
s1 = set('abc')
s2 = {True, False}
s3 = {'a', 100, 200}

print(s1.isdisjoint(s2))
print(s2.isdisjoint(s2))

s = set()
s.add(100)
print(s)
s.add(200)
print(s)

s = set('abc')
s.remove('a')
print(s)

s.discard('b')
print(s)

s.discard('x')
print(s)

s1= set('abc')
s2 = set('abcd')

print(s1 < s2)
print(s1 <= s2)

print(s2 >= s1)
print(s2 > s1)

s3 = set('abc')
print(s1 <= s3)

s1 = set('abc')
s2 = set('bcd')

print(s1 | s2)
sNew = s1.union(s2)

print(s1&s2)
print(s1.intersection(s2))

print(s1 - s2)
print(s1.difference(s2))

str_1 = 'python is an awesome language!'
str_2 = 'a python is also a snake.'

set1, set2 = set(str_1), set(str_2)
print(set1); print(set2)
print(set1 & set2)


s1 = {'AMZN', 'FB', 'AAPL', 'NFLX', 'GOOG', 'MSFT'}
s2 = {'BABA', 'WMT', 'COST'}
s3 = {'TSLA', 'F', 'GM'}
consolidated = s1 | s2 | s3
print(consolidated)

consolidated = list(s1 |s2 |s3)
print(consolidated)

sold = {'w1', 'w2', 'w3', 'w4'}
returned = {'w1'}

non_returned = sold - returned
print(non_returned)

alphabet = set('abcdefghijklmnopqrstuvwxyz')

import string #has something called the ascii_lowercase characters
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)

# help((string))

alphabet = set(string.ascii_letters)
text = 'The quick brown fox jumps over the lazy dog'

print(set(string.ascii_letters) - set(text))

print(set(string.ascii_letters.casefold()) - set(text.casefold()))

























