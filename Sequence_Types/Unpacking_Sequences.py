"""
consider a sequence:
data = (1,2,3) --> a tuple with three elements
We want to assign 1,2,3 to some symbols a,b,c respectively.

a = data[0]
b = data[1]
c = data[2]

But Python has a better way of doing this, known as unpacking!

Unpacking works with any sequence. It is simply creating multiple assignments.
--> The only warning to unpack is that the number of elements in the sequence on the RHS must be equal to the
number of variables on the LHS, else you get ValueError
--> Unpacking sequences are usually used in function and iterables (lists, tuples, and strings)
--> An application of unpacking is Swapping Two Variable Values
--> In an assignment, the RHS expression is evaluated first
    ---> Then the assignment takes place

a,b,c = (1,2,3) or a,b,c = 1,2,3
a,b = [10, 20]
a,b,c = 'XYZ'
a = X; b= Y, c = Z

"""

a,b,c = 1,2,3
print(a); print(b); print(c)

a,b,c = 'xyz'; print(a); print(b); print(c)

a,b,c = [1,2,3], [5, 6, 7], [19, 10]
print(a,b,c)

# SWAPPING VARIABLES
a = 10; b = 20
temp = a
a = b
b = temp;
print(a); print(b)

# OR...........................
a = 10; b = 20;
a,b = b,a
print(a,b)


# -----------------------------------------------------------------------------------------------------------------
rate = 5.0, 5.12
apr = rate[0]
apy = rate[1]
print(apr, apy)

apr, apy = rate[0], rate[1]
print(apr, apy)

apr, apy = rate
print(apr, apy)

a,b,c = 10, 3.14, 'abc'
print(a,b,c)

x,y,z = 'abc'
print(x,y,z)

a,b,c = [1,2,3]

s= 'abcdef'
a,b,c = (1+1, s[::-1], 3.14)
print(a,b,c)

a = 100
b = 3.14
a,b = b,a
print(a, b)

a = 100
b = 3.14
t = b, a

a,b = t
print(a,b)





















