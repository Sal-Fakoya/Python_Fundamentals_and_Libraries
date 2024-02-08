# Q1
l = [
    (1, 2),
    (-4, -5.5),
    (10, -10),
    (-2, 2)
]


def my_func(x):
    return abs(x[0] - x[1])


result = sorted(l, key=my_func, reverse=True)
print(result)
# OR
result = sorted(l, key=lambda x: abs(x[0] - x[1]), reverse=True)
print(result)

# Q2

suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

# print(''.split(ranks))
# ranks2suits = [[rank+suit for rank in ranks] for suit in suits]

r2s = lambda rank, suit: [[rank + suit for rank in ranks] for suit in suits]

r2s = sorted(r2s(ranks, suits), key=lambda d: d[-1], reverse=False)
print(r2s)


#   OR

def _rank2suits_(suits, ranks):
    def inner(reverse):
        f = lambda rank, suit: [[rank + suit for rank in ranks] for suit in suits]
        return sorted(f(suits, ranks), key=lambda d: d[-1], reverse=reverse)

    return inner


suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

result = _rank2suits_(suits=suits, ranks=ranks)
print(result(value=False))  # Descending
print(result(value=True))  # Ascending
