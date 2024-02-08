"""
                            NUMPY SECTION YAY!:
--> Numpy is a widely used library mainly used for working with arrays.
    --> It is very fast, memory efficient and flexible.

                        ARRAYS (Lists)
--> Arrays are basically lists.
--> A python list is a type of array.
--> Elements are indexed in an array, just like a list, e.g arr[0], arr[1], etc
--> Arrays can be sliced such as arr[start:stop:step]
--> Arrays can have variable size. We can add/remove elements from an array
--> Arrays are heterogeneous and have different data types.

                        ARRAYS (NUMPY ARRAYS): ndarray
--> NumPy array is another implementation of arrays
--> NumPy arrays have a fixed size once created, but elements can be mutated.
--> Elements in the NumPy array must be homogeneous (i.e, must be of the same data type)

                PYTHON list vs NUMPY ndarray
--> ndarray has fixed size, whereas list has a variable size.
--> ndarray can be reshaped whereas list would need to be looped through
--> ndarray is homogeneous whereas list is heterogeneous.
--> ndarray elements have specialized, restricted data types wheareas list elements can be any python objects.
--> ndarray can be indexed e.g arr[1], like lists
--> ndarray can be sliced e.g arr[start:stop:step], just like lists
--> ndarray gives us the ability to mask, which allows us to pick and choose elements of an array based on
conditional statements e.g arr[(arr>2) & (arr<10)] whereas lists do not.
--> ndarray allows us to pick out elements by specifying their index in a list, e.g arr[[0,3,4]] allows us to pick
elements in the array of index 0,3,4

                            NUMPY EFFICIENCY
--> NumPy is more space efficient than Python
--> Array manipulations and calculations are much faster through:
    --> Vectorization
--> However, NumPy arrays have fixed size once created.
    --> We cannot add/remove elements
    --> Elements can be replaced.
--> NumPy arrays homogeneous, i.e elements are of the same type,
    even in multidimensional arrays (arrays of arrays).
    All the arrays in a multidimensional array must be of the same type.
--> The data types in ndarray uses data types from underlying C language for memory efficiency and vectorization.

                        INTEGER SIZES
--> Integers are stored as sequences of bits (0s and 1s).
--> Number of bits determines how large the integer can be, so the largest number we can represent using 4bits is 15.
        --> range is [0,15]
    --> We may want negative numbers. In that case, one bit is reserved to keep track of the sign.
        -->so 3 bits [-8,7]

FOR SIGNED INTEGERS
--> 8 bits is [-128, 127]
--> 16 bits is [-32_768, 32_767]
--> 32 bits is a bigger range, and 64 bits and so on

FOR UNSIGNED INTEGERS
--> 8 bits is [0, 255]
--> 16 bits is [0, 65_535]
--> 32 bits is a bigger range, and 64 bits and so on

                        FLOATS
--> Python uses 64 bits to store floats.
    --> certain precision and size of exponent.


                        NUMPY DATA TYPES
--> In NumPy, you specify the data type of the array:
    --> If you choose an unsigned 8-bit integer, you can only store numbers [0,255]
--> signed integers: int8, int16, int32, int64
--> unsigned integers: uint8, uint16, uint32, uint64
--> floats: float32, float64
    --> float64 is compatible with python floats.
--> complex numbers: complex64, complex128
    --> complex64 means there are 32-bits for the real and 32-bits for complex numbers.
    --> complex128 uses 64-bits for the complex numbers and 64-bits for the real numbers
    --> complex128 us compatible with Python complex

                            VECTORIZATION
--> Suppose we want to multiply every element in one array by the corresponding element in another array,
    Instead of using lists and looping through, we can use numpy arrays to achieve this:
        --> e.g given a and b are Numpy Arrays (ndarray)
        --> we can use function or operator on the arrays, e.g multiply(a,b) or a * b
--> The process of pushing python loop and calculations down to C code by using universal functions (ufunc are sin(),
multiply, divide, add, etc used for calculations) is called "Vectorization".

                WHY ARE ARRAYS IMPORTANT:
--> Most data that we deal with is represented as arrays e.g in multidimensional arrays.
    --> For example, an image is a 2-Dimensional array of colored pixels where each pixel is array, e.g
        [red, green, blue, alpha]
    --> A video is an array of images
    --> Audio can be encoded into arrays
    --> Stock, quotes, tick data are arrays of data.
    --> An Excel spreadsheet is a 2-Dimensional array

                    APPLICATIONS OF NUMPY IN REAL LIFE:
--> NumPy is a huge library.
--> It has lots of universal functions such as financial, math, stats, linear algebra, sorting, sampling,
    Fourier transforms (discrete) and more...
--> We'll learn array creation and manipulation
    (indexing, slicing, fancy indexing, masking, reshaping, etc)
--> It is the foundation for Pandas_Library_UDEMY Library, which helps us deal with data sets of various types.

"""
import numpy
import numpy as np

arr = numpy.array([1, 2, 3])

print(np.concatenate((arr, arr), axis=0))
print(np.concatenate((arr, arr), axis=1))
