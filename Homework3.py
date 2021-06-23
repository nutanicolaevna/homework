# # Задание 1
def my_split(arg1, arg2):
    try:
        res = arg1/arg2
        return res
    except ZeroDivisionError:
        return 'На ноль не делится. Попробую снова.'

arg1 = int(input('Введите число: '))
arg2 = int(input('Ведите число: '))
sp = my_split(arg1, arg2)
print(sp)
#
# # # Задание 2
def parametrs(var_1, var_2, var_3, var_4, var_5, var_6):
    parametrs(var_1='Frank', var_2='Kharkov', var_3= 1956, var_4='Харьков', var_5='asd@mail.ru', var_6=7465654)


var_1 = input('Введи свое имя: ')
var_2 = input('Введи фамилию: ')
var_3 = int(input('Введи год рождения:'))
var_4 = input('Введи город проживания: ')
var_5 = input('Введи email: ')
var_6 = int(input('Введи номер телефона: '))
print(var_1, var_2, var_3, var_4, var_5, var_6)
#
# # Задание 3
def my_func(arg1, arg2, arg3):
    summ1 = arg1 + arg2
    summ2 = arg1 + arg3
    summ3 = arg2 + arg3
    if arg1 >= arg3 and arg2 >= arg3:
        return summ1
    elif arg1 > arg2 and arg1 < arg3:
        return summ2
    else:
        return summ3
#
#
arg1 = int(input('Введите число:'))
arg2 = int(input('Введите число: '))
arg3 = int(input('Введите число: '))
print(my_func(arg1, arg2, arg3))
#
#
# # Задание 4
# # Вариант 1
def my_func(x,y):
    result = x ** y
    return result
# # Вариант 2
def my_func(x,y):
    res1 = 1
    a = 1
    while a <= abs(y):
        res1 *= x
        a += 1
    return 1/res1

x = int(input('Введите положительное число: '))
y = int(input('Введите отрицательное целое число: '))
print(my_func(x,y))
#
# # Задание 5
sum1 = 0
while True:
    enter = input('Введите последовательность чисел через пробел. Для выхода нажми #: ').split()
    for i in enter:
        try:
            if i =='#':
                print(f'Выход')

            else:
                sum1 += int(i)
        except ValueError:
            print('Введите число или #')
    print(f'Сумма = {sum1}')


# Задание 6
def int_func(text):
    res = ''
    for letter in text:
        letter = letter[0].upper() + letter[1:]
        res += letter + ''
    return res

slovo = input('ведите строку из слов, разделенных  пробелом, гда слова состоят из латинских строчных букв: ')
print(int_func(slovo))