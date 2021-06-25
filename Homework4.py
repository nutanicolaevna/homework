# Задание 1
from sys import argv
print(argv)
work_h, stav_h, prem = map(int, argv[1:])
result = (work_h * stav_h) + prem
print(f'Заработная плата сотрудников = {result}')

# Задание 2
my_list = [10, 20, 12, 6, 90, 11, 13]
new_my_list = [num for num in my_list if num > my_list[my_list.index(num)-1]]
print(new_my_list)

# Задание 3
my_number = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(my_number)

# Задание 4
my_value = [17, 9, 9, 2, 3, 5, 5, 6, 34, 2, 3, 4, 8]
value = [i for i in my_value if my_value.count(i) == 1]
print(value)

# Задание 5
num = [i for i in range(100, 1001) if i % 2 == 0]
print(num)
from functools import reduce
def my_result(a1, a2):
    return a1 * a2
print(reduce(my_result, num))

# Задание 6
# a)
from itertools import count

for el in count(int(input('Введите целое число с которого нужно начать: '))):
    if el > 100:
        break
    else:
        print(el)
# b)
#
f = 0
a = int(input('Введите количество необходимых повторений: '))
from itertools import cycle
for el in cycle(['Добрый', 'день', 'успехов', 'в', 'работе']):
    if f > a:
        break
    else:
        print(el)
        f += 1

# Задание
from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)
res = fact()
a = 0
for num in res:
    if a < 12:
        print(num)
        a += 1
    else:
        break