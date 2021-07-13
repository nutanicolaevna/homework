# Задача 1
# class Data:
#     def __init__(self, data_month_year):
#         self.data_month_year = data_month_year
#
#     @classmethod
#     def ext(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-': my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#     @staticmethod
#     def validation(day, month, year):
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2022 >= year >= 0:
#                     return f'Все правильно'
#                 else:
#                     return f'Неправильно введен год'
#             else:
#                 return f'Неправильно введен месяц'
#         else:
#             return f'Неправильно введен день'
#
#     def __str__(self):
#         return f'Тякущая дата :{Data.ext(self.data_month_year)}'
#
#
# exmp = Data('10 - 07 - 2021')
# print(exmp)
# print(Data.validation(11, 11, 2024))
# print(exmp.validation(11, 13, 2011))
# print(Data.ext('11 - 11 - 2011'))
# print(exmp.ext('11 - 11 - 2020'))
# print(Data.validation(1, 11, 2000))

# Задача 2
# class My_error(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# def division():
#     try:
#         num_1 = int(input('Введите делимое: '))
#         num_2 = int(input('Введите делитель: '))
#         if num_2 == 0:
#             raise My_error("Делить на ноль нельзя!")
#         else:
#             result = num_1 / num_2
#             return result
#     except ValueError:
#         return "Вы ввели не число"
#     except My_error as err:
#         return err
#
#
# print(division())

# Задача 3
# class NotNumber(Exception):
#     pass
#
#
# my_list = []
# while True:
#     try:
#         value = input('Введите число в список:')
#         if value == 'q':
#             break
#         elif value.isdigit():
#             raise NotNumber(value)
#         my_list.append(int(value))
#
#
#
#
#     except ValueError:
#         print('Ошибка ввода')
#     except NotNumber as ex:
#         print(ex)
#
# print(my_list)

# Задача 4
class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):

        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
