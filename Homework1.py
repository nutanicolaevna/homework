
# Homework
# Задача 1
age = 78
name = "Аня"
print(name)
print(age, name)
print(type(name))
name = input("What`s your name?")
hi = 'Nice to meet you'
print(name, hi)
# #
weight = input("Enter your weight: ")
height = input('Enter your height: ')
print(weight, height)
print("excellently")
# # Задача  2
a = int(input('Введите количество секунд: '))
hh = a//3600
mm = (a//60) % 60
ss = a % 60
print('hh : {} mm : {} ss : {}' .format(hh, mm, ss))
# # Задача 3
n = int(input('Введи любое число'))
numb = str(n)
n1 = numb + numb
n2 = numb + numb + numb
summary = n + int(n1) + int(n2)
print('Результат:', summary)
# Задача 4
a = int(input('Введи число:'))
number = a % 10
a = a // 10
while a > 0:
    if a % 10 > number:
        number = a % 10
    a = a//10
print(number)
# Задача 5
profit = int(input('Введите прибыль:'))
costs = int(input('Введите затраты:'))
if profit > costs:
    print('Вы отработали с прибылью')
    ren = profit / costs
    print('Рентабельность: ', ren)
    peopl = int(input('Введите численность сотрудников фирмы: '))
    ren_pl = profit / peopl
    print('Прибыль на одного сотрудника:', ren_pl)
else:
    print('Вы отработали с убытком')
