from time import perf_counter

l = [10, 'abc', 3.14, True]

element = enumerate(l)
print(list(element))

my_iter = (f'{i}**{i}' for i in range(1, 10_001))

another_iter = list(my_iter)
print(another_iter)

#  2
start = perf_counter()
# starting counter
for _ in range(10):
    my_iter = (f'{i}**{i}' for i in range(1, 10_001))
    for _1 in range(5):
        next(my_iter)
# ending counter
end = perf_counter()
print(f"{end - start}")


start = perf_counter()
#  starting counter
my_iter = [f'{i}**{i}' for i in range(1, 10_001)]
for _ in range(10):
    for _1 in my_iter[0:4]:
        print(_1)
# ending counter
end = perf_counter()
print(f"{end - start}")




