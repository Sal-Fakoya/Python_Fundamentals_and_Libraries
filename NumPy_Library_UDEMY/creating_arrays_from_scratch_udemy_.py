"""
                                CREATING NUMOY ARRAYS FROM SCRATCH
--> np.zeros(size_or_shape, dtype): is used to create an array containing just zeros
    --> For 1-Dimensional array, we specify a single number, specifying the number of elements in the array
    --> For a 2-D or more, we specify the shape of the array.
        --> Recall that shape of an array is a TUPLE that specifies the number of elements in each dimensions
            of the array.
    --> It is optional to specify the dtype of the array. It defaults to float64.
--> np.ones(size_or_shape, dtype): is used to create an array filled with ones. It follows the same guide as np.zeros.
--> np.full(shape, fill_value, dtype) : creates array filled with some specified constant value
    --> For example, np.full((2,3), 5, dtype=np.int16)
    --> np.full can be used in place of np.ones and np.zeros
--> np.eye(N, M, K, dtype) generates identity matrices of 1 along the main diagonal.
    --> where N is an integer that specifies the number of rows in an array
    --> M is an optional integer that specifies the number of columns of the array. It defaults to N if not given.
    --> k is an optional integer that defines the index of the diagonal to fill with 1s.
--> np.arange(start, stop, step, dtype): generates a 1-Dimensional array based on a range
    --> Just like python range, it is exclusive of the stop value
--> np.linspace(start, stop, num, endpoint, dtype, axis): generates evenly-spaced numbers between start and stop with
    a uniform step size.
    --> start : is the first value of the array, optional, and defaults to 0
    --> stop: is the end of the interval, exclusive (or not included) if endpoint is set to False
    --> num: is the number of samples to generate between start/stop. It is optional and defaults to 50.
    --> endpoint : defaults to True, whether to include the stop value in the array. It is an optional argument
    --> axis: is the axis in the result to store the samples. It is optional and defaults to 0.
--> np.random.random: fills an array with random floats from [0,1), 1 exclusive.
    --> This has a seed method where we can set the seed
--> np.random.randint(low, high=None, shape=None, dtype=int) : generates an array filled with random integers between
[low_value, high_value) two values of low and high. Again it is exclusive of the high_value

"""
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

a = np.zeros(5)
print(a, a.dtype)


a = a.astype(dtype=int)
print(a, a.dtype)

a = a.astype(dtype=float)
print(a, a.dtype)

a = np.zeros((4, 3), dtype=np.uint8)
print(a, a.dtype)

m = np.ones((10, 2), dtype=float)
print(m, m.dtype)

m = np.full((2, 5), 3.14, dtype=np.float32)
print(m, m.dtype)

m = np.full((3, 4), 1, dtype=np.int32)
print(m, m.dtype)

id_matrix = np.eye(5)  # M defaults to 5, so 5x5 matrix
print(id_matrix)

m = id_matrix.astype(dtype=int)
print(m, m.dtype)

m = np.eye(5, 3, dtype=np.uint16)
print(m, m.dtype)

print(list(range(2, 11, 2)))  # in NumPy, we can use arange() to do this

m = np.arange(2, 11, 2)
print(m, m.dtype)

m = np.arange(2, 11, 2, dtype=np.uint8)
print(m, m.dtype)

m = np.linspace(2, 10, num=5)  # default of endpoint is True
print(m)

m = np.linspace(2, 10, num=5, endpoint=False)
print(m)

m = np.linspace(2, 8.4, num=5)
print(m, m.dtype)

arr = np.linspace(2, 10, 10, dtype=float)
print(arr)

x_coords = np.linspace(-2, 2 * math.pi, 50)
# print(x_coords)

y_values = np.array([math.sin(x) for x in x_coords])
print(y_values)

plt.plot(x_coords, y_values)
plt.show()

# Generating arrays using random numbers

# To generate 5 random numbers between 0 and 1
arr = np.random.random(5)
print(arr)

# Setting the seed for np.random.random to 0
np.random.seed(0)
print(np.random.random(5))  # this number will be re-producable since the seed is set

arr = np.random.random((5, 3))  # random numbers of 5 rows and 3 cols
print(arr)

np.random.seed(0)
arr = np.random.randint(1, 10, 50)

print(arr)

from numpy import random as npr

npr.seed(0)
arr = npr.randint(1, 6 + 1, 10)
print(arr)

npr.seed(0)
two_dice_10times = npr.randint(1, 7, (10, 2))
print(two_dice_10times)

npr.seed(0)
two_dice_5times = npr.randint(1, 7, (10, 5))
print(two_dice_5times)
