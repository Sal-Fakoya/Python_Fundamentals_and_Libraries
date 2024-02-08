
"""
            SKIPPING AN ITERATION: continue
--> Sometimes we want to skip an iteration, but without terminating the loop
--> The continue statement skips to the next iteration
--> continue is not used too often because it can sometimes make code difficult to read/understand

            EARLY TERMINATION: break
--> Loops can be exited early (before all element have been iterated)
--> Loops terminated using break is sometimes called abnormal or early termination

            ELSE CLAUSE
--> For loops can have an else clause, which has nothing to do with the else clause of an if statement
--> The else clause of an if statemnt of a for loop execute if and only if no break was encountered
--> It can be thought of as "else if no break"
    for i in range(5):
        codeblock1
    else: #if no break
        codeblock2 #Executes if loop terminates normally
"""

myList = [1, 2, 3, 100, 4, 5]
for i in myList:
    if i > 50:
        continue
    print(i)
print('done')

for i in myList:
    if i <= 50: print(i)
print('done')


myList = [1, 2, 3, 100, 4, 5]

for i in myList:
    if i > 50:
        break
    print(i)
print('done')


found = False

for el in myList:
    if el == "Python":
        found = True
        print('found')
        break
if not found:
    print('not found')

for el in myList:
    if el == 'Python':
        print('found')
        break
else: #if no break
        print('not found')

#  CODING
for i in range(100):
    print(i)
    if i >= 5:
        print("breaking out of loop...")
        break
print('done')

for i in range(1,11):
    if i%2 == 1:
        # odd number
        continue
    print(i)

for i in range(1,11):
    if i%2 == 0:
        print(i)

for i in range(1,5):
    for j in range(1,5):
        if (i + j) % 2 == 1:
            print(f"{i} + {j} is odd. skipping...")
            continue
        print(f"Adding numbers: {i} + {j} = {i + j}")
    print('-'*10)

for i in range(1,4):
    for j in range(1,4):
        if j >= 3:
            break
        print(i,j)
    print('-'*10)

i = 0
while True:
    i += 1
    if i > 5:
        break
    print(i)

data = [1, 2, 3, -4, 5, 6]
all_positive = True

for element in data:
    if element <= 10:
        all_positive = False
        break

if all_positive:
    print('processing all positive elements...')


for i in range(5):
    print(i)
    if i > 3:
        break
else: #no break
    print("loop terminated normally no break...")


data = [1, 2, 3, -4, 5, 6]

for element in data:
    if element < 0:
        break
else:
    print('processing all positive elements')







































































