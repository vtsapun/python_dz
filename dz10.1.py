def pow(x):
    return x ** 2

def somegen(begin, end, func):
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

from inspect import isgenerator

gen = somegen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
