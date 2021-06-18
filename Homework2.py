# Задание 1
lst = ['Добрый день', 10.6, 17, False, 'new', [1, 2, 3, 4], 'time']
print(lst)

for element in lst:
    print(type(element))

# Задание 2
ls = input('Введите последовательность элементов через пробел: ').split()
print(ls)
for i in range(0, len(ls)-1, 2):
    ls[i], ls[i+1] = ls[i+1], ls[i]
print(ls)

# Задание 3
# 1 Вариант
season = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
numbers = int(input('Введите номер месяца от 1 до 12: '))
for key in season:
    if numbers in season[key]:
        print(key)
# 2 Вариант
season = ['winter', 'spring', 'summer', 'autumn']
num = int(input('Введи номер месяца от 1 до 12: '))
if num == 1 or num == 12 or num == 2:
    print(season[0])
elif num == 3 or num == 4 or num == 5:
    print(season[1])
elif num == 6 or num == 7 or num == 8:
    print(season[2])
elif num == 9 or num == 10 or num == 11:
    print(season[3])
else:
    print('error')

#  Задание 4
words = input('Введите любые слова через пробел: ').split()
for number, word in enumerate(words, 1):
    if len(word) >= 10:
        print(number, word[0:11])
    else:
        print(number, word)
# Задача 5

rating = [9, 7, 6, 4, 3, 1]
number = int(input('Введи число:'))
for value in range(0, len(rating)):
    if rating[value] == number:
        rating.insert(value, number)
        break
    elif rating[0] < number:
        rating.insert(0, number)
    elif rating[-1] > number:
        rating.append(-1, number)
    elif rating[value] > number and rating[value+1] < number:
        rating.insert(value+1, number)
        break
print(rating)



