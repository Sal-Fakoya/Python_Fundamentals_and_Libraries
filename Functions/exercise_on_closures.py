#
# def approximate_func(func):
#     def inner(start, end, min_=True, max_=True):
#         if (min and max) == True:
#             return list(map(func, range(start, end))), min(range(start, end)), max(range(start,end))
#         elif min


# Question2
import math
from time import perf_counter

points = [
    (0, 0),
    (1, 1),
    (10, 20),
    (math.pi, math.e)
]


# USING LIST COMPREHENSION
def with_comprehension(points):
    result = [math.hypot(*coordinate) for coordinate in points]
    return result


# USING GENERATOR
def with_generator(points):
    result = (math.hypot(*coordinate) for coordinate in points)
    # result = [math.hypot(*i) for i in result]
    return list(result)


# USING A FOR-LOOP
def with_for_loop(points):
    result = []
    for coordinate in points:
        result.append(math.hypot(*coordinate))
    return list(result)


# USING THE MAP FUNCTION
def with_map_function(points):
    # x, y = (x for x,y in points), (y for x,y in points)
    result = map(math.hypot, (x for x, y in points), (y for x, y in points))
    return list(result)

# USING THE MAP FUNCTION: my_time_it as closure
def my_functions(points):
    def with_time_it(func):
        start = perf_counter()
        result = func(points)
        end = perf_counter()
        return f'Elapsed = {start - end}'

    return with_time_it



points = [
    (0, 0),
    (1, 1),
    (10, 20),
    (math.pi, math.e)
]


generating = my_functions(points)
print(generating(with_generator))
print(generating(with_map_function))
print(generating(with_comprehension))
print(generating(with_for_loop))


#QUESTION 3

def partial(my_func, n=2):
    def inner(x):
        result = my_func(x, n)
        return result
    return inner

def power(x, n):
    return x ** n

def dist(pt1, pt2):
    return math.sqrt(sum(coord_1 - coord_2 for coord_1, coord_2 in zip(pt1, pt2)))

squares = partial(power, 2)
print(squares(3))

dist_from_origin = partial(dist, (0, 0))
print(dist_from_origin((1,1)))


#QUESTION 4
def logged(f):
    result = f()
    pass


