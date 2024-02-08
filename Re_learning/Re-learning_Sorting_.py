"""
                        SORTED FUNCTION: sorted()
--> Given an iterable, sorted() function returns a list that has been sorted by different criteria.
-->
"""

data = [3, 1, -6, -2, -4, 5]

ans = sorted(data, key=abs)


def sort_key(x):
    return abs(x)
print(ans)

ans = sorted(data, key=sort_key)
print(ans)

ans = sorted(data, key=lambda x: abs(x))
print(ans)

data = {"a":300, 'b':100, 'c':200}
ans = sorted(data.keys(), key=lambda k: data[k])
print(ans)

ans = sorted(data.keys(), key=lambda k: data[k], reverse=True)
print(ans)


