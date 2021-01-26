from math import factorial


def fact(n):
    for i in range(1, n+1):
        yield factorial(i)


val = int(input(': '))

for el in fact(val):
    print(el)
