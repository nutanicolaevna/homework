# Задание 1

# m_file = open('data.txt', 'w', encoding='utf-8')
#
# while True:
#     elem = input('Введите текст')
#     n_elem = elem + '\n'
#     m_file.writelines(n_elem)
#     if elem == '':
#         break
# m_file.close()

# Задание 2
# try:
#     with open('file_for_2.txt', 'r', encoding='utf-8') as my_inform:
#         my_elem = my_inform.readlines()
#         for i in range(len(my_elem)):
#             per1 = my_elem[i].split()
#             print(f'Количество строк в файле:{len(my_elem)}. В {i+1} строке {len(per1)} слова')
# except FileNotFoundError:
#         print('Ошибка. Файла не существует')

# Задание 3
# with open('file_for_3.txt', 'r', encoding='utf-8') as file:
#     many = file.readlines()
#     person = []
#     summa = 0
#     for i in range(len(many)):
#         salary = int((many[i].split())[1])
#         if salary < 20000:
#             person.append((many[i].split())[0])
#         summa += salary
# print(f'Оклад меньше 20 тысяч {person}. Средняя зарплата: {summa/len(many)}')

# Задание 4
# rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# new_data = []
# with open('file_for_4.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for i in lines:
#         i = i.split('-', 1)
#         new_data.append(rus[i[0]] + '-' + i[1])
#     with open('new_file_for_4.txt', 'w', encoding='utf-8') as new_file:
#         f = new_file.writelines(new_data)

# Задание 5
# with open('sum_file.txt', 'w+', encoding='utf-8') as file:
#     ln = input('Введите набор чисел через пробел: ')
#     file.writelines(ln)
#     value = ln.split()
#
#     print(sum(map(int, value)))

# Задание 6
# my_dic = {}
# try:
#     with open('file_for_6.txt', 'r', encoding='utf-8') as file:
#         for line in file.readlines():
#             data = line.replace('(', ' ').split()
#             my_dic[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
#         print(my_dic)
# except ValueError:
#     print('Неверные данные')








