x = int(input("Введіть ціле число: "))
while x > 9:
    number = [int(digit) for digit in str(x)]
    product = 1
    for digit in number:
        product *= digit
    x = product
print(x)