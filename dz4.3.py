import random
my_list = [random.randint(3,10) for i in range(random.randint(3,10))]
print(my_list)
new_my_list = [my_list[0], my_list[2], my_list[-2]]
print(new_my_list)
