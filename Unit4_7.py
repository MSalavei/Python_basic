# Unit4_7

from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


g = fact(4)

for el in g:
    print(el)
