import string
x = input("Введіть рядок: ")
y = ''.join(char for char in x if char.isalnum() or char == ' ')
z = y.split()
hashtag = '#'
for word in z:
    hashtag += word.title()
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
print(hashtag)