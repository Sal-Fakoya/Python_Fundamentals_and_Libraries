"""
                        FUNCTIONS
--> When we create a function we may also want values to be passed into it when it is called,
    also known as arguments or parameters.
--> Parameters are smybols defined for the values that will be passed to the function
--> Arguments are values specified for functions when they are called

                FUNCTIONS ARE PYTHON OBJECTS
--> Just like everything in Python, functions are objects that have-->
        --> state such as name (maybe!), code, parameters
--> They are callable and always return somethinf when called
--> They can be assigned to a symbol
--> They can be passed as a parameter or argument to another function
--> They can be returned from a function call

                CALLABLES
--> An object is callable if it can be called using ()
--> Functions are run by calling them e.g print('hello'), math.sqrt(4),
--> Other types of objects are also callable, such as my_list.copy() --> calling a method on the my_list object
--> range(100), creates a new range object

                CUSTOM FUNCTIONS
--> Functions can be defined by using the def keyword
    def function_name():
        # indented block
        return <value> #Functions always returns some value
--> Function body creates any valid Python Code
--> It creates a function object
--> The function object is associated with the function_name
--> If a return value is not specified, the function will return None

            NAMESPACES
--> When a function is called, it knows nothing about how it was called before
--> Every time a function is called, an empty dictionary is created
--> The dictionary is populated with any arguments passed in
    --> key=parameter_name, value=argument
    --> The dictionary is called the (local) namespace and discarded when the function is finished running
"""


# -------------------CUSTOM FUNCTIONS
def say_hello():
    print('hello')


print(globals())

say_hello()
say_hello()


def one():
    return 1


result = one()
print(result)

from datetime import datetime


def current_time_utc():
    return datetime.utcnow().isoformat()


result = current_time_utc()
print(result)


def add(a, b):
    return a + b


result = add(2, 3)
print(result)


def subtract(a, b):
    return a - b


result = subtract(10, 7)
print(result)

# result = say_hello()
f = say_hello
print(f is say_hello)

print(say_hello.__name__)


def add(a, b, c):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    return a + b + c


result = add(1, 2, 3)

print(result)


def add(a, b, c):
    print(f"initial namesapce: {locals()}")
    sum_ = a + b + c
    print(f"after namesapce: {locals()}")
    return a + b + c


add(1, 2, 3)

add(10, 20, 30)


def find_max(a, b, c):
    max_ = a
    if b > max_:
        max_ = b
    if c > max_:
        max_ = c
    return max_


print(find_max(10, 20, 30))

from datetime import datetime


def log(message):
    curr_time = datetime.utcnow().isoformat()
    print(f"{curr_time} - [{message}]")


log('log 1')
result = log('log1')
print(type(result))

log('log 2')

data = [1, 2, 3, 4, 5, 6]
for element in data:
    if element < 0:
        break
else:  # no break
    print('processing all positive elements')

data = [1, 2, 3, 4, 5, 6, -1]
for element in data:
    if element < 0:
        break
else:  # no break
    print('processing all positive elements')


def is_all_positive(data):
    for i in data:
        if i < 0:
            return False
    return True


result1 = is_all_positive([1, 2, 3, 4])
print(result1)

result1 = is_all_positive([1, 2, 3, 4, -4, 100])
print(result1)

result1 = is_all_positive(range(1, 10))
print(result1)

result1 = is_all_positive(range(10, -20, -2))
print(result1)

d = {'a': 1, 'b': 2, 'c': -10}
another_result = is_all_positive(d.values())
print(another_result)


def gen_matrix(m, n, default_value):
    return [
        [default_value for i in range(n)]
        for j in range(m)
    ]


my_matrix = gen_matrix(2, 2, 1)
print(my_matrix)

print(gen_matrix(4, 8, 1))


def gen_matrix(rows, cols, default_value):
    return [
        [default_value for i in range(cols)]
        for j in range(rows)
    ]


my_matrix = gen_matrix(2, 2, 1)
print(my_matrix)

print(gen_matrix(4, 8, 1))

my_matrix = gen_matrix(rows=4, cols=8, default_value=2)
print(my_matrix)


my_matrix = gen_matrix(cols=8, rows=5, default_value=6)
print(my_matrix)

gen_matrix(5, cols=4, default_value=10)









