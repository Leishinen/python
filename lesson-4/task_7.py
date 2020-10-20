from functools import reduce


def mult(a, b):
    return a * b


def fact(n):
    for el in range(1, n + 1):
        yield reduce(mult, range(1, el + 1))


for el in fact(10):
    print(el)