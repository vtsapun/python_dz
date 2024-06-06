import keyword
import string
x = input()
y = True
if x in keyword.kwlist:
    y = False
if x.count('__') >= 1:
    y = False
if x[0].isdigit():
    y = False
for l in x:
    if l.isupper() or l.isspace() or (l in string.punctuation and l != '_'):
        y = False
        break
print(y)