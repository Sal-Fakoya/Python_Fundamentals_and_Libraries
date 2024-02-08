"""
                            ASSOCIATIVE ARRAYS
--> In Python Sequences and NumPy arrays, indexes are postional and implicit. There is an association between numpy
indices and values, known as associative array. An index provides unqiue mapping between indices and values.
--> Python dictionaries are another type of associative array. There is mapping between keys and values. Keys are not
positional based. The indexes are unique and not implicit.
--> Pandas series is another type of associative array.

                    PANDAS SERIES
--> Pandas series is another type of associative array.
    --> It has some dictionary-like properties.
    --> It has some sequence-like properties.
--> It is a sequence type, so elements have a definite position in collection.
    --> So, series have a positional index that are implicit like lists and NumPy.
--> We can also define an explicit index, also known as a second index.
    --> Indices are also referred to as labels.
--> We can reference items by positional indices.
--> We can also reference items by using the explicit index.
    --> We can even use slicing and fancy indexing, even with an implicit index that is not numerical, e.g
        we can slice using strings ['a':'c'], ['a':'c':some_step]
--> Slicing has a twist.
    --> We can use positional index : implicit indexing which is exclusive of the endpoint
    --> We can use defined indexes, i.e explicit indexes e.g ['a':'c']: which is inclusive of the endpoint.
--> If both implicit and explicit index contain integers,
    --> using a single index value: Pandas would use explicit indexing
    --> using a slice index: Pandas would use implicit indexing
        --> This can be confusing: so use loc and iloc attributes

                            LOC AND ILOC ATTRIBUTES
--> loc : location
--> iloc : implicit location
--> loc and iloc allow us to specifically indicate use of implicit or explicit indexing.
    e.g for a series :
                    s =  100, 200, 300, 400
        implicit index:   0,  1,    2,   3
        explicit index:   2,  3,    4,   5

        s.iloc[2] uses implicit index and returns 300
        s.loc[2] uses explicit index and returns 0

                    DELETING ITEMS FROM A SERIES
--> Indexes are immutable.
    --> Deleting an item would require deleting the corresponding value.
--> Use the .drop() method. This method returns a new series with new explicit index that's been modified appropriately.

                    CREATING SERIES OBJECTS
--> from pandas import Series
    --> We can create a Series from a dictionary by passing the dictionary into the Series: Series(some_dicitonary)
        s = Series({'a':1, 'b':2})
        values of dictionary for values
        positional values for implicit index : 0, 1
        keys for explicit index: a, b
    --> We can create a Series from a list, by specifying explicit index using another list, since a list only has
    positional values.
        --> s = Series([1, 2], index=['a', 'b'])

                    SERIES ATTRIBUTES AND METHODS
--> .index : returns the explicit index object
--> .values : returns a NumPy array of the values
--> .items : zips up the explicit index values (keys) and array values(values of a dictionary). Basically returns a
tuple of explicit index (key) and values like in dictionary
--> .iloc: used for indexing using implicit index
--> loc : used for indexing using explicit index.
--> .drop(): used for removing an element by using explicit index
"""
import pandas as pd
import numpy as np

# Series is basically a 1-Dimensional array with a specific index: explicit and implict

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

# Explicit indexing:
print(s['a'])
print(s['c'])

# Adding Additional vales to the series
s['d'] = 500
print(s)

# Creating a Series with Dictionary
capitals = {
    'USA': 'Washington D.C.',
    'Canada': 'Ottawa',
    'UK': 'London',
    'France': 'Paris'
}

# Keys in the dictionary become explicit indexes
# Values in the dictonary are values in the series
s = pd.Series(capitals)
print(s)

# Getting the index objects from a series by using the index property: some_series.index
print(s.index, type(s.index))
print(s.values, type(s.values))
print(s.index[0])
print(s.index[1])

# some_series.index() return a zip function of tuples containing index and values
print(s.items())
print(list(s.items()))

# Unlike a python dictionary, the index of a series can contain repeated elements
areas = pd.Series(
    ['USA', 'Topeka', 'France', 'Lyon', 'UK', 'Glasgow'],
    index=['country', 'city', 'country', 'city', 'country', 'city'])

# For repeated indexes, result would be a series containing the explicit index and the values
print(areas)
print(areas['country'])
print(areas['city'], type(areas['city']))

# Re-assigning all city's values in the series
areas['city'] = 'London'
print(areas)

areas = pd.Series(
    ['USA', 'Topeka', 'France', 'Lyon', 'UK', 'Glasgow'],
    index=['country', 'city', 'country', 'city', 'country', 'city'])

print(areas)
print(areas.iloc[0])
print(areas.iloc[1])
print(areas.iloc[2:])

areas.iloc[5] = 'London'
print(areas)

#
s = pd.Series([10, 20, 30, 40, 50], index=list('abcde'))
print(s)

# slicing from a to d : explicit indexing is inclusive of last element
print(s['a':'d'])

# slicing with implicit indexing is exclusive of last element
print(s.iloc[:3])

# Fancy indexing
print(s[['a', 'c', 'd']])
print(s[np.array(['a', 'c', 'd'])])

s = pd.Series([100, 200, 300], index=[10, 20, 30])
print(s)
print(s[10])  # is called explicitly.

#  Use .loc and .iloc to access explicit and implicit indexes from now on
# Explicit indexing
print(s.loc[10])
print(s.loc[10:30])

# implicit indexing, i.e positional indexing
print(s.iloc[0])
print(s.iloc[0:2])
print(s.iloc[[0, 2]])

s = pd.Series([100, 200, 300], index=[10, 20, 30])
print(s.iloc[0:3])

# To slice all the way to the last element, stop index can be out of bounds. This is mindblowing...
print(s.iloc[0:50])

a = list(range(1, 10))
print(a[0:60])
print(a[2: 8222])

arr = np.array(a)
print(arr[:55566])

arr = np.array([a])
print(arr)
print(arr[0, :652])

s.name = 'test'
print(s)


areas = pd.Series(
    ['USA', 'Topeka', 'France', 'Lyon', 'UK', 'Glasgow'],
    index=['country', 'city', 'country', 'city', 'country', 'city'],
    name='Areas')

print(areas)

# Boolean Masking
print(areas[areas != 'Glasgow'])

# Deleting/Removing items from a Series: drop() method
s = pd.Series([10, 20, 30], index=list('abc'), name='test')
print(s)

# Dropping 'a' : drop() doesn't mutate the series. It creates a new series
# Drop by explicit index
new = s.drop('a')
print(new)

new_s = s.drop(['a', 'c'])
print(new_s)

print(s)

# Retrieving explicit index with implicit index: .index(specify_implicit_index)
r = s.index[[0, 2]]
new_ = s.drop(r)
print(new_)










