a = int(input('Користувач може ввести будь-яке 4 значне ціле число: '))
b1 = a // 10000
b2 = (a // 1000) % 10
b3 = (a // 100) % 10
b4 = (a // 10) % 10
b5 = a % 10
print(b5,b4,b3,b2,b1)