first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_do = input('Введите действие')
if third_do == '+':
    print(first_number + second_number)
elif third_do == '-':
    print(first_number - second_number)
elif third_do == '/' and second_number != 0:
    print(first_number / second_number)
elif third_do == '*':
    print(first_number * second_number)
else:
    print('На ноль делить нельзя')
