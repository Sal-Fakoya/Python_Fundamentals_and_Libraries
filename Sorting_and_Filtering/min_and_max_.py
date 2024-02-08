"""
                        MIN AND MAX: min(iterable, key=func_name), max(iterable, key=func_name)
--> We can get the minimum in an iterable using a key as a basis, For instance, if we want a minimum to be based on
the absolute value,
    --> min(iterable, key=abs)
--> Min and Max is based on sorting
"""

data = [-1,2,-3,4,-5]

print(min(data, key=abs))

data = [1,-2,3,-4, 5,-6]
print(sorted(data))

min(data)

print(sorted(data, key=abs))

k = sorted(data, key=abs)
print(k[0])

print(min(data, key=abs))
print(max(data, key=abs))


data = [
    {'date': '2020-04-09', 'symbol': 'AAPL', 'open': 268.70, 'high': 270.04, 'low': 264.70, 'close': 267.99},
    {'date': '2020-04-09', 'symbol': 'MSFT', 'open': 166.36, 'high': 167.37, 'low': 163.33, 'close': 165.14},
    {'date': '2020-04-09', 'symbol': 'AMZN', 'open': 2_044.30, 'high': 2_053.00, 'low': 2_017.66, 'close': 2_042.76},
    {'date': '2020-04-09', 'symbol': 'FB', 'open': 175.90, 'high': 177.08, 'low': 171.57, 'close': 175.19}
]

smallest_low = min(data, key=lambda d: d['low'])
print(smallest_low)










