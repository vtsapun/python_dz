def common_elements():
    numbers_divisible_by_3 = [num for num in range(100) if num % 3 == 0]
    numbers_divisible_by_5 = [num for num in range(100) if num % 5 == 0]
    common_elements_set = set()
    for num in numbers_divisible_by_3:
        if num in numbers_divisible_by_5:
            common_elements_set.add(num)
    return common_elements_set
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}