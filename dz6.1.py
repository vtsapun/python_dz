import string

x = input("Введіть дві літери через дефіс (наприклад, 'a-z'): ")
y, z = x.split('-')
start_index = string.ascii_letters.index(y)
end_index = string.ascii_letters.index(z)
print(string.ascii_letters[start_index:end_index+1])