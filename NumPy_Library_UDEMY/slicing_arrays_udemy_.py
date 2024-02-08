"""
                        SLICING OF NUMPY ARRAYS
--> Slicing returns a new, independent array.
--> We can mutate a python list by using the assignment operator with a slice definition.
--> Since Python lists are not fixed size, we can also replace the slice with more or less elements.
--> 1-Dimensional NumPy is very similar to slicing python lists.
    --> arr[a:b] exclusive of b
    --> arr[start:stop:steps] exclusive of the stop value
    --> arr[start::steps] returns the start value to the end of the array
    --> arr[::-1] reverses the slicing from the end to the start of the array

                        SLICING 2-D ARRAYS
--> In python list slicing, we cannot slice elements of elements 2-D, ie. along multiple axes
--> NumPy provides support for slicing along multiple axis.
    --> arr[axis0_slice, axis1_slice]
--> We can also use steps in slicing:
    --> arr[axis0_start:stop:steps, axis1_start:stop:steps]
--> Slicing Assignment in NumPy arrays works very similarly to assigning to list slices.
    --> However, we cannot replace an array element with an array element of a different shape.
        --> It also means we cannot change the size of the original array. This makes sense since NumPy arrays are
        fixed size.
        --> Be careful with data types!
--> We can replace elements of a numpy array with a list/tuple/array of the same size as the element(s) being
    replaced in the array.
--> We can also assign a single value (not an array) to a slice.
    --> NumPy basically fills the slice with the same value repeated as many times as necessary. This is called
    "broadcasting"
    e.g arr[::3] = 0
--> Slices are "linked" to original array. This is similar to reshape function earlier.
    --> A slice is linked to the array it was sliced from, so replacing an element in the element will be seen by the
    array and vice versa.
--> To avoid this, make a copy using .copy() method on the slice.


"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
a[0:3] = np.array([10, 20, 30])

l = [1, 2, 3, 4, 5, 6]

arr = np.array(l)

print(arr[0:3])
print(arr[0::2])
print(arr[::-1])

slice_ = l[0:2]

slice_[0] = 100
print(slice_)
print(l)

# Arrays are linked to the slices and vice verse.
arr = np.array([1, 2, 3, 4, 5, 6])
slice_ = arr[0:2]

slice_[0] = 100
print(slice_)
print(arr)

arr = np.arange(1, 7)
slice_ = arr[3:]

arr[-1] = 60
print(slice_)
print(arr)

arr = np.arange(1, 7)
slice_ = arr[3:].copy()

slice_[0] = 0

print(slice_)
print(arr)

# Slicing 2-D Arrays
arr = np.arange(1, 26).reshape(5, 5)
print(arr)

slice_ = arr[:2, :2].copy()
print(slice_)

slice_ = arr[::2, ::2].copy()
print(slice_)

slice_ = arr[2, 1::2].copy()
print(slice_)

l = [1, 2, 3, 4, 5, 6]
l[0:3] = [10, 20, 30]
print(l)

l[0:3] = [10, 20, 30, 40, 50, 60]
print(l)

arr = np.array([1, 2, 3, 4, 5, 6])
arr[0:3] = np.array([10, 20, 30])
print(arr)

arr[0:3] = [10, 30, 50]
print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])
# arr[0:3] = [10, 20, 30, 40] This will raise a ValueError because the shapes do not match

# Broadcasting: means to assign a single scalar value into a shape that's needed for slice replacement
arr1 = np.arange(9).reshape(3, 3)
print(arr1)
arr1[::2, ::2] = [[10, 20], [30, 40]]  # same shape
print(arr1)

arr1[::2, ::2] = 100  # Broadcasting
print(arr1)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20])

arr1[0:2] = arr2
print(arr1)

arr2[0] = 100
print(arr1)

arr_n = np.arange(9).reshape(3, 3)
print(arr_n)
arr_n[:2, 1:] = [[10, 20], [40, 50]]
print(arr_n)

# arr_n[:2, 1:] = [10,20,30,40] retunrs ValueError because they are of different shapes

arr_n[:2, 1:] = np.array([10, 20, 30, 40]).reshape(2, 2)
print(arr_n)

arr1 = np.array([10,20,30,40,50], dtype=np.uint8)
# arr1[0:2] = [-100, 300] returns deprecation warning because they are of different types

