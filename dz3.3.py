lst1 = []
x = len(lst1)
y = (x + 1) // 2
my_list1 = lst1[0:y]
my_list2 = lst1[y:]
my_list3 = []
my_list3.append(my_list1)
my_list3.append(my_list2)
print(lst1)
print(my_list3)