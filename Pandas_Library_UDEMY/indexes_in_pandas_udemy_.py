"""
                INDEXES (OR INDICES) IN PANDAS
--> Indexes are also called indices
--> Indices can be identified by position (e.g in arrays and lists), by keys (in dictionaries) or labels (Pandas)
--> An index is a way to 'look' up one or more value in an array or dictionary.
--> The positional index is an implicit index, meaning, we use numbers to access the elements of the sequence.
--> In Pandas, we can define an explicit index (in addition to implicit index).
    --> idx = ['first', 'second', 'third', 'fourth']
        l = ['a', 'b', 'c', 'd']

                        PANDAS INDEX
--> pd.Index(some_list_tuple_nparray) : is the most generic type of Index
    --> they contain elements
    --> they are based on NumPy arrays
    --> They themselves have an implicit positional index.
--> We can create an index by passing a sequence e.g lists, tuple or NumPy array to Index class
    e.g idx = pd.Index([10,20,30,40])
        idx[0] returns 10 (positional indexing)
        idx[1:4] returns Index([20, 30]) : slicing
        idx[[0, 2]] returns Index([10, 30]) : fancy_indexing
        idx[idx%4==0] returns Index([20,40]) : boolean masking
--> Index values do not have to be unique.
    --> e.g pd.Index([1,1,2,3,4,5])
    --> An index value may refer to multiple values in the associated array.

                        SPECIALIZED INDEXES
--> int64 : for indexes that contain integer indexes
--> Float64 : for indexes that contain float indices
--> Range indexes: for integer sequence defined via a range
    --> This is similar to difference between Python list and range
        [0,1,2,3,4,5] : sequence is materialized
        range(0,6) : sequence is not materialized. Rather, elements are produces as requested when iterating.
    --> Range indexes can be more efficient (storage and computation)

                    INDEXES HAVE SET-LIKE PROPERTIES
--> We can define the union and intersection of indexes.
    --> .intersection for intersection of two indexes
    --> .union for union
    --> "in" to test for containment, i.e "element of"
--> Pandas will use broadcast data type needed for union/intersection.
--> RangeIndex indexes will try to return an RangeIndex as a result of union/intersection.

                    STRING, INTEGER AND FLOAT INDEXES
--> Strings will result in an Index object with an object data type (a catchall type)
    --> If indexes, are created with strings, we get an object data type index, e.g
        pd.Index(['a', 'b', 'c', 'd'])
--> Integers will result in an Int64 Index object
    --> pd.Index([1,2,3])
--> Floats will result in a Float64Index object.
    --> pd.Index([0.1, 0.2, 0.3])

                    RANGE INDEXES
--> We can create Range indexes by passing a range object into pd.Index()
    --> pd.Index(range(1, 10, 2))
        RECALL that range(start, stop, step)
--> We can use RangeIndex class directly:
    --> pd.RangeIndex(start, stop, step)

"""
import pandas as pd
import numpy as np

idx = pd.Index([10, 20, 30])
print(idx)

# When we mix data types, Pandas will find a data type that is suitable for all
idx = pd.Index([1, 3.14])
print(idx)

# For string indexes, dtype='object'
idx = pd.Index(['element 1', 'element 2'])
print(idx)

# Array-like behavior
idx = pd.Index([2, 4, 6, 8, 10])
print(idx)

print(idx[0])  # By position
print(idx[1:4])  # By slicing
print(idx[::-1])  # By slicing
print(idx[[1, 3, 4]])  # By Fancy Indexing
print(idx[np.array([1, 3, 4])])  # Fancy Indexing

idx = pd.Index(['London', 'Paris', 'New York', 'Tokyo'])
print(idx[idx != 'Tokyo'])  # Boolean Masking

try:
    idx[0] = 100
except TypeError as ex:
    print('TypeError', ex)

idx1 = pd.Index(['a', 'b', 'c'])
idx2 = pd.Index(['c', 'd', 'e'])

# Intersection of indexes
print(idx1.intersection(idx2))

# Union of Two indexes
print(idx1.union(idx2))

idx1 = pd.Index([1, 2, 3], dtype=np.int64)
idx2 = pd.Index([0.1, 0.2])
print(idx1.union(idx2))

# Range Indexes
idx_range1 = pd.Index(range(2, 10, 2))
print(idx_range1, type(idx_range1))

idx_range1 = pd.RangeIndex(2, 10, 2)
print(idx_range1, type(idx_range1))

print(idx_range1[0])
print(idx_range1[-1])
print(idx_range1[1:4])

idx1 = pd.Index(['a', 'b', 'c'])
idx2 = pd.RangeIndex(0, 10, 2)

print('b' in idx1)
print(6 in idx2)
print('x' in idx1)
print(1 in idx2)


# Pandas Indexes may not be unique
idx = pd.Index([1,1,2,2,3,3])
print(idx)

print(idx[0])
print(idx[1])
print(idx[2])
