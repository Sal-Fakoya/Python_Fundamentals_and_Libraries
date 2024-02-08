"""


"""
# Importing relevant modules...
import numpy as np

# Shape of an array.
arr = np.array([
    [1, 2, 3, 10],
    [4, 5, 6, 10],
    [7, 8, 9, 10]
])
print(arr)  # Arrays are not separated by commas like lists

# This will print (3,4) because we have 3 elements and inside those elements we have 4 elements.
print(arr.shape)
# Rows in a 2-D array must have the same number of columns

# RESHAPING ARRAYS
# Let's suppose we have an array of students' ages abd we have 3 students of each age
students = np.array([19, 19, 19, 20, 20, 20, 21, 21, 21])

# Let's suppose we have their average exam score over the year
exam_score = np.array([57, 60, 65, 59, 63, 70, 65, 72, 75])

# Splitting up exam_score
exam_split = exam_score.reshape(3, 3)
print(exam_split)

# We can't reshape every single array! e.g
# exam_split = exam_score.reshape(2, 4)
# The two numbers you input into the reshape command must multiple together to create the number of elements within
# the original array

exam_split2 = exam_score.reshape(1, 9)
print(exam_split2)

exam_split2 = exam_score.reshape(9, 1)
print(exam_split2)

# We can reshape into 3-Dimensional as well
one_dim = np.array([1, 2, 3, 4, 5, 6])
print(one_dim.reshape(1, 6))
two_dim = one_dim.reshape(2, 3)
three_dim = one_dim.reshape(2, 3, 1)
print(three_dim)
# This will take [1,2,3,4,5,6] and break it into 2 arrays
# and inside those two arrays, it will have 3 arrays of 1 element hence (2,3,1)

five_dim = np.array([17, 5], ndmin=5)
print(five_dim)
print(five_dim.shape)

three_dim = [[[1, 2, 3]]]

# Slicing One-Dimensional Arrays
one_dim = np.array([1, 2, 3, 4, 5])  # One-dimensional array
print(one_dim[0])
# This will return elements from the first element to the fourth element
print(one_dim[0:4])

# This will return elements from the second element to the third element
print(one_dim[1:3])

# This will return the whole array
print(one_dim[:])

# This will return elements from the second element to the end of the array
print(one_dim[1:])

# We can recall elements in steps
print(one_dim[:4:2])
print(one_dim[::2])
print(one_dim[:5:2])

# Two-Dimensional Array Slicing
two_dim = np.array([
    [1, 2, 3],
    [4, 5, 6]])
# This will return a slice from the first element to the second element from the second dimension [4,5]
print(two_dim[1, :2])

two_dim = np.vstack((two_dim, [7, 8, 9]))

# From first two elements, return first elements
print(two_dim[0:3, 0])

# From all elements, slice from index 0 to index 2
print(two_dim[0:3, 0:2])