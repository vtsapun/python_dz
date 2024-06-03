lst = [2,3,5,0,3,0,3,4,3,4,0,0,2,4,0,3,0]
i = 0
while i < len(lst):
    l = lst[i]
    i += 1
    if l != 0:
        continue
    lst.remove(l)
    lst.append(l)
print(lst)