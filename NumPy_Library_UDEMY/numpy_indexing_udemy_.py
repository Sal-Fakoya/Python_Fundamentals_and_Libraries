"""
                    INDEXING ARRAYS
--> Indexing elements in arrays is similar to indexing in lists
--> In 2-Dimensional arrays, we can access elements using the double brackets:
    --> arr[row_num][col_num]
    --> OR instead, we can pass the row_num and col_num as a tuple only one bracket, e.g
        arr[(row_num, col_num)]
        NOTE that we can also choose to omit the tuple parenthesus
        e.g arr[row_num, col_num]
--> For 1-Dimensional array, we can access it using the plain indexing like in lists

                        MUTATING ELEMENTS IN ARRAYS
--> We can mutate array elements just like python lists by re-assigning the array element with means of indexing
--> When replacing array elements, we need to be careful of data types.


"""

import numpy as np

a = [1,2,3,4]

print(a[2])

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(m[1])

print(m[1][1])

m[1][2] = 100

a = np.array([1,2,3])
print(a[0])

a[1] = 200
print(a)

m = np.eye(3)
print(m[1])

print(m[1][1])

m[1][2] = 100
print(m)

print(m[(1, 2)])
print(m[1, 2])

print(m[1,1])

m[1,2] = 0
print(m)

arr = np.array([1,2,3,4], dtype=np.uint8)
# arr[0]=-100 # Would cause DeprecationWarning
