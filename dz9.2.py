def difference(*args):
    if not args:
        return 0
    min_value = float('inf')
    max_value = float('-inf')
    for num in args:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    diff = max_value - min_value
    return round(diff, 2)
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
