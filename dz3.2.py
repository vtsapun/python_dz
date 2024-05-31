lst1 = []
if len(lst1) == 0:
    print(lst1)
else:
    x = lst1.pop()
    lst1.insert(0, x)
    print(lst1)