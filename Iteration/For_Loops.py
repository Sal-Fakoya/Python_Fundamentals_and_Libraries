"""
                    FOR LOOPS
--> For loops are used to iterate over elements of any iterable
--> The loop mechanism retrieves elements from the iterable one at a time
--> The body of the for loop is executed for each element retrieved
--> The loop determines when all elements have been iterated
--> Indentation is used to define the code blocks
--> We can iterate over range objects

            LOOP BODIES
--> can contain if-else blocks
--> can contain another loop (nested loops)

        ITERATING OVER DATA IN A RANGE OR LIST
--> This means we iterate over elements in a sequence or range
e.g for i in range(0,5):
        print(i)
    for i in [0,3,9,8]:
        print(i)

        ITERATING OVER A LOOP USING THE POSITIONS: enumerate function
--> Just like the range function, the enumerate function returns an iterable object rather than create an enumeration
--> enumerate is a function that takes an iterable argument and returns a new iterable
    whose elements are a tuple consisting of
            ---> the index number of the original element.
            ---> the original element itself.
            data = [10, 20, 30, 10, 40, 5]
            for t in enumerate(data):
                print(t)
        --> each element t is a tuple (index, element) which can be unpacked!
            for t in enumerate(data):
                index, element = t
                data[index] = 0 if data[index] < 0 else data[index]
--> We can also unpack the enumerate function in the for loopL
        --> for index, element in enumerate(data):
                if element < 0: data[index] = 0


"""

for x in ['a', 'b']:
    y = x + x
    print(y)
print('done')

for i in range(4):
    sq = i * i
    print(sq)

for i in range(1, 4):
    for j in range(1, i + 1):
        print(i, j, i * j)
    print("")

data = [10, 20, 30, -10, 40, -5]
for number in data:
    if number < 0: number = 0
    print(number)
print(data)

for i in range(0, len(data)):
    if data[i] < 0: data[i] = 0
    print(data)

for t in enumerate(data):
    print(t)

for t in enumerate(data):
    index, element = t
    if element < 0: data[index] = 0
print(data)

for t in enumerate(data):
    index, element = t
    data[index] = 0 if data[index] < 0 else data[index]
print(data)

for index, element in enumerate(data):
    # data[index] = 0 if element < 0 else data[index]
    if element < 0: data[index] = 0
print(data)

#  CODING
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

for suit in suits:
    print(f"{suit[0].upper()} = {suit}")

for c in "python":
    print(c)

for i in range(2, 11, 2):
    print(i)

print(list(range(2, 11, 2)))

for i in range(3):
    for j in range(3):
        print("\t" * 5 + f"i = {i}, j = {j}")

    print("\t" * 4 + "-" * 20)

# ITERATING OVER MATRICES
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_idx in range(3):
    for col_idx in range(3):
        print(f"[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}")

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f"[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}")

m = [
    [0, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9],
    [10]
]

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f"[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}")

for row_index, row in enumerate(m):
    for col_index, element in enumerate(row):
        print(f"{row_index, col_index} = {element}")

# BUILDING N-BY-N IDENTITY MATRIX
n = 5
matrix = []

for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

print(matrix)

n = 10
myMatrix = []

for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    myMatrix.append(row)

print(myMatrix)

data = list(range(10, 31, 10))
k = enumerate(data)
print(k)
print(type(k))

print(list(enumerate(data)))

for t in enumerate(data):
    print(t)

for t in k:
    print(t)

for i in enumerate(data):
    idx, el = i
    print(idx, el)

for idx, el in enumerate(data):
    print(idx, el)

m = [
    [0, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9],
    [10]
]

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f"[{row_idx}, {col_idx}] = {m[row_idx][col_idx]}")
# OR
for row_index, row in enumerate(m):
    for col_index, element in enumerate(row):
        print(f"{row_index, col_index} = {element}")
# OR
for row in m:
    for element in row:
        print(element)
# OR
for row_idx, row in enumerate(m):
    for col_idx, element in enumerate(row):
        print(f"[{row_idx}, {col_idx}] = {element}")

data = [10.5, 11.2, 9.8, None, 11.5, None]

count = 0
total = 0
for i in range(len(data)):
    if data[i] is not None:
        count += 1
        total += data[i]

avg = total / count
print(avg)

# OR
for index, element in enumerate(data):
    if data[index] is not None:
        count += 1
        total += data[index]
avg = total / count
print(avg)

#  OR
count = 0
total = 0

for val in data:
    if val is not None:
        count += 1
        total += val
avg = total / count
print(avg)

for i in range(len(data)):
    if data[i] is None:
        data[i] = avg
print(data)

data = [10.5, 11.2, 9.8, None, 11.5, None]
for index, val in enumerate(data):
    if val is None: data[index] = avg
print(data)

data = [10.5, 11.2, 9.8, None, 11.5, None]

count = sum(1 for val in data if val is not None)
total = sum(val for val in data if val is not None)
average = total/count
data = [val if val is not None else average for val in data]

from statistics import fmean
data = [10.5, 11.2, 9.8, None, 11.5, None]
avg = fmean(val for val in data if val is not None)
print(avg)
data2 = [val if val is not None else avg for val in data]
print(data2)
print(data is data2)

# import pandas as pd
# df = pd.DataFrame(data)
# df.fillna(df.mean(), inplace=True)
# df[0].tolist()
# print(df)
# #

dict_k = {'OneKey': 'OneValue', "SecondKey": 'SecondValue'}
for index, value in enumerate(dict_k.values()):
    print(index)
    print(value)

print("\n")
for index, key in enumerate(dict_k.keys()):
    print(index)
    print(key)
    print(dict_k[key])


