"""
1: a
2: d
3: c
4: c
5: d ANS: a
6: d
7: c
8: 6.27
9: Isaac Newton
10: a (I, II only) ANS: D




"""
from math import sqrt

f = lambda a, b, c: round((-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a), 2)

print(f(3, 4, -5))
print(f(1, -5, -8))


def encrypt(s):
    return ''.join(chr(ord(c) + 10) for c in s)


# print(encrypt('I like me'))

def decrypt(my_s):
    return ''.join(chr(ord(c) - 10) for c in my_s)


print(decrypt('S}kkm*Xo\x81~yx'))

currencies = 'USD, CAD, USD, JPY,  AUD'
values = [100, 200, 300, 400, 500]

currencies = list(currencies)
print(', '.join(currencies))


def find_first_negative(numbers):
    i = 0
    while numbers[i] >= 0:
        i += 1
    return i


print(find_first_negative([1, -5, -2, 9, 0]))
