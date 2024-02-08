"""



"""

s = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
in culpa qui officia deserunt mollit anim id est laborum.
"""
myLetters = []
# s = list(s)
print(s)
s_Dict = {}

for i in s:
    # print(i)
    # count = 0
    Capital = True if ord(i) in list(range(ord('A'), ord('Z') + 1)) else False
    Small = True if ord(i) in list(range(ord('a'), ord('z') + 1)) else False
    if Capital or Small:
        myLetters.append(i)
print(myLetters)
print(s)

for i in myLetters:
    count = 0
    for j in myLetters:
        if i == j:
            count += 1
            s_Dict[i] = count

print(s_Dict)

# EXERCISE 2
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}

allKeys = list()
allValues = list()
for key, value in d1.items():
    allKeys.append(key)
    allValues.append(value)
for key, value in d2.items():
    allKeys.append(key)
    allValues.append(value)
for key, value in d3.items():
    allKeys.append(key)
    allValues.append(value)

allKeys = list()
allValues = list()
for d in (d1, d2, d3):
    for key, value in d.items():
        allKeys.append(key)
        allValues.append(value)

print(allKeys)
print(allValues)

# EXERCISE 3
grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}
exam = {
    'Eric': 99,
    'John': 100,
    'Mike': 50
}

for key, value in grades.items():
    value.insert(0, exam.get(key))
print(grades)
