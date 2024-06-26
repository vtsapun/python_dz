def find_unique_value(some_list):
    count = {}
    for num in some_list:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, cnt in count.items():
        if cnt == 1:
            return num
    return None
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
