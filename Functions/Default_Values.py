"""
                    DEFAULT VALUES
--> It is possible to specify optional parameters, which means a function can be called without passing in the optional
argument
--> The parameter is still present, however, a default value is specified to use if the argument is not supplied


"""


def _func(a=1):  # 1 is the default value of a if a is not supplied when called
    print(a)


_func()
_func(10)


def my_func(b, a=1):
    pass


my_func(5)


def _func(a, b=1, *arg):
    print(a, b, arg)


_func(10)
_func(10, 2)
_func(10, 2, 3, 4)


# ----------------------------------CODING------------------------------------------------------
def func(a=1):
    return a


print(func())
print(func(10))

print(func(a=10))


def func(a, b=10, c=20):
    return a, b, c


print(func(1))
print(func(1, 2))
print(func(1, 2, 3))
print(func(1, c=100))  # default remains for b


def is_close(a, b, abs_tol=0.01):
    return abs(a - b) <= abs_tol


print(is_close(1.255, 1.256))
print(is_close(1255, 1256))
print(is_close(1255, 1256, abs_tol=5))


def parse(s, sep=',', strip_side=True):
    items = s.split(sep)
    if strip_side:
        return [item.strip() for item in items]
    else:
        return items


print(parse(' a, b, c,  '))
print(parse(' a, b, c,  ', strip_side=False))
print(parse('a:b: c: d', ':'))
print(parse('a\n|b\n|c\n', sep='|', strip_side=False))

print('a', 'b', 'c', sep='---')
print(*'abc', sep=',', end='***')
print('next print line')

print(*'abc', sep=',', end='***\n')
print('next print line')

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]


def process_data(data, item_sep=',', line_sep='\n'):
    output = ''
    for row in data:
        for element in row:
            output = output + str(element) + item_sep
        output = output + line_sep
    return output


print(process_data(data))


# print(process_data(data, item_sep="==", line_sep='\n\n'))

def process_data(data, item_sep=',', line_sep='\n'):
    output = ''
    row_strings = [
        item_sep.join(str(el) for el in row)
        for row in data
    ]
    return line_sep.join(row_strings)


print(process_data(data))


def process_row(row, item_sep):
    return item_sep.join(str(el) for el in row)


def process_data(data, item_sep=',', line_sep='\n'):
    output = ''
    row_strings = [process_row(row, item_sep) for row in data]
    print(type(row_strings))
    return line_sep.join(row_strings)


print(process_data(data))
print(process_data(data, item_sep='|', line_sep='\n\n'))


def process_row(row, item_sep):
    return item_sep.join(str(el) for el in row)

def process_data(data, item_sep=',', line_sep='\n'):
    output = ''
    row_strings = (process_row(row, item_sep) for row in data)
    print(type(row_strings))
    return line_sep.join(row_strings)


print(process_data(data))
print(process_data(data, item_sep='|', line_sep='\n\n'))
